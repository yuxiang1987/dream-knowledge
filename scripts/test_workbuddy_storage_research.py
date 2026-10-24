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

    def test_outline_keeps_results_and_actual_prompts_pending(self):
        outline = PAGE.read_text(encoding="utf-8").split("## 文章框架（待实测）", 1)[1]
        self.assertIn("不是已发生的实测记录", outline)
        self.assertIn("真实使用过的提示词与事后整理版分别标记", outline)
        self.assertIn("目标盘以用户实际选择为准", outline)
        self.assertIn("实际没有做的检查继续留空", outline)
        self.assertGreaterEqual(outline.count("【待补："), 4)
        self.assertNotIn("释放了8.5", outline)

    def test_returned_material_is_not_reported_as_real_migration(self):
        path = DATA.with_name("WorkBuddy迁移脚本材料核对.json")
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertFalse(data["state"]["real_migration_verified"])
        self.assertFalse(data["state"]["real_space_released_verified"])
        self.assertFalse(data["state"]["bat_entry_executed_in_shared_record"])
        self.assertFalse(data["state"]["local_main_directory_is_reparsepoint"])
        self.assertIn("先只检查，不移动或删除文件", data["actual_prompt"])
        names = {a["name"] for a in data["artifacts"]}
        self.assertIn("wb-migrate.ps1", names)
        self.assertIn("migrate-workbuddy.bat", names)
        self.assertTrue(all(re.fullmatch(r"[a-f0-9]{64}", a["sha256"]) for a in data["artifacts"]))
        findings = {a["id"] for a in data["findings"]}
        self.assertTrue({"rollback_rename", "double_count", "bat_validation", "workspace_scope"} <= findings)
        page = PAGE.read_text(encoding="utf-8")
        self.assertIn("还没有运行迁移 BAT", page)
        self.assertIn("不能将约2GB主数据写成已经释放的空间", page)
        self.assertIn(path.name, page)


if __name__ == "__main__":
    unittest.main()
