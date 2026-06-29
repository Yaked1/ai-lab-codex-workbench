#!/usr/bin/env python3
"""Deterministic safe formatting cleanup for text files.

This script intentionally avoids clever formatting. Clever formatting is how
simple repositories wake up with 900-line diffs and emotional damage.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

TEXT_EXTENSIONS = {
    ".md",
    ".txt",
    ".py",
    ".ps1",
    ".yml",
    ".yaml",
    ".json",
    ".toml",
    ".gitignore",
    ".editorconfig",
}

SKIP_DIRS = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".cache",
    "dist",
    "build",
    "logs",
    "outputs",
}

MAX_TEXT_BYTES = 1_000_000


def is_text_candidate(path: Path) -> bool:
    if any(part in SKIP_DIRS for part in path.parts):
        return False
    if not path.is_file():
        return False
    if path.stat().st_size > MAX_TEXT_BYTES:
        return False
    if path.name in {"LICENSE", "AGENTS.md", "README.md", "CONTRIBUTING.md", "SECURITY.md", "CHANGELOG.md"}:
        return True
    if path.name in {".gitignore", ".editorconfig"}:
        return True
    return path.suffix.lower() in TEXT_EXTENSIONS


def iter_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*")):
        if is_text_candidate(path):
            yield path


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.split("\n")]
    text = "\n".join(lines).rstrip("\n") + "\n"
    return text


def process_file(path: Path, write: bool) -> bool:
    try:
        original = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False
    fixed = normalize_text(original)
    changed = fixed != original
    if changed and write:
        path.write_text(fixed, encoding="utf-8", newline="\n")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Safe deterministic autofix")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Fail if files need formatting fixes")
    mode.add_argument("--write", action="store_true", help="Apply safe formatting fixes")
    parser.add_argument("--root", default=".", help="Repository root")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    changed: list[Path] = []
    for path in iter_files(root):
        if process_file(path, write=args.write):
            changed.append(path.relative_to(root))

    if changed:
        action = "Fixed" if args.write else "Needs fix"
        for path in changed:
            print(f"{action}: {path}")
        return 0 if args.write else 1

    print("No safe formatting changes needed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
