"""Validate the local WorkBuddy skill installation and its resources."""
import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents/skills/wechat-viral-topic"


class ViralTopicInstallTest(unittest.TestCase):
    def test_original_files_preserved(self):
        manifest = json.loads((ROOT / "scripts/wechat_viral_topic_install.json").read_text(encoding="utf-8"))
        for relative, digest in manifest["sha256"].items():
            with self.subTest(file=relative):
                self.assertEqual(hashlib.sha256((SKILL / relative).read_bytes()).hexdigest(), digest)

    def test_entrypoint_and_references(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8-sig")
        self.assertTrue(text.startswith("---\n"))
        self.assertIn("name: wechat-viral-topic\n", text)
        self.assertIn("description:", text)
        references = re.findall(r"@((?:references|templates)/[\w-]+\.md)", text)
        self.assertTrue(references)
        for relative in references:
            with self.subTest(reference=relative):
                self.assertTrue((SKILL / relative).read_text(encoding="utf-8-sig").strip())


if __name__ == "__main__":
    unittest.main()
