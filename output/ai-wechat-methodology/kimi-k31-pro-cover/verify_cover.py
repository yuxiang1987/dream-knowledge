"""封面交付检查；屏幕文字拼写仍须视觉审阅，不以像素检测代替OCR。"""
from pathlib import Path
import unittest
from PIL import Image, ImageFont

HERE = Path(__file__).resolve().parent


class CoverDeliveryTest(unittest.TestCase):
    def test_final_canvas(self):
        with Image.open(HERE / 'cover-v2-900x383.png') as im:
            im.load()
            self.assertEqual(im.size, (900, 383))
            self.assertEqual(im.mode, 'RGB')
            self.assertEqual(im.format, 'PNG')

    def test_typography_fits_left_column(self):
        title = ImageFont.truetype('C:/Windows/Fonts/msyhbd.ttc', 48)
        subtitle = ImageFont.truetype('C:/Windows/Fonts/msyh.ttc', 20)
        self.assertLessEqual(title.getlength('Kimi K3.1 Pro'), 405)
        self.assertLessEqual(subtitle.getlength('四个项目实测 · 有惊喜，也有槽点'), 405)

    def test_screen_is_no_longer_blank(self):
        with Image.open(HERE / 'cover-v2-900x383.png') as im:
            screen = im.crop((607, 170, 637, 201)).convert('RGB')
            cyan = sum(g > 130 and b > 130 and r < 130
                       for r, g, b in screen.get_flattened_data())
            self.assertGreater(cyan, 10)

    def test_source_and_edit_assets_decode(self):
        for name in ('fabric-source-frame.png', 'background.png', 'background-v2.png'):
            with self.subTest(asset=name), Image.open(HERE / name) as im:
                im.verify()


if __name__ == '__main__':
    unittest.main()
