#!/usr/bin/env python3
"""Validate the first-success tutorial report without external dependencies."""
from pathlib import Path
import sys

REPORT = Path(__file__).with_name("report.md")
REQUIRED = (
    "## Summary",
    "## Evidence",
    "## Missing Details",
    "## Verification",
    "python scripts/repo_health_check.py",
    "reviewing the command output",
    "passing result",
    "documented but not executed",
)


def main() -> int:
    if not REPORT.is_file():
        print(f"FAIL: create {REPORT}")
        return 1
    text = REPORT.read_text(encoding="utf-8")
    normalized = " ".join(text.split())
    missing = [item for item in REQUIRED if item not in normalized]
    if missing:
        print("FAIL: report is missing:")
        for item in missing:
            print(f"- {item}")
        return 1
    print("PASS: first reviewed agent report satisfies the contract")
    return 0


if __name__ == "__main__":
    sys.exit(main())
