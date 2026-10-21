"""Verify an orange color preview preserves the full reviewed blue export."""
import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]


class OrangePreview(unittest.TestCase):
    def test_only_requested_colors_change(self):
        record = json.loads((ROOT / 'scripts/deepseek_orange_layout.json').read_text(encoding='utf-8'))
        base = ROOT / record['base_fragment']
        self.assertEqual(hashlib.sha256(base.read_bytes()).hexdigest(), record['base_sha256'])
        html = base.read_text(encoding='utf-8')
        colors = record['colors']
        expected = re.sub(r'style="([^"]*)"', lambda m: 'style="' + re.sub(
            r'#[0-9a-f]{6}\b', lambda c: colors.get(c[0].lower(), c[0]), m[1], flags=re.I) + '"', html)
        output = ROOT / record['output']
        actual = (output / 'article-layout.wechat.html').read_text(encoding='utf-8')
        self.assertEqual(actual, expected)
        self.assertEqual(actual.count('<img'), 9)
        self.assertIn('>END</p>', actual)
        self.assertIn('background-color:#fff0e8', actual)
        self.assertIn('color:#f2784b', actual)
        for name, expected_sha in record['files'].items():
            self.assertEqual(hashlib.sha256((output / name).read_bytes()).hexdigest(), expected_sha)
        self.assertEqual(hashlib.sha256((ROOT / record['source']).read_bytes()).hexdigest(), record['source_sha256'])


if __name__ == '__main__':
    unittest.main()
