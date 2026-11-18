"""校验完整讨论稿的原始材料、提示词、图像、范围和字数。"""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
META = json.loads((HERE / "draft-record.json").read_text(encoding="utf-8"))
TEXT = (HERE / META["draft"]).read_bytes().decode("utf-8")
ORIGINAL = (HERE / META["snapshot"]).read_bytes().decode("utf-8")

class FullDraftChecks(unittest.TestCase):
    def test_raw_sources_untouched(self):
        self.assertEqual(hashlib.sha256((ROOT / META["source"]).read_bytes()).hexdigest(), META["source_sha256"])
        self.assertEqual(hashlib.sha256((HERE / META["snapshot"]).read_bytes()).hexdigest(), META["source_sha256"])
        self.assertEqual(hashlib.sha256((ROOT / META["benchmark"]).read_bytes()).hexdigest(), META["benchmark_sha256"])

    def test_user_prompt_preserved_verbatim(self):
        pattern = r"```自定义指令[\s\S]*?```"
        before, after = re.findall(pattern, ORIGINAL), re.findall(pattern, TEXT)
        self.assertEqual(len(before), 1)
        self.assertEqual(before, after)
        self.assertEqual(hashlib.sha256(after[0].encode()).hexdigest(), META["prompt_sha256"])

    def test_all_media_exist_and_originals_keep_order(self):
        names = re.findall(r"!\[\[(.*?)\]\]", TEXT)
        self.assertEqual(names, [item["name"] for item in META["media"]])
        self.assertEqual([name for name in names if name in META["original_media"]], META["original_media"])
        for item in META["media"]:
            data = (HERE / "assets" / item["name"]).read_bytes()
            self.assertTrue(data.startswith(b"\x89PNG\r\n\x1a\n"))
            self.assertEqual(hashlib.sha256(data).hexdigest(), item["sha256"])

    def test_seven_sections_and_user_scope(self):
        self.assertEqual(re.findall(r"^## (0[1-7]) ", TEXT, re.M), [f"{i:02}" for i in range(1, 8)])
        self.assertNotIn("云端记忆", TEXT)
        self.assertNotIn("数据导入", TEXT)
        self.assertNotIn("XXX", TEXT)
        self.assertEqual(len(re.findall(r"【待补图：[^】]+】", TEXT)), 3)
        self.assertEqual(set(re.findall(r"\]\((https://[^)]+)\)", TEXT)), set(META["source_urls"]))

    def test_length_and_fixed_bio(self):
        path = ROOT / ".agents/skills/wechat-article-writing/scripts/check_article_length.py"
        spec = importlib.util.spec_from_file_location("length", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        result = module.check_length(TEXT)
        self.assertEqual(result, META["length"])
        self.assertTrue(result["passed"])
        self.assertEqual(TEXT.count(module.AUTHOR_BIO), 1)

if __name__ == "__main__":
    unittest.main()
