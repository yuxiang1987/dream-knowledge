"""工具箱候选：一次顶中砖、七个图标散开、片尾与循环导出。"""
import hashlib
import json
from pathlib import Path
import unittest

from PIL import Image, ImageChops

ART = Path(__file__).resolve().parents[1] / 'output/ai-wechat-methodology/程序员梦哥像素闯关-v5工具箱'


class PixelToolboxTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = json.loads((ART / 'manifest.json').read_text(encoding='utf8'))

    def test_only_middle_brick_is_hit_once(self):
        m = self.m
        self.assertEqual(m['hits'], [.8])
        self.assertEqual(m['brick_words'], [])
        hit = next(s for s in m['states'] if s['t'] == .8)
        self.assertEqual(hit['brick_centers'], [420, 540, 660])
        self.assertEqual(hit['interactive_brick'], 1)
        self.assertEqual(hit['unlocked'], [False, True, False])
        self.assertLess(abs(hit['x']+38-540), 3)
        height = m['sprite_boxes'][hit['frame']]['h']*m['sprite_scale']
        self.assertLess(abs(hit['y']-height-m['brick_bottom']), 3)
        states = m['states']
        rises = [i for i, s in enumerate(states) if s['pose'] == 'rise' and (i == 0 or states[i-1]['pose'] != 'rise')]
        self.assertEqual(len(rises), 1)
        for s in states:
            self.assertEqual(s['unlocked'][::2], [False, False])

    def test_seven_icons_scatter_without_final_overlap(self):
        m = self.m
        self.assertEqual(m['topic_icons'], ['codex', 'claude', 'workbuddy', 'kimi', 'user07', 'minimax', 'deepseek'])
        full = next(s for s in m['states'] if s['t'] == 1.8)['topic']
        half = m['icon_size']/2
        for i, v in enumerate(full):
            self.assertEqual(v['alpha'], 1)
            self.assertEqual([v['x'], v['y']], v['target'])
            self.assertGreaterEqual(v['x']-half, 0)
            self.assertGreaterEqual(v['y']-half, 0)
            for w in full[i+1:]:
                self.assertTrue(abs(v['x']-w['x']) >= half*2 or abs(v['y']-w['y']) >= half*2)
        for s in m['states']:
            for i, v in enumerate(s['topic']):
                if s['t'] < .8+i*m['icon_stagger']:
                    self.assertEqual(v['alpha'], 0)
            if s['title_alpha'] > 0:
                self.assertEqual(s['brick_alpha'], 0)
        with Image.open(ART / 'topic.png') as im:
            for v in full:
                box = tuple(int(n) for n in (v['x']-half, v['y']-half, v['x']+half, v['y']+half))
                self.assertGreater(len(im.crop(box).getcolors() or []), 2)

    def test_icon_sources_and_actual_pixel_files(self):
        source = json.loads((ART / 'icons/sources.json').read_text(encoding='utf8'))
        self.assertEqual(len(source['icons']), 7)
        for record in source['icons']:
            filename = record['name']+'-source.png'
            self.assertEqual(hashlib.sha256((ART / 'icons' / filename).read_bytes()).hexdigest(), record['sha256'])
        hashes = []
        for name in self.m['topic_icons']:
            with Image.open(ART / f'{name}-pixel.png') as im:
                self.assertEqual(im.size, (24, 24))
                self.assertEqual({c[3] for _, c in im.getcolors()}, {0, 255})
                hashes.append(hashlib.sha256(im.tobytes()).hexdigest())
        self.assertEqual(len(set(hashes)), 7)

    def test_new_footer_and_encoded_loop(self):
        m = self.m
        self.assertEqual(m['visible_title'], '分享AI、少踩坑')
        self.assertFalse(m['wechat_verified'])
        self.assertAlmostEqual(m['brand_hold'][1]-m['brand_hold'][0], 2)
        self.assertLessEqual(m['flag_lowering'][1], m['brick_fade'][0])
        self.assertLessEqual(m['brick_fade'][1], m['title_reveal'][0])
        with Image.open(ART / 'intro.gif') as gif:
            self.assertEqual(gif.n_frames, 220)
            self.assertEqual(gif.size, (1200, 360))
            self.assertEqual(gif.info['loop'], 0)
            frames, duration = [], 0
            for i in range(gif.n_frames):
                gif.seek(i)
                frames.append(gif.convert('RGB').copy())
                duration += gif.info['duration']
        self.assertEqual(duration, 8800)
        self.assertIsNone(ImageChops.difference(frames[0], frames[-1]).getbbox())
        for f in frames[157:208]:
            self.assertIsNone(ImageChops.difference(f, frames[157]).getbbox())
        self.assertLess((ART / 'intro.gif').stat().st_size, 2_000_000)


if __name__ == '__main__':
    unittest.main()
