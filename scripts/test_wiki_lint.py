"""Exercise the lint CLI against real source paths containing commas."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

LINT = Path(__file__).with_name("wiki_lint.py")


class SourcePathTests(unittest.TestCase):
    def lint(self, sources, existing):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "wiki").mkdir()
            for name in existing:
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("original source", encoding="utf-8")
            (root / "wiki/source.md").write_text(
                "---\ntitle: sample\ntype: source\nstatus: 稳定\nsources: " + sources
                + "\ncreated: 2026-11-13\nupdated: 2026-11-13\n---\n", encoding="utf-8")
            return subprocess.run([sys.executable, str(LINT), "--root", str(root)],
                                  capture_output=True, encoding="utf-8")

    def test_quoted_comma_path_and_second_source_exist(self):
        paths = ["raw/100,000,000 Token.md", "raw/another.md"]
        result = self.lint(json.dumps(paths), paths)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_comma_path_is_reported_whole(self):
        path = "raw/missing,source.md"
        result = self.lint(json.dumps([path]), [])
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("sources 指向的文件不存在 - " + path, result.stdout)
        self.assertNotIn("文件不存在 - source.md", result.stdout)

    def test_existing_unquoted_yaml_list_still_resolves(self):
        paths = ["raw/first.md", "raw/second.md"]
        result = self.lint("[raw/first.md, raw/second.md]", paths)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
