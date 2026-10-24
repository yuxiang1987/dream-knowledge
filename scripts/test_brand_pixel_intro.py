"""验收独立SVG、GIF循环、身份素材与导出边界，不调用生成模型。"""
import json
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "output/ai-wechat-methodology/程序员拾梦像素片头-v1"


class BrandPixelIntroTest(unittest.TestCase):
    def test_standalone_svg_needs_no_external_resources_or_script(self):
        root = ET.parse(ART / "intro.svg").getroot()
        self.assertEqual(root.attrib["viewBox"], "0 0 1246 220")
        self.assertIn("程序员拾梦", root.attrib["aria-label"])
        animated = 0
        for node in root.iter():
            tag = node.tag.rsplit("}", 1)[-1]
            self.assertNotIn(tag.lower(), ("script", "foreignobject"))
            for key, value in node.attrib.items():
                self.assertFalse(key.lower().startswith("on"))
                if key.rsplit("}", 1)[-1] == "href":
                    self.assertTrue(value.startswith("data:image/png;base64,"))
            if tag in ("animate", "animateTransform"):
                animated += 1
                self.assertEqual(node.attrib["dur"], "6s")
                self.assertEqual(node.attrib["repeatCount"], "indefinite")
                self.assertEqual(len(node.attrib["values"].split(";")),
                                 len(node.attrib["keyTimes"].split(";")))
        self.assertGreater(animated, 1)

    def test_gif_has_closed_loop_and_expected_delivery_dimensions(self):
        with Image.open(ART / "intro.gif") as gif:
            self.assertEqual(gif.size, (1246, 220))
            self.assertEqual(gif.info["loop"], 0)
            self.assertEqual(gif.n_frames, 120)
            first = gif.convert("RGB")
            duration = 0
            for frame in range(gif.n_frames):
                gif.seek(frame)
                duration += gif.info["duration"]
            self.assertEqual(duration, 6000)
            self.assertIsNone(ImageChops.difference(first, gif.convert("RGB")).getbbox())
            gif.seek(70)
            self.assertIsNotNone(ImageChops.difference(first, gif.convert("RGB")).getbbox())
        self.assertLess((ART / "intro.gif").stat().st_size, 3_000_000)

    def test_identity_assets_and_delivery_claims(self):
        with Image.open(ART / "avatar-pixel.png") as avatar:
            self.assertIn("A", avatar.getbands())
            alpha = avatar.getchannel("A")
            self.assertEqual(alpha.getpixel((0, 0)), 0)
            self.assertGreater(alpha.getextrema()[1], 0)
        with Image.open(ART / "avatar-clean.png") as clean:
            self.assertEqual(clean.width, clean.height)
        manifest = json.loads((ART / "manifest.json").read_text(encoding="utf-8"))
        self.assertFalse(manifest["mobile_wechat_verified"])
        self.assertEqual(manifest["text"], ["程序员拾梦", "折腾 AI，分享实用玩法"])
        self.assertIn("375px", (ART / "preview.html").read_text(encoding="utf-8"))
        self.assertIn("尚未在公众号后台", (ART / "README.md").read_text(encoding="utf-8"))

    def test_three_variants_are_standalone_svg_with_the_same_avatar(self):
        folder = ART / "variants"
        manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual({v["id"] for v in manifest}, {"code-window", "file-flow", "spark-orbit"})
        ns = "{http://www.w3.org/2000/svg}"
        href = "{http://www.w3.org/1999/xlink}href"
        base_avatar = ET.parse(ART / "intro.svg").getroot().find(ns + "image").attrib[href]
        for variant in manifest:
            with self.subTest(variant=variant["id"]):
                root = ET.parse(folder / (variant["id"] + ".svg")).getroot()
                self.assertEqual(root.attrib["viewBox"], "0 0 1246 220")
                self.assertEqual(root.find(ns + "image").attrib[href], base_avatar)
                for node in root.iter():
                    self.assertNotIn(node.tag.rsplit("}", 1)[-1].lower(), ("script", "foreignobject"))
                    for key, value in node.attrib.items():
                        self.assertFalse(key.lower().startswith("on"))
                        if key.rsplit("}", 1)[-1] == "href":
                            self.assertTrue(value.startswith("data:image/png;base64,"))
                    if "keyTimes" in node.attrib:
                        self.assertEqual(len(node.attrib["keyTimes"].split(";")),
                                         len(node.attrib["values"].split(";")))
                self.assertFalse(variant["mobile_wechat_verified"])

    def test_variant_gifs_close_their_loops(self):
        for name in ("code-window", "file-flow", "spark-orbit"):
            with self.subTest(variant=name), Image.open(ART / "variants" / (name + ".gif")) as gif:
                self.assertEqual(gif.size, (1246, 220))
                self.assertEqual(gif.n_frames, 120)
                self.assertEqual(gif.info["loop"], 0)
                first = gif.convert("RGB")
                duration = 0
                for i in range(gif.n_frames):
                    gif.seek(i)
                    duration += gif.info["duration"]
                self.assertEqual(duration, 6000)
                self.assertIsNone(ImageChops.difference(first, gif.convert("RGB")).getbbox())
                self.assertLess((ART / "variants" / (name + ".gif")).stat().st_size, 3_000_000)

    def test_only_right_motion_changes_and_three_scenes_differ(self):
        with Image.open(ART / "poster.png") as im:
            poster = im.convert("RGB")
        stills = []
        for name in ("code-window", "file-flow", "spark-orbit"):
            with Image.open(ART / "variants" / (name + "-poster.png")) as im:
                self.assertIsNone(ImageChops.difference(poster, im.convert("RGB")).getbbox())
            with Image.open(ART / "variants" / (name + "-still.png")) as im:
                still = im.convert("RGB")
            self.assertIsNone(ImageChops.difference(poster.convert("RGB").crop((0, 0, 235, 220)),
                                                   still.crop((0, 0, 235, 220))).getbbox())
            stills.append(still.crop((600, 0, 1246, 220)))
        for i in range(len(stills)):
            for j in range(i + 1, len(stills)):
                self.assertIsNotNone(ImageChops.difference(stills[i], stills[j]).getbbox())


if __name__ == "__main__":
    unittest.main()
