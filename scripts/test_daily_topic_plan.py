"""核对个人工具状态、明日计划与模拟材料；不填造产品实测结果。"""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/ai-wechat-methodology"
PACK = OUT / "豆包电脑版明日选题包"


class DailyTopicPlanTest(unittest.TestCase):
    def test_doubao_is_available_by_user_report_without_invented_entitlements(self):
        pool = json.loads((OUT / "程序员拾梦可用工具池.json").read_text(encoding="utf-8"))
        product = next(p for p in pool["products"] if p["name"] == "豆包电脑版")
        self.assertEqual(product["membership_duration_user_reported"], "一个月")
        for key in ("membership_tier", "expires_at", "quota", "actual_sponsor"):
            self.assertIsNone(product[key])
        self.assertFalse(product["task_mode_verified"])
        self.assertFalse(product["public_offer_verified"])
        self.assertEqual(product["historical_article_ids"], ["LRJ60-24", "LRJ60-42", "LRJ60-52"])
        self.assertFalse(pool["availability"]["automatic_publication_authorized"])
        self.assertEqual(pool["availability"]["target_publish_date"], "2026-10-17")

    def test_historical_dataset_is_not_recounted_as_new_sponsorship(self):
        historical = json.loads((OUT / "路人甲TM六十篇拆解台账.json").read_text(encoding="utf-8"))
        self.assertEqual(len(historical["articles"]), 60)
        p = next(p for p in historical["products"] if p["name"] == "豆包工作")
        self.assertEqual(len(p["primary_article_ids"]), 3)
        chart = (OUT / "路人甲TM选题与客户速查表.md").read_text(encoding="utf-8")
        for text in ("豆包电脑版", "3篇", "映射待实操核对", "不改变60篇历史统计"):
            self.assertIn(text, chart)

    def test_simulated_materials_have_consistent_attendance_and_budget(self):
        text = (PACK / "模拟资料/报名与预算.md").read_text(encoding="utf-8")
        rows = re.findall(r"\| P\d+ \| ([^|]+) \|", text)
        self.assertEqual(len(rows), 12)
        self.assertEqual(sum(s.strip() == "确认参加" for s in rows), 8)
        self.assertEqual(sum(s.strip() == "候补" for s in rows), 2)
        self.assertEqual(sum(s.strip() == "已取消" for s in rows), 2)
        costs = re.findall(r"\| ([^|]+) \| (\d+) \| (\d+) \| (\d+) \| ([^|]+) \|", text)
        self.assertEqual(len(costs), 4)
        for _, quantity, price, subtotal, _ in costs:
            self.assertEqual(int(quantity) * int(price), int(subtotal))
        total = sum(int(r[3]) for r in costs)
        self.assertEqual(total, 860)
        self.assertEqual(total - 120, 740)
        for p in (PACK / "模拟资料").glob("*.md"):
            self.assertIn("模拟", p.read_text(encoding="utf-8"))
        answer = (PACK / "核对参考.md").read_text(encoding="utf-8")
        for expected in ("740", "860", "140", "260", "15:00—18:00", "安禾", "已付金额都是0"):
            self.assertIn(expected, answer)

    def test_task_prompts_do_not_feed_reference_answers_or_fake_performance(self):
        text = (PACK / "给豆包的提示词.md").read_text(encoding="utf-8")
        first = text.split("## 第一段", 1)[1].split("## 第二段", 1)[0]
        self.assertNotIn("740", first)
        self.assertNotIn("860", first)
        for expected in ("不要上传", "模拟数据", "不要修改上传的源文件", "不要对外发布", "实际看到"):
            self.assertIn(expected, text)
        record = (PACK / "实测记录.md").read_text(encoding="utf-8")
        self.assertIn("状态：待实操", record)
        self.assertGreater(record.count("待填写"), 15)

    def test_plan_files_timing_and_publication_ownership_are_clear(self):
        plan = (PACK / "选题与实操安排.md").read_text(encoding="utf-8")
        for expected in ("target_publish_date: 2026-10-17", "21:00 Asia/Shanghai", "待实操",
                         "今晚", "明天上午", "作者人工", "不是产品速度承诺", "不创建自动任务"):
            self.assertIn(expected, plan)
        for filename in ("模拟资料/活动原计划.md", "模拟资料/报名与预算.md", "模拟资料/群聊补充.md",
                         "给豆包的提示词.md", "核对参考.md", "实测记录.md"):
            self.assertTrue((PACK / filename).is_file())

    def test_knowledge_entries_and_counts_are_linked(self):
        index = (ROOT / "wiki/index.md").read_text(encoding="utf-8")
        for link in ("[[entities/豆包电脑版]]", "[[topics/公众号每日选题决策]]"):
            self.assertIn(link, index)
        count = sum(p.name not in ("index.md", "log.md") for p in (ROOT / "wiki").rglob("*.md"))
        self.assertEqual(int(re.search(r"知识页：(\d+) 页", index).group(1)), count)
        product = (ROOT / "wiki/entities/豆包电脑版.md").read_text(encoding="utf-8")
        self.assertIn("历史", product)
        self.assertIn("不凭名称直接判断", product)
        self.assertIn("用户在2026-10-16确认", product)


if __name__ == "__main__":
    unittest.main()
