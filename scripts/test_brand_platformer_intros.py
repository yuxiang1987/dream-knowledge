"""检查五款片头的交付文件、循环、关键动作和独立预览入口。"""
import json
from pathlib import Path
import subprocess
import unittest

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / 'output/ai-wechat-methodology/程序员拾梦闯关片头五案-v1'


class PlatformerIntroTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads((ART / 'manifest.json').read_text(encoding='utf-8'))

    def test_five_complete_animated_deliverables(self):
        self.assertEqual(len(self.manifest['variants']), 5)
        for variant in self.manifest['variants']:
            with self.subTest(variant=variant['id']):
                folder = ART / variant['id']
                self.assertLess((folder / 'intro.gif').stat().st_size, 2_000_000)
                with Image.open(folder / 'intro.gif') as gif:
                    self.assertEqual(gif.size, (1200, 360))
                    self.assertEqual(gif.info['loop'], 0)
                    self.assertEqual(gif.n_frames, 160)
                    first = gif.convert('RGB')
                    total = 0
                    for frame in range(gif.n_frames):
                        gif.seek(frame)
                        total += gif.info['duration']
                    self.assertEqual(total, 8000)
                    # Exact first/last equality catches a broken reset transition.
                    self.assertIsNone(ImageChops.difference(first, gif.convert('RGB')).getbbox())
                    gif.seek(80)
                    self.assertIsNotNone(ImageChops.difference(first, gif.convert('RGB')).getbbox())
                probe = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0',
                                        '-show_entries', 'stream=width,height,nb_frames,duration',
                                        '-of', 'json', str(folder / 'intro.mp4')],
                                       check=True, capture_output=True, text=True)
                stream = json.loads(probe.stdout)['streams'][0]
                self.assertEqual((stream['width'], stream['height']), (1200, 360))
                self.assertEqual(int(stream['nb_frames']), 160)
                self.assertAlmostEqual(float(stream['duration']), 8)

    def test_character_has_all_poses_and_true_alpha(self):
        for pose in ('idle', 'run', 'jump', 'wave'):
            with Image.open(ART / f'sprite-{pose}.png') as sprite:
                self.assertEqual(sprite.mode, 'RGBA')
                alpha = sprite.getchannel('A')
                self.assertEqual(alpha.getextrema(), (0, 255))
                self.assertGreater(sprite.height, 300)
        self.assertTrue((ART / 'avatar-reference.png').is_file())

    def test_distinct_motion_and_landing(self):
        for variant in self.manifest['variants']:
            states = variant['states']
            self.assertTrue(any(s['pose'] == 'jump' for s in states) or variant['id'] == '02-pipe')
            final = states[120]
            self.assertEqual(final['pose'], 'wave')
            self.assertEqual(final['y'], 308)
            self.assertAlmostEqual(final['reveal'], 1)
        flag = self.manifest['variants'][3]['states']
        # Two platforms must not cause an instantaneous fall at a stage boundary.
        for boundary in (20, 40):
            self.assertLess(abs(flag[boundary]['y'] - flag[boundary - 1]['y']), 25)
        pipe = self.manifest['variants'][1]['states']
        self.assertGreater(max(s['y'] for s in pipe), 400)
        self.assertLess(pipe[120]['x'], 715)

    def test_preview_links_and_verification_boundary(self):
        html = (ART / 'preview.html').read_text(encoding='utf-8')
        self.assertIn('375px', html)
        self.assertFalse(self.manifest['mobile_wechat_verified'])
        self.assertIn('尚未验收', html)
        for variant in self.manifest['variants']:
            for file in ('intro.gif', 'intro.mp4', 'keyframes.png'):
                self.assertIn(f"{variant['id']}/{file}", html)
                self.assertTrue((ART / variant['id'] / file).is_file())


if __name__ == '__main__':
    unittest.main()
