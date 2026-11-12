"""像素冒险：头像复用、碰撞时间线、固定标题与真实GIF循环。"""
from pathlib import Path
import hashlib
import json
import unittest

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / 'output/ai-wechat-methodology/程序员梦哥像素冒险-v1'


class MenggePixelAdventureTest(unittest.TestCase):
    def test_identity_collision_and_rest(self):
        m = json.loads((ART / 'manifest.json').read_text(encoding='utf-8'))
        self.assertEqual(m['name'], '程序员梦哥')
        self.assertEqual(m['tagline'], '折腾 AI，分享实用玩法')
        self.assertFalse(m['wechat_verified'])
        for pose in ('idle', 'jump'):
            old = ART.parent / '程序员拾梦闯关片头五案-v1' / f'sprite-{pose}.png'
            self.assertEqual(hashlib.sha256(old.read_bytes()).digest(),
                             hashlib.sha256((ART / old.name).read_bytes()).digest())
        hit = min(m['states'], key=lambda s: abs(s['t'] - m['hit_at']))
        self.assertEqual(hit['pose'], 'jump')
        self.assertLessEqual(abs(hit['y'] - hit['hero_height'] - m['block_bottom']), 4)
        self.assertTrue(any(s['sy'] < .92 and s['y'] == m['ground'] for s in m['states']))
        self.assertTrue(any(s['star_alpha'] == 1 and s['star_x'] > 1100 for s in m['states']))
        for s in m['states']:
            if 3 <= s['t'] <= 4.5:
                self.assertEqual(s['pose'], 'idle')
                self.assertEqual(s['y'], m['ground'])

    def test_gif_and_title_stability(self):
        with Image.open(ART / 'intro.gif') as gif:
            self.assertEqual(gif.size, (1200, 360))
            self.assertEqual(gif.n_frames, 140)
            self.assertEqual(gif.info['loop'], 0)
            frames, duration = [], 0
            for i in range(gif.n_frames):
                gif.seek(i)
                frames.append(gif.convert('RGB').copy())
                duration += gif.info['duration']
        self.assertEqual(duration, 5600)
        self.assertIsNone(ImageChops.difference(frames[0], frames[-1]).getbbox())
        self.assertGreater(len({hashlib.sha256(f.tobytes()).digest() for f in frames}), 45)
        title = frames[0].crop((565, 70, 990, 160))
        for frame in frames:
            self.assertIsNone(ImageChops.difference(title, frame.crop((565, 70, 990, 160))).getbbox())
        self.assertLess((ART / 'intro.gif').stat().st_size, 2_000_000)
        self.assertIn('375px', (ART / 'preview.html').read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
