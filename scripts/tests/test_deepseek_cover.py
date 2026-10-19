from pathlib import Path
import unittest
from PIL import Image

class CoverTest(unittest.TestCase):
    def test_cover_deliverables(self):
        folder = Path(__file__).resolve().parents[2] / 'output/deepseek-flash-1017-cover'
        for name, size in [('cover-v1.png', (900, 383)), ('thumbnail.png', (360, 153))]:
            with Image.open(folder / name) as image:
                self.assertEqual(image.format, 'PNG')
                self.assertEqual(image.size, size)
                image.verify()
        self.assertTrue((folder / 'design.md').is_file())

if __name__ == '__main__':
    unittest.main()
