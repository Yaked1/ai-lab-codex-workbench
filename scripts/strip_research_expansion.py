"""Remove RESEARCH-GRADE-EXPANSION comment blocks from tracked files.

Deterministic inverse of mechanical_research_expansion.py: deletes every
BEGIN..END marker block (inclusive) plus the blank lines that padded it.
Marker lines containing quote characters are treated as source code, not
block delimiters, so the inserter script and the JSON manifest are safe.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

MARKER_BEGIN = "RESEARCH-GRADE-EXPANSION:BEGIN"
MARKER_END = "RESEARCH-GRADE-EXPANSION:END"

SKIP_PATHS = {
    "scripts/mechanical_research_expansion.py",
    "scripts/strip_research_expansion.py",
    "docs/review/mechanical-research-expansion-manifest.json",
}


def is_marker_line(line: str, marker: str) -> bool:
    return marker in line and '"' not in line and "'" not in line


def strip_blocks(text: str) -> tuple[str, int]:
    """Return (new_text, blocks_removed). Idempotent."""
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    removed = 0
    i = 0
    while i < len(lines):
        if is_marker_line(lines[i], MARKER_BEGIN):
            j = i + 1
            while j < len(lines) and not is_marker_line(lines[j], MARKER_END):
                j += 1
            if j < len(lines):
                while out and out[-1].strip() == "":
                    out.pop()
                removed += 1
                i = j + 1
                continue
        out.append(lines[i])
        i += 1
    new_text = "".join(out)
    if removed and new_text and not new_text.endswith("\n"):
        new_text += "\n"
    return new_text, removed


def tracked_files(root: Path) -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files"], cwd=root, capture_output=True, text=True, check=True
    )
    return [root / line for line in result.stdout.splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report only, no writes")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    changed = 0
    total_blocks = 0
    for path in tracked_files(root):
        if path.relative_to(root).as_posix() in SKIP_PATHS:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, FileNotFoundError):
            continue
        new_text, removed = strip_blocks(text)
        if removed:
            changed += 1
            total_blocks += removed
            if args.check:
                print(f"Would strip {removed} block(s): {path.relative_to(root)}")
            else:
                path.write_text(new_text, encoding="utf-8", newline="")
    verb = "Would strip" if args.check else "Stripped"
    print(f"{verb} {total_blocks} block(s) from {changed} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
