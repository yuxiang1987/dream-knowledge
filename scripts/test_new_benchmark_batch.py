"""Check source coverage and traceability for the three-author benchmark batch."""

from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "output/ai-wechat-methodology/三位新增作者拆解台账.json"


class NewBenchmarkBatchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.rows = cls.data["articles"]
        cls.by_id = {r["id"]: r for r in cls.rows}

    def test_selected_sources_are_covered_exactly_once(self):
        expected = {
            p.relative_to(ROOT).as_posix()
            for author in ("大鼻哥嘚巴嘚", "洛洛AI说", "小林coding")
            for p in (ROOT / "raw/article" / author).glob("*.md")
        }
        self.assertEqual(len(self.rows), 19)
        self.assertEqual(Counter(r["author"] for r in self.rows),
                         {"大鼻哥嘚巴嘚": 4, "洛洛AI说": 5, "小林coding": 10})
        self.assertEqual({r["raw_path"] for r in self.rows}, expected)
        self.assertEqual(len(self.by_id), 19)
        self.assertEqual(len({r["source_page"] for r in self.rows}), 19)

    def test_raw_snapshots_and_quoted_anchors(self):
        for r in self.rows:
            with self.subTest(article=r["id"]):
                raw = ROOT / r["raw_path"]
                content = raw.read_bytes().replace(b"\r\n", b"\n")
                self.assertEqual(hashlib.sha256(content).hexdigest(), r["raw_sha256"])
                text = raw.read_text(encoding="utf-8-sig")
                page = (ROOT / r["source_page"]).read_text(encoding="utf-8")
                self.assertGreaterEqual(len(r["anchors"]), 2)
                for anchor in r["anchors"]:
                    self.assertIn(anchor, text)
                    self.assertIn(anchor, page)
                self.assertIn(r["raw_path"], page.split("\n---\n", 1)[0])
                self.assertIn(r["question"], page)
                self.assertIn(r["own_idea"], page)

    def test_pages_can_be_found_from_the_index_and_author_topics(self):
        index = (ROOT / "wiki/index.md").read_text(encoding="utf-8")
        for r in self.rows:
            link = f"[[sources/{Path(r['source_page']).stem}]]"
            topic = ROOT / f"wiki/topics/{r['author']}文章写法拆解.md"
            self.assertIn(link, index)
            self.assertIn(link, topic.read_text(encoding="utf-8"))
        comparison = (ROOT / "wiki/comparisons/公众号对标三位新增作者写法对比.md").read_text(encoding="utf-8")
        for author in ("大鼻哥嘚巴嘚", "洛洛AI说", "小林coding"):
            self.assertIn(f"[[topics/{author}文章写法拆解]]", comparison)
        count = sum(p.name not in ("index.md", "log.md") for p in (ROOT / "wiki").rglob("*.md"))
        self.assertEqual(int(re.search(r"知识页：(\d+) 页", index).group(1)), count)

    def test_third_party_demos_and_unverified_claims_are_identified(self):
        for article_id in ("LL-05", "XL-07"):
            r = self.by_id[article_id]
            self.assertEqual(r["primary_type"], "整合型")
            self.assertEqual(r["evidence_role"], "第三方案例整理")
            page = (ROOT / r["source_page"]).read_text(encoding="utf-8")
            self.assertIn("第三方", page)
        for r in self.rows:
            self.assertFalse(r["media_reviewed"])
            self.assertFalse(r["product_retested"])
            self.assertIsNone(r["sponsor"])
            page = (ROOT / r["source_page"]).read_text(encoding="utf-8")
            self.assertIn("图片、动图和视频未核看", page)
            self.assertIn("未独立核实", page)
        unlimited = (ROOT / self.by_id["DB-04"]["source_page"]).read_text(encoding="utf-8")
        self.assertIn("无限", unlimited)
        self.assertIn("额度", unlimited)

    def test_editorial_judgments_do_not_invent_conflicts_or_results(self):
        for article_id in ("XL-01", "XL-02"):
            text = (ROOT / self.by_id[article_id]["source_page"]).read_text(encoding="utf-8")
            self.assertNotIn("status: 有冲突", text)
        for r in self.rows:
            self.assertTrue("待实操" in r["own_idea"] or "待验证" in r["own_idea"])
            self.assertRegex(r["published_at"], r"^2026-\d{2}-\d{2} \d{2}:\d{2}$")
            if r["author"] == "小林coding":
                self.assertTrue(r["original_url"].startswith("https://mp.weixin.qq.com/s/"))
        ll = (ROOT / self.by_id["LL-03"]["source_page"]).read_text(encoding="utf-8")
        self.assertIn("未提供八集完整生产记录", ll)
        self.assertIn("不能断言作者绝对没做八集", ll)


if __name__ == "__main__":
    unittest.main()
