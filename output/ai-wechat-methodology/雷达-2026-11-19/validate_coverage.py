"""Offline incremental radar acceptance; never invokes collection APIs."""
import hashlib
import importlib.util
import json
from pathlib import Path

BATCH = Path(__file__).resolve().parent
ROOT = BATCH.parents[2]
spec = importlib.util.spec_from_file_location(
    "prior_radar_acceptance", BATCH.parent / "雷达-2026-11-11" / "validate_coverage.py")
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)


def validate(batch=BATCH):
    return prior.validate(batch)


def validate_preservation(batch=BATCH, root=ROOT):
    protected = json.loads((batch / "preexisting-raw-sha256.json").read_text(encoding="utf-8"))
    for path, digest in protected.items():
        assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest, path
    return len(protected)


def validate_report(batch=BATCH):
    rows = json.loads((batch / "coverage.json").read_text(encoding="utf-8"))
    report = json.loads((batch / "report.json").read_text(encoding="utf-8"))
    pending = set(report["raw_without_source"])
    for row in rows:
        if row["disposition"] != "excluded":
            assert row["raw_path"] not in pending, "Completed source still reported pending"
    assert report["analysis_scope"]["covered"] == len(rows), "Stale analysis coverage"


if __name__ == "__main__":
    counts = validate()
    preserved = validate_preservation()
    validate_report()
    result = {"result": "PASS", "covered": sum(counts[k] for k in ("deep", "excluded", "reused")),
              **counts, "preserved_raw_files": preserved,
              "scope": "Offline coverage, hashes, exact anchors, source ownership, author/index navigation, case cards and final report; not product or reader-effect verification."}
    (BATCH / "verification.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
