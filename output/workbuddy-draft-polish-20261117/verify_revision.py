"""校验本轮三节改稿的原稿、提示词、媒体与范围。"""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
META = json.loads((HERE / "revision.json").read_text(encoding="utf-8"))
BEFORE = (HERE / META["snapshot"]).read_bytes().decode("utf-8")
AFTER = (HERE / META["draft"]).read_bytes().decode("utf-8")

class RevisionChecks(unittest.TestCase):
    def test_source_untouched_and_snapshot_intact(self):
        digest = META["source_snapshot_sha256"]
        self.assertEqual(hashlib.sha256((ROOT / META["source"]).read_bytes()).hexdigest(), digest)
        self.assertEqual(hashlib.sha256((HERE / META["snapshot"]).read_bytes()).hexdigest(), digest)

    def test_prompt_preserved(self):
        pattern = r"```自定义指令[\s\S]*?```"
        original = re.findall(pattern, BEFORE)
        revised = re.findall(pattern, AFTER)
        self.assertEqual(len(original), 1)
        self.assertEqual(original, revised)
        self.assertEqual(hashlib.sha256(revised[0].encode()).hexdigest(), META["prompt_sha256"])

    def test_media_order_and_bytes(self):
        refs = r"!\[\[(.*?)\]\]"
        self.assertEqual(re.findall(refs, BEFORE), re.findall(refs, AFTER))
        self.assertEqual(re.findall(refs, AFTER), [item["name"] for item in META["media"]])
        for item in META["media"]:
            self.assertEqual(hashlib.sha256((HERE / "assets" / item["name"]).read_bytes()).hexdigest(), item["sha256"])

    def test_scope_and_length(self):
        self.assertEqual(len(re.findall(r"^## ", AFTER, re.M)), 3)
        self.assertNotIn("XXX", AFTER)
        path = ROOT / ".agents/skills/wechat-article-writing/scripts/check_article_length.py"
        spec = importlib.util.spec_from_file_location("length", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertEqual(module.check_length(AFTER), META["length"])

if __name__ == "__main__":
    unittest.main()
