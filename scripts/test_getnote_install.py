"""本机得到大脑 CLI 安装验收；不读取凭证、不访问或修改云端笔记。

用法：python scripts/test_getnote_install.py
仅在安装得到大脑 CLI 的 Windows 电脑上运行。
"""
import json
import os
from pathlib import Path
import shutil
import subprocess
import unittest


class GetNoteInstallTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.node = shutil.which("node")
        if not cls.node:
            raise RuntimeError("未找到 Node.js")
        cls.prefix = Path(os.environ["APPDATA"]) / "npm"
        cls.package = cls.prefix / "node_modules" / "@getnote" / "cli"
        cls.metadata = json.loads(
            (cls.package / "package.json").read_text(encoding="utf-8")
        )

    def run_cli(self, *args):
        result = subprocess.run(
            [self.node, str(self.package / "bin" / "getnote.js"), *args],
            capture_output=True, text=True, encoding="utf-8", timeout=20,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def test_installed_binary_matches_package_version(self):
        self.assertEqual(self.metadata["name"], "@getnote/cli")
        self.assertEqual(
            self.run_cli("--version").strip(),
            "getnote version " + self.metadata["version"],
        )

    def test_required_commands_are_available(self):
        help_text = self.run_cli("--help")
        for command in ("auth", "doctor", "notes", "search", "save"):
            with self.subTest(command=command):
                self.assertRegex(help_text, rf"(?m)^\s+{command}\s+")

    def test_global_launchers_are_on_path(self):
        for command in ("getnote", "gnote"):
            with self.subTest(command=command):
                expected = self.prefix / (command + ".cmd")
                self.assertTrue(expected.is_file())
                actual = shutil.which(command + ".cmd")
                self.assertIsNotNone(actual)
                self.assertEqual(Path(actual).resolve(), expected.resolve())


if __name__ == "__main__":
    unittest.main()
