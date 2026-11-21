import importlib.util
import json
from pathlib import Path
import unittest
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/ai-wechat-methodology/mengge-luban-svg-intro-v1'

spec = importlib.util.spec_from_file_location('moyu', ROOT / 'scripts/analyze_moyu_intro.py')
moyu = importlib.util.module_from_spec(spec)
spec.loader.exec_module(moyu)


class MengGeLubanSvgIntroTests(unittest.TestCase):
    def test_svg_pure_smil_structure_and_zero_external_deps(self):
        svg_path = OUT / 'intro.svg'
        self.assertTrue(svg_path.exists())
        svg = svg_path.read_text(encoding='utf-8')
        meta = json.loads((OUT / 'motion.json').read_text(encoding='utf-8'))

        scan = moyu.SVGScan()
        scan.feed(svg)

        self.assertEqual(scan.root.get('viewbox'), '0 0 1246 220')
        self.assertNotIn('script', scan.tags)
        self.assertNotIn('text', scan.tags)
        self.assertNotIn('image', scan.tags)
        self.assertEqual(scan.external_refs, [])

        self.assertEqual(scan.tags['path'], meta['path_count'])
        self.assertEqual(scan.tags['rect'], meta['rect_count'])
        self.assertEqual(scan.tags['animate'], meta['animate_count'])
        self.assertEqual(scan.tags['animatetransform'], meta['animateTransform_count'])
        self.assertGreaterEqual(scan.tags['animate'], 70)
        self.assertGreaterEqual(scan.tags['animatetransform'], 60)
        self.assertGreaterEqual(sum(a.get('calcmode') == 'spline' for a in scan.animations), 60)

        # Verify five-act narrative groups exist in SVG
        for group_id in (
            'brand-character-stage',
            'act0-brand-intro',
            'transition-particles',
            'topic-scene-root',
            'deepseek-fish-cartridge',
            'image26-workbench',
            'luban-ocean-character',
            'whale-hat-blue',
            'whale-hat-pink',
            'local-edit-selection',
            'whale-cannon-projectile',
            'output-card-1',
            'output-card-2',
            'output-card-3',
        ):
            self.assertIn(f'id="{group_id}"', svg)

    def test_gif_fallback_and_distinct_keyframes(self):
        gif_path = OUT / 'intro.gif'
        self.assertTrue(gif_path.exists())
        self.assertLess(gif_path.stat().st_size, 1_500_000)

        with Image.open(gif_path) as gif:
            self.assertEqual(gif.size, (1246, 220))
            self.assertEqual(getattr(gif, 'n_frames', 1), 160)

        keyframe_names = [
            'keyframe-0.5s-brand.png',
            'keyframe-1.6s-particles.png',
            'keyframe-2.6s-blue-luban.png',
            'keyframe-4.2s-pink-edit.png',
            'keyframe-5.3s-cannon-fire.png',
            'keyframe-6.4s-full-deliverables.png',
        ]
        raw_bytes = []
        for name in keyframe_names:
            p = OUT / name
            self.assertTrue(p.exists(), name)
            with Image.open(p) as im:
                self.assertEqual(im.size, (1246, 220))
            raw_bytes.append(p.read_bytes())

        # Every keyframe must represent a distinct visual stage
        self.assertEqual(len(set(raw_bytes)), len(keyframe_names))

    def test_preview_and_wechat_snippet_exist(self):
        preview = (OUT / 'preview.html').read_text(encoding='utf-8')
        wechat_html = (OUT / 'intro.wechat.html').read_text(encoding='utf-8')
        self.assertIn('freezeAt(0.5)', preview)
        self.assertIn('freezeAt(4.2)', preview)
        self.assertIn('freezeAt(6.4)', preview)
        self.assertIn('GPT Image 叒叒叒更新了，我用它手搓了一套鲁班皮肤', preview)
        self.assertTrue(wechat_html.startswith('<section'))
        self.assertIn('<svg ', wechat_html)


if __name__ == '__main__':
    unittest.main()
