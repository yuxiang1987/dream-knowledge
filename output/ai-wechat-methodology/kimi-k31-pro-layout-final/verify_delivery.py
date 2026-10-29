"""验证更新Skill直接生成的完整交付，不代替微信粘贴与手机验收。"""
import base64
from hashlib import sha256
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import unittest
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
class Document(HTMLParser):
 def __init__(self): super().__init__();self.images=[];self.text=[];self.styles=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='img':self.images.append(a['src'])
  if 'style' in a:self.styles.append((tag,a['style']))
  if tag=='br':self.text.append('\n')
 def handle_endtag(self,tag):
  if tag=='code':self.text.append('\n')
 def handle_data(self,s):self.text.append(s)
class FullDeliveryTest(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.meta=json.loads((HERE/'source-manifest.json').read_text(encoding='utf-8'))
  cls.source=(ROOT/cls.meta['source']).read_text(encoding='utf-8')
  cls.md=(HERE/'article-layout.md').read_text(encoding='utf-8')
  cls.html=(HERE/'article-layout.wechat.html').read_text(encoding='utf-8')
  cls.page=(HERE/'article-layout.preview.html').read_text(encoding='utf-8')
  cls.doc=Document();cls.doc.feed(cls.html)
 def test_source_and_copy_preserved(self):
  self.assertEqual(sha256((ROOT/self.meta['source']).read_bytes()).hexdigest(),self.meta['sha256'])
  normalize=lambda s:re.sub(r'\s+','',s.replace('==',''))
  self.assertEqual(normalize(self.md.split('\n',1)[1]),normalize(self.source))
 def test_prompts_complete(self):
  pattern=r'```prompt\n(.*?)\n\s*```'
  prompts=re.findall(pattern,self.source,re.S)
  self.assertEqual(len(prompts),3)
  self.assertEqual(re.findall(pattern,self.md,re.S),prompts)
  text=''.join(self.doc.text).replace('\xa0','')
  for p in prompts:self.assertIn(p,text)
  self.assertNotIn('**',text)
 def test_images_and_video_positions(self):
  self.assertEqual(len(self.doc.images),6)
  self.assertEqual(base64.b64decode(self.doc.images[0].split(',',1)[1]),(ROOT/self.meta['cover']).read_bytes())
  for uri in self.doc.images:self.assertLess(len(base64.b64decode(uri.split(',',1)[1])),2*1024*1024)
  text=''.join(self.doc.text)
  for video in re.findall(r'!\[\[([^\]]+\.mp4)\]\]',self.source):self.assertIn(video,text)
 def test_no_lost_text(self):
  old=Document();old.feed((HERE.parent/'kimi-k31-pro-layout/article-layout.full.wechat.html').read_text(encoding='utf-8'))
  normalize=lambda s:re.sub(r'\s+','',s)
  self.assertEqual(normalize(''.join(self.doc.text)),normalize(''.join(old.text)))
  self.assertEqual(self.doc.images,old.images)
 def test_full_copy_and_native_features(self):
  self.assertIn('<article id="content">'+self.html+'</article>',self.page)
  self.assertIn('复制完整公众号排版',self.page)
  self.assertEqual(self.html.count('max-height:320px;overflow:auto;'),3)
  self.assertGreater(self.html.count('data-reading-tail'),10)
  centered=[s for tag,s in self.doc.styles if tag=='section' and 'padding:0 32px;' in s]
  self.assertEqual(len(centered),6)
  for s in centered:self.assertIn('text-align:center;',s)
 def test_structure_report(self):
  report=json.loads((HERE/'structure-check.json').read_text(encoding='utf-8-sig'))
  self.assertTrue(report['isValid']);self.assertEqual(report['violations'],[])
if __name__=='__main__':unittest.main()
