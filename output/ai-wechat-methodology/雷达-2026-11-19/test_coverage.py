"""Isolated offline regressions for consumer-visible batch evidence failures."""
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("radar_acceptance", HERE / "validate_coverage.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.batch = Path(temp.name)
        self.rows = json.loads((HERE / "coverage.json").read_text(encoding="utf-8"))
        (self.batch / "fetch-summary.json").write_bytes((HERE / "fetch-summary.json").read_bytes())

    def reject(self, rows, message=".*"):
        (self.batch / "coverage.json").write_text(json.dumps(rows, ensure_ascii=False), encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaisesRegex(AssertionError, message):
                validator.validate(self.batch)

    def test_missing_article(self):
        self.reject(self.rows[1:], "Coverage gap")

    def test_duplicate_article(self):
        self.reject(self.rows + [copy.deepcopy(self.rows[0])], "Coverage gap")

    def test_changed_raw_hash(self):
        self.rows[0]["raw_sha256"] = "0" * 64
        self.reject(self.rows)

    def test_forged_anchor(self):
        row = next(r for r in self.rows if r["disposition"] != "excluded")
        row["anchors"][0] = "原文不存在的虚构证据20261119"
        self.reject(self.rows)

    def test_exclusion_requires_reason(self):
        self.rows[0].update(disposition="excluded", source_path=None, reason="", case_card=None)
        self.reject(self.rows)

    def test_nonexistent_case_is_rejected(self):
        row = next(r for r in self.rows if r["disposition"] != "excluded")
        row["case_card"] = "### 虚构的本账号亲测卡20261119"
        self.reject(self.rows, "Missing case card")

    def test_detects_modified_preexisting_raw(self):
        raw = self.batch / "original.md"
        raw.write_bytes(b"original")
        snapshot = {"original.md": hashlib.sha256(raw.read_bytes()).hexdigest()}
        (self.batch / "preexisting-raw-sha256.json").write_text(json.dumps(snapshot), encoding="utf-8")
        raw.write_bytes(b"changed")
        with self.assertRaises(AssertionError):
            validator.validate_preservation(self.batch, self.batch)

    def test_report_cannot_leave_completed_source_pending(self):
        row = next(r for r in self.rows if r["disposition"] != "excluded")
        (self.batch / "coverage.json").write_text(json.dumps(self.rows, ensure_ascii=False), encoding="utf-8")
        report = {"raw_without_source": [row["raw_path"]], "analysis_scope": {"covered": len(self.rows)}}
        (self.batch / "report.json").write_text(json.dumps(report, ensure_ascii=False), encoding="utf-8")
        with self.assertRaisesRegex(AssertionError, "still reported pending"):
            validator.validate_report(self.batch)


if __name__ == "__main__":
    unittest.main()
