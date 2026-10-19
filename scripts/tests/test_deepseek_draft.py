"""Protect the reviewed draft's media, structure and historical prompts."""
import hashlib
import json
from pathlib import Path
import re
import unittest

FIXTURE = json.loads(r'''{"path": "raw/article/程序员拾梦/实测DeepSeek V4.1 Flash-1017：许愿式编程，还真有点东西.md", "media": ["Pasted image 20261019144926.png", "Pasted image 20261019145825.png", "Pasted image 20261019145959.png", "ChatGPT GIF 2026年10月19日 15_18_33.gif", "动效.mp4", "Pasted image 20261019160528.png", "深夜拉面.avi", "Pasted image 20261019153243.png", "Pasted image 20261019153123.png", "复古收音机.avi", "Pasted image 20261019153422.png", "小镇.avi", "Pasted image 20261019153620.png"], "headings": ["## 先让它给自己做一份作品集", "## 再让它开一家深夜拉面店", "## 把一台老收音机拆开", "## 最后，造一座会生活的小镇", "## 最后"], "prompt_sha256": ["6d6ddefc8725305eccd857d379fc91612cfd10f74a874d1024e114168cfbd5c1", "9a9176d786ba3f934463cc398e6edde72b1d456f2bdb165953527b7b2d9b3d10", "6a2dbfd8d9eab64ce5e352a51a114d061349f7dd3575a06e0a977c83fcd6704f"]}''')

class DraftIntegrity(unittest.TestCase):
    def test_reviewed_material_preserved(self):
        root = Path(__file__).resolve().parents[2]
        text = (root / FIXTURE['path']).read_text(encoding='utf-8')
        self.assertEqual(re.findall(r'!\[\[([^\]]+)\]\]', text), FIXTURE['media'])
        self.assertEqual(re.findall(r'^## .+$', text, re.M), FIXTURE['headings'])
        prompts = re.findall(r'```提示词\n(.*?)\n```', text, re.S)
        self.assertEqual([hashlib.sha256(x.encode()).hexdigest() for x in prompts], FIXTURE['prompt_sha256'])
        for media in FIXTURE['media']:
            self.assertTrue(any(root.rglob(media)), media)

if __name__ == '__main__':
    unittest.main()
