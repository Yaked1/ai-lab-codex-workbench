#!/usr/bin/env python3
"""Audit and strip generated research-expansion blocks from tracked text files."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


MARKER_BEGIN = "RESEARCH-GRADE-EXPANSION:BEGIN"
MARKER_END = "RESEARCH-GRADE-EXPANSION:END"

SCRIPT_PATH = "scripts/mechanical_research_expansion.py"
REPORT_PATH = "docs/review/mechanical-research-expansion-report.md"
MANIFEST_PATH = "docs/review/mechanical-research-expansion-manifest.json"
EXCLUDED_PATHS = {SCRIPT_PATH, REPORT_PATH, MANIFEST_PATH}

LINE_COMMENT_SUFFIXES = {".py", ".yml", ".yaml", ".gitignore", ".gitattributes", ".editorconfig"}
HTML_COMMENT_SUFFIXES = {".md", ".html", ".svg"}


class MarkerError(ValueError):
    """Raised when a target contains an unsafe or incomplete marker block."""


def run_git_ls_files(root: Path) -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    paths = result.stdout.decode("utf-8").split("\0")
    return sorted(path for path in paths if path)


def approved_tracked_paths(root: Path) -> list[str]:
    """Return the deterministic tracked target set for the current worktree."""
    return [relative for relative in run_git_ls_files(root) if relative not in EXCLUDED_PATHS]


def _marker_pattern(relative: str) -> re.Pattern[str] | None:
    begin = re.escape(MARKER_BEGIN)
    end = re.escape(MARKER_END)
    suffix = Path(relative).suffix.lower()

    if suffix in LINE_COMMENT_SUFFIXES or Path(relative).name in {".gitignore", ".gitattributes", ".editorconfig"}:
        return re.compile(
            rf"^[ \t]*#[ \t]*{begin}[^\r\n]*(?:\r?\n|$).*?"
            rf"^[ \t]*#[ \t]*{end}[^\r\n]*(?:\r?\n|$)",
            re.MULTILINE | re.DOTALL,
        )
    if suffix == ".ps1":
        return re.compile(
            rf"^[ \t]*<#[ \t]*\r?\n"
            rf"(?=[ \t]*{begin}[ \t]*(?:\r?\n|$)).*?"
            rf"^[ \t]*{end}[ \t]*\r?\n[ \t]*#>[ \t]*(?:\r?\n|$)",
            re.MULTILINE | re.DOTALL,
        )
    if suffix in {".md", ".html"}:
        return re.compile(
            rf"^[ \t]*<!--[ \t]*{begin}[ \t]*(?:-->)?.*?"
            rf"^[ \t]*<!--[ \t]*{end}[ \t]*-->[ \t]*(?:\r?\n|$)",
            re.MULTILINE | re.DOTALL,
        )
    if suffix == ".svg":
        return re.compile(
            rf"^[ \t]*<!--[ \t]*{begin}[ \t]*(?:-->)?.*?"
            rf"^[ \t]*(?:<!--[ \t]*)?{end}[ \t]*-->[ \t]*(?:\r?\n|$)",
            re.MULTILINE | re.DOTALL,
        )
    if suffix == ".css":
        return re.compile(
            rf"^[ \t]*/\*[ \t]*{begin}[^\r\n]*(?:\r?\n|$).*?"
            rf"^[ \t]*{end}[ \t]*\*/[ \t]*(?:\r?\n|$)",
            re.MULTILINE | re.DOTALL,
        )
    return None


CSS_RESIDUE_PATTERN = re.compile(
    r"^[ \t]*\.research-grade-addendum[ \t]*\{\r?\n"
    r"[ \t]*border-top: 1px solid #d8dee8;\r?\n"
    r"[ \t]*margin-top: 2rem;\r?\n"
    r"[ \t]*padding-top: 1rem;\r?\n"
    r"[ \t]*\}[ \t]*(?:\r?\n|$)",
    re.MULTILINE,
)


def _find_marker_spans(relative: str, text: str) -> list[tuple[int, int]]:
    begin_count = text.count(MARKER_BEGIN)
    end_count = text.count(MARKER_END)
    if begin_count != end_count:
        raise MarkerError(
            f"{relative}: unmatched generated markers "
            f"(begin={begin_count}, end={end_count})"
        )
    if begin_count == 0:
        return []

    pattern = _marker_pattern(relative)
    if pattern is None:
        raise MarkerError(f"{relative}: generated markers use unsupported syntax")

    matches = list(pattern.finditer(text))
    if len(matches) != begin_count:
        raise MarkerError(
            f"{relative}: malformed generated marker block "
            f"(expected {begin_count}, parsed {len(matches)})"
        )
    return [(match.start(), match.end()) for match in matches]


def _next_line_end(text: str, position: int) -> int:
    newline = text.find("\n", position)
    return len(text) if newline == -1 else newline + 1


def _is_blank_line_at(text: str, position: int) -> bool:
    if position >= len(text):
        return False
    end = text.find("\n", position)
    segment = text[position:] if end == -1 else text[position : end + 1]
    return bool(segment) and not segment.strip(" \t\r\n")


def _extend_generated_boundary(text: str, start: int, end: int) -> tuple[int, int]:
    if _is_blank_line_at(text, end):
        end = _next_line_end(text, end)

    if end == len(text) and start > 0:
        previous_line_start = text.rfind("\n", 0, start - 1) + 1
        if previous_line_start < start and not text[previous_line_start:start].strip(" \t\r\n"):
            start = previous_line_start
    return start, end


def _merge_spans(text: str, spans: list[tuple[int, int]]) -> list[tuple[int, int]]:
    extended = [_extend_generated_boundary(text, start, end) for start, end in spans]
    merged: list[tuple[int, int]] = []
    for start, end in sorted(extended):
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    if merged and merged[-1][1] == len(text):
        start, end = merged[-1]
        if start > 0:
            previous_line_start = text.rfind("\n", 0, start - 1) + 1
            if previous_line_start < start and not text[previous_line_start:start].strip(" \t\r\n"):
                merged[-1] = (previous_line_start, end)
    return merged


def _remove_spans(text: str, spans: list[tuple[int, int]]) -> str:
    merged = _merge_spans(text, spans)
    pieces: list[str] = []
    cursor = 0
    for start, end in merged:
        pieces.append(text[cursor:start])
        cursor = end
    pieces.append(text[cursor:])
    stripped = "".join(pieces)

    if text and stripped and text.endswith(("\n", "\r")) and not stripped.endswith(("\n", "\r")):
        stripped += "\r\n" if text.endswith("\r\n") else "\n"
    return stripped


def strip_text(relative: str, text: str) -> str:
    """Remove complete generated blocks and the exact generated CSS residue."""
    spans = _find_marker_spans(relative, text)
    if Path(relative).suffix.lower() == ".css":
        spans.extend((match.start(), match.end()) for match in CSS_RESIDUE_PATTERN.finditer(text))
    if not spans:
        return text
    return _remove_spans(text, spans)


def audit_text(relative: str, text: str) -> list[str]:
    try:
        stripped = strip_text(relative, text)
    except MarkerError as error:
        return [str(error)]
    if stripped != text:
        return [f"{relative}: removable generated content remains"]
    return []


def _read_utf8(path: Path) -> str | None:
    raw = path.read_bytes()
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        marker_bytes = (MARKER_BEGIN.encode("utf-8"), MARKER_END.encode("utf-8"))
        if any(marker in raw for marker in marker_bytes):
            raise MarkerError(f"{path.as_posix()}: generated marker found in non-UTF-8 content")
        return None


def scan_repo(root: Path) -> tuple[list[str], list[tuple[str, str]]]:
    errors: list[str] = []
    changes: list[tuple[str, str]] = []
    for relative in approved_tracked_paths(root):
        path = root / Path(relative)
        if not path.is_file():
            continue
        try:
            text = _read_utf8(path)
            if text is None:
                continue
            stripped = strip_text(relative, text)
        except MarkerError as error:
            errors.append(str(error))
            continue
        if stripped != text:
            changes.append((relative, stripped))
    return errors, changes


def _write_changes(root: Path, changes: list[tuple[str, str]]) -> None:
    for relative, text in changes:
        (root / Path(relative)).write_bytes(text.encode("utf-8"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit or strip generated research-expansion blocks.")
    parser.add_argument("--root", default=Path(__file__).resolve().parents[1], type=Path)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--check", "--audit", action="store_true", help="audit without writing; this is the default")
    modes.add_argument("--write", action="store_true", help="strip complete generated blocks")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    try:
        errors, changes = scan_repo(root)
    except (OSError, subprocess.CalledProcessError) as error:
        print(f"strip audit failed: {error}", file=sys.stderr)
        return 1

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    if args.write:
        _write_changes(root, changes)
        remaining_errors, remaining_changes = scan_repo(root)
        if remaining_errors:
            for error in remaining_errors:
                print(error, file=sys.stderr)
            return 1
        if remaining_changes:
            for relative, _ in remaining_changes:
                print(f"{relative}: generated content remains after write", file=sys.stderr)
            return 1
        print(f"Strip write complete: {len(changes)} changed files.")
        return 0

    if changes:
        print(f"Strip audit found {len(changes)} changed files:")
        for relative, _ in changes:
            print(f"- {relative}")
        return 1
    print("Strip audit clean: 0 changed files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
