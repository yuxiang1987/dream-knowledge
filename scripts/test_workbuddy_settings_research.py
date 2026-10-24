"""检查 WorkBuddy 设置调研入库的结构、待核实边界与双向保留，不验证产品行为。"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "wiki/sources/WorkBuddy官方设置文档核对.md"
TOPIC = ROOT / "wiki/topics/WorkBuddy设置技巧文章.md"
INDEX = ROOT / "wiki/index.md"
LOG = ROOT / "wiki/log.md"
LINK = "[[sources/WorkBuddy官方设置文档核对]]"

BENCHMARKS = (
    "wiki/sources/阿胖WorkBuddy设置文章拆解.md",
    "wiki/sources/大刘WorkBuddy设置文章拆解.md",
)

OFFICIAL_FACTS = (
    "200K",
    "3000 MB",
    "50 个",
    "快速",
    "均衡",
    "极致",
    "自动安装可信技能",
    "完全访问",
    "沙箱",
    "Max 模式",
)


class WorkBuddySettingsResearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = PAGE.read_text(encoding="utf-8")
        cls.topic = TOPIC.read_text(encoding="utf-8")
        cls.index = INDEX.read_text(encoding="utf-8")
        cls.log = LOG.read_text(encoding="utf-8")

    def test_frontmatter_and_page_type(self):
        front = self.text.split("---", 2)[1]
        self.assertIn("title: WorkBuddy官方设置文档核对", front)
        self.assertIn("type: source", front)
        self.assertIn("status: 待核实", front)
        self.assertIn("sources: []", front)
        for field in ("created:", "updated:"):
            self.assertRegex(front, rf"(?m)^{field}\s*2026-10-24$")

    def test_access_limit_and_pending_status_are_declared(self):
        for marker in ("ERR_CONNECTION_CLOSED", "逐字通读",
                       "status: 待核实", "发布前"):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.text)
        self.assertIn("检索日期 2026-10-24", self.text)

    def test_official_facts_are_recorded_with_sources(self):
        for fact in OFFICIAL_FACTS:
            with self.subTest(fact=fact):
                self.assertIn(fact, self.text)
        for doc in ("Function-Description/Setting", "Function-Description/Memory",
                    "Function-Description/Model", "Function-Description/Permission-Modes"):
            with self.subTest(doc=doc):
                self.assertIn(doc, self.text)

    def test_conflicts_are_kept_on_both_sides(self):
        table = self.text.split("## 与两篇对标文章结论相反的地方", 1)[1]
        for benchmark in BENCHMARKS:
            name = Path(benchmark).stem
            with self.subTest(benchmark=name):
                self.assertIn(f"[[sources/{name}]]", table)
        for topic in ("是否开完全访问", "上下文要不要调大"):
            with self.subTest(topic=topic):
                self.assertIn(topic, table)
        self.assertIn("官方文档内部口径不一致的地方", self.text)
        self.assertIn("200K", self.text)

    def test_benchmark_pages_stay_unverified(self):
        for relative in BENCHMARKS:
            with self.subTest(page=relative):
                text = (ROOT / relative).read_text(encoding="utf-8")
                self.assertIn("以下“作者报告”不代表本库已验证", text)
                self.assertNotIn("已独立核实", text)

    def test_topic_page_links_research_and_keeps_draft_status(self):
        self.assertIn(LINK, self.topic)
        self.assertRegex(self.topic, r"(?m)^status: 草稿$")
        for boundary in ("当前均未实测", "未重新联网核实"):
            with self.subTest(boundary=boundary):
                self.assertIn(boundary, self.topic)
        self.assertIn("官方文档核对后需要修正的三处", self.topic)
        self.assertIn("本轮实测设计", self.topic)

    def test_index_and_log_are_updated(self):
        self.assertIn(LINK, self.index)
        count = sum(path.name not in {"index.md", "log.md"}
                    for path in (ROOT / "wiki").rglob("*.md"))
        self.assertEqual(int(re.search(r"知识页：(\d+) 页", self.index).group(1)), count)
        entry = re.search(r"(?m)^## \[2026-10-24\] (\S+) \| (\S.*)$", self.log)
        self.assertIsNotNone(entry)
        self.assertEqual(entry.group(1), "ingest")
        self.assertIn("WorkBuddy官方设置文档核对.md", self.log)


if __name__ == "__main__":
    unittest.main()
