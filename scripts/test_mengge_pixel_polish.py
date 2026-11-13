"""v3验收：实际动作表使用、接触位置、双砖合拢与静止阅读时间。"""
import hashlib
import json
from pathlib import Path
import unittest

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / 'output/ai-wechat-methodology/程序员梦哥像素闯关-v3'


class MenggePixelPolishTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = json.loads((ART / 'manifest.json').read_text(encoding='utf8'))

    def test_pose_sheet_is_used_for_each_action(self):
        m = self.m
        with Image.open(ART / 'action-sheet.png') as sheet:
            self.assertEqual(sheet.mode, 'RGBA')
            self.assertLessEqual(sheet.getpixel((0, 0))[3], 3)
            hashes = []
            for box in m['sprite_boxes']:
                cell = sheet.crop((box['x'], box['y'], box['x']+box['w'], box['y']+box['h']))
                self.assertGreater(cell.width, 100)
                hashes.append(hashlib.sha256(cell.tobytes()).digest())
            self.assertEqual(len(set(hashes)), 16)
        states = m['states']
        self.assertEqual({s['frame'] for s in states if s['pose'] == 'run'}, set(range(8)))
        self.assertEqual({s['frame'] for s in states if s['pose'] == 'shoot'}, {8, 9, 10, 11})
        self.assertTrue({12, 13, 14, 15}.issubset({s['frame'] for s in states}))
        self.assertGreaterEqual(m['sprite_boxes'][2]['h']*m['sprite_scale'], 128)

    def test_contacts_projectiles_and_brand_landing(self):
        m = self.m
        self.assertEqual(m['visible_title'], '折腾ai，专业踩坑')
        for i, hit in enumerate(m['hits']):
            s = min(m['states'], key=lambda s: abs(s['t']-hit))
            height = m['sprite_boxes'][s['frame']]['h']*m['sprite_scale']
            self.assertLess(abs(s['y']-height-m['brick_bottom']), 3)
            self.assertLess(abs(s['x']+38-s['brick_centers'][i]), 3)
        for i, target in enumerate((340, 810)):
            before = max((s for s in m['states'] if s['t'] < m['impacts'][i] and s['bullets']), key=lambda s: s['t'])
            self.assertLess(abs(before['bullets'][0]['x']-target), 20)
            self.assertTrue(263 <= before['bullets'][0]['y'] <= 318)
        s = next(s for s in m['states'] if s['t'] == 9)
        self.assertEqual(s['unlocked'], [True, True])
        self.assertEqual(s['monster_alive'], [False, False])
        self.assertEqual(s['flag_y'], 264)
        gap = s['brick_centers'][1]-s['brick_centers'][0]-116*s['brick_scale']
        self.assertTrue(0 < gap < 20)
        self.assertAlmostEqual(m['brand_hold'][1]-m['brand_hold'][0], 2)
        self.assertFalse(m['wechat_verified'])

    def test_gif_static_finale_and_seam(self):
        with Image.open(ART / 'intro.gif') as gif:
            self.assertEqual(gif.size, (1200, 360))
            self.assertEqual(gif.n_frames, 290)
            self.assertEqual(gif.info['loop'], 0)
            frames, duration = [], 0
            for i in range(gif.n_frames):
                gif.seek(i)
                frames.append(gif.convert('RGB').copy())
                duration += gif.info['duration']
        self.assertEqual(duration, 11600)
        self.assertIsNone(ImageChops.difference(frames[0], frames[-1]).getbbox())
        for frame in frames[215:264]:
            self.assertIsNone(ImageChops.difference(frame, frames[215]).getbbox())
        title = frames[0].crop((340, 0, 860, 70))
        for frame in frames:
            self.assertIsNone(ImageChops.difference(title, frame.crop((340, 0, 860, 70))).getbbox())
        self.assertLess((ART / 'intro.gif').stat().st_size, 2_000_000)
        self.assertGreater(len({hashlib.sha256(f.tobytes()).digest() for f in frames}), 170)


if __name__ == '__main__':
    unittest.main()
