"""Validate the installed gzh-daily-pipeline skill and its handover contract."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents/skills/gzh-daily-pipeline"
MANIFEST = ROOT / "scripts/installed_skills.json"

DISPATCHED_SKILLS = (
    "wechat-viral-topic",
    "wechat-article-writing",
    "gzh-final-check",
    "gzh-webchat-cover",
    "md-wechat-layout",
)


def run_pipeline(*args: str) -> subprocess.CompletedProcess:
    """Run the skill script with the workspace interpreter."""
    return subprocess.run(
        [sys.executable, str(SKILL / "scripts/pipeline.py"), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


def fill_placeholders(text: str) -> str:
    """Replace every template placeholder with a filled marker."""
    return re.sub(r"\{\{[^{}]+\}\}", "已填", text)


def clear_must_change_table(text: str) -> str:
    """Drop the sample data row under the 必须修改 heading, keep the header."""
    lines = text.splitlines()
    out: list[str] = []
    inside = False
    seen_header = False
    for line in lines:
        if line.startswith("## "):
            inside = line.strip() == "## 必须修改"
            seen_header = False
        elif inside and line.strip().startswith("|"):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if set("".join(cells)) <= set("-: "):
                out.append(line)
                continue
            if not seen_header:
                seen_header = True
                out.append(line)
                continue
            continue  # 数据行清零
        out.append(line)
    return "\n".join(out) + "\n"


class DailyPipelineInstallTest(unittest.TestCase):
    def test_manifest_records_skill(self):
        """The install manifest pins the pipeline skill with upstream hashes."""
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertIn("gzh-daily-pipeline", manifest["skills"])
        self.assertRegex(manifest["skill_commits"]["gzh-daily-pipeline"], r"^[0-9a-f]{40}$")
        recorded = {key for key in manifest["sha256"] if key.startswith("gzh-daily-pipeline/")}
        actual = {"gzh-daily-pipeline/" + path.relative_to(SKILL).as_posix()
                  for path in SKILL.rglob("*") if path.is_file()
                  and "__pycache__" not in path.parts}
        self.assertEqual(recorded, actual)
        for relative, expected in manifest["sha256"].items():
            if not relative.startswith("gzh-daily-pipeline/"):
                continue
            with self.subTest(file=relative):
                data = (ROOT / ".agents/skills" / relative).read_bytes()
                self.assertEqual(hashlib.sha256(data).hexdigest(), expected)

    def test_entrypoint_documents_full_chain(self):
        """SKILL.md names every stage, every dispatched skill and the hard gate."""
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        self.assertIn("name: gzh-daily-pipeline\n", text)
        self.assertIn("description:", text)
        for stage in ("S0", "S1", "S2", "S3", "S4", "S5", "S6"):
            with self.subTest(stage=stage):
                self.assertIn(stage, text)
        for name in DISPATCHED_SKILLS:
            with self.subTest(skill=name):
                self.assertIn(name, text)
        self.assertIn("03_证据与实测.md", text)
        self.assertIn("硬关口", text)

    def test_local_resources_are_discoverable(self):
        """References, templates and regression cases are reachable from SKILL.md."""
        entry = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        links = re.findall(r"\]\(([^)]+)\)", entry)
        local = [target for target in links if "://" not in target and not target.startswith("#")]
        self.assertTrue(local)
        for target in local:
            with self.subTest(link=target):
                resource = (SKILL / target.split("#")[0]).resolve()
                self.assertTrue(resource.is_relative_to(SKILL.resolve()))
                self.assertTrue(resource.is_file(), target)
        for relative in ("references/handoff-contract.md", "references/stage-checklists.md"):
            self.assertTrue((SKILL / relative).is_file())
        for template in ("00_style.md", "01_选题卡.md", "02_案例决策卡.md", "03_证据与实测.md",
                         "04_正文.md", "05_检查报告.md", "06_标题.md", "09_发布记录.md"):
            with self.subTest(template=template):
                self.assertTrue((SKILL / "templates" / template).is_file())
        cases = list((SKILL / "tests").glob("*.md"))
        self.assertTrue(cases)
        for case in cases:
            self.assertIn(f"]({case.relative_to(SKILL).as_posix()})", entry)

    def test_handover_contract_states_valid_statuses(self):
        """The contract fixes the frontmatter fields and the allowed status values."""
        contract = (SKILL / "references/handoff-contract.md").read_text(encoding="utf-8")
        for field in ("stage", "status", "topic", "source_skill", "created", "updated"):
            with self.subTest(field=field):
                self.assertIn(f"`{field}`", contract)
        for status in ("待办", "待确认", "已确认", "已跳过", "已废弃"):
            with self.subTest(status=status):
                self.assertIn(status, contract)

    def test_scaffolder_and_checker_round_trip(self):
        """init scaffolds a run directory, check blocks the unfinished hard gate."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "pipeline"
            created = run_pipeline("init", "--root", str(root), "--date", "2026-10-23", "--slug", "验收用例")
            self.assertEqual(created.returncode, 0, created.stdout + created.stderr)
            run_dir = root / "2026-10-23-验收用例"
            self.assertTrue(run_dir.is_dir())
            self.assertTrue((run_dir / "04_正文.md").is_file())
            self.assertTrue((run_dir / "03_证据与实测.md").is_file())

            # 模板原样交付时，各阶段都在待确认，不该报结构错误。
            pending = run_pipeline("check", "--dir", str(run_dir))
            self.assertEqual(pending.returncode, 0, pending.stdout + pending.stderr)

            # 正文先确认，实测关口没过，检查必须拦住。
            body = run_dir / "04_正文.md"
            body.write_text(
                fill_placeholders(body.read_text(encoding="utf-8")).replace(
                    "status: 待确认", "status: 已确认"),
                encoding="utf-8")
            blocked = run_pipeline("check", "--dir", str(run_dir))
            self.assertEqual(blocked.returncode, 1)
            self.assertIn("03_证据与实测.md", blocked.stdout)

            # 全部阶段确认、产物齐备后，检查通过。
            for path in run_dir.glob("*.md"):
                text = fill_placeholders(path.read_text(encoding="utf-8"))
                if path.name == "05_检查报告.md":
                    text = clear_must_change_table(text)
                text = text.replace("status: 待确认", "status: 已确认")
                path.write_text(text, encoding="utf-8")
            (run_dir / "07_封面.png").write_bytes(b"\x89PNG\r\n\x1a\n")
            (run_dir / "08_排版").mkdir()
            passed = run_pipeline("check", "--dir", str(run_dir))
            self.assertEqual(passed.returncode, 0, passed.stdout + passed.stderr)
            self.assertIn("交接校验通过", passed.stdout)

            status = run_pipeline("status", "--dir", str(run_dir))
            self.assertEqual(status.returncode, 0, status.stdout + status.stderr)
            self.assertIn("流水线状态", status.stdout)

    def test_init_refuses_to_overwrite(self):
        """A second init on the same day and slug must not destroy the run."""
        with tempfile.TemporaryDirectory() as tmp:
            first = run_pipeline("init", "--root", tmp, "--date", "2026-10-23", "--slug", "同名")
            self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
            second = run_pipeline("init", "--root", tmp, "--date", "2026-10-23", "--slug", "同名")
            self.assertEqual(second.returncode, 1)
            self.assertIn("目录已存在", second.stdout)


if __name__ == "__main__":
    unittest.main()
