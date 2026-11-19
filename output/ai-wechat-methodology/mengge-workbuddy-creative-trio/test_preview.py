"""Verify the three distinct motion systems in the rendered Chrome preview."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent
CHROME = os.environ.get('CHROME', r'C:\Program Files\Google\Chrome\Application\chrome.exe')


class CreativeTrioTest(unittest.TestCase):
    def test_orbit_morph_and_assembly(self):
        preview = (ROOT / 'preview.html').read_text(encoding='utf-8')
        checks = '''<script>
          addEventListener('load', async () => {
            const roots = [...document.querySelectorAll('main svg')];
            const node = id => document.getElementById(id);
            const value = (id, axis) => node(id).transform.animVal.getItem(0).matrix[axis];
            const opacity = id => +getComputedStyle(node(id)).opacity;
            const wait = () => new Promise(resolve => setTimeout(resolve, 38));
            async function at(t) { roots.forEach(s => { s.pauseAnimations(); s.setCurrentTime(t); }); await wait(); }
            function check(ok, name) { if (!ok) throw Error(name); }
            try {
              await at(1.6);
              const bearing = value('a-sweep','a');
              const firstWidth = node('b-surface').getBBox().width;
              check(opacity('a-feature-0') === 1 && opacity('b-feature-0') === 1, 'first setting readable');
              check(opacity('c-tile-0') === 1 && Math.abs(value('c-tile-0','f')) > 1, 'first tile in transit');
              await at(2.08);
              const during = node('b-surface').getBBox().width;
              check(value('a-sweep','a') > bearing, 'sweep rotates');
              check(during < firstWidth && during > 138, 'same path interpolates before second setting');
              await at(2.36);
              check(node('b-surface').getBBox().width === 138 && opacity('b-feature-1') === 1, 'second shape and label');
              check(opacity('c-tile-1') === 1 && opacity('c-tile-2') < 1, 'tiles enter in sequence');
              document.querySelector('[data-frame="6.48"]').click();
              await wait();
              check(roots.every(s => s.animationsPaused()), 'comparison can freeze');
              for (let i = 0; i < 7; i++) {
                check(opacity(`a-node-${i}`) === 1, 'all radar nodes visited');
                check(opacity(`c-tile-${i}`) === 1 && Math.abs(value(`c-tile-${i}`,'f')) < .01, 'all tiles settled');
              }
              check(opacity('c-lock') === 1 && opacity('b-feature-6') === 1, 'final states visible');
              document.querySelector('#replay').click();
              check(roots.every(s => !s.animationsPaused() && s.getCurrentTime() < .1), 'replay');
              document.body.dataset.check = 'pass';
            } catch (error) { document.body.dataset.check = error.message; }
          }, {once: true});
        </script>'''
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
            tmp = Path(tmp)
            html = tmp / 'preview.html'
            html.write_text(preview.replace('</body>', checks + '</body>'), encoding='utf8')
            result = subprocess.run([CHROME, '--headless', '--no-first-run', f'--user-data-dir={tmp / "profile"}',
                                     '--virtual-time-budget=1400', '--run-all-compositor-stages-before-draw',
                                     '--dump-dom', html.as_uri()], capture_output=True, encoding='utf8',
                                    errors='replace', check=True, timeout=25)
        self.assertEqual(result.stdout.partition('<body data-check="')[2].partition('"')[0], 'pass')


if __name__ == '__main__':
    unittest.main()
