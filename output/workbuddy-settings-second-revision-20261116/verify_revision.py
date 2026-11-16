"""核对第二节独立改稿，原稿只读，提示词逐字保留。"""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
META = json.loads((HERE / "revision.json").read_text(encoding="utf-8"))

def read_raw(name):
    return (HERE / name).read_bytes().decode("utf-8")

class RevisionChecks(unittest.TestCase):
    def test_prompt_preserved_byte_for_byte(self):
        pattern = r"```自定义指令[\s\S]*?```"
        before = re.findall(pattern, read_raw(META["original_section"]))
        after = re.findall(pattern, read_raw(META["draft"]))
        self.assertEqual(len(before), 1)
        self.assertEqual(before, after)
        self.assertEqual(hashlib.sha256(after[0].encode()).hexdigest(), META["prompt_sha256"])

    def test_media_preserved(self):
        pattern = r"!\[\[(.*?)\]\]"
        self.assertEqual(re.findall(pattern, read_raw(META["draft"])),
                         re.findall(pattern, read_raw(META["original_section"])))
        data = (HERE / "assets" / META["image"]["name"]).read_bytes()
        self.assertEqual(hashlib.sha256(data).hexdigest(), META["image"]["sha256"])

    def test_only_second_setting_is_delivered(self):
        draft = read_raw(META["draft"])
        self.assertEqual(len(re.findall(r"^## ", draft, re.M)), 1)
        self.assertNotIn("先看存储路径", draft)
        self.assertNotIn("XXX", draft)
        self.assertIn("只优化第二个设置", META["scope"])

    def test_length_report_matches_delivered_section(self):
        path = ROOT / ".agents/skills/wechat-article-writing/scripts/check_article_length.py"
        spec = importlib.util.spec_from_file_location("length", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertEqual(module.check_length(read_raw(META["draft"])), META["length"])

if __name__ == "__main__":
    unittest.main()
