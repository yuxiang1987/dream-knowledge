"""核对切入点归纳的原文身份和证据边界；不验证传播或商业效果。"""
import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "wiki/topics/公众号文章切入点方法.md"


class EntrypointEvidenceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = PAGE.read_text(encoding="utf-8")
        cls.section = cls.text.split("## 2026-10-16：最新60篇的切入点归纳", 1)[1].split("## 当前进展", 1)[0]
        data = json.loads((ROOT / "output/ai-wechat-methodology/路人甲TM六十篇拆解台账.json").read_text(encoding="utf-8"))
        cls.articles = {a["id"]: a for a in data["articles"]}

    def test_each_representative_resolves_to_the_same_source_and_unchanged_raw(self):
        refs = re.findall(r"(LRJ60-\d+)：\[\[([^\]]+)\]\]", self.section)
        self.assertEqual(len(refs), 8)
        self.assertEqual(len(set(a for a, _ in refs)), 8)
        source_list = self.text.split("sources: [", 1)[1].split("]", 1)[0]
        for article_id, link in refs:
            with self.subTest(article=article_id):
                a = self.articles[article_id]
                self.assertEqual("wiki/" + link + ".md", a["source_page"])
                self.assertTrue((ROOT / a["source_page"]).is_file())
                self.assertIn(a["raw_path"], source_list)
                self.assertEqual(hashlib.sha256((ROOT / a["raw_path"]).read_bytes()).hexdigest(), a["raw_sha256"])

    def test_case_motivation_is_not_misreported_as_the_opening(self):
        self.assertIn("此处是案例引入；首段先讲产品疑问", self.section)
        self.assertIn("原文开头先问同类设计Agent这么多", self.section)
        expected = {"LRJ60-14": "我很想把这个动作拍出来", "LRJ60-59": "带着这个脑洞", "LRJ60-24": "我估计很多人跟我一样懵逼", "LRJ60-58": "为啥腾讯要再出一个"}
        for article_id, evidence in expected.items():
            text = (ROOT / self.articles[article_id]["readable_path"]).read_text(encoding="utf-8")
            self.assertIn(evidence, text)

    def test_editorial_categories_do_not_invent_frequencies_or_effects(self):
        for caveat in ("本知识库的编辑归纳", "类别不互斥", "未给60篇逐一标记", "不统计占比", "不代表作者真实接单", "本批没有采集完整评论区"):
            self.assertIn(caveat, self.section)
        self.assertIn("原文业务数字及效果不在本次重新核实", self.text)
        self.assertIn("2026-10-01将节日列为待补证建议", self.section)

    def test_next_day_candidate_remains_unconfirmed_and_indexed(self):
        for boundary in ("明确标注合成", "并非用户已确认", "已锁定题目或已完成实测", "只覆盖八类中的一类"):
            self.assertIn(boundary, self.section)
        self.assertIn("[[topics/公众号每日选题决策]]", self.section)
        self.assertIn("[[topics/公众号文章切入点方法]]", (ROOT / "wiki/index.md").read_text(encoding="utf-8"))

    def test_data_source_plan_does_not_claim_a_nonexistent_installed_skill_or_collection(self):
        installed = json.loads((ROOT / "scripts/installed_skills.json").read_text(encoding="utf-8"))
        self.assertIn("wechat-article-writing", installed["skills"])
        self.assertTrue((ROOT / ".agents/skills/wechat-article-writing/references/case-and-hook-selection.md").is_file())
        self.assertNotIn("gzh-entrypoint", installed["skills"])
        self.assertFalse((ROOT / "skills/gzh-entrypoint").exists())
        self.assertIn("不能据旧记录声称它目前可调用", self.text)
        self.assertIn("不代表已接通任何来源、已采评论或已安排持续监控", self.text)
        self.assertIn("尚未修改或新建Skill", self.text)
        self.assertIn("不必先开发API或自动采集", self.text)


if __name__ == "__main__":
    unittest.main()
