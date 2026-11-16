"""Consumer-visible batch evidence regressions; isolated and offline."""
import contextlib
import copy
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
        row["anchors"][0] = "原文没有的虚构证据20261116"
        self.reject(self.rows)

    def test_exclusion_requires_reason(self):
        row = self.rows[0]
        row.update(disposition="excluded", source_path=None, reason="", case_card=None)
        self.reject(self.rows)

    def test_nonexistent_case_is_rejected(self):
        row = next(r for r in self.rows if r["disposition"] != "excluded")
        row["case_card"] = "### 虚构的本账号实测卡20261116"
        self.reject(self.rows, "Missing case card")


if __name__ == "__main__":
    unittest.main()
