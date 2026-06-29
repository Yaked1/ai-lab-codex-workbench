#!/usr/bin/env python3
"""Repository health checks for the Codex workbench."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CHANGELOG.md",
    ".gitignore",
    ".editorconfig",
    ".github/workflows/ci.yml",
    ".github/workflows/autofix.yml",
    ".github/workflows/merge-pr.yml",
    "scripts/safe_autofix.py",
    "scripts/repo_health_check.py",
]

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
}

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY-----"),
    re.compile(r"ghp_[A-Za-z0-9_]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk-[A-Za-z0-9]{24,}"),
]

TEXT_SUFFIXES = {".md", ".txt", ".py", ".ps1", ".yml", ".yaml", ".json", ".toml"}


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def iter_text_files(root: Path):
    for path in root.rglob("*"):
        if should_skip(path) or not path.is_file():
            continue
        if path.name in {"LICENSE", ".gitignore", ".editorconfig"} or path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def check_required_files(root: Path) -> list[str]:
    errors = []
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"Missing required file: {relative}")
    return errors


def check_secret_patterns(root: Path) -> list[str]:
    errors = []
    for path in iter_text_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"Possible secret pattern in {path.relative_to(root)}")
    return errors


def check_large_files(root: Path) -> list[str]:
    warnings = []
    for path in root.rglob("*"):
        if should_skip(path) or not path.is_file():
            continue
        size = path.stat().st_size
        if size > 5_000_000:
            warnings.append(f"Large file over 5 MB: {path.relative_to(root)} ({size} bytes)")
    return warnings


def check_final_newlines(root: Path) -> list[str]:
    errors = []
    for path in iter_text_files(root):
        try:
            data = path.read_bytes()
        except OSError:
            continue
        if data and not data.endswith(b"\n"):
            errors.append(f"Missing final newline: {path.relative_to(root)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Repository health check")
    parser.add_argument("--root", default=".")
    parser.add_argument("--ci", action="store_true", help="CI mode")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors = []
    warnings = []

    errors.extend(check_required_files(root))
    errors.extend(check_secret_patterns(root))
    errors.extend(check_final_newlines(root))
    warnings.extend(check_large_files(root))

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    if errors:
        print(f"Repository health check failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print("Repository health check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
