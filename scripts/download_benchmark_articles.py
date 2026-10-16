"""下载用户指定账号最新60篇图文；密钥只从环境或用户指定的本机文件读取。

python scripts/download_benchmark_articles.py --key-file <本机凭据文件>
不会覆盖已有raw文件；不采集互动、评论或另行下载视频等媒体。
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
import hashlib
import html
import json
import os
from pathlib import Path
import re
import time
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlencode, urlsplit, urlunsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SEED_URL = "https://mp.weixin.qq.com/s/ZkI8xg3MzLMjB1Im1nap9A"
API = "https://api.tikhub.io/api/v1/"


def read_key(key_file=None):
    if key_file:
        content = Path(key_file).read_text(encoding="utf-8-sig").strip()
        try:
            obj = json.loads(content)
        except json.JSONDecodeError:
            obj = None
        if isinstance(obj, dict):
            key = obj.get("TIKHUB_API_KEY") or obj.get("tikhub_api_key") or obj.get("api_key")
        else:
            match = re.search(r"(?m)^\s*(?:export\s+)?TIKHUB_API_KEY\s*=\s*(.+?)\s*$", content)
            key = match.group(1).strip().strip("\"'") if match else content
    else:
        key = os.environ.get("TIKHUB_API_KEY")
    if not isinstance(key, str) or not key.strip() or any(c.isspace() for c in key.strip()):
        raise ValueError("缺少有效TikHub配置；需提供TIKHUB_API_KEY环境变量或--key-file路径")
    return key.strip()


def clean_url(url):
    parts = urlsplit(html.unescape(url))
    if (parts.scheme not in ("http", "https") or parts.netloc != "mp.weixin.qq.com"
            or not re.fullmatch(r"/s(?:/[A-Za-z0-9_-]+)?", parts.path)):
        raise ValueError("文章链接不是有效的微信公众号HTTPS链接")
    query = parse_qs(parts.query)
    keep = {k: query[k][0] for k in ("__biz", "mid", "idx", "sn") if k in query}
    # 账号列表返回HTTP原链时升级为HTTPS，后续请求不使用明文连接。
    return urlunsplit(("https", parts.netloc, parts.path, urlencode(keep), ""))


def article_id(item):
    if item.get("app_msg_id") is not None:
        return f'{item["app_msg_id"]}:{item.get("idx", 1)}'
    return clean_url(item["url"])


def unique_latest(items, limit):
    unique = {}
    for item in items:
        if item.get("url"):
            unique.setdefault(article_id(item), item)
    return sorted(unique.values(), key=lambda x: int(x.get("create_time") or 0), reverse=True)[:limit]


class TikHubClient:
    def __init__(self, key):
        self.key = key

    def post(self, endpoint, payload):
        if endpoint not in ("wechat_mp/v2/fetch_article_detail_h5", "wechat_mp/v2/fetch_account_articles"):
            raise ValueError("不支持的采集接口")
        request = Request(API + endpoint,
                          data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
                          headers={"Authorization": "Bearer " + self.key,
                                   "Content-Type": "application/json",
                                   "User-Agent": "Mozilla/5.0"}, method="POST")
        for attempt in range(3):
            try:
                with urlopen(request, timeout=45) as response:
                    result = json.load(response)
                if result.get("code") not in (None, 0, 200):
                    raise RuntimeError(f'TikHub业务状态异常：{result.get("code")}')
                if not isinstance(result.get("data"), dict):
                    raise RuntimeError("TikHub返回的数据结构不完整")
                return result["data"]
            except HTTPError as error:
                if attempt < 2 and error.code in (429, 500, 502, 503, 504):
                    time.sleep(2)
                    continue
                # 不输出完整响应或请求，避免其中回显凭据。
                raise RuntimeError(f"TikHub请求失败，HTTP {error.code}") from None
            except (URLError, TimeoutError):
                if attempt < 2:
                    time.sleep(2)
                    continue
                raise RuntimeError("TikHub连接中断或超时，重试后仍未恢复") from None
        raise RuntimeError("TikHub请求未完成")


def account_articles(client, username, limit):
    items, cursor, seen = [], "", set()
    for _ in range(20):
        payload = {"username": username, "page_size": 20, "raw": False}
        if cursor:
            payload["offset"] = cursor
        page = client.post("wechat_mp/v2/fetch_account_articles", payload)
        if page.get("biz_username") and page["biz_username"] != username:
            raise RuntimeError("分页返回的公众号身份与种子文章不符")
        items.extend(page.get("articles") or [])
        selected = unique_latest(items, limit)
        if len(selected) >= limit or page.get("is_end"):
            return selected
        cursor = page.get("next_offset")
        if not cursor or cursor in seen:
            raise RuntimeError("公众号分页游标缺失或重复，无法证明已经取得最新60篇")
        seen.add(cursor)
    raise RuntimeError("分页达到上限，未取得足够的不重复文章")


def detail(client, item, username):
    data = client.post("wechat_mp/v2/fetch_article_detail_h5",
                       {"url": clean_url(item["url"]), "raw": False})
    content = data.get("content") or {}
    if content.get("user_name") != username:
        raise RuntimeError("文章详情的公众号身份与目标账号不符")
    body = content.get("content_noencode") or content.get("content_text") or ""
    if len(re.sub(r"<[^>]+>", "", body).strip()) < 100:
        raise RuntimeError("正文过短或不可读，未记作下载成功")
    return {"item": item, "content": content, "body": body,
            "source": clean_url(content.get("link") or data.get("url") or item["url"])}


def write_article(result, folder, acquired):
    item, content, body = result["item"], result["content"], result["body"]
    title = content.get("title") or item.get("title") or "未命名文章"
    stem = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", title).strip(" .")[:110] or "未命名文章"
    digest = hashlib.sha256(body.encode("utf-8")).hexdigest()
    # 同一公开链接已经有用户提供的原文时，引用它，不改写为接口版本。
    urls = {result["source"], clean_url(item["url"])}
    for original in folder.parent.glob("*.md"):
        existing = original.read_text(encoding="utf-8-sig")
        match = re.search(r'^source:\s*"(https://mp\.weixin\.qq\.com/[^"\s]+)"\s*$', existing, re.M)
        if match and clean_url(match.group(1)) in urls:
            return {"id": article_id(item), "title": title, "url": result["source"],
                    "published": content.get("create_time"), "status": "reused_existing",
                    "raw_path": original.relative_to(ROOT).as_posix(),
                    "raw_sha256": hashlib.sha256(original.read_bytes()).hexdigest()}
    # 内容变更产生新的原始快照，同一次快照重跑复用；绝不覆盖旧文件。
    identity_hash = hashlib.sha256(article_id(item).encode("utf-8")).hexdigest()[:8]
    path = folder / f"{stem}-{identity_hash}-{digest[:10]}.md"
    metadata = {
        "title": title, "source": result["source"],
        "author": content.get("author") or content.get("nick_name"),
        "account": content.get("nick_name"), "account_username": content.get("user_name"),
        "published": content.get("create_time"), "downloaded_at": acquired,
        "downloaded_via": "TikHub WeChat MP V2 H5", "body_sha256": digest,
    }
    text = "---\n" + "\n".join(f"{key}: {json.dumps(value, ensure_ascii=False)}"
                                for key, value in metadata.items()) + "\n---\n\n" + body + "\n"
    status = "downloaded"
    try:
        with path.open("x", encoding="utf-8") as output:
            output.write(text)
    except FileExistsError:
        existing = path.read_text(encoding="utf-8")
        saved_body = existing.split("\n---\n\n", 1)[-1]
        if (f'body_sha256: "{digest}"' not in existing or saved_body != body + "\n"
                or f'source: {json.dumps(result["source"], ensure_ascii=False)}' not in existing):
            raise RuntimeError("文件名冲突，已停止以保护已有原始资料")
        status = "reused"
    return {"id": article_id(item), "title": title, "url": result["source"],
            "published": content.get("create_time"), "status": status,
            "raw_path": path.relative_to(ROOT).as_posix(), "body_sha256": digest}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--key-file", help="本机凭据文件；不会写入仓库或采集结果")
    parser.add_argument("--seed-url", default=SEED_URL)
    parser.add_argument("--limit", type=int, choices=range(1, 61), default=60)
    parser.add_argument("--probe", action="store_true", help="只验证密钥和目标公众号身份")
    args = parser.parse_args()
    client = TikHubClient(read_key(args.key_file))
    seed = client.post("wechat_mp/v2/fetch_article_detail_h5", {"url": clean_url(args.seed_url), "raw": False})
    identity = seed.get("content") or {}
    username, nickname = identity.get("user_name"), identity.get("nick_name")
    if not username or nickname not in ("路人甲TM", "路人甲"):
        raise RuntimeError("种子链接未返回已知目标账号，停止下载以避免串号")
    print(f"已验证TikHub与目标账号：{nickname}", flush=True)
    if args.probe:
        return
    selected = account_articles(client, username, args.limit)
    acquired = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")
    folder = ROOT / "raw/article/lurenjiaTM/最新60篇下载"
    folder.mkdir(parents=True, exist_ok=True)
    entries = []
    with ThreadPoolExecutor(max_workers=2) as pool:
        pending = {pool.submit(detail, client, item, username): item for item in selected}
        for future in as_completed(pending):
            item = pending[future]
            try:
                entries.append(write_article(future.result(), folder, acquired))
            except Exception as error:
                message = str(error).replace(client.key, "[已隐藏凭据]")
                entries.append({"id": article_id(item), "title": item.get("title"),
                                "url": clean_url(item["url"]), "status": "failed", "error": message})
            print(f"处理进度 {len(entries)}/{len(selected)}；成功 {sum(e['status'] != 'failed' for e in entries)}", flush=True)
    rank = {article_id(item): i for i, item in enumerate(selected)}
    entries.sort(key=lambda x: rank[x["id"]])
    complete = len(entries) == args.limit and all(e["status"] != "failed" for e in entries)
    manifest = {"account": nickname, "account_username": username, "requested": args.limit,
                "acquired_at": acquired, "complete": complete,
                "scope": "公众号文章栏目最新去重图文；保留原始HTML正文与媒体链接，未下载媒体文件", "articles": entries}
    output = ROOT / "output/ai-wechat-methodology/路人甲TM最新60篇下载清单.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if not complete:
        raise RuntimeError("本次未完整取得目标数量，详见下载清单；未宣称60篇全部成功")
    print(f"完成：{len(entries)}篇正文，清单与原始资料已保存。", flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        # 网络层仅报状态；凭据值不出现在此输出。
        print(f"未完成：{exc}")
        raise SystemExit(1)
