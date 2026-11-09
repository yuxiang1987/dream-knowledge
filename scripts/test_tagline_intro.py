"""校验实际GIF动画、落地位置、顶砖时刻与循环接缝。"""
import json
from pathlib import Path
import unittest
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / 'output/ai-wechat-methodology/wechat-tagline-intro-v1'


class TaglineIntroTest(unittest.TestCase):
    def test_exported_gif_is_a_real_loop(self):
        with Image.open(ART / 'intro.gif') as gif:
            self.assertEqual(gif.size, (1200, 400))
            self.assertEqual(gif.info['loop'], 0)
            self.assertEqual(gif.n_frames, 144)
            first = gif.convert('RGB')
            elapsed = 0
            unique = set()
            for i in range(gif.n_frames):
                gif.seek(i)
                elapsed += gif.info['duration']
                unique.add(gif.convert('RGB').tobytes())
            self.assertEqual(elapsed, 7200)
            self.assertGreater(len(unique), 80)
            self.assertIsNone(ImageChops.difference(first, gif.convert('RGB')).getbbox())
        self.assertLess((ART / 'intro.gif').stat().st_size, 2_000_000)

    def test_hit_landing_and_reading_hold(self):
        manifest = json.loads((ART / 'manifest.json').read_text(encoding='utf-8'))
        self.assertEqual(manifest['text'], '折腾ai，分享实用玩法')
        states = {round(s['t'], 2): s for s in manifest['states']}
        impact = states[1.7]
        self.assertAlmostEqual(impact['x'], 365)
        self.assertAlmostEqual(impact['y'] - 128, 162)
        self.assertTrue(impact['hit'])
        self.assertEqual(states[2.2]['y'], 350)
        for time in [4.5, 5.5, 6.5]:
            self.assertEqual(states[time]['y'], 350)
            self.assertEqual(states[time]['x'], 1040)
            self.assertEqual(states[time]['pose'], 'wave')
        self.assertFalse(manifest['mobile_wechat_verified'])
        self.assertIn('not native Image 2.6', manifest['animation_method'])


if __name__ == '__main__':
    unittest.main()
