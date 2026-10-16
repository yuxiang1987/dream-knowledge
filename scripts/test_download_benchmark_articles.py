"""不消耗付费接口；验证分页、身份隔离及原始资料保护。"""
import hashlib
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import download_benchmark_articles as mod


class Client:
    def __init__(self, pages):
        self.pages = iter(pages)
        self.payloads = []

    def post(self, endpoint, payload):
        self.payloads.append(payload)
        return next(self.pages)


def item(i):
    return {"app_msg_id": str(i), "idx": 1, "url": f"https://mp.weixin.qq.com/s/a{i}",
            "title": "标题", "create_time": i}


class DownloadTest(unittest.TestCase):
    def test_public_urls_strip_tracking_and_reject_other_hosts(self):
        self.assertEqual(mod.clean_url("https://mp.weixin.qq.com/s?mid=12&idx=1&poc_token=secret#abc"),
                         "https://mp.weixin.qq.com/s?mid=12&idx=1")
        for url in ("https://mp.weixin.qq.com.evil/s/a", "http://mp.weixin.qq.com/s/a",
                    "https://user@mp.weixin.qq.com/s/a", "https://mp.weixin.qq.com/settings"):
            with self.assertRaises(ValueError):
                mod.clean_url(url)

    def test_pagination_deduplicates_and_keeps_latest(self):
        client = Client([{"articles": [item(3), item(2)], "next_offset": "next"},
                         {"articles": [item(2), item(1)], "is_end": True}])
        result = mod.account_articles(client, "gh_target", 3)
        self.assertEqual([r["app_msg_id"] for r in result], ["3", "2", "1"])
        self.assertEqual(client.payloads[1]["offset"], "next")
        self.assertEqual(mod.article_id(item(1234567890123456789)), "1234567890123456789:1")

    def test_bad_cursors_and_mixed_accounts_stop(self):
        for pages in ([{"articles": []}],
                      [{"articles": [], "next_offset": "x"}, {"articles": [], "next_offset": "x"}],
                      [{"biz_username": "other", "articles": [item(1)]}]):
            with self.assertRaises(RuntimeError):
                mod.account_articles(Client(pages), "gh_target", 60)

    def test_detail_rejects_other_accounts_and_empty_bodies(self):
        for content in ({"user_name": "other", "content_text": "正文" * 100},
                        {"user_name": "gh_target", "content_text": ""}):
            with self.assertRaises(RuntimeError):
                mod.detail(Client([{"content": content}]), item(1), "gh_target")

    def test_snapshots_never_overwrite_and_distinguish_articles(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(mod, "ROOT", Path(tmp)):
            folder = Path(tmp) / "raw" / "download"
            folder.mkdir(parents=True)
            result = {"item": item(1), "content": {"title": "标题"}, "body": "正文" * 100,
                      "source": item(1)["url"]}
            first = mod.write_article(result, folder, "2026-10-16")
            path = Path(tmp) / first["raw_path"]
            before = path.read_bytes()
            self.assertEqual(mod.write_article(result, folder, "later")["status"], "reused")
            self.assertEqual(path.read_bytes(), before)
            changed = dict(result, body="新正文" * 100)
            self.assertNotEqual(mod.write_article(changed, folder, "later")["raw_path"], first["raw_path"])
            other = dict(result, item=item(2), source=item(2)["url"])
            self.assertNotEqual(mod.write_article(other, folder, "later")["raw_path"], first["raw_path"])
            path.write_text(before.decode("utf-8").replace("正文", "篡改"), encoding="utf-8")
            with self.assertRaises(RuntimeError):
                mod.write_article(result, folder, "later")

    def test_reuse_user_supplied_raw_without_changes(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(mod, "ROOT", Path(tmp)):
            folder = Path(tmp) / "raw" / "download"
            folder.mkdir(parents=True)
            original = folder.parent / "原文.md"
            original.write_text('---\nsource: "https://mp.weixin.qq.com/s/a1"\n---\n原始正文', encoding="utf-8")
            before = original.read_bytes()
            result = {"item": item(1), "content": {"title": "标题"}, "body": "正文" * 100,
                      "source": item(1)["url"]}
            entry = mod.write_article(result, folder, "2026-10-16")
            self.assertEqual(entry["status"], "reused_existing")
            self.assertEqual(entry["raw_sha256"], hashlib.sha256(before).hexdigest())
            self.assertEqual(original.read_bytes(), before)
            self.assertEqual(list(folder.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
