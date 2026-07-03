#!/usr/bin/env python3
"""Score public research candidates for manual curation."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from discover_ai_sources import DEFAULT_CANDIDATES


def score_candidate(candidate: dict[str, Any]) -> int:
    if candidate.get("blocked"):
        return 0

    score = 10
    status = str(candidate.get("source_status", "")).lower()
    metadata = candidate.get("metadata", {}) or {}

    if candidate.get("official"):
        score += 25
    if status in {"official", "official-docs", "official-repository"}:
        score += 25
    elif status in {"community", "community-repository", "public-repository"}:
        score += 12
    elif "unofficial" in status:
        score += 3
    if "leak" in status:
        score -= 35

    if candidate.get("license_hint") and "unknown" not in str(candidate.get("license_hint")).lower():
        score += 5
    if candidate.get("summary"):
        score += 5
    if candidate.get("safety_note"):
        score += 5

    http_status = metadata.get("http_status")
    if http_status == 200:
        score += 8
    elif isinstance(http_status, int) and 200 <= http_status < 400:
        score += 4
    if metadata.get("error"):
        score -= 8
    if metadata.get("github_license"):
        score += 4
    if metadata.get("github_pushed_at"):
        score += 4

    return max(0, min(100, score))


def quality_label(score: int, blocked: bool = False) -> str:
    if blocked:
        return "blocked"
    if score >= 75:
        return "high"
    if score >= 45:
        return "medium"
    if score > 0:
        return "low"
    return "review-required"


def score_payload(payload: dict[str, Any]) -> dict[str, Any]:
    candidates = []
    for candidate in payload.get("candidates", []):
        if not isinstance(candidate, dict):
            continue
        scored = dict(candidate)
        score = score_candidate(scored)
        scored["score"] = score
        scored["quality"] = quality_label(score, blocked=bool(scored.get("blocked")))
        candidates.append(scored)

    payload = dict(payload)
    payload["candidates"] = sorted(
        candidates,
        key=lambda item: (-int(item.get("score", 0)), str(item.get("category", "")), str(item.get("id", ""))),
    )
    return payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Score research candidates.")
    parser.add_argument("--candidates", default=DEFAULT_CANDIDATES, type=Path)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    if not args.candidates.is_file():
        payload = {"schema_version": 1, "generated_at": "", "candidates": []}
    else:
        payload = json.loads(args.candidates.read_text(encoding="utf-8"))
    scored = score_payload(payload)
    if args.dry_run:
        print(json.dumps(scored, indent=2, sort_keys=True))
        return 0
    args.candidates.parent.mkdir(parents=True, exist_ok=True)
    args.candidates.write_text(json.dumps(scored, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Scored {len(scored.get('candidates', []))} candidate(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
