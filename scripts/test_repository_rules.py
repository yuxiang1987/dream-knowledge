"""Validate mandatory delivery rules in the repository instructions."""
from pathlib import Path
import unittest


class RepositoryRulesTest(unittest.TestCase):
    def test_delivery_rules(self):
        text = (Path(__file__).resolve().parents[1] / "AGENTS.md").read_text(encoding="utf-8-sig")
        self.assertIn("每次改动完成后，都必须创建一个对应的 Git Commit", text)
        self.assertIn("每次改动后，都必须编写和更新相关测试", text)
        self.assertIn("确保所有测试和验证都全部通过", text)

    def test_automatic_commit_and_push_rule(self):
        text = (Path(__file__).resolve().parents[1] / "AGENTS.md").read_text(encoding="utf-8-sig")
        rule = next(line for line in text.splitlines() if line.startswith("- 每次文件改动完成后"))
        for requirement in (
            "相关测试和验证全部通过后",
            "按文件归属自动提交 Git 并推送到 GitHub",
            "知识库文件提交到 `https://github.com/yuxiang1987/dream-knowledge.git`",
            "公众号 Skill 优化文件提交到 `https://github.com/yuxiang1987/dream-skills.git`",
            "提交记录必须清楚说明本次改动内容",
            "`wiki/log.md`",
            "提交或推送失败时，必须如实告知用户",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, rule)

    def test_skill_changes_return_to_source_repository(self):
        text = (Path(__file__).resolve().parents[1] / "AGENTS.md").read_text(encoding="utf-8-sig")
        rule = next(line for line in text.splitlines() if line.startswith("- `.agents/skills/`"))
        for requirement in (
            "工作空间安装副本",
            "必须将改动同步回 `dream-skills` 的对应技能目录",
            "在该仓库更新相关测试、验证并提交、推送",
            "不得仅提交安装副本到知识库仓库就视为完成",
            "分别验证、提交和推送，并分别报告结果",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, rule)


if __name__ == "__main__":
    unittest.main()
