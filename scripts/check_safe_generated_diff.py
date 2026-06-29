#!/usr/bin/env python3
"""Check that a diff touches only generated research files."""
from __future__ import annotations

import argparse
import posixpath
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import NamedTuple

ALLOWED_EXACT = {"data/research/candidates.json"}
ALLOWED_INBOX_DIR = ("docs", "research", "inbox")
ALLOWED_CURATED_DIR = ("docs", "research", "curated")


class DiffReport(NamedTuple):
    allowed: list[str]
    refused: list[str]

    @property
    def is_safe(self) -> bool:
        return not self.refused


def normalize_changed_path(path: str) -> str:
    normalized = path.strip().replace("\\", "/")
    while normalized.startswith("./"):
        normalized = normalized[2:]
    normalized = posixpath.normpath(normalized)
    if normalized == ".":
        return ""
    return normalized


def is_safe_relative_path(path: str) -> bool:
    if not path or path.startswith("/") or path.startswith("../") or "/../" in path:
        return False
    parts = PurePosixPath(path).parts
    return bool(parts) and "." not in parts and ".." not in parts


def is_allowed_generated_file(path: str) -> bool:
    normalized = normalize_changed_path(path)
    if not is_safe_relative_path(normalized):
        return False
    if normalized in ALLOWED_EXACT:
        return True

    parts = PurePosixPath(normalized).parts
    if len(parts) != 4:
        return False

    parent = parts[:3]
    name = parts[3]
    if parent == ALLOWED_INBOX_DIR:
        return name.endswith(".md") and name != ".md"
    if parent == ALLOWED_CURATED_DIR:
        return name.startswith("curator-prompt-") and name.endswith(".md")
    return False


def classify_changed_files(paths: list[str]) -> DiffReport:
    normalized = sorted({normalize_changed_path(path) for path in paths if normalize_changed_path(path)})
    allowed = [path for path in normalized if is_allowed_generated_file(path)]
    refused = [path for path in normalized if not is_allowed_generated_file(path)]
    return DiffReport(allowed=allowed, refused=refused)


def git_changed_files(root: Path, base: str | None, head: str | None, staged: bool) -> list[str]:
    command = ["git", "diff", "--name-only"]
    if staged:
        command.append("--cached")
    elif base and head:
        command.append(f"{base}...{head}")
    elif base or head:
        raise ValueError("Both base and head refs are required when checking refs.")

    result = subprocess.run(
        command,
        cwd=root,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git diff failed")
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def print_report(report: DiffReport) -> None:
    print("Safe generated-file diff check")
    if report.allowed:
        print("Allowed changed files:")
        for path in report.allowed:
            print(f"  OK  {path}")
    else:
        print("Allowed changed files: none")

    if report.refused:
        print("Refused changed files:")
        for path in report.refused:
            print(f"  NO  {path}")
        print("Result: refused")
    else:
        print("Refused changed files: none")
        print("Result: allowed")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Allow only generated research files in a diff.")
    parser.add_argument("refs", nargs="*", help="Optional base and head refs.")
    parser.add_argument("--base", default=None, help="Base ref for git diff.")
    parser.add_argument("--head", default=None, help="Head ref for git diff.")
    parser.add_argument("--staged", action="store_true", help="Check staged changes.")
    parser.add_argument("--root", default=Path("."), type=Path, help="Repository root.")
    args = parser.parse_args(argv)

    if args.refs:
        if len(args.refs) != 2:
            parser.error("Provide either zero refs or exactly two refs: base head.")
        if args.base or args.head:
            parser.error("Use either positional refs or --base/--head, not both.")
        args.base, args.head = args.refs

    if args.staged and (args.base or args.head):
        parser.error("--staged cannot be combined with base/head refs.")

    try:
        paths = git_changed_files(args.root.resolve(), args.base, args.head, args.staged)
    except (RuntimeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    report = classify_changed_files(paths)
    print_report(report)
    return 0 if report.is_safe else 1


if __name__ == "__main__":
    raise SystemExit(main())
