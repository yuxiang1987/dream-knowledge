"""验收Agent资料覆盖、文图一致性、输出可读性及敏感商务信息边界。

使用带有pypdf和Pillow的工作空间依赖Python运行。
"""
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

from PIL import Image
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/ai-wechat-methodology"
PDF = ROOT / "output/pdf/AI垂类公众号经营全流程.pdf"


class MethodologyDeliverableTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = (OUT / "AI垂类公众号经营方法论.md").read_text(encoding="utf-8")
        cls.svg = ET.parse(OUT / "AI垂类公众号经营全流程.svg")

    def test_complete_agent_reference_and_attribution(self):
        headings = re.findall(r"^## (\d+)\. ", self.text, re.M)
        self.assertEqual(headings, [str(n) for n in range(1, 18)])
        for needed in ("audience: AI Agent", "并非路人甲或易洋的逐字原文",
                       "不能把两位作者的分享描述为两套相互独立",
                       "7gvozqXeM4Lmb", "易洋-AI公众号商单.md", "综合执行设计",
                       "线索、选题、角度与案例", "观察标准", "停止条件",
                       "提报", "实际到账", "单笔订单贡献", "当期经营结余",
                       "不授权Agent自动发消息"):
            with self.subTest(needed=needed):
                self.assertIn(needed, self.text)

    def test_eight_steps_agree_between_reference_svg_and_pdf(self):
        expected = ("定位人群", "选题与案例", "实测与写作", "发布与分发",
                    "询价与获客", "报价与成交", "交付与回款", "复盘与复购")
        ns = {"s": "http://www.w3.org/2000/svg"}
        svg_texts = [node.text for node in self.svg.findall(".//s:text", ns)]
        reader = PdfReader(PDF)
        self.assertEqual(len(reader.pages), 1)
        pdf_text = reader.pages[0].extract_text()
        for step in expected:
            with self.subTest(step=step):
                self.assertIn(step, self.text)
                self.assertIn(step, svg_texts)
                self.assertIn(step, pdf_text)
        self.assertIn("反馈回流", "".join(svg_texts))
        self.assertIn("成交与回款待验证", pdf_text)

    def test_rendered_dimensions_and_embedded_fonts(self):
        with Image.open(OUT / "AI垂类公众号经营全流程.png") as rendered:
            self.assertEqual(rendered.size, (1200, 2200))
            self.assertGreater(len(rendered.getcolors(1000000) or []), 100)
        page = PdfReader(PDF).pages[0]
        self.assertEqual(tuple(float(x) for x in page.mediabox), (0, 0, 600, 1100))
        fonts = page["/Resources"]["/Font"].get_object()
        embedded = [font.get_object().get("/FontDescriptor") for font in fonts.values()]
        self.assertTrue(any(desc and "/FontFile2" in desc.get_object() for desc in embedded))

    def test_current_case_is_not_a_revenue_claim(self):
        for needed in ("7篇文章全部发布", "962粉丝", "52085", "由客户主动联系",
                       "尚无最终确认、履约和回款证据", "全部使用过加热",
                       "尚不明确", "完整商业闭环待验证"):
            self.assertIn(needed, self.text)
        for private_price in ("4500", "5000元", "对私打款", "小凶许"):
            self.assertNotIn(private_price, self.text)
        commercial = (ROOT / "wiki/topics/AI公众号商单商业闭环.md").read_text(encoding="utf-8")
        for filename in ("AI垂类公众号经营方法论.md", "AI垂类公众号经营全流程.png",
                         "AI垂类公众号经营全流程.svg", "AI垂类公众号经营全流程.pdf"):
            self.assertIn(filename, commercial)


if __name__ == "__main__":
    unittest.main()
