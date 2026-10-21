"""Check this article's blue export without changing the source draft."""
import base64
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]


class ArticleHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.headings = []
        self.numbers = []
        self._heading = False
        self._number = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'img':
            self.images.append(attrs['src'])
        if tag == 'h2':
            self._heading = True
        if tag == 'p' and attrs.get('aria-hidden') == 'true':
            self._number = True

    def handle_data(self, data):
        if self._heading:
            self.headings.append(data)
        if self._number:
            self.numbers.append(data)

    def handle_endtag(self, tag):
        if tag == 'h2':
            self._heading = False
        if tag == 'p':
            self._number = False


class DeepSeekBlueLayout(unittest.TestCase):
    def setUp(self):
        self.receipt = json.loads((ROOT / 'scripts/deepseek_blue_layout.json').read_text(encoding='utf-8'))
        self.out = ROOT / self.receipt['output']

    def test_source_and_export_integrity(self):
        source = ROOT / self.receipt['source']
        self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), self.receipt['source_sha256'])
        original = source.read_text(encoding='utf-8')
        prepared = (self.out / 'article-layout.md').read_text(encoding='utf-8')
        names = re.findall(r'!\[\[([^\]]+\.(?:png|gif))\]\]', original)
        self.assertEqual(len(names), 9)
        for name, item in zip(names, self.receipt['images']):
            original = original.replace(f'![[{name}]]', f'![[{item["file"]}]]')
            data = (self.out / item['file']).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), item['sha256'])
            self.assertLess(len(data), 2 * 1024 * 1024)
        self.assertEqual(prepared, original)
        for name, expected in self.receipt['files'].items():
            with self.subTest(file=name):
                self.assertEqual(hashlib.sha256((self.out / name).read_bytes()).hexdigest(), expected)

    def test_numbered_headings_images_and_video_positions(self):
        html = (self.out / 'article-layout.wechat.html').read_text(encoding='utf-8')
        source = (ROOT / self.receipt['source']).read_text(encoding='utf-8')
        parsed = ArticleHTML()
        parsed.feed(html)
        self.assertEqual(parsed.headings, re.findall(r'^## (.+)$', source, re.M))
        self.assertEqual(parsed.numbers, ['01', '02', '03', '04', '05'])
        self.assertEqual(len(parsed.images), 9)
        for encoded, image in zip(parsed.images, self.receipt['images']):
            self.assertTrue(encoded.startswith('data:image/'))
            self.assertEqual(base64.b64decode(encoded.split(',', 1)[1]), (self.out / image['file']).read_bytes())
        for name in ['动效.mp4', '深夜拉面.avi', '复古收音机.avi', '小镇.avi']:
            self.assertIn(f'（嵌入文件：{name}）', html)
        self.assertIn('color:#91bfe3', html)
        self.assertNotIn('**', html)
        self.assertNotIn('<script', html)
        # The draft contains no ==markers==, so ordinary bold remains bold.
        self.assertNotIn('<mark', html)


if __name__ == '__main__':
    unittest.main()
