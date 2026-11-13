"""像素粒子退场：原图层拆分连续、确定性、片尾时序及真实GIF。"""
import json
from pathlib import Path
import subprocess
import unittest

from PIL import Image, ImageChops

ART = Path(__file__).resolve().parents[1] / 'output/ai-wechat-methodology/程序员梦哥像素闯关-v8粒子转场'
PREV = ART.parent / '程序员梦哥像素闯关-v7入场版'


class PixelDissolveTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = json.loads((ART / 'manifest.json').read_text(encoding='utf8'))

    def test_accepted_front_and_drawn_icons_are_preserved(self):
        self.assertEqual((ART / 'topic.png').read_bytes(), (PREV / 'topic.png').read_bytes())
        for name in self.m['topic_icons']:
            self.assertEqual((ART / f'{name}-pixel.png').read_bytes(), (PREV / f'{name}-pixel.png').read_bytes())
        self.assertFalse(self.m['combat'])
        self.assertEqual(self.m['hits'], [1.9])
        self.assertEqual(self.m['visible_title'], '分享AI、少踩坑')
        for s in self.m['states']:
            self.assertEqual((s['bullets'], s['monster_alive']), ([], []))

    def test_particle_tiles_reconstruct_layer_without_jump(self):
        script = """
const assert=require('node:assert/strict');
const {createCanvas,loadImage}=require('../程序员拾梦闯关片头五案-v1/node_modules/@napi-rs/canvas');
const {makeParticles,sample,START,END}=require('./particles.cjs');
(async()=>{
  const im=await loadImage('particle-source.png'),c=createCanvas(im.width,im.height),g=c.getContext('2d');g.drawImage(im,0,0);
  const data=g.getImageData(0,0,im.width,im.height).data,parts=makeParticles(data,im.width,im.height);
  assert.ok(parts.length>300&&parts.length<2000);
  assert.equal(JSON.stringify(parts),JSON.stringify(makeParticles(data,im.width,im.height)));
  const out=createCanvas(im.width,im.height),o=out.getContext('2d');
  for(const p of parts){
    const v=sample(p,0);assert.deepEqual([v.x,v.y,v.alpha,v.scale],[p.x,p.y,1,1]);
    o.drawImage(c,p.x,p.y,p.w,p.h,p.x,p.y,p.w,p.h);
    assert.equal(sample(p,END-START).alpha,0);
  }
  assert.ok(Buffer.from(data).equals(Buffer.from(o.getImageData(0,0,im.width,im.height).data)));
})().catch(e=>{console.error(e);process.exitCode=1;});
"""
        result = subprocess.run(['node', '-e', script], cwd=ART, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        with Image.open(ART / 'particle-source.png') as im:
            self.assertIsNone(im.getchannel('A').crop((0, 170, 1200, 360)).getbbox())
            self.assertIsNone(im.getchannel('A').crop((900, 0, 1200, 360)).getbbox())

    def test_flag_dissolve_and_footer_overlap_are_controlled(self):
        m = self.m
        particle = m['particle_dissolve']
        self.assertGreaterEqual(particle['start'], m['flag_lowering'][1])
        self.assertGreater(m['title_reveal'][0], particle['start']+.5)
        self.assertLessEqual(particle['end']-m['title_reveal'][0], .13)
        self.assertAlmostEqual(m['brand_hold'][1]-m['brand_hold'][0], 2)
        for s in m['states']:
            self.assertEqual(s['particle_active'], particle['start'] <= s['t'] < particle['end'])
            if s['t'] < m['title_reveal'][0]:
                self.assertEqual(s['title_alpha'], 0)
            if s['t'] >= particle['start']:
                self.assertEqual(s['brick_alpha'], 0)
        script = """
const assert=require('node:assert/strict'),{state}=require('./motion.cjs');
const times=[0,1.9,3.1,5.44,5.46,5.78,6.04,6.16,6.56,8.76,8.8];
const values=times.map(t=>JSON.stringify(state(t)));
for(let i=times.length-1;i>=0;i--)assert.equal(JSON.stringify(state(times[i])),values[i]);
"""
        result = subprocess.run(['node', '-e', script], cwd=ART, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_encoded_gif_transition_and_two_second_finale(self):
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
        # 粒子变化确实进入编码帧，且位于图标/砖块区域。
        box = (216, 0, 880, 195)
        self.assertIsNotNone(ImageChops.difference(frames[273].crop(box), frames[289].crop(box)).getbbox())
        self.assertIsNotNone(ImageChops.difference(frames[289].crop(box), frames[300].crop(box)).getbbox())
        self.assertLess((ART / 'intro.gif').stat().st_size, 2_000_000)
        self.assertFalse(self.m['wechat_verified'])


if __name__ == '__main__':
    unittest.main()
