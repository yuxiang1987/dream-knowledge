"""Consumer-visible evidence boundaries: coverage, forgery and case ownership."""
import contextlib
import copy
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("batch_validator", HERE / "validate_coverage.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class EvidenceBoundaryTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.batch = Path(temp.name)
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
        next(r for r in rows if r["disposition"] == "deep")["anchors"][0] = "伪造锚点20261111不存在"
        with self.assertRaises(AssertionError):
            self.validate(rows)

    def test_excluded_article_cannot_claim_tested_case(self):
        rows = copy.deepcopy(self.rows)
        next(r for r in rows if r["disposition"] == "excluded")["case_card"] = "官方转述误当实测"
        with self.assertRaisesRegex(AssertionError, "Excluded article"):
            self.validate(rows)

    def test_forged_exclusion_anchor_rejected(self):
        rows = copy.deepcopy(self.rows)
        next(r for r in rows if r["disposition"] == "excluded")["anchors"][0] = "伪造筛选依据20261111不存在"
        with self.assertRaisesRegex(AssertionError, "Unlocatable exclusion anchor"):
            self.validate(rows)


if __name__ == "__main__":
    unittest.main()
