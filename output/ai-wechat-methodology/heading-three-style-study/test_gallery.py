from pathlib import Path
import unittest
from xml.etree import ElementTree

from PIL import Image


ROOT = Path(__file__).resolve().parent


class HeadingGalleryTest(unittest.TestCase):
    def test_ten_different_styles_share_one_example(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        grid = html.split('<div class="grid">', 1)[1].split("</div>", 1)[0]
        cards = list(ElementTree.fromstring("<grid>" + grid + "</grid>"))
        self.assertEqual([c.findtext("h2/b") for c in cards], [f"{i:02}" for i in range(1, 11)])
        styles = {c.find("h3").attrib["class"] for c in cards}
        self.assertEqual(len(styles), 10)
        for style in styles:
            self.assertIn("." + style + " ", html)
        self.assertEqual(len({c.findtext("h3/span") for c in cards}), 1)
        self.assertEqual(len({"".join(c.find("p").itertext()) for c in cards}), 1)

    def test_screenshot_includes_bottom_margin(self):
        with Image.open(ROOT / "overview.png") as image:
            w, h = image.size
            self.assertEqual(image.getpixel((0, 0)), image.getpixel((w // 4, h - 1)))
            self.assertIsNotNone(image.crop((0, h - 200, w, h)).getcolors(100000))
            self.assertGreater(len(image.crop((0, h - 200, w, h)).getcolors(100000)), 32)


if __name__ == "__main__":
    unittest.main()
