"""一次性：通过 TikHub 文章列表接口取各号封面 URL，不重复调用付费接口。

用法：python fetch_covers.py
凭据只从 TIKHUB_API_KEY 或 <知识库>/.local/tikhub.json 读取，不写入任何文件。
"""
import importlib.util
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
SKILL = ROOT / ".agents/skills/gzh-benchmark-radar/scripts/ingest.py"
OUT = pathlib.Path(__file__).resolve().parent


def load_module():
    spec = importlib.util.spec_from_file_location("ingest", SKILL)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    ing = load_module()
    accounts = json.loads((ROOT / ".agents/skills/gzh-benchmark-radar/references/accounts.example.json")
                          .read_text(encoding="utf-8"))["accounts"]
    key = ing.load_key(ROOT)
    if not key:
        print("未找到凭据")
        return 1
    client = ing.Client(key)
    rows, calls = [], 0
    for account in accounts:
        name = account["name"]
        data, _ = client.post("wechat_mp/v2/fetch_account_articles",
                              {"username": account["username"], "page_size": 30, "raw": False}, tries=1)
        calls += 1
        items = data.get("articles") or []
        if data.get("biz_username") and data["biz_username"] != account["username"]:
            print(f"{name}：身份不符，跳过")
            continue
        for item in items:
            covers = item.get("covers") or {}
            rows.append({
                "account": name,
                "username": account["username"],
                "title": item.get("title"),
                "digest": item.get("digest"),
                "url": item.get("url"),
                "app_msg_id": item.get("app_msg_id"),
                "idx": item.get("idx"),
                "create_time": item.get("create_time"),
                "cover": item.get("cover"),
                "cover_235_1": covers.get("235_1"),
                "cover_16_9": covers.get("16_9"),
                "cover_3_4": covers.get("3_4"),
                "cover_1_1": covers.get("1_1"),
            })
        print(f"{name}：{len(items)} 篇")
    (OUT / "covers-index.json").write_text(
        json.dumps({"fetched_at_calls": calls, "accounts": len(accounts), "articles": len(rows),
                    "note": "cover 为原图地址；covers 为各裁剪比例，235_1 即 2.35:1 首图",
                    "items": rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"完成：{len(rows)} 篇，付费调用 {calls} 次")
    return 0


if __name__ == "__main__":
    sys.exit(main())
