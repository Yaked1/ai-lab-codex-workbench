#!/usr/bin/env python3
"""Repository health checks for the Codex workbench."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

MANIFEST_NAME = "repository-manifest.json"
SKIP_DIRS = {
    ".git", ".venv", "venv", "node_modules", "__pycache__",
    ".pytest_cache", ".mypy_cache", ".cache", "dist", "build",
    "logs", "outputs", ".tmp", ".idea", ".vscode", ".omc",
}
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY-----"),
    re.compile(r"ghp_[A-Za-z0-9_]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk-[A-Za-z0-9]{24,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9-]{20,}"),
    re.compile(r"AIza[0-9A-Za-z_-]{30,}"),
    re.compile(r"npm_[A-Za-z0-9]{30,}"),
)
SPECIAL_TEXT_FILES = {"LICENSE", ".gitignore", ".editorconfig"}


def load_manifest(root: Path) -> dict[str, object]:
    path = root / MANIFEST_NAME
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot load {MANIFEST_NAME}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{MANIFEST_NAME} must contain a JSON object")
    return value


def _string_list(manifest: dict[str, object], key: str) -> list[str]:
    value = manifest.get(key)
    if not isinstance(value, list) or not all(
        isinstance(item, str) and item for item in value
    ):
        raise ValueError(f"{MANIFEST_NAME}.{key} must be a string list")
    return value


def required_files(root: Path) -> list[str]:
    return _string_list(load_manifest(root), "required_files")


def text_suffixes(root: Path) -> set[str]:
    return set(_string_list(load_manifest(root), "text_suffixes"))


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def iter_text_files(root: Path):
    suffixes = text_suffixes(root)
    for path in root.rglob("*"):
        if should_skip(path) or not path.is_file():
            continue
        if path.name in SPECIAL_TEXT_FILES or path.suffix.lower() in suffixes:
            yield path


def check_required_files(root: Path) -> list[str]:
    return [
        f"Missing required file: {relative}"
        for relative in required_files(root)
        if not (root / relative).is_file()
    ]


def check_secret_patterns(root: Path) -> list[str]:
    errors = []
    for path in iter_text_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if any(pattern.search(text) for pattern in SECRET_PATTERNS):
            errors.append(f"Possible secret pattern in {path.relative_to(root)}")
    return errors


def check_large_files(root: Path) -> list[str]:
    warnings = []
    for path in root.rglob("*"):
        if should_skip(path) or not path.is_file():
            continue
        size = path.stat().st_size
        if size > 5_000_000:
            warnings.append(
                f"Large file over 5 MB: {path.relative_to(root)} ({size} bytes)"
            )
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
    try:
        errors = check_required_files(root)
        errors.extend(check_secret_patterns(root))
        errors.extend(check_final_newlines(root))
        warnings = check_large_files(root)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        print(
            f"Repository health check failed with {len(errors)} error(s).",
            file=sys.stderr,
        )
        return 1
    print("Repository health check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
