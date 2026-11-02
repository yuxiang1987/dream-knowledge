"""Reuse established offline evidence checks; add manual topic-filter verification."""
import importlib.util
import json
from pathlib import Path

BATCH = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "previous_radar_validator", BATCH.parent / "雷达-2026-11-01" / "validate_coverage.py")
evidence = importlib.util.module_from_spec(spec)
spec.loader.exec_module(evidence)


def validate(batch=BATCH):
    previous = evidence.BATCH
    evidence.BATCH = Path(batch)
    try:
        counts = evidence.validate()
        rows = json.loads((Path(batch) / "coverage.json").read_text(encoding="utf-8"))
        for row in rows:
            if row["disposition"] == "excluded":
                assert not row.get("case_card"), "Excluded article cannot own a tested case"
                author_text = (evidence.ROOT / "wiki/topics/小林coding文章写法拆解.md").read_text(encoding="utf-8")
                for anchor in row["anchors"]:
                    assert evidence.visible(anchor) in evidence.visible((evidence.ROOT / row["raw_path"]).read_text(encoding="utf-8")), "Unlocatable exclusion anchor"
                    assert anchor in author_text, "Missing exclusion evidence"
        return counts
    finally:
        evidence.BATCH = previous


if __name__ == "__main__":
    validate()
