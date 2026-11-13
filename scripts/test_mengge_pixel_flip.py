"""翻转候选：透视几何、正面/侧面端点、文字可读性和真实导出。"""
import json
from pathlib import Path
import subprocess
import unittest

from PIL import Image, ImageChops

ART = Path(__file__).resolve().parents[1] / 'output/ai-wechat-methodology/程序员梦哥像素闯关-v9翻转转场'
PREV = ART.parent / '程序员梦哥像素闯关-v8粒子转场'


class PixelFlipTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = json.loads((ART / 'manifest.json').read_text(encoding='utf8'))

    def test_original_scene_icons_and_final_text_are_preserved(self):
        for name in ['topic.png', 'poster.png', 'mobile.png']:
            self.assertEqual((ART / name).read_bytes(), (PREV / name).read_bytes())
        for name in self.m['topic_icons']:
            self.assertEqual((ART / f'{name}-pixel.png').read_bytes(), (PREV / f'{name}-pixel.png').read_bytes())
        self.assertEqual(self.m['visible_title'], '分享AI、少踩坑')
        self.assertFalse(self.m['combat'])
        self.assertNotIn('particle_dissolve', self.m)
        self.assertEqual(self.m['flip_transition']['cards'], 10)

    def test_flip_has_perspective_and_exact_endpoint_images(self):
        script = """
const assert=require('node:assert/strict');
const {createCanvas,loadImage}=require('../程序员拾梦闯关片头五案-v1/node_modules/@napi-rs/canvas');
const {project,drawFlip,angleAt,START,END}=require('./flip.cjs');
assert.deepEqual(project(30,20,0,500),{x:30,y:20});
assert.ok(Math.abs(project(30,20,90,500).x)<1e-10);
assert.ok(Math.abs(project(-30,20,45,500).y)>Math.abs(project(30,20,45,500).y));
for(const delay of [0,.025,.04,.07,.1,.15]){
  assert.equal(angleAt(START,delay),0);assert.equal(angleAt(END+.001,delay),90);
  let prev=0;for(let t=START;t<=END;t+=.02){const a=angleAt(t,delay);assert.ok(a>=prev&&a<=90);prev=a;}
}
(async()=>{
  const im=await loadImage('title-face.png'),direct=createCanvas(600,100),face=createCanvas(600,100);
  direct.getContext('2d').drawImage(im,0,0);drawFlip(face.getContext('2d'),im,300,50,600,100,0,1600);
  assert.ok(direct.toBuffer('image/png').equals(face.toBuffer('image/png')));
  for(const angle of [-90,90]){
    const edge=createCanvas(600,100);drawFlip(edge.getContext('2d'),im,300,50,600,100,angle,1600);
    assert.ok(edge.getContext('2d').getImageData(0,0,600,100).data.every(v=>v===0));
  }
})().catch(e=>{console.error(e);process.exitCode=1;});
"""
        result = subprocess.run(['node', '-e', script], cwd=ART, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_transition_timing_and_reproducible_seeking(self):
        m = self.m
        self.assertGreaterEqual(m['flip_transition']['start'], m['flag_lowering'][1])
        self.assertLess(m['title_reveal'][0], m['flip_transition']['end'])
        self.assertAlmostEqual(m['brand_hold'][1]-m['brand_hold'][0], 2)
        for s in m['states']:
            self.assertTrue(-90 <= s['title_angle'] <= 0)
            if s['t'] >= 6.56:
                self.assertEqual((s['title_angle'], s['title_alpha'], s['title_offset']), (0, 1, 0))
        script = """
const assert=require('node:assert/strict'),{state}=require('./motion.cjs');
const times=[0,1.9,3.1,5.44,5.62,5.8,5.98,6.12,6.3,6.56,8.76,8.8];
const snapshots=times.map(t=>JSON.stringify(state(t)));
for(let i=times.length-1;i>=0;i--)assert.equal(JSON.stringify(state(times[i])),snapshots[i]);
"""
        result = subprocess.run(['node', '-e', script], cwd=ART, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_encoded_flip_and_two_second_static_finale(self):
        with Image.open(ART / 'intro.gif') as gif:
            self.assertEqual((gif.n_frames, gif.size, gif.info['loop']), (450, (1200, 360), 0))
            frames, duration = [], 0
            for i in range(gif.n_frames):
                gif.seek(i)
                self.assertEqual(gif.info['duration'], 20)
                duration += gif.info['duration']
                frames.append(gif.convert('RGB').copy())
        self.assertEqual(duration, 9000)
        self.assertIsNone(ImageChops.difference(frames[0], frames[-1]).getbbox())
        for f in frames[328:429]:
            self.assertIsNone(ImageChops.difference(f, frames[328]).getbbox())
        box = (216, 0, 880, 195)
        self.assertIsNotNone(ImageChops.difference(frames[273].crop(box), frames[290].crop(box)).getbbox())
        self.assertIsNotNone(ImageChops.difference(frames[290].crop(box), frames[306].crop(box)).getbbox())
        self.assertLess((ART / 'intro.gif').stat().st_size, 2_000_000)
        self.assertFalse(self.m['wechat_verified'])


if __name__ == '__main__':
    unittest.main()
