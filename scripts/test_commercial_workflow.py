"""验收商业流程文档的可执行关口、来源边界和入口，不验证经营收益。"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "wiki/topics/AI公众号商单商业闭环.md"
LINK = "[[topics/AI公众号商单商业闭环]]"


class CommercialWorkflowTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = PAGE.read_text(encoding="utf-8")

    def test_each_stage_has_actionable_gate_and_failure_path(self):
        stages = re.findall(
            r"^### (\d)\. (.*?)(?=^### |^## |\Z)",
            self.text, re.M | re.S,
        )
        self.assertEqual([number for number, _ in stages], list("12345678"))
        for number, stage in stages:
            with self.subTest(stage=number):
                for field in ("**输入**", "**动作**", "**产物**",
                              "**过关条件**", "**未过关时**"):
                    self.assertIn(field, stage)

    def test_sources_and_uncertainty_are_explicit(self):
        self.assertIn("sources: []", self.text)
        self.assertIn("status: 草稿", self.text)
        for evidence in (
            "https://www.biji.com/note/share_note/7gvozqXeM4Lmb",
            "E:/work/note/笔记/笔记/易洋-AI公众号商单.md",
            "不是两项独立验证", "不是 30 天接单承诺",
            "未在本次独立核实", "统计口径未对齐",
            "未复制、修改原始材料", "尚未在",
        ):
            with self.subTest(evidence=evidence):
                self.assertIn(evidence, self.text)

    def test_economics_and_cash_are_separate(self):
        for requirement in (
            "单笔订单贡献 =", "当期经营结余 =", "当期现金净流入 =",
            "不重复", "自然来源、付费来源", "预算到顶", "垫款峰值",
            "应收", "到账", "实际复投才记复购", "率的分母为 0",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, self.text)

    def test_schedule_and_discovery(self):
        for week in range(1, 5):
            self.assertIn(f"第 {week} 周", self.text)
        self.assertIn("四张表和一个证据目录", self.text)
        index = (ROOT / "wiki/index.md").read_text(encoding="utf-8")
        pipeline = (ROOT / "wiki/topics/公众号内容生产线.md").read_text(encoding="utf-8")
        self.assertIn(LINK, index)
        self.assertIn(LINK, pipeline)
        page_count = sum(
            p.name not in ("index.md", "log.md")
            for p in (ROOT / "wiki").rglob("*.md")
        )
        self.assertIn(f"知识页：{page_count} 页", index)


if __name__ == "__main__":
    unittest.main()
