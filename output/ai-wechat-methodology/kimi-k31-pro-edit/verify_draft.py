"""校验本次改稿的保真性；不验证产品表现或视频内容。原稿须在本机存在。"""
from hashlib import sha256
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'raw/article/程序员拾梦/实测 Kimi 3.1 Pro.md'
DRAFT = Path(__file__).with_name('实测 Kimi K3.1 Pro-优化稿.md')
SOURCE_HASH = '2ce818c5d2027331dc9d9f89c5e2c8bb603eb36d0b184e18048c2e51b3188b43'


class DraftIntegrityTest(unittest.TestCase):
    def test_source_unchanged(self):
        self.assertEqual(sha256(SOURCE.read_bytes()).hexdigest(), SOURCE_HASH)

    def test_historical_prompts_verbatim(self):
        pattern = r'```prompt\n(.*?)\n\s*```'
        original = re.findall(pattern, SOURCE.read_text(encoding='utf-8'), re.S)
        edited = re.findall(pattern, DRAFT.read_text(encoding='utf-8'), re.S)
        self.assertEqual(len(original), 3)
        self.assertEqual(edited, original)

    def test_media_preserved_and_available(self):
        pattern = r'!\[\[([^\]]+)\]\]'
        original = re.findall(pattern, SOURCE.read_text(encoding='utf-8'))
        edited = re.findall(pattern, DRAFT.read_text(encoding='utf-8'))
        self.assertEqual(len(original), 9)
        self.assertEqual(edited, original)
        for name in edited:
            with self.subTest(media=name):
                self.assertTrue((ROOT / name).is_file())

    def test_markdown_fences_balanced(self):
        lines = [line.strip() for line in DRAFT.read_text(encoding='utf-8').splitlines()
                 if line.strip().startswith('```')]
        self.assertEqual(lines, ['```prompt', '```'] * 3)


if __name__ == '__main__':
    unittest.main()
