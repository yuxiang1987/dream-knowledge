"""检查传播样本的计算、缺失项处理与研究边界，不调用付费接口。"""
import json
from pathlib import Path
import re
import statistics
import unittest

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "output/ai-wechat-methodology/WorkBuddy存储迁移选题数据.json"
PAGE = ROOT / "wiki/topics/WorkBuddy存储迁移选题调研.md"


class StorageResearchTest(unittest.TestCase):
    def test_comparison_excludes_failed_samples(self):
        data = json.loads(DATA.read_text(encoding="utf-8"))
        good = [a for a in data["baseline"] if "stats" in a]
        reads = [a["stats"]["read_num"] for a in good]
        comparison = data["comparison"]
        self.assertEqual(comparison["requested"], len(data["baseline"]))
        self.assertEqual(comparison["succeeded"], len(good))
        self.assertGreater(len(data["baseline"]), len(good))
        self.assertEqual(len({a["id"] for a in data["baseline"]}), len(data["baseline"]))
        self.assertEqual(comparison["median_read_num"], statistics.median(reads))
        self.assertAlmostEqual(comparison["target_vs_median"],
                               data["stats"]["read_num"] / statistics.median(reads))
        self.assertEqual(comparison["max_sample_read_num"], max(reads))

    def test_partial_comments_and_unverified_claims_stay_explicit(self):
        data = json.loads(DATA.read_text(encoding="utf-8"))
        scope = data["comments_scope"]
        self.assertLess(scope["retrieved"], scope["elected_total"])
        self.assertTrue(scope["has_more"])
        self.assertTrue(scope["includes_ai_replies"])
        page = PAGE.read_text(encoding="utf-8")
        for phrase in ("尚不能确认低粉", "发布时间不同", "未取得", "没有执行迁移"):
            self.assertIn(phrase, page + "\n" + "\n".join(data["limits"]))
        for private_field in ('"identity_name"', '"nick_name": "苏', '"debug_info"', '"api_key"'):
            self.assertNotIn(private_field, DATA.read_text(encoding="utf-8"))

    def test_index_count_and_source_explanation(self):
        index = (ROOT / "wiki/index.md").read_text(encoding="utf-8")
        pages = [p for p in (ROOT / "wiki").rglob("*.md") if p.name not in ("index.md", "log.md")]
        self.assertEqual(int(re.search(r"知识页：(\d+) 页", index).group(1)), len(pages))
        self.assertIn("[[topics/WorkBuddy存储迁移选题调研]]", index)
        page = PAGE.read_text(encoding="utf-8")
        self.assertIn("sources: []", page)
        self.assertIn("本轮未向 raw 写入", page)
        self.assertIn(DATA.name, page)


if __name__ == "__main__":
    unittest.main()
