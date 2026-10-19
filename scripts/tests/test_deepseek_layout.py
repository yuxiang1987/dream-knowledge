import unittest
import json
import hashlib
from pathlib import Path
from html.parser import HTMLParser

class Images(HTMLParser):
    def __init__(self):
        super().__init__(); self.images = []
    def handle_starttag(self, tag, attrs):
        if tag == 'img': self.images.append(dict(attrs).get('src', ''))

class LayoutTest(unittest.TestCase):
    def test_export(self):
        root = Path(__file__).resolve().parents[2]
        folder = root / 'output/deepseek-flash-1017-layout-v1'
        manifest = json.loads((folder / 'manifest.json').read_text(encoding='utf-8'))
        self.assertEqual(hashlib.sha256((root / manifest['source']).read_bytes()).hexdigest(), manifest['source_sha256'])
        html = next(folder.glob('*.wechat.html')).read_text(encoding='utf-8')
        parser = Images(); parser.feed(html)
        self.assertEqual(len(parser.images), 9)
        self.assertTrue(all(x.startswith('data:image/') for x in parser.images))
        for phrase in ['作品集', '深夜拉面', '收音机', '小镇', '拿出全部本事']:
            self.assertIn(phrase, html)
        for name, digest in manifest['files'].items():
            self.assertEqual(hashlib.sha256((folder / name).read_bytes()).hexdigest(), digest)

if __name__ == '__main__': unittest.main()
