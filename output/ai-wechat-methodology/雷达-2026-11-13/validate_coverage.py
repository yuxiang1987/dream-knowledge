"""Offline evidence acceptance, reusing the existing incremental batch validator."""
import importlib.util
from pathlib import Path

BATCH = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "previous_radar_validator", BATCH.parent / "雷达-2026-11-11" / "validate_coverage.py")
previous = importlib.util.module_from_spec(spec)
spec.loader.exec_module(previous)


def validate(batch=BATCH):
    return previous.validate(batch)


if __name__ == "__main__":
    validate()
