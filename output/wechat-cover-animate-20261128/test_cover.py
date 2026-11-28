"""Check publishing dimensions and title layout at the delivered size."""
import unittest
from PIL import Image, ImageDraw, ImageFont
from compose import HERE, TEXT


class CoverTest(unittest.TestCase):
    def test_png_dimensions(self):
        for name, size in [("cover.png", (900, 383)), ("thumbnail.png", (360, 153))]:
            with Image.open(HERE / name) as image:
                self.assertEqual(image.format, "PNG")
                self.assertEqual(image.size, size)
                image.verify()

    def test_type_stays_inside_left_safe_area(self):
        draw = ImageDraw.Draw(Image.new("RGB", (900, 383)))
        for text, position, size, font, _ in TEXT:
            left, top, right, bottom = draw.textbbox(
                position, text, font=ImageFont.truetype(font, size)
            )
            self.assertGreaterEqual(left, 45)
            self.assertGreaterEqual(top, 20)
            self.assertLessEqual(right, 365)
            self.assertLessEqual(bottom, 363)


if __name__ == "__main__":
    unittest.main()
