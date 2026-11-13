"""图标候选：检查真实导出、顶砖接触、图标出场及收尾时序。"""
import json
from pathlib import Path
import unittest

from PIL import Image, ImageChops

ART = Path(__file__).resolve().parents[1] / 'output/ai-wechat-methodology/程序员梦哥像素闯关-v4图标版'


class PixelIconsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = json.loads((ART / 'manifest.json').read_text(encoding='utf8'))

    def test_icons_are_distinct_crisp_pixel_assets(self):
        self.assertEqual(self.m['topic_words'], [])
        self.assertEqual(self.m['brick_words'], [])
        self.assertEqual(self.m['topic_icons'], ['codex', 'claude'])
        pixels = []
        for name in self.m['topic_icons']:
            with Image.open(ART / f'{name}-pixel.png') as im:
                self.assertEqual(im.size, (24, 24))
                self.assertEqual(im.getpixel((0, 0))[3], 0)
                self.assertEqual({c[3] for _, c in im.getcolors()}, {0, 255})
                pixels.append(im.tobytes())
        self.assertNotEqual(*pixels)
        with Image.open(ART / 'topic.png') as im:
            # 两个图标均真正画入定帧，且落在对应砖块正上方。
            self.assertEqual(im.getpixel((390, 36))[:3], (32, 43, 59))
            self.assertEqual(im.getpixel((610, 36))[:3], (219, 121, 88))

    def test_hits_shots_and_pose_coverage(self):
        m = self.m
        for i, hit in enumerate(m['hits']):
            s = min(m['states'], key=lambda s: abs(s['t']-hit))
            height = m['sprite_boxes'][s['frame']]['h']*m['sprite_scale']
            self.assertLess(abs(s['y']-height-m['brick_bottom']), 3)
            self.assertLess(abs(s['x']+38-s['brick_centers'][i]), 3)
        for i, x in enumerate((740, 880)):
            s = max((s for s in m['states'] if s['t'] < m['impacts'][i] and s['bullets']), key=lambda s: s['t'])
            self.assertLess(abs(s['bullets'][0]['x']-x), 20)
        self.assertEqual({s['frame'] for s in m['states'] if s['pose'] == 'run'}, set(range(8)))
        self.assertEqual({s['frame'] for s in m['states'] if s['pose'] == 'shoot'}, {8, 9, 10, 11})

    def test_pop_visibility_and_finale_order(self):
        m = self.m
        self.assertLess(m['topic_settled'], 3)
        self.assertLessEqual(m['flag_lowering'][1], m['brick_fade'][0])
        self.assertLessEqual(m['brick_fade'][1], m['title_reveal'][0])
        self.assertAlmostEqual(m['brand_hold'][1]-m['brand_hold'][0], 2)
        for s in m['states']:
            for i, hit in enumerate(m['hits']):
                v = s['topic'][i]
                if s['t'] < hit:
                    self.assertEqual(v['alpha'], 0)
                if s['t'] >= hit+m['topic_pop_duration']:
                    self.assertEqual((v['alpha'], v['y']), (1, 42))
                if v['alpha'] > 0 and s['t'] >= hit+.28:
                    self.assertGreaterEqual(v['y']-m['icon_size']/2, 0)
            if s['title_alpha'] > 0:
                self.assertEqual(s['brick_alpha'], 0)
        self.assertEqual(m['visible_title'], '折腾AI、少踩坑')
        self.assertFalse(m['wechat_verified'])

    def test_encoded_gif_loop_and_two_second_hold(self):
        with Image.open(ART / 'intro.gif') as gif:
            self.assertEqual(gif.size, (1200, 360))
            self.assertEqual(gif.n_frames, 220)
            self.assertEqual(gif.info['loop'], 0)
            frames, duration = [], 0
            for i in range(gif.n_frames):
                gif.seek(i)
                frames.append(gif.convert('RGB').copy())
                duration += gif.info['duration']
        self.assertEqual(duration, 8800)
        self.assertIsNone(ImageChops.difference(frames[0], frames[-1]).getbbox())
        for frame in frames[157:208]:
            self.assertIsNone(ImageChops.difference(frame, frames[157]).getbbox())
        self.assertLess((ART / 'intro.gif').stat().st_size, 2_000_000)


if __name__ == '__main__':
    unittest.main()
