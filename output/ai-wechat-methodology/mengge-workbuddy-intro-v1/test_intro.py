from pathlib import Path
import unittest

from PIL import Image, ImageChops


class IntroTest(unittest.TestCase):
    def test_gif_keeps_avatar_and_switches_reply(self):
        gif = Path(__file__).with_name('intro.gif')
        self.assertLess(gif.stat().st_size, 1_000_000)
        with Image.open(gif) as image:
            self.assertEqual(image.size, (1000, 236))
            self.assertEqual(image.info['loop'], 0)
            frames = {}
            elapsed = 0
            for index in range(image.n_frames):
                image.seek(index)
                for instant in (0, 1400, 2100, 3650, 5350):
                    if instant not in frames and elapsed <= instant < elapsed + image.info['duration']:
                        frames[instant] = image.convert('RGB')
                elapsed += image.info['duration']
        self.assertEqual(elapsed, 5400)
        for frame in frames.values():
            self.assertLess(frame.crop((53, 53, 131, 164)).convert('L').getextrema()[0], 40)
        before, after = frames[2100], frames[3650]
        self.assertEqual(before.getpixel((928, 53)), (238, 246, 255))
        self.assertEqual(after.getpixel((928, 53)), (34, 95, 218))
        self.assertEqual(after.getpixel((878, 150)), (34, 95, 218))
        brand = (206, 44, 697, 192)
        self.assertIsNotNone(ImageChops.difference(frames[1400].crop(brand), frames[0].crop(brand)).getbbox())
        loop_delta = ImageChops.difference(frames[5350].crop(brand), frames[0].crop(brand))
        self.assertLessEqual(max(hi for _, hi in loop_delta.getextrema()), 6)


if __name__ == '__main__':
    unittest.main()
