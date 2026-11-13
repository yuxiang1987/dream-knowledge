"""v3验收：动作表、顶砖金币、降旗后退砖与片尾渐显。"""
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
        self.assertEqual(m['visible_title'], '梦哥爱折腾')
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
        self.assertEqual(s['brick_alpha'], 0)
        self.assertEqual(s['title_alpha'], 1)
        self.assertAlmostEqual(m['brand_hold'][1]-m['brand_hold'][0], 2)
        self.assertFalse(m['wechat_verified'])

    def test_gif_static_finale_and_seam(self):
        with Image.open(ART / 'intro.gif') as gif:
            self.assertEqual(gif.size, (1200, 360))
            self.assertEqual(gif.n_frames, 295)
            self.assertEqual(gif.info['loop'], 0)
            frames, duration = [], 0
            for i in range(gif.n_frames):
                gif.seek(i)
                frames.append(gif.convert('RGB').copy())
                duration += gif.info['duration']
        self.assertEqual(duration, 11800)
        self.assertIsNone(ImageChops.difference(frames[0], frames[-1]).getbbox())
        for frame in frames[218:269]:
            self.assertIsNone(ImageChops.difference(frame, frames[218]).getbbox())
        # 开场标题区只有天空；片尾文字确实出现在画面中。
        self.assertTrue(all(hi-lo <= 6 for lo, hi in frames[0].crop((350, 0, 850, 70)).getextrema()))
        self.assertIsNotNone(ImageChops.difference(frames[0].crop((350, 90, 850, 185)),
                                                 frames[225].crop((350, 90, 850, 185))).getbbox())
        self.assertEqual(frames[225].getpixel((410, 86)), frames[225].getpixel((0, 0)))
        self.assertLess((ART / 'intro.gif').stat().st_size, 2_000_000)
        self.assertGreater(len({hashlib.sha256(f.tobytes()).digest() for f in frames}), 170)

    def test_coins_and_finale_order(self):
        m = self.m
        self.assertLessEqual(m['flag_lowering'][1], m['brick_fade'][0])
        self.assertLessEqual(m['brick_fade'][1], m['title_reveal'][0])
        for hit, x in zip(m['hits'], (460, 680)):
            coins = [coin for s in m['states'] if hit <= s['t'] < hit+m['coin_duration']
                     for coin in s['coins'] if coin['x'] == x]
            self.assertGreater(len(coins), 10)
            self.assertLess(min(c['y'] for c in coins), 25)
            self.assertGreater(coins[-1]['y'], min(c['y'] for c in coins))
        for s in m['states']:
            if s['t'] < m['flag_lowering'][1]:
                self.assertEqual(s['title_alpha'], 0)
            if s['title_alpha'] > 0:
                self.assertEqual(s['brick_alpha'], 0)


if __name__ == '__main__':
    unittest.main()
