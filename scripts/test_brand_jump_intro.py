"""检查跳字片头的实际导出、落脚位置和角色裁切边界。"""
import json
import math
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

from PIL import Image, ImageChops

ART = Path(__file__).resolve().parents[1] / "output/ai-wechat-methodology/程序员拾梦跳字片头-v1"


class BrandJumpIntroTest(unittest.TestCase):
    def test_exported_gif_is_animated_and_seamless(self):
        with Image.open(ART / "intro.gif") as gif:
            self.assertEqual(gif.size, (1246, 300))
            self.assertEqual(gif.n_frames, 160)
            self.assertEqual(gif.info["loop"], 0)
            first = gif.convert("RGB")
            duration = 0
            for i in range(gif.n_frames):
                gif.seek(i)
                duration += gif.info["duration"]
            self.assertEqual(duration, 8000)
            self.assertIsNone(ImageChops.difference(first, gif.convert("RGB")).getbbox())
            gif.seek(13)
            self.assertIsNotNone(ImageChops.difference(first, gif.convert("RGB")).getbbox())
        self.assertLess((ART / "intro.gif").stat().st_size, 2_000_000)

    def test_hops_land_on_letters_and_keep_character_in_frame(self):
        motion = json.loads((ART / "motion.json").read_text(encoding="utf-8"))
        self.assertEqual(motion["route"], [0, 1, 2, 3, 4, 3, 2, 1, 0])
        centers = [300, 460, 620, 780, 940]
        for v in motion["states"]:
            if not v["air"]:
                self.assertAlmostEqual(v["x"], centers[v["idx"]])
                self.assertAlmostEqual(v["foot"], motion["baseline"] + v["dy"][v["idx"]])
            else:
                self.assertLessEqual(min(centers[v["from"]], centers[v["to"]]), v["x"])
                self.assertGreaterEqual(max(centers[v["from"]], centers[v["to"]]), v["x"])
            angle = math.radians(v["angle"])
            half = motion["sprite_width"] * v["sx"] / 2
            for x in (-half, half):
                for y in (-motion["sprite_height"] * v["sy"], 0):
                    px = v["x"] + x * math.cos(angle) - y * math.sin(angle)
                    py = v["foot"] + x * math.sin(angle) + y * math.cos(angle)
                    self.assertGreaterEqual(px, 0)
                    self.assertLessEqual(px, motion["width"])
                    self.assertGreaterEqual(py, 4, f"头部裁切风险 t={v['t']}")
                    self.assertLessEqual(py, motion["height"])
        first, last = motion["states"][0], motion["states"][-1]
        self.assertEqual({k: v for k, v in first.items() if k != "t"},
                         {k: v for k, v in last.items() if k != "t"})

    def test_svg_is_standalone_and_animation_tracks_are_complete(self):
        root = ET.parse(ART / "intro.svg").getroot()
        self.assertEqual(root.attrib["viewBox"], "0 0 1246 300")
        ids = {n.attrib.get("id") for n in root.iter()}
        self.assertTrue({f"letter-{i}" for i in range(5)} <= ids)
        tracks = 0
        for n in root.iter():
            self.assertNotIn(n.tag.rsplit("}", 1)[-1].lower(), ("script", "foreignobject"))
            for key, value in n.attrib.items():
                self.assertFalse(key.lower().startswith("on"))
                if key.rsplit("}", 1)[-1] == "href":
                    self.assertTrue(value.startswith("data:image/png;base64,"))
            if "keyTimes" in n.attrib:
                tracks += 1
                self.assertEqual(n.attrib["dur"], "8s")
                self.assertEqual(n.attrib["repeatCount"], "indefinite")
                times = [float(t) for t in n.attrib["keyTimes"].split(";")]
                self.assertEqual(times, sorted(times))
                self.assertEqual((times[0], times[-1]), (0, 1))
                self.assertEqual(len(times), len(n.attrib["values"].split(";")))
        self.assertGreater(tracks, 10)

    def test_identity_source_and_delivery_boundary(self):
        with Image.open(ART / "jumper.png") as sprite:
            self.assertIn("A", sprite.getbands())
            self.assertEqual(sprite.getchannel("A").getpixel((0, 0)), 0)
        motion = json.loads((ART / "motion.json").read_text(encoding="utf-8"))
        self.assertFalse(motion["mobile_wechat_verified"])
        self.assertIn("375px", (ART / "preview.html").read_text(encoding="utf-8"))
        self.assertIn("尚未在公众号后台", (ART / "README.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
