"""检查对话草稿归档的完整性、可发现性与未实测边界，不验证产品行为。"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "wiki/topics/WorkBuddy设置技巧文章.md"
LINK = "[[topics/WorkBuddy设置技巧文章]]"


class WorkBuddyArticleArchiveTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = PAGE.read_text(encoding="utf-8")
        cls.article = cls.text.split("## 完整正文草稿\n", 1)[1].split(
            "## 待办与发布前核验\n", 1
        )[0]

    def test_complete_draft_and_templates(self):
        self.assertEqual(re.findall(r"^## (0[1-6]) ", self.article, re.M),
                         ["01", "02", "03", "04", "05", "06"])
        self.assertEqual(len(re.findall(r"^```text$", self.article, re.M)), 5)
        self.assertEqual(len(re.findall(r"^```$", self.article, re.M)), 5)
        self.assertIn("## 改完设置，拿一个小任务试一下", self.article)

    def test_draft_provenance_and_pending_evidence(self):
        self.assertRegex(self.text, r"(?m)^status: 草稿$")
        for raw in ("raw/article/阿胖ai手记/刚装好workbuddy别急着聊天，花2分钟做好这6类设置，让你的workbuddy聪明10倍（附详细步骤）.md",
                    "raw/article/爱ai的大刘/WorkBuddy 可以直接复制的简单设置，立刻让你的 WorkBuddy 比别人聪明百倍。（附提示词）.md"):
            with self.subTest(raw=raw):
                self.assertIn(raw, self.text)
                self.assertTrue((ROOT / raw).is_file())
        self.assertIn("本次聊天", self.text)
        for boundary in ("未重新联网核实", "当前均未实测", "当前没有实际媒体附件",
                         "不是用户已执行的历史输入"):
            with self.subTest(boundary=boundary):
                self.assertIn(boundary, self.text)

    def test_discoverable_and_scoped_preferences(self):
        for relative in ("wiki/index.md", "wiki/topics/公众号内容生产线.md",
                         "wiki/entities/程序员拾梦.md"):
            with self.subTest(page=relative):
                self.assertIn(LINK, (ROOT / relative).read_text(encoding="utf-8"))
        self.assertIn("这不排斥把 WorkBuddy 设置教程写成公众号文章", self.text)
        for backstage in ("阿胖", "大刘", "两篇对标", "参考了"):
            with self.subTest(backstage=backstage):
                self.assertNotIn(backstage, self.article)

    def test_final_article_and_linked_artifacts_are_retrievable(self):
        page = ROOT / "wiki/sources/WorkBuddy七处设置教程定稿.md"
        text = page.read_text(encoding="utf-8")
        original = ROOT / "raw/article/程序员梦哥/WorkBuddy 做好这几个设置，让WorkBuddy越来越懂你.md"
        self.assertIn(f'sources: ["{original.relative_to(ROOT).as_posix()}"]', text)
        markdown = original.read_text(encoding="utf-8")
        headers = re.findall(r"^## (.*)$", markdown, re.M)
        self.assertEqual(len(headers[:-1]), 7)
        self.assertEqual(headers[-1], "写在最后")
        references = re.findall(r"!\[\[([^\]]+)\]\]", markdown)
        self.assertEqual(len(references), 12)
        self.assertEqual(len(references), len(set(references)))
        for file in references:
            self.assertTrue((original.parent / "assets" / original.stem / file).is_file())
        targets = re.findall(r"\]\(<([^>]+)>\)", text)
        self.assertEqual(len(targets), 5)
        for target in targets:
            self.assertTrue((page.parent / target).is_file(), target)

    def test_final_article_is_indexed_with_validation_boundaries(self):
        source = "[[sources/WorkBuddy七处设置教程定稿]]"
        for path in ("wiki/index.md", "wiki/topics/WorkBuddy设置技巧文章.md",
                     "wiki/topics/公众号内容生产线.md", "wiki/log.md"):
            with self.subTest(path=path):
                self.assertIn(source, (ROOT / path).read_text(encoding="utf-8"))
        final = (ROOT / "wiki/sources/WorkBuddy七处设置教程定稿.md").read_text(encoding="utf-8")
        self.assertIn("已定稿、已排版", final)
        self.assertIn("公众号发布链接和发布效果未核实", final)
        self.assertIn("不能证明实际迁移", final)
        self.assertIn("整篇粘贴及保存后播放未核实", final)

    def test_index_page_count_and_official_links(self):
        index = (ROOT / "wiki/index.md").read_text(encoding="utf-8")
        count = sum(path.name not in {"index.md", "log.md"}
                    for path in (ROOT / "wiki").rglob("*.md"))
        self.assertEqual(int(re.search(r"知识页：(\d+) 页", index).group(1)), count)
        for suffix in ("Setting", "Memory", "Model"):
            with self.subTest(document=suffix):
                self.assertIn("https://www.workbuddy.cn/docs/workbuddy/"
                              "From-Beginner-to-Expert-Guide/Function-Description/"
                              + suffix, self.article)


if __name__ == "__main__":
    unittest.main()
