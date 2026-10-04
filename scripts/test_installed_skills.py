"""Verify workspace skill files against the recorded upstream snapshot."""
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class InstalledSkillsTest(unittest.TestCase):
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
