"""Offline acceptance using the existing incremental evidence contract."""
import hashlib
import importlib.util
import json
from pathlib import Path

BATCH = Path(__file__).resolve().parent
ROOT = BATCH.parents[2]
spec = importlib.util.spec_from_file_location(
    "prior_validator", BATCH.parent / "雷达-2026-11-13" / "validate_coverage.py")
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)


def validate(batch=BATCH):
    return prior.validate(batch)


if __name__ == "__main__":
    validate()
    protected = json.loads((BATCH / "preexisting-raw-sha256.json").read_text(encoding="utf-8"))
    for name, digest in protected.items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
    print(f"Preexisting raw unchanged: {len(protected)} files")
