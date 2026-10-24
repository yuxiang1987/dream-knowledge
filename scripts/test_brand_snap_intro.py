"""验收响指切换片头的导出、时间线和角色位置。"""
import json
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "output/ai-wechat-methodology/程序员拾梦响指片头-v1"


class BrandSnapIntroTest(unittest.TestCase):
    def test_gif_is_animated_and_closes(self):
        with Image.open(ART / "intro.gif") as gif:
            self.assertEqual(gif.size, (1246, 300))
            self.assertEqual(gif.n_frames, 144)
            self.assertEqual(gif.info["loop"], 0)
            first = gif.convert("RGB")
            duration = 0
            for i in range(gif.n_frames):
                gif.seek(i)
                duration += gif.info["duration"]
            self.assertEqual(duration, 7200)
            self.assertIsNone(ImageChops.difference(first, gif.convert("RGB")).getbbox())
            gif.seek(43)
            self.assertIsNotNone(ImageChops.difference(first, gif.convert("RGB")).getbbox())
        self.assertLess((ART / "intro.gif").stat().st_size, 2_000_000)

    def test_timeline_has_snap_blink_and_text_swap(self):
        motion = json.loads((ART / "motion.json").read_text(encoding="utf-8"))
        self.assertEqual(motion["timeline"]["title"], "程序员拾梦")
        self.assertEqual(motion["timeline"]["tagline"], "折腾 AI，分享实用玩法")
        self.assertAlmostEqual(motion["timeline"]["snap_at"], 2.15)
        self.assertAlmostEqual(motion["timeline"]["blink_at"], 2.25)
        self.assertEqual(motion["character"]["x"], 215)
        self.assertTrue(any(v["titleA"] > .99 and v["tagA"] == 0 for v in motion["states"]))
        self.assertTrue(any(v["snap"] > .99 for v in motion["states"]))
        self.assertTrue(any(v["blink"] > .99 for v in motion["states"]))
        self.assertTrue(any(v["titleA"] == 0 and v["tagA"] > .99 for v in motion["states"]))
        first, last = motion["states"][0], motion["states"][-1]
        self.assertEqual({k: v for k, v in first.items() if k != "t"},
                         {k: v for k, v in last.items() if k != "t"})

    def test_svg_is_standalone(self):
        root = ET.parse(ART / "intro.svg").getroot()
        self.assertEqual(root.attrib["viewBox"], "0 0 1246 300")
        tracks = 0
        for node in root.iter():
            tag = node.tag.rsplit("}", 1)[-1].lower()
            self.assertNotIn(tag, ("script", "foreignobject"))
            for key, value in node.attrib.items():
                self.assertFalse(key.lower().startswith("on"))
                if key.rsplit("}", 1)[-1] == "href":
                    self.assertTrue(value.startswith("data:image/png;base64,"))
            if "keyTimes" in node.attrib:
                tracks += 1
                self.assertEqual(node.attrib["dur"], "7.2s")
                self.assertEqual(node.attrib["repeatCount"], "indefinite")
                self.assertEqual(len(node.attrib["keyTimes"].split(";")),
                                 len(node.attrib["values"].split(";")))
        self.assertGreater(tracks, 1)

    def test_delivery_boundary(self):
        motion = json.loads((ART / "motion.json").read_text(encoding="utf-8"))
        self.assertFalse(motion["mobile_wechat_verified"])
        self.assertIn("375px", (ART / "preview.html").read_text(encoding="utf-8"))
        with Image.open(ART / "jumper.png") as sprite:
            self.assertEqual(sprite.getchannel("A").getpixel((0, 0)), 0)


if __name__ == "__main__":
    unittest.main()
