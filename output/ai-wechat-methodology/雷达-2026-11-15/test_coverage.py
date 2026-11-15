"""Catch lost article coverage and fabricated evidence without network calls."""
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
        self.reject([], "Coverage gap")

    def test_duplicate_article(self):
        self.reject(self.rows + copy.deepcopy(self.rows), "Coverage gap")

    def test_forged_anchor(self):
        self.rows[0]["anchors"][0] = "这不是原文的锚点20261115"
        self.reject(self.rows)

    def test_changed_raw_hash(self):
        self.rows[0]["raw_sha256"] = "0" * 64
        self.reject(self.rows)

    def test_unperformed_case_cannot_gain_card(self):
        self.rows[0]["case_card"] = "### 虚构的Carbon完成实测卡"
        self.reject(self.rows, "Missing case card")


if __name__ == "__main__":
    unittest.main()
