"""Verify iris, wipe, reel and shared controls in Chromium."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

OUT = Path(__file__).resolve().parent
CHROME = os.environ.get('CHROME', r'C:\Program Files\Google\Chrome\Application\chrome.exe')


class LubanTest(unittest.TestCase):
    def test_three_distinct_animations(self):
        preview = (OUT / 'preview.html').read_text(encoding='utf-8')
        script = '''<script>
          addEventListener('load', async () => {
            const art = [...document.querySelectorAll('main svg')];
            const get = id => document.getElementById(id);
            const iris = () => get('iris').r.animVal.value;
            const wipe = () => get('reveal').width.animVal.value;
            const reel = () => get('reel').transform.animVal.getItem(0).matrix.e;
            const wait = () => new Promise(resolve => setTimeout(resolve, 35));
            async function seek(t) { art.forEach(s => { s.pauseAnimations(); s.setCurrentTime(t); }); await wait(); }
            function check(ok, reason) { if (!ok) throw Error(reason); }
            try {
              await seek(.8);
              check(iris() === 0 && wipe() === 0 && reel() === 0, 'opening states');
              await seek(2.4);
              check(iris() > 47 && iris() < 118 && wipe() > 0 && wipe() < 386, 'iris and comparison open');
              await seek(3.01);
              check(reel() > -362 && reel() < 0, 'film moves between stills');
              document.querySelector('[data-frame="5.87"]').click();
              await wait();
              check(iris() === 106 && wipe() === 386 && reel() === -1086, 'all three settle');
              await seek(8.35);
              check(iris() === 0 && wipe() === 0, 'reveal clears for the loop');
              document.querySelector('#replay').click();
              check(art.every(s => !s.animationsPaused() && s.getCurrentTime() < .1), 'synced replay');
              document.body.dataset.check = 'pass';
            } catch (error) { document.body.dataset.check = error.message; }
          }, {once: true});
        </script>'''
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
            tmp = Path(tmp)
            html = tmp / 'test.html'
            html.write_text(preview.replace('</body>', script + '</body>'), encoding='utf-8')
            result = subprocess.run([CHROME, '--headless', '--no-first-run', f'--user-data-dir={tmp / "profile"}',
                                     '--virtual-time-budget=1500', '--run-all-compositor-stages-before-draw',
                                     '--dump-dom', html.as_uri()], capture_output=True, check=True, encoding='utf-8',
                                    errors='replace', timeout=25)
        self.assertEqual(result.stdout.partition('<body data-check="')[2].partition('"')[0], 'pass')


if __name__ == '__main__':
    unittest.main()
