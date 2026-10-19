from pathlib import Path
import json,re,unittest,hashlib
from PIL import Image

class ExportFix(unittest.TestCase):
 def test_compressed_export(self):
  root=Path(__file__).resolve().parents[2]; out=root/'output/deepseek-flash-1017-layout-v2'
  html=(out/'article-layout.wechat.html').read_text(encoding='utf-8')
  self.assertEqual(len(re.findall(r'<img\b',html)),9)
  self.assertNotIn('**',html)
  report=json.loads((out/'image-report.json').read_text(encoding='utf-8'))
  self.assertEqual(len(report),9)
  for item in report:
   p=out/'images'/item['output'];self.assertLess(p.stat().st_size,2*1024*1024)
   with Image.open(p) as im:
    if p.suffix=='.gif':self.assertGreater(im.n_frames,1)
    else:im.verify()
  source=root/'raw/article/程序员拾梦/实测DeepSeek V4.1 Flash-1017：许愿式编程，还真有点东西.md'
  self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(),'05b16cf30301925a27692cb20d916b1f5b6bebd829c7c37e564fd62669d7d46e')

if __name__=='__main__':unittest.main()
