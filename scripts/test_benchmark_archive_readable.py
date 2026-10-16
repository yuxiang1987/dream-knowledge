import unittest
from build_benchmark_archive_readable import readable


class ReadableTest(unittest.TestCase):
    def test_preserves_content_images_and_links(self):
        output = readable('<section><h2>实战</h2><p>中文&amp;文字<br>下一行</p>'
                          '<img data-src="https://example.com/a.jpg" alt="案例">'
                          '<a href="https://example.com">查看案例</a></section>')
        for part in ('## 实战', '中文&文字\n下一行', '![案例](https://example.com/a.jpg)',
                     '[查看案例](https://example.com)'):
            self.assertIn(part, output)

    def test_excludes_code_and_unsafe_link_targets(self):
        output = readable('<div><style>隐藏样式</style><script>隐藏脚本</script>'
                          '<a href="javascript:alert(1)">正文</a><img src="data:abc"></div>')
        self.assertEqual(output, '正文')

    def test_preserves_markdown_unchanged(self):
        self.assertEqual(readable('## 案例\n\n- 第一步\n- 第二步\n'), '## 案例\n\n- 第一步\n- 第二步')


if __name__ == '__main__':
    unittest.main()
