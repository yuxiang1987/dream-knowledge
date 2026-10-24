"""五位新增对标作者批次的独立验收。"""

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BATCH = ROOT / "output/ai-wechat-methodology/five-new-benchmark-batch"
MANIFEST = BATCH / "manifest.json"
ANALYSES = BATCH / "analyses.json"
AUTHORS = ("苍何", "爱ai的大刘", "公子龙", "管三", "阿胖ai手记")


class FiveAuthorBenchmarkBatchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.rows = cls.manifest["articles"]
        cls.by_id = {row["id"]: row for row in cls.rows}
        cls.analyses = json.loads(ANALYSES.read_text(encoding="utf-8"))
        cls.index = (ROOT / "wiki" / "index.md").read_text(encoding="utf-8")

    def test_every_source_article_is_covered_once(self):
        expected = set()
        for author in AUTHORS:
            folder = ROOT / "raw" / "article" / author
            expected |= {p.relative_to(ROOT).as_posix() for p in folder.glob("*.md")}
        self.assertEqual(len(self.rows), 12)
        self.assertEqual({row["raw_path"] for row in self.rows}, expected)
        self.assertEqual(len(self.by_id), 12)
        self.assertEqual(len({row["source_page"] for row in self.rows}), 12)
        self.assertEqual(len(self.analyses), 12)

    def test_raw_snapshots_are_unchanged_and_anchors_resolve(self):
        for row in self.rows:
            with self.subTest(article=row["id"]):
                raw = ROOT / row["raw_path"]
                content = raw.read_bytes().replace(b"\r\n", b"\n")
                self.assertEqual(hashlib.sha256(content).hexdigest(), row["raw_sha256"])
                text = raw.read_text(encoding="utf-8-sig")
                page = (ROOT / row["source_page"]).read_text(encoding="utf-8")
                anchors = self.analyses[row["id"]]["anchor_terms"]
                self.assertGreaterEqual(len(anchors), 2)
                for anchor in anchors:
                    self.assertIn(anchor, text)
                    self.assertIn(anchor, page)

    def test_each_page_declares_scope_and_pending_direction(self):
        for row in self.rows:
            with self.subTest(article=row["id"]):
                page = (ROOT / row["source_page"]).read_text(encoding="utf-8")
                self.assertIn("图片、动图和视频未核看", page)
                self.assertIn("未独立核实", page)
                self.assertIn(row["raw_path"], page.split("\n---\n", 1)[0])
                self.assertIn(row["question"], page)
                self.assertIn(row["own_idea"], page)
                self.assertTrue("待实操" in row["own_idea"] or "待验证" in row["own_idea"])
                self.assertEqual(row["evidence_role"], "作者亲测")
                self.assertRegex(row["published_at"], r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$")

    def test_navigation_and_counts_are_consistent(self):
        for row in self.rows:
            link = f"[[sources/{Path(row['source_page']).stem}]]"
            self.assertIn(link, self.index)
            topic = ROOT / f"wiki/topics/{row['author']}文章写法拆解.md"
            self.assertIn(link, topic.read_text(encoding="utf-8"))
        for author in AUTHORS:
            topic_path = ROOT / f"wiki/topics/{author}文章写法拆解.md"
            self.assertTrue(topic_path.is_file())
            topic_text = topic_path.read_text(encoding="utf-8")
            self.assertEqual(topic_text, topic_text.rstrip() + "\n")
            self.assertIn(f"[[topics/{author}文章写法拆解]]", self.index)
        comparison = (ROOT / "wiki/comparisons/公众号对标五位新增作者写法对比.md").read_text(encoding="utf-8")
        for author in AUTHORS:
            self.assertIn(f"[[topics/{author}文章写法拆解]]", comparison)
        count = sum(p.name not in ("index.md", "log.md") for p in (ROOT / "wiki").rglob("*.md"))
        self.assertEqual(int(re.search(r"知识页：(\d+) 页", self.index).group(1)), count)

    def test_conflicting_advice_is_kept_on_both_sides(self):
        comparison = (ROOT / "wiki/comparisons/公众号对标五位新增作者写法对比.md").read_text(encoding="utf-8")
        self.assertIn("冲突记录", comparison)
        self.assertIn("[[sources/大刘WorkBuddy设置文章拆解]]", comparison)
        self.assertIn("[[sources/大刘WorkBuddy飞书工作流文章拆解]]", comparison)
        self.assertIn("[[sources/阿胖WorkBuddy设置文章拆解]]", comparison)
        boundary = (ROOT / "wiki/topics/证据与边界库.md").read_text(encoding="utf-8")
        self.assertIn("## 五位新增作者：本批需要保留的区分", boundary)
        self.assertIn("同一作者两篇对上下文建议相反", boundary)

    def test_no_article_is_marked_as_independently_verified(self):
        for row in self.rows:
            with self.subTest(article=row["id"]):
                self.assertFalse(row["media_reviewed"])
                self.assertFalse(row["product_retested"])
                self.assertIsNone(row["sponsor"])
                page = (ROOT / row["source_page"]).read_text(encoding="utf-8")
                self.assertNotIn("已独立核实", page)
                self.assertNotIn("status: 有冲突", page)


if __name__ == "__main__":
    unittest.main()
