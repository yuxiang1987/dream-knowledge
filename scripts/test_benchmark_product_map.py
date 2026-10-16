"""验证文章全覆盖、来源对应、产品关联与商业证据层次，不证明当前投放预算。"""
from pathlib import Path
import hashlib
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/ai-wechat-methodology"


class BenchmarkProductMapTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((OUT / "路人甲TM文章产品台账.json").read_text(encoding="utf-8"))
        cls.page = (ROOT / "wiki/topics/AI公众号产品选题与客户地图.md").read_text(encoding="utf-8")

    def test_all_local_articles_have_one_summary(self):
        articles = self.data["articles"]
        actual = {p.relative_to(ROOT).as_posix()
                  for p in (ROOT / "raw/article/lurenjiaTM").glob("*.md")}
        self.assertEqual(len(articles), 23)
        self.assertEqual(len({r["id"] for r in articles}), 23)
        self.assertEqual({r["raw_path"] for r in articles}, actual)
        for r in articles:
            with self.subTest(article=r["id"]):
                raw = ROOT / r["raw_path"]
                self.assertEqual(hashlib.sha256(raw.read_bytes()).hexdigest(), r["raw_sha256"])
                self.assertIn(r["raw_path"], (ROOT / r["source_page"]).read_text(encoding="utf-8"))
                self.assertTrue(r["public_url"].startswith("https://mp.weixin.qq.com/s/"))
                self.assertNotIn("?", r["public_url"])

    def test_product_edges_are_bidirectional(self):
        products = {p["id"]: p for p in self.data["products"]}
        self.assertEqual(len(products), 20)
        for r in self.data["articles"]:
            self.assertTrue(r["case"])
            self.assertIn(r["primary_type"], self.data["content_types"])
            for pid in r["primary_product_ids"]:
                self.assertIn(pid, products)
                self.assertIn(r["id"], products[pid]["article_ids"])
            self.assertIn(r["id"], self.page)

    def test_commercial_claim_is_retained_without_invented_contacts(self):
        self.assertIn("100%商单", self.data["account_claim"]["claim"])
        self.assertEqual(self.data["account_claim"]["timestamp"], "21:00")
        for r in self.data["articles"]:
            self.assertIsNone(r["sponsor_id"])
            self.assertIsNone(r["current_budget"])
            self.assertIsNone(r["contact"])
        for p in self.data["products"]:
            self.assertIsNone(p["official_contact"])
            self.assertEqual(p["budget_status"], "未知")
        for fact in ("账号级商业依据", "不是账号全部历史", "整合」与「整活",
                     "不编造评论需求", "不得将苹果当作已确认客户"):
            self.assertIn(fact, self.page)

    def test_type_origin_and_methodology_link(self):
        self.assertEqual(self.data["content_types"],
                         ["实战型", "解决问题型", "整合型", "教程型", "观点型", "资讯型"])
        text = (OUT / "AI垂类公众号经营方法论.md").read_text(encoding="utf-8")
        self.assertIn("### 5.7 ", text)
        self.assertIn("路人甲TM文章产品台账.json", text)
        self.assertIn("表现标签", text)
        self.assertIn("原作者逐字定义", text)

    def test_index_count_and_new_source_discovery(self):
        index = (ROOT / "wiki/index.md").read_text(encoding="utf-8")
        count = sum(p.name not in ("index.md", "log.md") for p in (ROOT / "wiki").rglob("*.md"))
        self.assertEqual(int(re.search(r"知识页：(\d+) 页", index).group(1)), count)
        self.assertIn("[[topics/AI公众号产品选题与客户地图]]", index)
        self.assertIn("[[sources/WorkBuddy小程序教程文章拆解]]", index)


if __name__ == "__main__":
    unittest.main()
