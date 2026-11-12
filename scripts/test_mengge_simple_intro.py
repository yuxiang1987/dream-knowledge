"""新账号片头：名称、可移植SVG、文字切换和循环导出。"""
from pathlib import Path
import hashlib
import json
import unittest
import xml.etree.ElementTree as ET

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / 'output/ai-wechat-methodology/程序员梦哥简洁片头-v1'


class MenggeSimpleIntroTest(unittest.TestCase):
    def test_name_assets_and_svg_portability(self):
        motion = json.loads((ART / 'motion.json').read_text(encoding='utf-8'))
        self.assertEqual(motion['name'], '程序员梦哥')
        self.assertFalse(motion['wechat_verified'])
        source = ART / motion['avatar_source']
        self.assertEqual(hashlib.sha256(source.read_bytes()).digest(),
                         hashlib.sha256((ART / 'avatar-reference.png').read_bytes()).digest())
        root = ET.parse(ART / 'intro.svg').getroot()
        self.assertIn('程序员梦哥', root.attrib['aria-label'])
        self.assertNotIn('拾梦', root.attrib['aria-label'])
        tracks = 0
        for node in root.iter():
            tag = node.tag.rsplit('}', 1)[-1]
            self.assertNotIn(tag.lower(), ('script', 'foreignobject', 'text'))
            for key, value in node.attrib.items():
                self.assertFalse(key.lower().startswith('on'))
                if key.rsplit('}', 1)[-1] == 'href':
                    self.assertTrue(value.startswith('data:image/png;base64,'))
            if tag in ('animate', 'animateTransform'):
                tracks += 1
                self.assertEqual(node.attrib['dur'], '5.2s')
                self.assertEqual(node.attrib['repeatCount'], 'indefinite')
                self.assertEqual(len(node.attrib['values'].split(';')),
                                 len(node.attrib['keyTimes'].split(';')))
        self.assertEqual(tracks, 4)

    def test_gif_holds_transitions_and_seam(self):
        with Image.open(ART / 'intro.gif') as gif:
            self.assertEqual(gif.size, (1200, 260))
            self.assertEqual(gif.info['loop'], 0)
            frames, times, t = [], [], 0
            for i in range(gif.n_frames):
                gif.seek(i)
                frames.append(gif.convert('RGB').copy())
                times.append(t)
                t += gif.info['duration']
            self.assertEqual(t, 5200)
        def at(ms):
            return frames[max(i for i, start in enumerate(times) if start <= ms)]
        self.assertIsNone(ImageChops.difference(at(0), at(1800)).getbbox())
        self.assertIsNone(ImageChops.difference(at(2800), at(4400)).getbbox())
        self.assertIsNotNone(ImageChops.difference(at(0), at(3200)).getbbox())
        self.assertIsNone(ImageChops.difference(frames[0], frames[-1]).getbbox())
        # 头像和账号名全程固定，变化只能在介绍文字区域。
        base = frames[0]
        for frame in frames:
            box = ImageChops.difference(base, frame).getbbox()
            if box:
                self.assertGreaterEqual(box[0], 340)
                self.assertGreaterEqual(box[1], 130)
                self.assertLessEqual(box[3], 212)
        self.assertGreater(len({hashlib.sha256(f.tobytes()).digest() for f in frames}), 20)
        self.assertLess((ART / 'intro.gif').stat().st_size, 2_000_000)


if __name__ == '__main__':
    unittest.main()
