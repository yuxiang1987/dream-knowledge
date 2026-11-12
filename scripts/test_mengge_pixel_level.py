"""闯关v2：发炮命中、两词解锁、降旗与真实循环导出。"""
import hashlib
import json
from pathlib import Path
import unittest

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / 'output/ai-wechat-methodology/程序员梦哥像素闯关-v2'


class MenggePixelLevelTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = json.loads((ART / 'manifest.json').read_text(encoding='utf-8'))

    def test_two_shots_and_two_bricks(self):
        m = self.m
        self.assertEqual(m['visible_title'], '折腾ai，专业踩坑')
        self.assertEqual(m['brick_words'], ['dream', 'coder'])
        for impact, target, index in zip(m['impacts'], (300, 850), (0, 1)):
            before = max((s for s in m['states'] if s['t'] < impact and s['bullets']), key=lambda s: s['t'])
            self.assertTrue(before['monster_alive'][index])
            self.assertLess(abs(before['bullets'][0]['x'] - target), 25)
            self.assertTrue(270 <= before['bullets'][0]['y'] <= m['ground'])
            after = min((s for s in m['states'] if s['t'] >= impact), key=lambda s: s['t'])
            self.assertFalse(after['monster_alive'][index])
        for i, hit in enumerate(m['hits']):
            contact = min(m['states'], key=lambda s: abs(s['t'] - hit))
            self.assertEqual(contact['pose'], 'jump')
            self.assertLess(abs(contact['y'] - contact['hero_height'] - m['brick_bottom']), 3)
            self.assertLess(abs(contact['x'] + 30 - (440, 650)[i]), 3)
            after = min((s for s in m['states'] if s['t'] >= hit), key=lambda s: s['t'])
            self.assertTrue(after['unlocked'][i])
        intermediate = next(s for s in m['states'] if s['t'] == 4)
        self.assertEqual(intermediate['unlocked'], [True, False])

    def test_flag_direction_and_asset_identity(self):
        states = [s for s in self.m['states'] if 7.2 <= s['t'] <= 8.5]
        self.assertLess(states[0]['flag_y'], states[-1]['flag_y'])
        self.assertTrue(all(a['flag_y'] <= b['flag_y'] for a, b in zip(states, states[1:])))
        final = next(s for s in self.m['states'] if s['t'] == 8.5 or s['t'] == 8.48)
        self.assertEqual(final['unlocked'], [True, True])
        self.assertEqual(final['monster_alive'], [False, False])
        self.assertEqual(final['flag_y'], 264)
        for pose in ('idle', 'run', 'jump'):
            old = ART.parent / '程序员拾梦闯关片头五案-v1' / f'sprite-{pose}.png'
            self.assertEqual(hashlib.sha256(old.read_bytes()).digest(),
                             hashlib.sha256((ART / old.name).read_bytes()).digest())
        self.assertFalse(self.m['wechat_verified'])

    def test_gif_decode_title_and_seam(self):
        with Image.open(ART / 'intro.gif') as gif:
            self.assertEqual(gif.size, (1200, 360))
            self.assertEqual(gif.n_frames, 250)
            self.assertEqual(gif.info['loop'], 0)
            frames, duration = [], 0
            for i in range(gif.n_frames):
                gif.seek(i)
                frames.append(gif.convert('RGB').copy())
                duration += gif.info['duration']
        self.assertEqual(duration, 10000)
        self.assertIsNone(ImageChops.difference(frames[0], frames[-1]).getbbox())
        title = frames[0].crop((335, 0, 865, 100))
        for frame in frames:
            self.assertIsNone(ImageChops.difference(title, frame.crop((335, 0, 865, 100))).getbbox())
        self.assertGreater(len({hashlib.sha256(f.tobytes()).digest() for f in frames}), 140)
        self.assertLess((ART / 'intro.gif').stat().st_size, 2_000_000)
        self.assertIn('375px', (ART / 'preview.html').read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
