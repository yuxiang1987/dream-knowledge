"""检查本次排版的内容保真和交付完整性，不代替微信粘贴验收。"""
import base64
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import unittest

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
META=json.loads((HERE/'source-manifest.json').read_text(encoding='utf-8'))

class Document(HTMLParser):
    def __init__(self): super().__init__(); self.images=[]; self.text=[]
    def handle_starttag(self,tag,attrs):
        if tag=='img': self.images.append(dict(attrs)['src'])
        if tag=='br': self.text.append('\n')
    def handle_endtag(self,tag):
        # 渲染器以逐行块级code保留换行，HTML文本提取时还原行边界。
        if tag=='code': self.text.append('\n')
    def handle_data(self,data): self.text.append(data)

class LayoutDeliveryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source=(ROOT/META['source']).read_text(encoding='utf-8')
        cls.copy=(HERE/'article-layout.md').read_text(encoding='utf-8')
        cls.html=(HERE/'article-layout.wechat.html').read_text(encoding='utf-8')
        cls.dom=Document(); cls.dom.feed(cls.html)

    def test_source_unchanged(self):
        self.assertEqual(hashlib.sha256((ROOT/META['source']).read_bytes()).hexdigest(),META['sha256'])

    def test_copy_preserves_all_wording_and_media(self):
        copy_body=self.copy.split('\n',1)[1]
        normalize=lambda t:re.sub(r'\s+','',t.replace('==',''))
        self.assertEqual(normalize(copy_body),normalize(self.source))
        media=lambda t:re.findall(r'!\[\[([^\]]+)\]\]',t)
        self.assertEqual(media(self.copy),media(self.source))

    def test_historical_prompts_verbatim(self):
        pattern=r'```prompt\n(.*?)\n\s*```'
        original=re.findall(pattern,self.source,re.S)
        self.assertEqual(len(original),3)
        self.assertEqual(re.findall(pattern,self.copy,re.S),original)
        rendered=''.join(self.dom.text).replace('\xa0','')
        for prompt in original:
            self.assertIn(prompt,rendered)
        self.assertNotIn('**',rendered)

    def test_cover_first_and_images_complete(self):
        self.assertEqual(len(self.dom.images),6)
        self.assertEqual(base64.b64decode(self.dom.images[0].split(',',1)[1]),(ROOT/META['cover']).read_bytes())
        for uri in self.dom.images:
            self.assertTrue(uri.startswith('data:image/'))
            self.assertLess(len(base64.b64decode(uri.split(',',1)[1])),2*1024*1024)
        rendered=''.join(self.dom.text)
        for video in re.findall(r'!\[\[([^\]]+\.mp4)\]\]',self.source):
            self.assertIn(video,rendered)

    def test_preview_scroll_preserves_export(self):
        page=(HERE/'article-layout.preview.html').read_text(encoding='utf-8')
        self.assertIn('max-height:320px;overflow-y:auto!important',page)
        self.assertIn('::-webkit-scrollbar-thumb',page)
        self.assertNotIn('max-height:none;overflow-y:visible!important',page)
        self.assertEqual(self.html.count('max-height:320px;overflow:auto;'),3)
        original=Document()
        original.feed((HERE/'article-layout.full.wechat.html').read_text(encoding='utf-8'))
        self.assertEqual(''.join(self.dom.text),''.join(original.text))
        self.assertEqual(self.dom.images,original.images)
        # 预览的复制区始终保留正文全部HTML，不在滚动时删减节点。
        self.assertIn('<article id="content">'+self.html+'</article>',page)

    def test_initial_layout_browser_and_structure_reports(self):
        structure=json.loads((HERE/'structure-check.json').read_text(encoding='utf-8-sig'))
        self.assertTrue(structure['isValid'])
        self.assertEqual(structure['violations'],[])
        mobile=json.loads((HERE/'mobile-review.json').read_text(encoding='utf-8'))
        self.assertEqual(mobile['scrollWidth'],mobile['viewport'])
        self.assertEqual(mobile['longParagraphs'],[])
        self.assertTrue(all(i['loaded'] for i in mobile['images']))
        self.assertEqual(len(mobile['headings']),5)

if __name__=='__main__': unittest.main()
