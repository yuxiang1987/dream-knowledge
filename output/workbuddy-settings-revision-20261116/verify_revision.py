"""只读核对本轮改稿的范围、原稿和媒体完整性。"""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
META = json.loads((HERE / "revision.json").read_text(encoding="utf-8"))


class RevisionChecks(unittest.TestCase):
    def test_original_unchanged(self):
        source = ROOT / META["source"]
        self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), META["source_sha256"])

    def test_media_preserved_in_order_and_readable(self):
        draft = (HERE / META["draft"]).read_text(encoding="utf-8")
        refs = re.findall(r"!\[[^\]]*\]\(assets/([^)]*)\)", draft)
        self.assertEqual(refs, [item["name"] for item in META["media"]])
        for item in META["media"]:
            with self.subTest(name=item["name"]):
                data = (HERE / "assets" / item["name"]).read_bytes()
                self.assertTrue(data.startswith(b"\x89PNG\r\n\x1a\n"))
                self.assertEqual(hashlib.sha256(data).hexdigest(), item["sha256"])

    def test_scope_remains_one_setting(self):
        source = (ROOT / META["source"]).read_text(encoding="utf-8")
        draft = (HERE / META["draft"]).read_text(encoding="utf-8")
        self.assertEqual(len(re.findall(r"^## ", draft, re.M)), len(re.findall(r"^## ", source, re.M)))
        self.assertNotIn("已完成迁移", draft)
        self.assertTrue(META["pending"])

    def test_length_is_reported_as_fragment(self):
        path = ROOT / ".agents/skills/wechat-article-writing/scripts/check_article_length.py"
        spec = importlib.util.spec_from_file_location("article_length", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        result = module.check_length((HERE / META["draft"]).read_text(encoding="utf-8"))
        self.assertEqual(result, META["length"])
        self.assertIn("非完整正文", META["scope"])


if __name__ == "__main__":
    unittest.main()
