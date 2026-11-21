"""Offline checks for this batch's evidence, source ownership and final report."""
import hashlib
import json
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

BATCH = Path(__file__).resolve().parent
ROOT = BATCH.parents[2]


class BodyText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        self.skip += tag in {"script", "style", "svg"}

    def handle_endtag(self, tag):
        self.skip -= tag in {"script", "style", "svg"} and self.skip > 0

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def read(path):
    return (ROOT / path).read_text(encoding="utf-8-sig")


def visible_body(path):
    parser = BodyText()
    parser.feed(read(path).split("---", 2)[2])
    return re.sub(r"\s+", "", "".join(parser.parts))


class DailyEvidence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = json.loads(read(BATCH / "coverage.json"))
        cls.fetch = json.loads(read(BATCH / "fetch-summary.json"))
        cls.report = json.loads(read(BATCH / "report.json"))
        cls.index = read("wiki/index.md").split("## 雷达2026-11-21新增拆解与筛选登记", 1)[1].split("\n## ", 1)[0]

    def test_each_capture_has_one_disposition(self):
        expected = [(a["account"], r["id"], r["url"], r["raw_path"]) for a in self.fetch["accounts"]
                    for r in a["added_articles"]]
        actual = [(r["account"], r["id"], r["url"], r["raw_path"]) for r in self.rows]
        self.assertCountEqual(actual, expected)
        self.assertEqual(len(actual), len({r[3] for r in actual}))
        self.assertCountEqual([r["disposition"] for r in self.rows],
                              ["excluded", "reused", "deep", "deep", "deep", "deep"])

    def test_anchored_evidence_and_only_one_source_owner(self):
        sources = {p.relative_to(ROOT).as_posix(): read(p).split("---", 2)[1]
                   for p in (ROOT / "wiki/sources").glob("*.md")}
        for row in self.rows:
            path = row["raw_path"]
            with self.subTest(path=path):
                self.assertEqual(hashlib.sha256((ROOT / path).read_bytes()).hexdigest(), row["raw_sha256"])
                body = visible_body(path)
                self.assertGreaterEqual(len(set(row["anchors"])), 2)
                for anchor in row["anchors"]:
                    self.assertIn(re.sub(r"\s+", "", anchor), body)
                author_section = re.search(r"(?m)^## [^\n]*2026-11-21[^\n]*\n", read(row["author_path"]))
                self.assertIsNotNone(author_section)
                author = author_section.string[author_section.end():].split("\n## ", 1)[0]
                self.assertIn(path, author)
                source = row["source_path"]
                owners = [p for p, front in sources.items() if path in front]
                if row["disposition"] == "excluded":
                    self.assertFalse(owners)
                    self.assertIn("仅登记", author)
                    continue
                self.assertEqual(owners, [source])
                link = source.removeprefix("wiki/").removesuffix(".md")
                self.assertIn(f"[[{link}", author)
                self.assertIn(f"[[{link}", self.index)
                if row["disposition"] == "reused":
                    self.assertIn("仅登记", author)
                    original = row["original_raw_path"]
                    self.assertIn(original, sources[source])
                    self.assertEqual(body, visible_body(original))
                else:
                    page = read(source)
                    for anchor in row["anchors"]:
                        self.assertIn(anchor, page)
                    for section in ("主问题与证据身份", "标题与开头", "结构推进", "案例、解释与观察",
                                    "原文定位锚点", "失败、限制与不宜照搬处", "可迁移写法与自己的待测方向", "商业披露"):
                        self.assertIn(section, page)

    def test_cases_preserve_human_owned_fields(self):
        cards = read("wiki/topics/AI写作案例库.md").split("## 雷达2026-11-21：", 1)[1].split("\n## ", 1)[0]
        expected = [r for r in self.rows if r["case_card"]]
        self.assertEqual(len(re.findall(r"^### 案例：", cards, re.M)), len(expected))
        for row in expected:
            card = cards.split(f"\n### {row['case_card']}\n", 1)[1].split("\n### ", 1)[0]
            self.assertRegex(card, r"(?m)^- 测试角度：[ \t]*$")
            self.assertRegex(card, r"(?m)^- 步骤：[ \t]*$")
            self.assertIn(Path(row["source_path"]).stem, card)
        self.assertCountEqual([r["source_page"] for r in self.report["case_candidates"]],
                              [r["source_path"] for r in expected])

    def test_report_distinguishes_registered_from_pending(self):
        expected = {r["raw_path"] for r in self.rows if r["disposition"] == "excluded"}
        batch_paths = {r["raw_path"] for r in self.rows}
        self.assertEqual(set(self.report["raw_without_source"]) & batch_paths, expected)
        self.assertEqual(self.report["analysis_scope"]["batch_unreviewed"], 0)
        stats = json.loads(read(BATCH / "stats-2026-11-21/all-stats.json"))
        self.assertCountEqual([s["id"] for s in stats], [r["id"] for r in self.rows])
        briefing = read(BATCH / "雷达简报-2026-11-21.md")
        self.assertIn("互动成功 4", briefing)
        self.assertIn("HTTP 400，未重试", briefing)
        self.assertIn("雷达日报 9 号采集，5 号各新增 1 篇", read("wiki/log.md"))


if __name__ == "__main__":
    unittest.main()
