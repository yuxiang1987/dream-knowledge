"""Offline acceptance for this incremental radar batch; no network requests."""
import importlib.util
import json
import re
from pathlib import Path

BATCH = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "radar_evidence", BATCH.parent / "雷达-2026-11-01" / "validate_coverage.py")
evidence = importlib.util.module_from_spec(spec)
spec.loader.exec_module(evidence)


def validate(batch=BATCH):
    batch = Path(batch)
    previous = evidence.BATCH
    evidence.BATCH = batch
    try:
        counts = evidence.validate()
        rows = json.loads((batch / "coverage.json").read_text(encoding="utf-8"))
        for row in rows:
            author = (evidence.ROOT / row["author_path"]).read_text(encoding="utf-8")
            assert row["raw_path"] in author, "Missing author batch provenance"
            raw = evidence.visible((evidence.ROOT / row["raw_path"]).read_text(encoding="utf-8"))
            if row["disposition"] == "excluded":
                assert not row.get("case_card"), "Excluded article cannot own a tested case"
                assert row["anchors"], "Missing exclusion evidence"
                for anchor in row["anchors"]:
                    assert evidence.visible(anchor) in raw, "Unlocatable exclusion anchor"
            else:
                source = (evidence.ROOT / row["source_path"]).read_text(encoding="utf-8")
                for heading in ("主问题与证据身份", "标题与开头", "结构推进", "案例、解释与观察", "原文定位锚点", "结尾怎样收束", "失败、限制与不宜照搬处", "可迁移写法与自己的待测方向", "相关页面"):
                    assert heading in source, (row["title"], heading)
                assert "待实操" in source or "待验证" in source, "Missing untested boundary"
                assert "披露" in source, "Missing commercial disclosure boundary"
                if row.get("case_card"):
                    assert "待实操" in row["case_card"], "Case must not claim our own test"
        return counts
    finally:
        evidence.BATCH = previous


if __name__ == "__main__":
    validate()
