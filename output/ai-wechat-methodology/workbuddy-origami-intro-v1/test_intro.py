"""Structural and causal timing checks for the delivered animation."""
import hashlib
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from PIL import Image, ImageChops, ImageStat

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SVG = "{http://www.w3.org/2000/svg}"


class IntroDeliveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = (HERE / "intro.svg").read_text(encoding="utf-8")
        cls.svg = ET.fromstring(cls.source)

    def test_portable_svg_and_copy_bundle(self):
        self.assertEqual(self.svg.get("viewBox"), "0 0 1246 220")
        forbidden = {"text", "image", "script", "defs", "style", "foreignObject"}
        for node in self.svg.iter():
            self.assertNotIn(node.tag.split("}")[-1], forbidden)
            self.assertFalse(any("href" in key for key in node.attrib))
        self.assertIn(self.source, (HERE / "intro.wechat.html").read_text(encoding="utf-8"))
        self.assertIn(self.source, (HERE / "preview.html").read_text(encoding="utf-8"))

    def test_all_animation_keyframes_are_valid(self):
        animations = [n for n in self.svg.iter() if n.tag in {SVG+"animate", SVG+"animateTransform"}]
        self.assertGreater(len(animations), 80)
        for node in animations:
            with self.subTest(attribute=node.get("attributeName"), values=node.get("values")):
                self.assertEqual(node.get("repeatCount"), "indefinite")
                if node.get("keyTimes"):
                    keys = list(map(float, node.get("keyTimes").split(";")))
                    self.assertEqual(keys[0], 0)
                    self.assertEqual(keys[-1], 1)
                    self.assertTrue(all(a < b for a, b in zip(keys, keys[1:])))
                    self.assertEqual(len(keys), len(node.get("values").split(";")))
                    if node.get("calcMode") == "spline":
                        curves = node.get("keySplines").split(";")
                        self.assertEqual(len(curves), len(keys)-1)
                        self.assertTrue(all(0 <= float(v) <= 1 for c in curves for v in c.split()))

    def test_activation_follows_button_press(self):
        ring = self.svg.find(f'.//*[@id="energy-ring"]')
        anim = ring.find(SVG+"animate")
        keys = list(map(float, anim.get("keyTimes").split(";")))
        self.assertGreaterEqual(keys[1]*8, 5.60)
        self.assertLess(keys[2]*8, 7.04)
        self.assertNotIn("正式上线", self.svg.get("aria-label"))
        for name in ["request-note", "three-prototypes", "origami-phone", "runner"]:
            self.assertIsNotNone(self.svg.find(f'.//*[@id="{name}"]'))

    def test_original_article_is_unchanged(self):
        article = ROOT / "raw/article/程序员梦哥/WorkBuddy + huashu skill 手搓健身小程序（附提示词）.md"
        self.assertEqual(hashlib.sha256(article.read_bytes()).hexdigest(),
                         "5a910ddebd0866c25209046a37dfb1e0f3cf3b21e7873b9c95f528163af7c496")

    def test_gif_duration_and_agreement_with_browser_frames(self):
        with Image.open(HERE / "intro.gif") as gif:
            self.assertEqual(gif.size, (1246, 220))
            self.assertEqual(gif.n_frames, 160)
            self.assertEqual(gif.info.get("loop"), 0)
            duration = 0
            for i in range(gif.n_frames):
                gif.seek(i)
                duration += gif.info["duration"]
            self.assertEqual(duration, 8000)
            for index in [10, 44, 67, 89, 112, 133]:
                with self.subTest(frame=index), Image.open(HERE / f"frame-{index/20:.2f}s.png") as png:
                    gif.seek(index)
                    difference = ImageChops.difference(png.convert("RGB"), gif.convert("RGB"))
                    self.assertLess(max(ImageStat.Stat(difference).mean), 2.5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
