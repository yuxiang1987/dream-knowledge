"""两个独立技能的门槛、资源与合成CLI验证记录。"""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / '.agents/skills'
NAMES = ['wechat-article-writing', 'gzh-final-check']


class ArticleLengthConstraintTest(unittest.TestCase):
    def test_self_contained_counters_and_tests_are_identical(self):
        for resource in ['scripts/check_article_length.py', 'tests/test_article_length.py']:
            self.assertEqual((SKILLS / NAMES[0] / resource).read_bytes(),
                             (SKILLS / NAMES[1] / resource).read_bytes())

    def test_both_entrypoints_require_measured_count_and_boundaries(self):
        manifest = json.loads((ROOT / 'scripts/installed_skills.json').read_text(encoding='utf8'))
        for name in NAMES:
            entry = (SKILLS / name / 'SKILL.md').read_text(encoding='utf8')
            for expected in ['至少2500字（含2500字）', '当前最终版本实际统计',
                             '固定个人简介不计', 'scripts/check_article_length.py',
                             'tests/test_article_length.py']:
                self.assertIn(expected, entry)
            self.assertIn(name+'/scripts/check_article_length.py', manifest['sha256'])
            self.assertIn(name+'/tests/test_article_length.py', manifest['sha256'])
        writing = (SKILLS / NAMES[0] / 'SKILL.md').read_text(encoding='utf8')
        self.assertNotIn('不固定字数、案例数或段落配额', writing)
        final = (SKILLS / NAMES[1] / 'SKILL.md').read_text(encoding='utf8')
        self.assertIn('还有必须修改的问题', final)
        self.assertIn('默认只检查不改稿，不因缺字数擅自扩写', final)

    def test_recorded_cli_boundaries_and_nonpassing_padded_body(self):
        evidence = json.loads((ROOT / 'output/ai-wechat-methodology/2500字约束验证/验证结果.json').read_text(encoding='utf8'))
        self.assertEqual(len(evidence['results']), 8)
        for result in evidence['results']:
            count = result['body_characters']
            self.assertEqual(result['passed'], count >= 2500)
            self.assertEqual(result['shortfall'], max(0, 2500-count))
            self.assertEqual(result['exit_code'], 0 if count >= 2500 else 1)
            if result['case'] == '正文2499加附加内容':
                self.assertEqual(count, 2499)


if __name__ == '__main__':
    unittest.main()
