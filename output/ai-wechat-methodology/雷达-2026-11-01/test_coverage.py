"""Regression checks for incomplete or fabricated batch evidence; no network or repo writes."""
import contextlib
import copy
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("coverage_validator", HERE / "validate_coverage.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)

class CoverageEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.batch = Path(self.temp.name)
        self.original_batch = validator.BATCH
        self.addCleanup(setattr, validator, "BATCH", self.original_batch)
        validator.BATCH = self.batch
        self.rows = json.loads((HERE / "coverage.json").read_text(encoding="utf-8"))
        (self.batch / "fetch-summary.json").write_bytes((HERE / "fetch-summary.json").read_bytes())

    def check_rows(self, rows):
        (self.batch / "coverage.json").write_text(json.dumps(rows, ensure_ascii=False), encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()):
            return validator.validate()

    def test_complete_evidence_with_aliased_author_links(self):
        counts = self.check_rows(self.rows)
        self.assertEqual(sum(counts[k] for k in ("deep", "excluded", "reused")), len(self.rows))

    def test_missing_article_rejected(self):
        with self.assertRaisesRegex(AssertionError, "Coverage gap"):
            self.check_rows(self.rows[:-1])

    def test_duplicate_article_rejected(self):
        with self.assertRaisesRegex(AssertionError, "Coverage gap"):
            self.check_rows(self.rows + [copy.deepcopy(self.rows[0])])

    def test_changed_raw_fingerprint_rejected(self):
        rows = copy.deepcopy(self.rows)
        rows[0]["raw_sha256"] = "0" * 64
        with self.assertRaises(AssertionError):
            self.check_rows(rows)

    def test_unlocatable_anchor_rejected(self):
        rows = copy.deepcopy(self.rows)
        row = next(r for r in rows if r["disposition"] == "deep")
        row["anchors"][0] = "伪造且不在原文中的证据锚点-coverage-test"
        with self.assertRaises(AssertionError):
            self.check_rows(rows)

if __name__ == "__main__":
    unittest.main()
