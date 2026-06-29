#!/usr/bin/env python3
"""Summarize Repository Autopilot state without requiring GitHub CLI."""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any

DEFAULT_CANDIDATES = Path("data/research/candidates.json")


def run_git(root: Path, args: list[str]) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=root,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except (FileNotFoundError, OSError):
        return "unavailable"
    if result.returncode != 0:
        return "unavailable"
    return result.stdout.strip() or "clean"


def latest_files(root: Path, relative_dir: str, pattern: str, limit: int = 5) -> list[str]:
    directory = root / relative_dir
    if not directory.is_dir():
        return []
    files = sorted(
        directory.glob(pattern),
        key=lambda path: (path.stat().st_mtime, path.name),
        reverse=True,
    )
    return [path.relative_to(root).as_posix() for path in files[:limit]]


def load_candidate_payload(root: Path, path: Path = DEFAULT_CANDIDATES) -> dict[str, Any]:
    candidate_path = root / path
    if not candidate_path.is_file():
        return {"generated_at": "missing", "candidates": []}
    try:
        payload = json.loads(candidate_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"generated_at": "invalid-json", "candidates": []}
    if not isinstance(payload, dict):
        return {"generated_at": "invalid-json", "candidates": []}
    candidates = payload.get("candidates", [])
    if not isinstance(candidates, list):
        candidates = []
    return {"generated_at": payload.get("generated_at", "unknown"), "candidates": candidates}


def candidate_summary(root: Path) -> dict[str, Any]:
    payload = load_candidate_payload(root)
    candidates = [candidate for candidate in payload["candidates"] if isinstance(candidate, dict)]
    blocked = [candidate for candidate in candidates if candidate.get("blocked")]
    top = sorted(
        candidates,
        key=lambda item: (-int(item.get("score", 0) or 0), str(item.get("category", "")), str(item.get("id", ""))),
    )[:5]
    return {
        "generated_at": payload["generated_at"],
        "candidate_count": len(candidates),
        "blocked_count": len(blocked),
        "top_candidates": [
            {
                "id": str(candidate.get("id", "unknown")),
                "score": int(candidate.get("score", 0) or 0),
                "category": str(candidate.get("category", "uncategorized")),
            }
            for candidate in top
        ],
    }


def build_status(root: Path) -> dict[str, Any]:
    root = root.resolve()
    summary = candidate_summary(root)
    return {
        "current_branch": run_git(root, ["branch", "--show-current"]),
        "git_status": run_git(root, ["status", "--short", "--branch"]),
        "latest_inbox_reports": latest_files(root, "docs/research/inbox", "*.md"),
        "latest_curator_prompts": latest_files(root, "docs/research/curated", "curator-prompt-*.md"),
        **summary,
    }


def render_status(status: dict[str, Any]) -> str:
    lines = [
        "Repository Autopilot Status",
        "",
        f"Current branch: {status['current_branch']}",
        "",
        "Git status:",
    ]
    for line in str(status["git_status"]).splitlines():
        lines.append(f"  {line}")

    lines.extend(["", "Latest research inbox files:"])
    inbox = status["latest_inbox_reports"]
    lines.extend([f"  - {path}" for path in inbox] or ["  - none"])

    lines.extend(["", "Latest curator prompt files:"])
    prompts = status["latest_curator_prompts"]
    lines.extend([f"  - {path}" for path in prompts] or ["  - none"])

    lines.extend(
        [
            "",
            "Candidate summary:",
            f"  generated_at: {status['generated_at']}",
            f"  candidate_count: {status['candidate_count']}",
            f"  blocked_count: {status['blocked_count']}",
            "  top_candidates:",
        ]
    )
    top_candidates = status["top_candidates"]
    if top_candidates:
        for candidate in top_candidates:
            lines.append(
                f"    - {candidate['id']} | score={candidate['score']} | category={candidate['category']}"
            )
    else:
        lines.append("    - none")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Print Repository Autopilot status.")
    parser.add_argument("--root", default=Path("."), type=Path)
    args = parser.parse_args(argv)
    print(render_status(build_status(args.root)), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
