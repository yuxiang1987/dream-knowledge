"""GSAP版验收：确定性取帧、释放顺序、接触、收尾及实际GIF。"""
import json
import math
from pathlib import Path
import subprocess
import unittest

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / 'output/ai-wechat-methodology/程序员梦哥像素闯关-v6丝滑版'


class PixelGsapTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = json.loads((ART / 'manifest.json').read_text(encoding='utf8'))

    def test_gsap_is_installed_and_drives_repeatable_samples(self):
        package = json.loads((ART / 'package.json').read_text(encoding='utf8'))
        self.assertEqual(package['dependencies']['gsap'], self.m['animation_engine']['version'])
        installation = json.loads((ART / 'skills-install.json').read_text(encoding='utf8'))
        self.assertEqual(len(installation['skills']), 8)
        script = """
const assert=require('node:assert/strict'),{state}=require('./motion.cjs');
const times=[0,.4,.8,.94,1.2,1.91,3.2,5.6,6.36,8.54,8.6];
const before=times.map(t=>JSON.stringify(state(t)));
for(let i=times.length-1;i>=0;i--)assert.equal(JSON.stringify(state(times[i])),before[i]);
console.log('random-access samples match');
"""
        result = subprocess.run(['node', '-e', script], cwd=ART, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('samples match', result.stdout)

    def test_one_hit_center_out_release_and_settled_icons(self):
        m = self.m
        self.assertEqual(m['hits'], [.8])
        hit = next(s for s in m['states'] if s['t'] == .8)
        self.assertEqual(hit['unlocked'], [False, True, False])
        self.assertEqual(hit['interactive_brick'], 1)
        self.assertLess(abs(hit['x']+38-540), 3)
        height = m['sprite_boxes'][hit['frame']]['h']*m['sprite_scale']*hit['sy']
        self.assertLess(abs(hit['y']-height-m['brick_bottom']), 3)
        first = []
        for i in range(7):
            first.append(min(s['t'] for s in m['states'] if s['topic'][i]['alpha'] > 0))
        self.assertEqual(sorted(range(7), key=lambda i: first[i]), [2, 1, 3, 0, 4, 5, 6])
        full = next(s for s in m['states'] if s['t'] == 2)['topic']
        for i, v in enumerate(full):
            self.assertEqual((v['x'], v['y']), tuple(m['icon_targets'][i]))
            self.assertEqual((v['alpha'], v['scale'], v['angle']), (1, 1, 0))
            for w in full[i+1:]:
                self.assertTrue(abs(v['x']-w['x']) >= 72 or abs(v['y']-w['y']) >= 72)
        # 旋转/放大时也不能从上边缘裁掉图标。
        for s in m['states']:
            for v in s['topic']:
                if v['alpha'] <= 0:
                    continue
                a = math.radians(v['angle'])
                radius = 36*v['scale']*(abs(math.cos(a))+abs(math.sin(a)))
                self.assertGreaterEqual(v['y']-radius, -1)
        for name in m['topic_icons']:
            self.assertEqual((ART / f'{name}-pixel.png').read_bytes(),
                             (ART.parent / '程序员梦哥像素闯关-v5工具箱' / f'{name}-pixel.png').read_bytes())

    def test_flag_clear_footer_and_reset_are_ordered(self):
        m = self.m
        self.assertEqual(m['visible_title'], '分享AI、少踩坑')
        self.assertLessEqual(m['flag_lowering'][1], m['brick_fade'][0])
        self.assertLessEqual(m['brick_fade'][1], m['title_reveal'][0])
        self.assertAlmostEqual(m['brand_hold'][1]-m['brand_hold'][0], 2)
        for s in m['states']:
            if s['title_alpha'] > 0:
                self.assertEqual(s['brick_alpha'], 0)
            if 6.36 <= s['t'] <= 8.36:
                self.assertEqual((s['title_alpha'], s['title_offset']), (1, 0))
            if 8.52 <= s['t'] < 8.58:
                self.assertEqual(s['unlocked'], [False, True, False])
                self.assertEqual(s['monster_alive'], [False, False])
        self.assertFalse(m['wechat_verified'])

    def test_gif_really_has_50fps_closed_loop_and_static_footer(self):
        with Image.open(ART / 'intro.gif') as gif:
            self.assertEqual(gif.n_frames, 440)
            self.assertEqual(gif.size, (1200, 360))
            self.assertEqual(gif.info['loop'], 0)
            frames, duration = [], 0
            for i in range(gif.n_frames):
                gif.seek(i)
                self.assertEqual(gif.info['duration'], 20)
                duration += gif.info['duration']
                frames.append(gif.convert('RGB').copy())
        self.assertEqual(duration, 8800)
        self.assertIsNone(ImageChops.difference(frames[0], frames[-1]).getbbox())
        for f in frames[318:419]:
            self.assertIsNone(ImageChops.difference(f, frames[318]).getbbox())
        self.assertLess((ART / 'intro.gif').stat().st_size, 2_000_000)


if __name__ == '__main__':
    unittest.main()
