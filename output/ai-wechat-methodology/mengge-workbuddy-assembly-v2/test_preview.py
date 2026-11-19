from base64 import b64decode
from io import BytesIO
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

from PIL import Image

OUT = Path(__file__).resolve().parent
spec = spec_from_file_location('assembly_v2', OUT / 'build.py')
assembly_v2 = module_from_spec(spec)
spec.loader.exec_module(assembly_v2)
PREVIOUS, SHEET, creative, idle_pose = (
    assembly_v2.PREVIOUS, assembly_v2.SHEET, assembly_v2.creative, assembly_v2.idle_pose)

NS = '{http://www.w3.org/2000/svg}'


class AssemblyTest(unittest.TestCase):
    def test_exact_default_character_and_no_group_heading(self):
        art = (OUT / 'intro.svg').read_text(encoding='utf-8')
        root = ET.fromstring(art)
        hero = root.find(f'{NS}image[@id="hero"]')
        with Image.open(BytesIO(b64decode(hero.get('href').split(',', 1)[1]))) as exported:
            with Image.open(SHEET) as source:
                w, h = source.size
                reference = source.convert('RGBA').crop((w // 2 + 67, 27, w // 2 + 225, 334))
            self.assertEqual(exported.tobytes(), reference.tobytes())
        self.assertEqual(idle_pose().size, (158, 307))
        self.assertNotIn('七项设置', art)
        for key, label in zip(range(7), creative.LABELS):
            card = root.find(f'.//{NS}g[@id="tile-{key}"]')
            self.assertIsNotNone(card.find(f'.//{NS}g[@aria-label="{label}"]'))
        self.assertIn(art, (OUT / 'preview.html').read_text(encoding='utf-8'))

    def test_original_assembly_rebuild_remains_identical(self):
        baseline = (PREVIOUS / 'c.svg').read_text(encoding='utf-8')
        self.assertEqual(baseline.split('">', 1)[1], creative.assembly() + '</svg>\n')


if __name__ == '__main__':
    unittest.main()
