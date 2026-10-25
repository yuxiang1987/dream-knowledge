"""知识库资料覆盖验收：检查来源可追溯及原始资料没有静默漏处理。"""
from pathlib import Path
import unittest

from wiki_lint import parse_frontmatter, parse_list

ROOT = Path(__file__).resolve().parents[1]


class DistillationCoverageTest(unittest.TestCase):
    def test_raw_material_has_knowledge_page(self):
        covered = set()
        for page in (ROOT / 'wiki').rglob('*.md'):
            front, _ = parse_frontmatter(page.read_text(encoding='utf-8-sig'))
            if front:
                covered.update(parse_list(front.get('sources', '')))
        raw = {p.relative_to(ROOT).as_posix() for p in (ROOT / 'raw').rglob('*.md')}
        self.assertEqual(sorted(raw - covered), [], '存在尚未记录处理结果的原始资料')

    def test_source_pages_have_existing_raw_provenance(self):
        for page in (ROOT / 'wiki/sources').glob('*.md'):
            front, body = parse_frontmatter(page.read_text(encoding='utf-8-sig'))
            if not front:
                self.fail(f'{page.name} 缺少元数据')
            for source in parse_list(front.get('sources', '')):
                with self.subTest(page=page.name, source=source):
                    self.assertTrue(source.startswith('raw/'))
                    self.assertTrue((ROOT / source).is_file())


if __name__ == '__main__':
    unittest.main()
