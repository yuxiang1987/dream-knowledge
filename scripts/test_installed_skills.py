"""Verify workspace skill files against the recorded upstream snapshot."""
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class InstalledSkillsTest(unittest.TestCase):
    def test_layout_theme_snapshot(self):
        """Verify the complete layout installation separately from other skills."""
        manifest = json.loads((ROOT / "scripts/installed_skills.json").read_text(encoding="utf-8"))
        commit = manifest["skill_commits"]["md-wechat-layout"]
        self.assertRegex(commit, r"^[0-9a-f]{40}$")
        files = {key: value for key, value in manifest["sha256"].items()
                 if key.startswith("md-wechat-layout/")}
        for resource in ("scripts/blue-journal.mjs", "references/blue-journal.md",
                         "assets/blue-journal-demo.md", "tests/blue-journal.test.mjs"):
            self.assertIn("md-wechat-layout/" + resource, files)
        for relative, expected in files.items():
            with self.subTest(file=relative):
                data = (ROOT / ".agents/skills" / relative).read_bytes()
                self.assertEqual(hashlib.sha256(data).hexdigest(), expected)

    def test_skill_entrypoints(self):
        manifest = json.loads((ROOT / "scripts/installed_skills.json").read_text(encoding="utf-8"))
        for name in manifest["skills"]:
            with self.subTest(skill=name):
                folder = ROOT / ".agents/skills" / name
                text = (folder / "SKILL.md").read_text(encoding="utf-8-sig")
                self.assertTrue(text.startswith("---\n"))
                self.assertIn(f"name: {name}\n", text)
                self.assertIn("description:", text)
                self.assertTrue((folder / "agents/openai.yaml").is_file())

    def test_final_review_regression_resource(self):
        folder = ROOT / ".agents/skills/gzh-final-check"
        text = (folder / "SKILL.md").read_text(encoding="utf-8")
        import re
        for target in re.findall(r"\]\((tests/[^)]+)\)", text):
            with self.subTest(reference=target):
                resource = folder / target
                self.assertTrue(resource.is_file())
                self.assertTrue(resource.read_text(encoding="utf-8").strip())
        manifest = json.loads((ROOT / "scripts/installed_skills.json").read_text(encoding="utf-8"))
        self.assertIn("gzh-final-check/tests/review-cases.md", manifest["sha256"])

    def test_upstream_files_unchanged(self):
        manifest = json.loads((ROOT / "scripts/installed_skills.json").read_text(encoding="utf-8"))
        for relative, expected in manifest["sha256"].items():
            with self.subTest(file=relative):
                data = (ROOT / ".agents/skills" / relative).read_bytes()
                self.assertEqual(hashlib.sha256(data).hexdigest(), expected)


if __name__ == "__main__":
    unittest.main()
