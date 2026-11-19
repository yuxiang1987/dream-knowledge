"""Browser checks for the timing and bounds of the three caption treatments."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

OUT = Path(__file__).resolve().parent
CHROME = os.environ.get('CHROME', r'C:\Program Files\Google\Chrome\Application\chrome.exe')


class PreviewTest(unittest.TestCase):
    def test_labels_follow_each_treatment(self):
        page = (OUT / 'preview.html').read_text(encoding='utf-8')
        script = '''<script>
        addEventListener('load', async () => {
          const roots = [...document.querySelectorAll('main svg')];
          const get = id => document.getElementById(id);
          const wait = () => new Promise(resolve => setTimeout(resolve, 35));
          const visible = id => +getComputedStyle(get(id)).opacity > .95;
          const words = (mode, type = 'word') => Array.from({length: 7}, (_, i) => visible(`${mode}-${type}-${i}`));
          async function seek(t) { roots.forEach(svg => { svg.pauseAnimations(); svg.setCurrentTime(t); }); await wait(); }
          function check(ok, reason) { if (!ok) throw Error(reason); }
          try {
            roots.forEach(svg => { svg.style.width = '375px'; svg.style.maxWidth = 'none'; });
            await seek(1.74);
            check(words('a', 'plain').every(Boolean), 'A names visible before first stop');
            check(!words('c').some(Boolean), 'C starts without names');
            for (let i = 0; i < 7; i++) {
              await seek(2.10 + i * .69);
              check(words('a').every((value, j) => value === (j <= i)), `A highlight ${i + 1}`);
              check(words('b').every((value, j) => value === (j === i)), `B shows only ${i + 1}`);
              check(words('c').every((value, j) => value === (j <= i)), `C retains ${i + 1} short labels`);
            }
            for (const mode of ['a','c']) {
              const boxes = Array.from({length: 7}, (_, i) => get(`${mode}-word-${i}`).getBoundingClientRect());
              const canvas = get(`${mode}-scene`).ownerSVGElement.getBoundingClientRect();
              check(boxes.every((b, i) => b.left > canvas.left && b.right < canvas.right && b.bottom < canvas.bottom
                   && (!i || b.left > boxes[i-1].right)), `${mode} labels fit at 375px`);
            }
            await seek(8.3);
            check(['a','b','c'].every(k => +getComputedStyle(get(`${k}-scene`)).opacity === 0), 'captions clear before loop');
            document.querySelector('#replay').click();
            check(roots.every(svg => !svg.animationsPaused() && svg.getCurrentTime() < .1), 'synchronized replay');
            document.body.dataset.check = 'pass';
          } catch (error) { document.body.dataset.check = error.message; }
        }, {once: true});
        </script>'''
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as folder:
            folder = Path(folder)
            case = folder / 'preview.html'
            case.write_text(page.replace('</body>', script + '</body>'), encoding='utf-8')
            result = subprocess.run([CHROME, '--headless', '--no-first-run', f'--user-data-dir={folder / "profile"}',
                                     '--virtual-time-budget=1500', '--run-all-compositor-stages-before-draw',
                                     '--dump-dom', case.as_uri()], capture_output=True, encoding='utf-8',
                                    errors='replace', check=True, timeout=25)
        self.assertEqual(result.stdout.partition('<body data-check="')[2].partition('"')[0], 'pass')


if __name__ == '__main__':
    unittest.main()
