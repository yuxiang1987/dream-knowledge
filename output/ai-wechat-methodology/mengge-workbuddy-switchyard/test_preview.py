"""Probe rendered SMIL states in Chrome, not just the SVG attributes."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

OUT = Path(__file__).resolve().parent
CHROME = os.environ.get('CHROME', r'C:\Program Files\Google\Chrome\Application\chrome.exe')


class SwitchyardTest(unittest.TestCase):
    def test_browser_keeps_old_task_and_redirects_new_task(self):
        page = (OUT / 'preview.html').read_text(encoding='utf-8')
        probe = '''<script>
          addEventListener('load', async () => {
            const svg = document.querySelector('main svg');
            const get = id => document.getElementById(id);
            const rod = get('rail');
            const point = id => svg.getCTM().inverse().multiply(get(id).getCTM());
            const end = () => rod.getPointAtLength(rod.getTotalLength());
            const wait = () => new Promise(resolve => setTimeout(resolve, 35));
            async function at(t) { svg.pauseAnimations(); svg.setCurrentTime(t); await wait(); }
            function assert(ok, message) { if (!ok) throw Error(message); }
            try {
              await at(1.9);
              const first = end();
              await at(2.58);
              const old = point('old-folder');
              const extended = end();
              assert(first.x < 500 && extended.x > 710 && extended.y === 112, 'underline extends');
              assert(Math.abs(point('route-light').e - 574) < 12, 'light reaches lever');
              await at(3.0);
              assert(end().y > 112 && end().y < 167, 'continuous path bends');
              await at(3.55);
              assert(end().x === 896 && end().y === 167 && point('route-light').f > 112, 'same light uses new branch');
              await at(4.2);
              const traveling = point('cargo');
              assert(traveling.e > 450 && traveling.e < 896, 'folder travels along route');
              document.querySelector('[data-frame="4.95"]').click();
              await wait();
              const moved = point('cargo');
              const still = point('old-folder');
              assert(Math.abs(moved.e - 896) < 1 && Math.abs(moved.f - 167) < 1, 'new task lands');
              assert(old.e === still.e && old.f === still.f, 'old task stays');
              await at(6.36);
              assert(+getComputedStyle(get('switch-scene')).opacity === 0, 'loop clears');
              document.querySelector('#replay').click();
              assert(!svg.animationsPaused() && svg.getCurrentTime() < .1, 'replay');
              document.body.dataset.check = 'pass';
            } catch (error) { document.body.dataset.check = error.message; }
          }, {once: true});
        </script>'''
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
            temp = Path(tmp)
            html = temp / 'preview.html'
            html.write_text(page.replace('</body>', probe + '</body>'), encoding='utf-8')
            browser = subprocess.run([CHROME, '--headless', '--no-first-run', f'--user-data-dir={temp / "profile"}',
                                      '--virtual-time-budget=1000', '--run-all-compositor-stages-before-draw',
                                      '--dump-dom', html.as_uri()], capture_output=True, encoding='utf-8',
                                     errors='replace', check=True, timeout=25)
        self.assertEqual(browser.stdout.partition('<body data-check="')[2].partition('"')[0], 'pass')


if __name__ == '__main__':
    unittest.main()
