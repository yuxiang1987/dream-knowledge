"""核对七篇文章数据与实施状态；不将询价、混合阅读当作经营收益。"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "wiki/topics/公众号商单实施复盘.md"
LINK = "[[topics/公众号商单实施复盘]]"


class CommercialProgressTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = PAGE.read_text(encoding="utf-8")

    def test_seven_real_sources_and_snapshot_rows(self):
        source_line = next(x for x in self.text.splitlines()
                           if x.startswith("sources: ["))
        sources = source_line.removeprefix("sources: [").removesuffix("]").split(", ")
        self.assertEqual(len(sources), 7)
        for source in sources:
            self.assertTrue((ROOT / source).is_file(), source)
        rows = re.findall(
            r"^\| ([^|]+) \| ([^|]+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|$",
            self.text, re.M,
        )
        self.assertEqual(len(rows), 7)
        self.assertEqual([int(row[2]) for row in rows],
                         [1599, 9312, 8680, 11518, 8446, 11227, 1303])
        self.assertEqual(sum(int(row[2]) for row in rows), 52085)
        self.assertEqual(sum(int(row[4]) for row in rows), 5432)
        for total in ("52085", "8680", "22745", "4638", "5432"):
            self.assertIn(total, self.text)

    def test_screenshots_and_metric_boundaries(self):
        for number in (1, 2):
            screenshot = (ROOT / "wiki/assets/公众号商单实施数据"
                          / f"2026-10-16-后台截图-{number}.png")
            self.assertTrue(screenshot.is_file())
            self.assertEqual(screenshot.read_bytes()[:8], b"\x89PNG\r\n\x1a\n")
        for boundary in ("自然与付费混合", "不同累积时长", "次数/人数",
                         "具体日期待确认", "962", "获粉成本", "归因"):
            self.assertIn(boundary, self.text)

    def test_inbound_lead_is_not_a_completed_order(self):
        for fact in ("7 篇文章均已发布", "7 篇都使用了加热", "客户主动联系",
                     "入站询价", "提报", "尚未见最终合作确认",
                     "不等于客户接受价格", "本机复盘文件", "不能断定已完成提报"):
            self.assertIn(fact, self.text)

    def test_current_pages_point_to_progress(self):
        for relative in ("wiki/index.md", "wiki/entities/程序员拾梦.md",
                         "wiki/topics/公众号内容生产线.md",
                         "wiki/topics/AI公众号商单商业闭环.md",
                         "wiki/sources/公众号定位与写作风格规范.md"):
            with self.subTest(page=relative):
                self.assertIn(LINK, (ROOT / relative).read_text(encoding="utf-8"))
        account = (ROOT / "wiki/entities/程序员拾梦.md").read_text(encoding="utf-8")
        self.assertNotIn("新账号，尚无真实读者反馈数据", account)


if __name__ == "__main__":
    unittest.main()
