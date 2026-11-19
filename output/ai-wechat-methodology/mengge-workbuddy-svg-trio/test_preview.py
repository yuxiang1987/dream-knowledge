"""Run the standalone SVG/preview checks in Chrome. Set CHROME to override its path."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
import xml.etree.ElementTree as ET

OUT = Path(__file__).resolve().parent
NS = '{http://www.w3.org/2000/svg}'
CHROME = os.environ.get('CHROME', r'C:\Program Files\Google\Chrome\Application\chrome.exe')


class TrioTest(unittest.TestCase):
    def test_svg_requires_neither_assets_nor_scripts_and_has_valid_timelines(self):
        for name in ('a', 'b', 'c'):
            with self.subTest(name=name):
                root = ET.parse(OUT / f'{name}.svg').getroot()
                self.assertEqual(root.get('viewBox'), '0 0 1000 216')
                for node in root.iter():
                    self.assertIn(node.tag.removeprefix(NS), {'svg', 'rect', 'circle', 'ellipse', 'path', 'g', 'animate', 'animateTransform'})
                    self.assertFalse(any('href' in k or k.startswith('on') for k in node.attrib))
                    if not node.tag.removeprefix(NS).startswith('animate'):
                        continue
                    keys = list(map(float, node.get('keyTimes').split(';')))
                    self.assertEqual(keys, sorted(set(keys)))
                    self.assertEqual((keys[0], keys[-1]), (0, 1))
                    self.assertEqual(len(node.get('values').split(';')), len(keys))
                    self.assertEqual(len(node.get('keySplines').split(';')), len(keys) - 1)

    def test_chrome_interpolation_and_controls(self):
        preview = (OUT / 'preview.html').read_text(encoding='utf-8')
        checks = '''<script>
        async function verify() {
          try {
            const get = id => document.getElementById(id);
            const opacity = id => +getComputedStyle(get(id)).opacity;
            const roots = [...document.querySelectorAll('main svg')];
            const tick = () => new Promise(resolve => setTimeout(resolve, 35));
            const go = async t => {
              roots.forEach(svg => { svg.pauseAnimations(); svg.setCurrentTime(t); });
              await tick();
            };
            const dx = id => get(id).transform.animVal.getItem(0).matrix.e;
            function check(condition, label) { if (!condition) throw Error(label); }
            await go(.5);
            check(opacity('a-brand') === 1 && opacity('a-scene') === 0, 'brand opening');
            await go(1.54);
            check(opacity('a-brand') > 0 && opacity('a-brand') < 1 && opacity('a-scene') > 0, 'overlapping transitions');
            await go(2.15);
            check(opacity('a-old') === 1 && opacity('a-new') === 0 && dx('b-card') === 0, 'initial states');
            await go(2.83);
            check(dx('b-card') > 17 && dx('b-card') < 319, 'card interpolates');
            const mid = parseFloat(getComputedStyle(get('c-line')).strokeDashoffset);
            check(mid > 0 && mid < 100, 'path drawing interpolates');
            document.querySelector('[data-frame="4.35"]').click();
            await tick();
            check(roots.every(svg => Math.abs(svg.getCurrentTime() - 4.35) < .001 && svg.animationsPaused()), 'synced freeze');
            check(opacity('a-new') === 1 && opacity('a-picked') === 1 && opacity('a-old') === 0, 'reply replacement');
            check(dx('b-card') === 319 && opacity('b-done') === 1, 'card lands');
            check(opacity('c-done') === 1 && !parseFloat(getComputedStyle(get('c-line')).strokeDashoffset), 'progress arrived');
            await go(6.35);
            check(opacity('a-brand') === 1 && opacity('a-scene') === 0, 'loop returns to brand');
            get('slow').click();
            check(get('slow').getAttribute('aria-pressed') === 'true' && roots.every(svg => svg.animationsPaused()), 'slow mode');
            get('replay').click();
            check(roots.every(svg => svg.getCurrentTime() < .1 && !svg.animationsPaused()), 'synced replay');
            document.body.dataset.check = 'pass';
          } catch (err) { document.body.dataset.check = err.message; }
        }
        addEventListener('load', verify, {once: true});
        </script>'''
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as temp:
            temp = Path(temp)
            testcase = temp / 'testcase.html'
            testcase.write_text(preview.replace('</body>', checks + '</body>'), encoding='utf-8')
            process = subprocess.run([CHROME, '--headless', '--no-first-run', f'--user-data-dir={temp / "chrome"}',
                                      '--virtual-time-budget=1000', '--run-all-compositor-stages-before-draw',
                                      '--dump-dom', testcase.as_uri()], capture_output=True, check=True,
                                     encoding='utf-8', errors='replace', timeout=25)
            state = process.stdout.partition('<body data-check="')[2].partition('"')[0]
            self.assertEqual(state, 'pass')


if __name__ == '__main__':
    unittest.main()
