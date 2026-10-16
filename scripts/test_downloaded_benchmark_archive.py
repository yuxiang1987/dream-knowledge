"""验收实际下载清单和原文，不验证文章中的产品宣传或商务关系。"""
import hashlib
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "output/ai-wechat-methodology/路人甲TM最新60篇下载清单.json"


class DownloadedArchiveTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_sixty_unique_complete_articles(self):
        manifest = self.manifest
        self.assertEqual(manifest["account"], "路人甲TM")
        self.assertEqual(manifest["account_username"], "gh_d516081071ec")
        self.assertEqual(manifest["requested"], 60)
        self.assertTrue(manifest["complete"])
        entries = manifest["articles"]
        self.assertEqual(len(entries), 60)
        for field in ("id", "url", "raw_path"):
            self.assertEqual(len({e[field] for e in entries}), 60)
        self.assertTrue(all(e["status"] in ("downloaded", "reused", "reused_existing") for e in entries))
        dates = [e["published"] for e in entries]
        self.assertEqual(dates, sorted(dates, reverse=True))

    def test_each_raw_exists_and_body_matches_recorded_hash(self):
        for entry in self.manifest["articles"]:
            with self.subTest(title=entry["title"]):
                path = (ROOT / entry["raw_path"]).resolve()
                self.assertTrue(path.is_relative_to(ROOT / "raw/article/lurenjiaTM"))
                self.assertTrue(path.is_file())
                if entry["status"] == "reused_existing":
                    self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), entry["raw_sha256"])
                    continue
                text = path.read_text(encoding="utf-8")
                front, body = text[4:].split("\n---\n\n", 1)
                metadata = {line.split(": ", 1)[0]: json.loads(line.split(": ", 1)[1])
                            for line in front.splitlines()}
                self.assertEqual(metadata["account_username"], self.manifest["account_username"])
                self.assertEqual(metadata["source"], entry["url"])
                self.assertEqual(metadata["body_sha256"], entry["body_sha256"])
                self.assertEqual(hashlib.sha256(body[:-1].encode("utf-8")).hexdigest(), entry["body_sha256"])
                self.assertGreaterEqual(len(re.sub(r"<[^>]+>", "", body).strip()), 100)

    def test_archive_has_safe_sources_and_no_auth_headers(self):
        text = MANIFEST.read_text(encoding="utf-8")
        for entry in self.manifest["articles"]:
            self.assertTrue(entry["url"].startswith("https://mp.weixin.qq.com/s"))
            self.assertNotIn("poc_token", entry["url"])
            self.assertNotIn("Authorization", (ROOT / entry["raw_path"]).read_text(encoding="utf-8"))
        self.assertNotIn("Bearer ", text)
        self.assertNotIn("TIKHUB_API_KEY", text)

    def test_readable_directory_and_knowledge_index_are_complete(self):
        folder = MANIFEST.parent / "路人甲TM最新60篇可读版"
        self.assertEqual(len(list(folder.glob("*.md"))), 60)
        index = (MANIFEST.parent / "路人甲TM最新60篇文章目录.md").read_text(encoding="utf-8")
        for link in re.findall(r"\]\(([^)]+)\)", index):
            self.assertTrue((MANIFEST.parent / unquote(link)).resolve().is_file(), link)
        for i, entry in enumerate(self.manifest["articles"], 1):
            path = folder / f"{i:02d}-{Path(entry['raw_path']).name}"
            text = path.read_text(encoding="utf-8")
            self.assertIn(entry["title"], text)
            self.assertIn(entry["url"], text)
            self.assertGreater(len(text.split("\n---\n", 1)[1].strip()), 100)
        wiki = (ROOT / "wiki/index.md").read_text(encoding="utf-8")
        self.assertIn("路人甲TM最新60篇文章目录.md", wiki)
        actual = len(list((ROOT / "raw").rglob("*.md")))
        self.assertEqual(int(re.search(r"原始资料：(\d+) 篇", wiki).group(1)), actual)


if __name__ == "__main__":
    unittest.main()
