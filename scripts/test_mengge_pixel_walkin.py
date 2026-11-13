"""左侧入场候选：无战斗、原绘像素图标、一次顶砖及循环导出。"""
import hashlib
import json
from pathlib import Path
import subprocess
import unittest

from PIL import Image, ImageChops

ART = Path(__file__).resolve().parents[1] / 'output/ai-wechat-methodology/程序员梦哥像素闯关-v7入场版'


class PixelWalkinTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = json.loads((ART / 'manifest.json').read_text(encoding='utf8'))

    def test_left_approach_one_contact_and_no_combat(self):
        m = self.m
        self.assertFalse(m['combat'])
        self.assertEqual(m['impacts'], [])
        self.assertEqual(m['hits'], [1.9])
        approach = [s for s in m['states'] if .04 <= s['t'] <= 1.3]
        self.assertLess(approach[0]['x'], 120)
        self.assertEqual(approach[-1]['x'], 502)
        self.assertTrue(all(a['x'] <= b['x'] for a, b in zip(approach, approach[1:])))
        self.assertEqual({s['frame'] for s in approach if s['pose'] == 'walk'}, set(range(8)))
        for s in m['states']:
            self.assertEqual(s['bullets'], [])
            self.assertEqual(s['monster_alive'], [])
            self.assertNotEqual(s['pose'], 'shoot')
        hit = next(s for s in m['states'] if s['t'] == 1.9)
        self.assertEqual(hit['unlocked'], [False, True, False])
        self.assertEqual(hit['x']+38, 540)
        height = m['sprite_boxes'][hit['frame']]['h']*m['sprite_scale']*hit['sy']
        self.assertLess(abs(hit['y']-height-150), 3)
        self.assertTrue(all(s['x'] == 502 for s in m['states'] if 1.3 <= s['t'] <= 3.14))

    def test_pixel_icons_are_procedural_and_not_sampled_screenshots(self):
        script = """
const fs=require('fs'),assert=require('node:assert/strict');
const {createCanvas}=require('../程序员拾梦闯关片头五案-v1/node_modules/@napi-rs/canvas');
const {drawIcons}=require('./icons.cjs');
for(const [name,im] of drawIcons(createCanvas))assert.ok(im.toBuffer('image/png').equals(fs.readFileSync(name+'-pixel.png')));
console.log('all seven icons reproduced from geometry');
"""
        result = subprocess.run(['node', '-e', script], cwd=ART, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        icon_source = (ART / 'icons.cjs').read_text(encoding='utf8')
        self.assertNotIn('loadImage', icon_source)
        self.assertNotIn('drawImage', icon_source)
        hashes = []
        for name in self.m['topic_icons']:
            f = ART / f'{name}-pixel.png'
            with Image.open(f) as im:
                self.assertEqual(im.size, (24, 24))
                self.assertEqual({c[3] for _, c in im.getcolors()}, {0, 255})
                self.assertLessEqual(len(im.getcolors()), 9)
            hashes.append(hashlib.sha256(f.read_bytes()).hexdigest())
            self.assertNotEqual(f.read_bytes(), (ART.parent / '程序员梦哥像素闯关-v6丝滑版' / f.name).read_bytes())
        self.assertEqual(len(set(hashes)), 7)

    def test_scatter_and_random_seeking(self):
        full = next(s for s in self.m['states'] if s['t'] == 3.1)['topic']
        for i, v in enumerate(full):
            self.assertEqual((v['x'], v['y']), tuple(v['target']))
            self.assertEqual((v['alpha'], v['scale'], v['angle']), (1, 1, 0))
            for w in full[i+1:]:
                self.assertTrue(abs(v['x']-w['x']) >= 72 or abs(v['y']-w['y']) >= 72)
        for s in self.m['states']:
            if s['t'] <= 1.9:
                self.assertTrue(all(v['alpha'] == 0 for v in s['topic']))
            if s['title_alpha'] > 0:
                self.assertEqual(s['brick_alpha'], 0)
        script = """
const assert=require('node:assert/strict'),{state}=require('./motion.cjs');
const times=[0,.7,1.3,1.9,2.2,3.1,4,5.6,6.5,8.54,8.6];
const snapshots=times.map(t=>JSON.stringify(state(t)));
for(let i=times.length-1;i>=0;i--)assert.equal(JSON.stringify(state(times[i])),snapshots[i]);
"""
        result = subprocess.run(['node', '-e', script], cwd=ART, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_encoded_loop_and_static_footer(self):
        self.assertEqual(self.m['visible_title'], '分享AI、少踩坑')
        self.assertFalse(self.m['wechat_verified'])
        with Image.open(ART / 'intro.gif') as gif:
            self.assertEqual((gif.n_frames, gif.size, gif.info['loop']), (440, (1200, 360), 0))
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
        # 原怪物所在区域在入场和顶砖期间保持为静止背景。
        self.assertIsNone(ImageChops.difference(frames[0].crop((700, 250, 940, 310)),
                                               frames[145].crop((700, 250, 940, 310))).getbbox())
        self.assertLess((ART / 'intro.gif').stat().st_size, 2_000_000)


if __name__ == '__main__':
    unittest.main()
