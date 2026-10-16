"""验证60篇研究的来源覆盖、原文保护、分类与证据角色；不证明营销效果。"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
import unittest
from urllib.parse import unquote

import build_benchmark_research as build

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/ai-wechat-methodology"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class BenchmarkResearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((OUT / "路人甲TM六十篇拆解台账.json").read_text(encoding="utf-8"))
        cls.records = cls.data["articles"]
        cls.by_rank = {r["archive_rank"]: r for r in cls.records}

    def test_exact_archive_coverage_without_duplicate_source_pages(self):
        manifest = json.loads((OUT / "路人甲TM最新60篇下载清单.json").read_text(encoding="utf-8"))
        self.assertEqual(len(self.records), 60)
        self.assertEqual([r["archive_rank"] for r in self.records], list(range(1, 61)))
        self.assertEqual(len({r["id"] for r in self.records}), 60)
        self.assertEqual(len({r["source_page"] for r in self.records}), 60)
        self.assertEqual({r["raw_path"] for r in self.records}, {r["raw_path"] for r in manifest["articles"]})
        self.assertEqual(sum(r["review_mode"].startswith("新样本") for r in self.records), 38)
        self.assertEqual(sum("previous_record_id" in r for r in self.records), 22)

    def test_every_analysis_has_real_source_anchor_and_specific_case(self):
        for r in self.records:
            with self.subTest(article=r["id"]):
                source = (ROOT / r["source_page"]).read_text(encoding="utf-8")
                body = build.plain((ROOT / r["readable_path"]).read_text(encoding="utf-8").split("\n---\n", 1)[1])
                self.assertIn(r["raw_path"], source.split("\n---\n", 1)[0])
                self.assertIn(r["anchor"], body)
                self.assertIn("[[topics/路人甲TM文章经营全景]]", source)
                for field in ("question", "hook", "cases", "structure", "method", "boundary", "own_idea"):
                    self.assertGreater(len(r[field]), 8, field)
                self.assertEqual(sha(ROOT / r["raw_path"]), r["raw_sha256"])
        new = [r for r in self.records if r["review_mode"].startswith("新样本")]
        self.assertEqual(len({r["cases"] for r in new}), 38)
        self.assertEqual(len({r["own_idea"] for r in new}), 38)

    def test_old_raw_and_old_analysis_body_are_preserved(self):
        original = json.loads((OUT / "路人甲TM文章产品台账.json").read_text(encoding="utf-8"))
        for r in original["articles"]:
            self.assertEqual(sha(ROOT / r["raw_path"]), r["raw_sha256"])
        for r in self.records:
            if "previous_record_id" not in r:
                continue
            command = ["git", "-c", f"safe.directory={ROOT.as_posix()}", "show", f"HEAD:{r['source_page']}"]
            baseline = subprocess.run(command, cwd=ROOT, capture_output=True, check=True).stdout.decode("utf-8")
            baseline_body = baseline.split("\n---\n", 1)[1].split(build.SOURCE_MARK, 1)[0].rstrip()
            current = (ROOT / r["source_page"]).read_text(encoding="utf-8")
            current_body = current.split("\n---\n", 1)[1].split(build.SOURCE_MARK, 1)[0].rstrip()
            self.assertEqual(current_body, baseline_body, r["source_page"])

    def test_counts_and_product_relations_match_the_actual_records(self):
        stats = self.data["stats"]
        self.assertEqual(stats["types"], dict(Counter(r["primary_type"] for r in self.records)))
        self.assertEqual(stats["directions"], dict(Counter(r["direction"] for r in self.records)))
        self.assertEqual(sum(stats["types"].values()), 60)
        self.assertEqual(stats["types"], {"资讯型": 2, "解决问题型": 16, "实战型": 31,
                                           "教程型": 6, "整合型": 3, "观点型": 2})
        for p in self.data["products"]:
            self.assertEqual(p["primary_article_ids"], [r["id"] for r in self.records if p["name"] in r["primary_products"]])
            self.assertEqual(p["supporting_article_ids"], [r["id"] for r in self.records if p["name"] in r["supporting_products"]])
        workbuddy = next(p for p in self.data["products"] if p["name"] == "WorkBuddy")
        self.assertEqual(len(workbuddy["primary_article_ids"]), 8)
        self.assertIn("LRJ60-08", workbuddy["supporting_article_ids"])
        self.assertNotIn("LRJ60-08", workbuddy["primary_article_ids"])

    def test_media_demo_and_sponsor_roles_are_not_invented(self):
        self.assertEqual(self.by_rank[56]["primary_type"], "资讯型")
        self.assertIn("尚未排到", self.by_rank[56]["boundary"])
        self.assertIn("单人玩 + 实时榜", self.by_rank[16]["anchor"])
        self.assertEqual(self.by_rank[50]["primary_products"], ["Flova"])
        self.assertIn("Seedance", self.by_rank[50]["supporting_products"])
        self.assertIn("100%商单", self.data["account_claim"]["claim"])
        self.assertIn("整活为表现标签", self.data["classification"])
        for r in self.records:
            self.assertFalse(r["media_reviewed"])
            self.assertFalse(r["comments_collected"])
            for field in ("sponsor", "contact", "current_budget"):
                self.assertIsNone(r[field])
        for p in self.data["products"]:
            for field in ("actual_sponsor", "current_budget", "verified_contact"):
                self.assertIsNone(p[field])

    def test_numerical_conflicts_keep_both_claims(self):
        rabbit = (ROOT / self.by_rank[8]["source_page"]).read_text(encoding="utf-8")
        price = (ROOT / self.by_rank[55]["source_page"]).read_text(encoding="utf-8")
        for text in (rabbit, price):
            self.assertIn("status: 有冲突", text)
        for word in ("20", "15", "41", "76", "80"):
            self.assertIn(word, rabbit)
        for word in ("132", "243", "54.3%", "不到一半"):
            self.assertIn(word, price)
        self.assertIn("0.174", self.by_rank[37]["boundary"])

    def test_product_names_are_not_misread_as_technical_abbreviations(self):
        for n in (4, 13):
            page = (ROOT / self.by_rank[n]["source_page"]).read_text(encoding="utf-8")
            self.assertNotIn("VI指品牌视觉规范", page)
        record = dict(self.by_rank[12], cases=self.by_rank[12]["cases"] + "VI规范。")
        page = build.new_source(record)
        self.assertIn("VI指品牌视觉规范", page)

    def test_index_references_and_agent_reference_are_updated(self):
        index = (ROOT / "wiki/index.md").read_text(encoding="utf-8")
        count = sum(p.name not in ("index.md", "log.md") for p in (ROOT / "wiki").rglob("*.md"))
        self.assertEqual(int(re.search(r"知识页：(\d+) 页", index).group(1)), count)
        self.assertIn("[[topics/路人甲TM文章经营全景]]", index)
        for r in self.records:
            if r["review_mode"].startswith("新样本"):
                self.assertIn(f"[[sources/{Path(r['source_page']).stem}]]", index)
        text = (OUT / "AI垂类公众号经营方法论.md").read_text(encoding="utf-8")
        self.assertIn("version: 1.3", text)
        self.assertIn("### 5.8 ", text)
        self.assertIn("路人甲TM六十篇拆解台账.json", text)
        quick = OUT / "路人甲TM选题与客户速查表.md"
        for url in re.findall(r"\]\(([^)]+)\)", quick.read_text(encoding="utf-8")):
            self.assertTrue((quick.parent / unquote(url)).resolve().is_file())

    def test_recompilation_is_stable_and_does_not_touch_raw(self):
        targets = [ROOT / r["source_page"] for r in self.records]
        targets += [ROOT / "wiki/topics/路人甲TM文章经营全景.md", OUT / "路人甲TM六十篇拆解台账.json"]
        before = {str(p): sha(p) for p in targets}
        raw_before = {r["raw_path"]: sha(ROOT / r["raw_path"]) for r in self.records}
        build.main()
        self.assertEqual(before, {str(p): sha(p) for p in targets})
        self.assertEqual(raw_before, {r["raw_path"]: sha(ROOT / r["raw_path"]) for r in self.records})


if __name__ == "__main__":
    unittest.main()
