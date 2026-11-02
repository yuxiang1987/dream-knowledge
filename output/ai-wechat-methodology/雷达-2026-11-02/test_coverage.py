"""Offline regressions: missing coverage, forged evidence and excluded-case leakage."""
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
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.batch = Path(self.temp.name)
        self.rows = json.loads((HERE / "coverage.json").read_text(encoding="utf-8"))
        (self.batch / "fetch-summary.json").write_bytes((HERE / "fetch-summary.json").read_bytes())

    def validate(self, rows):
        (self.batch / "coverage.json").write_text(json.dumps(rows, ensure_ascii=False), encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()):
            return validator.validate(self.batch)

    def test_missing_article_rejected(self):
        with self.assertRaisesRegex(AssertionError, "Coverage gap"):
            self.validate(self.rows[:-1])

    def test_duplicate_article_rejected(self):
        with self.assertRaisesRegex(AssertionError, "Coverage gap"):
            self.validate(self.rows + [copy.deepcopy(self.rows[0])])

    def test_changed_raw_rejected(self):
        rows = copy.deepcopy(self.rows)
        rows[0]["raw_sha256"] = "0" * 64
        with self.assertRaises(AssertionError):
            self.validate(rows)

    def test_forged_deep_anchor_rejected(self):
        rows = copy.deepcopy(self.rows)
        next(r for r in rows if r["disposition"] == "deep")["anchors"][0] = "不在原文的伪造锚点-20261102"
        with self.assertRaises(AssertionError):
            self.validate(rows)

    def test_excluded_article_cannot_claim_tested_case(self):
        rows = copy.deepcopy(self.rows)
        next(r for r in rows if r["disposition"] == "excluded")["case_card"] = "把官方实验误记为作者实测"
        with self.assertRaisesRegex(AssertionError, "Excluded article"):
            self.validate(rows)

    def test_forged_exclusion_anchor_rejected(self):
        rows = copy.deepcopy(self.rows)
        next(r for r in rows if r["disposition"] == "excluded")["anchors"][0] = "伪造的排除依据-20261102"
        with self.assertRaisesRegex(AssertionError, "Unlocatable exclusion anchor"):
            self.validate(rows)


if __name__ == "__main__":
    unittest.main()
