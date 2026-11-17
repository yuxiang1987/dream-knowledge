"""校验五节续稿的范围、待补材料、引用和字数，不实测产品。"""
import importlib.util
import json
from pathlib import Path
import re
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
META = json.loads((HERE / "draft-record.json").read_text(encoding="utf-8"))
TEXT = (HERE / META["draft"]).read_text(encoding="utf-8")

class DraftChecks(unittest.TestCase):
    def test_five_requested_sections_only(self):
        headings = re.findall(r"^## (.+)$", TEXT, re.M)
        self.assertEqual(len(headings), 5)
        for name, heading in zip(["回复风格", "记忆", "Skill", "模型", "恢复"], headings):
            self.assertIn(name, heading)

    def test_missing_demonstrations_stay_explicit(self):
        markers = re.findall(r"【待插入：([^】]+)】", TEXT)
        self.assertEqual(len(markers), 3)
        self.assertTrue(any("真实输出" in item for item in markers))
        self.assertTrue(any("复用" in item for item in markers))
        self.assertTrue(any("恢复" in item for item in markers))
        self.assertNotIn("我实测发现", TEXT)

    def test_source_links_and_fences_are_complete(self):
        self.assertEqual(set(re.findall(r"\]\((https://[^)]+)\)", TEXT)), set(META["source_urls"]))
        self.assertEqual(sum(line.startswith("```") for line in TEXT.splitlines()) % 2, 0)

    def test_length_matches_delivered_draft(self):
        path = ROOT / ".agents/skills/wechat-article-writing/scripts/check_article_length.py"
        spec = importlib.util.spec_from_file_location("length", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertEqual(module.check_length(TEXT), META["length"])
        self.assertTrue(META["combined_length_at_read"]["passed"])

if __name__ == "__main__":
    unittest.main()
