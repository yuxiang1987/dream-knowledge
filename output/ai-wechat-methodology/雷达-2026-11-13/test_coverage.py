"""Reject incomplete coverage, forged evidence and false tested-case attribution."""
import contextlib
import copy
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("current_validator", HERE / "validate_coverage.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class EvidenceBoundaryTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.batch = Path(temp.name)
        self.rows = json.loads((HERE / "coverage.json").read_text(encoding="utf-8"))
        (self.batch / "fetch-summary.json").write_bytes((HERE / "fetch-summary.json").read_bytes())

    def reject(self, rows, message=None):
        (self.batch / "coverage.json").write_text(json.dumps(rows, ensure_ascii=False), encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaisesRegex(AssertionError, message or ".*"):
                validator.validate(self.batch)

    def test_missing_article_rejected(self):
        self.reject(self.rows[:-1], "Coverage gap")

    def test_duplicate_article_rejected(self):
        self.reject(self.rows + [copy.deepcopy(self.rows[0])], "Coverage gap")

    def test_changed_raw_fingerprint_rejected(self):
        self.rows[0]["raw_sha256"] = "0" * 64
        self.reject(self.rows)

    def test_forged_deep_anchor_rejected(self):
        next(r for r in self.rows if r["disposition"] == "deep")["anchors"][0] = "不存在的伪造证据20261113"
        self.reject(self.rows)

    def test_excluded_article_cannot_claim_tested_case(self):
        next(r for r in self.rows if r["disposition"] == "excluded")["case_card"] = "误标亲测"
        self.reject(self.rows, "Excluded article")

    def test_forged_exclusion_anchor_rejected(self):
        next(r for r in self.rows if r["disposition"] == "excluded")["anchors"][0] = "不存在的排除引文20261113"
        self.reject(self.rows, "Unlocatable exclusion anchor")


if __name__ == "__main__":
    unittest.main()
