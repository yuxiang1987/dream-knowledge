"""Check that the visible SVG sequence follows the moving light in Chrome."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

OUT = Path(__file__).resolve().parent
CHROME = os.environ.get('CHROME', r'C:\Program Files\Google\Chrome\Application\chrome.exe')


class SevenSettingsTest(unittest.TestCase):
    def test_light_triggers_all_seven_in_order(self):
        page = (OUT / 'preview.html').read_text(encoding='utf8')
        script = '''<script>
        addEventListener('load', async () => {
          const svg = document.querySelector('main svg');
          const get = id => svg.querySelector(`#${id}`);
          const keys = ['storage','instruction','reply','persona','evolve','model','import'];
          const opacity = id => +getComputedStyle(get(id)).opacity;
          const wait = () => new Promise(resolve => setTimeout(resolve, 35));
          async function seek(t) { svg.pauseAnimations(); svg.setCurrentTime(t); await wait(); }
          function check(ok, reason) { if (!ok) throw Error(reason); }
          try {
            for (let i = 0; i < keys.length; i++) {
              await seek(1.86 + .69 * i);
              const x = svg.getCTM().inverse().multiply(get('light').getCTM()).e;
              check(Math.abs(x - (252 + i * 110)) < 1, `light reaches ${keys[i]}`);
              const rail = get('progress').x2.animVal.value;
              check(Math.abs(rail - x) < 1, 'light and rail agree');
              await seek(2.09 + .69 * i);
              check(keys.every((k, j) => opacity(k) === (j <= i ? 1 : 0)), `station ${i + 1} settles`);
            }
            document.querySelector('[data-frame="6.56"]').click();
            await wait();
            check(keys.every(k => opacity(k) === 1) && opacity('brand') === 0, 'freeze all seven');
            await seek(8.32);
            check(opacity('scene') === 0 && opacity('brand') === 1, 'returns to brand');
            document.querySelector('#replay').click();
            check(!svg.animationsPaused() && svg.getCurrentTime() < .1, 'replay restarts');
            document.body.dataset.check = 'pass';
          } catch (error) { document.body.dataset.check = error.message; }
        }, {once: true});
        </script>'''
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
            temp = Path(tmp)
            test = temp / 'test.html'
            test.write_text(page.replace('</body>', script + '</body>'), encoding='utf8')
            result = subprocess.run([CHROME, '--headless', '--no-first-run', f'--user-data-dir={temp / "profile"}',
                                     '--virtual-time-budget=1500', '--run-all-compositor-stages-before-draw',
                                     '--dump-dom', test.as_uri()], capture_output=True, check=True,
                                    encoding='utf8', errors='replace', timeout=25)
        self.assertEqual(result.stdout.partition('<body data-check="')[2].partition('"')[0], 'pass')


if __name__ == '__main__':
    unittest.main()
