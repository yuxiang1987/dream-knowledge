"""Verify the three native timelines using Chromium. Set CHROME to override its path."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
import xml.etree.ElementTree as ET

OUT = Path(__file__).resolve().parent
CHROME = os.environ.get('CHROME', r'C:\Program Files\Google\Chrome\Application\chrome.exe')


class StorageTrioTest(unittest.TestCase):
    def test_standalone_exports(self):
        preview = (OUT / 'preview.html').read_text(encoding='utf8')
        for name in 'abc':
            image = (OUT / f'{name}.svg').read_text(encoding='utf8')
            root = ET.fromstring(image)
            self.assertIn(image, preview)
            self.assertEqual(root.get('viewBox'), '0 0 1000 216')
            self.assertTrue(any(node.tag.endswith('}animateTransform') for node in root.iter()))
            self.assertFalse(any(node.tag.rsplit('}', 1)[-1] in {'script', 'image', 'text', 'foreignObject'}
                                 or any('href' in key or key.startswith('on') for key in node.attrib)
                                 for node in root.iter()))

    def test_distinct_motion_and_result(self):
        preview = (OUT / 'preview.html').read_text(encoding='utf8')
        script = '''<script>
          addEventListener('load', async () => {
            const roots = [...document.querySelectorAll('main svg')];
            const node = id => document.getElementById(id);
            const css = id => getComputedStyle(node(id));
            const x = id => node(id).transform.animVal.getItem(0).matrix.e;
            const fade = id => +css(id).opacity;
            const tick = () => new Promise(resolve => setTimeout(resolve, 35));
            async function go(time) {
              roots.forEach(svg => { svg.pauseAnimations(); svg.setCurrentTime(time); });
              await tick();
            }
            function check(valid, label) { if (!valid) throw new Error(label); }
            try {
              await go(2.46);
              check(x('a-beam') > 0 && fade('a-focus') === 0, 'scanner starts before focus');
              await go(2.94);
              check(x('a-beam') < 651 && x('b-folder') > 76 && x('b-folder') < 429, 'scanner and folder travel');
              check(+parseFloat(css('b-route').strokeDashoffset) < 100, 'workspace route draws');
              check(x('c-lens') > 0 && x('c-lens') < 265 && fade('c-item-0') === 1 && fade('c-item-2') === 0, 'checklist follows the lens');
              document.querySelector('[data-frame="4.35"]').click();
              await tick();
              check(roots.every(svg => svg.animationsPaused()), 'preview freeze');
              check(fade('a-focus') === 1 && x('b-folder') === 429 && x('c-lens') === 530, 'three outcomes');
              check([0, 1, 2].every(i => fade(`c-item-${i}`) === 1), 'checklist completed');
              document.querySelector('#replay').click();
              check(roots.every(svg => !svg.animationsPaused() && svg.getCurrentTime() < .1), 'preview replay');
              document.body.dataset.check = 'pass';
            } catch (error) { document.body.dataset.check = error.message; }
          }, {once: true});
        </script>'''
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as temp:
            directory = Path(temp)
            page = directory / 'verify.html'
            page.write_text(preview.replace('</body>', script + '</body>'), encoding='utf8')
            result = subprocess.run([CHROME, '--headless', '--no-first-run', f'--user-data-dir={directory / "chrome"}',
                                     '--virtual-time-budget=1000', '--run-all-compositor-stages-before-draw',
                                     '--dump-dom', page.as_uri()], capture_output=True, check=True,
                                    encoding='utf8', errors='replace', timeout=25)
        self.assertEqual(result.stdout.partition('<body data-check="')[2].partition('"')[0], 'pass')


if __name__ == '__main__':
    unittest.main()
