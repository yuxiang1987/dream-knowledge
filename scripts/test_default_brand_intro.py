"""排版默认片头身份与示例导出，微信平台验收单独保留。"""
import base64
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import unittest

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / '.agents/skills/md-wechat-layout'
DEMO = ROOT / 'output/ai-wechat-methodology/默认粒子片头排版验收'
SHA = 'b75cb025527976a3182fdeef3cae6f305dc40693c59c084fe33e4353423c4d34'
COMPACT_SHA = '01a3000a59713fdbb0242e833bf7a96aa1d06a0b143b5118682101dacd10080f'


class Images(HTMLParser):
    def __init__(self):
        super().__init__()
        self.srcs = []
        self.texts = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            self.srcs.append(dict(attrs)['src'])

    def handle_data(self, data):
        self.texts.append(data)


class DefaultBrandIntroTest(unittest.TestCase):
    def test_bundled_asset_is_approved_particle_animation(self):
        asset = SKILL / 'assets/brand-intro/intro.gif'
        self.assertEqual(hashlib.sha256(asset.read_bytes()).hexdigest(), SHA)
        original = ROOT / 'output/ai-wechat-methodology/程序员梦哥像素闯关-v8粒子转场/intro.gif'
        self.assertEqual(asset.read_bytes(), original.read_bytes())
        with Image.open(asset) as gif:
            self.assertEqual((gif.size, gif.n_frames, gif.info['loop']), ((1200, 360), 450, 0))

    def test_complete_export_starts_with_exact_animated_gif(self):
        fragment = (DEMO / '默认片头排版示例.wechat.html').read_text(encoding='utf8')
        page = (DEMO / '默认片头排版示例.preview.html').read_text(encoding='utf8')
        parser = Images()
        parser.feed(fragment)
        self.assertEqual(len(parser.srcs), 1)
        self.assertTrue(parser.srcs[0].startswith('data:image/gif;base64,'))
        data = base64.b64decode(parser.srcs[0].split(',', 1)[1])
        self.assertEqual(hashlib.sha256(data).hexdigest(), COMPACT_SHA)
        self.assertLess(fragment.index('<img'), fragment.index('<h1'))
        self.assertIn('<article id="content">'+fragment+'</article>', page)
        self.assertIn('这是一份排版功能示例', fragment)
        self.assertNotIn('![', (DEMO / '默认片头排版示例.md').read_text(encoding='utf8'))

    def test_installation_records_asset_tests_and_user_override(self):
        manifest = json.loads((ROOT / 'scripts/installed_skills.json').read_text(encoding='utf8'))
        self.assertEqual(manifest['sha256']['md-wechat-layout/assets/brand-intro/intro.gif'], SHA)
        self.assertIn('md-wechat-layout/tests/brand-intro.test.mjs', manifest['sha256'])
        text = (SKILL / 'SKILL.md').read_text(encoding='utf8')
        self.assertIn('A、B、C 三个片头动画方案', text)
        self.assertIn('等待用户选定', text)
        self.assertIn('用 `--intro-svg` 将它嵌入全文', text)
        self.assertIn('直接运行 CLI 且未指定片头参数', text)
        self.assertIn('--no-brand-intro', text)
        self.assertIn('像素粒子消散版GIF', text)
        self.assertIn('单独下载片头 GIF', text)
        report = json.loads((DEMO / '默认片头排版示例.report.json').read_text(encoding='utf8'))
        self.assertTrue(any('检查微信转存和动画播放' in w for w in report['warnings']))

    def test_workbuddy_export_uses_the_same_compact_gif_in_both_forms(self):
        asset = SKILL / 'assets/brand-intro/intro-wechat.gif'
        gif = asset.read_bytes()
        digest = COMPACT_SHA
        self.assertEqual(hashlib.sha256(gif).hexdigest(), digest)
        manifest = json.loads((ROOT / 'scripts/installed_skills.json').read_text(encoding='utf8'))
        self.assertEqual(manifest['sha256']['md-wechat-layout/assets/brand-intro/intro-wechat.gif'], digest)
        folder = ROOT / 'output/workbuddy-wechat-layout-20261118'
        title = 'WorkBuddy 做好这几个设置，让WorkBuddy越来越懂你'
        fragment = (folder / (title + '.wechat.html')).read_text(encoding='utf8')
        preview = (folder / (title + '.preview.html')).read_text(encoding='utf8')
        parser = Images()
        parser.feed(fragment)
        self.assertEqual(len(parser.srcs), 13)
        self.assertTrue(parser.srcs[0].startswith('data:image/gif;base64,'))
        self.assertEqual(base64.b64decode(parser.srcs[0].split(',', 1)[1]), gif)
        self.assertEqual((folder / (title + '.intro.gif')).read_bytes(), gif)
        self.assertLess(fragment.index('最近我发现'), fragment.index(parser.srcs[1]))
        self.assertLess(fragment.index(parser.srcs[1]), fragment.index('更有意思的是'))
        self.assertLess(preview.index('单独下载片头 GIF'), preview.index('<article id="content">'))
        self.assertNotIn('单独下载片头 GIF', fragment)
        self.assertIn('<article id="content">'+fragment+'</article>', preview)

    def test_user_bio_is_the_exact_final_paragraph(self):
        bio = '我是梦哥，十年程序员，爱折腾 AI。分享实用 AI 工具、有趣玩法和实操心得，一起把想法做出来。'
        fragment = (DEMO / '默认片头排版示例.wechat.html').read_text(encoding='utf8')
        parser = Images()
        parser.feed(fragment)
        self.assertTrue(''.join(parser.texts).strip().endswith(bio))
        self.assertEqual(fragment.count(bio), 1)
        self.assertNotIn(bio, (DEMO / '默认片头排版示例.md').read_text(encoding='utf8'))
        entry = (SKILL / 'SKILL.md').read_text(encoding='utf8')
        self.assertIn('我是梦哥，十年程序员，爱折腾 AI。分享实用 AI 工具、有趣玩法和实操心得，一起把想法做出来。', entry)
        self.assertIn('--no-author-bio', entry)


if __name__ == '__main__':
    unittest.main()
