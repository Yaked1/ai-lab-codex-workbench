#!/usr/bin/env python3
"""Discover public AI guide candidates from a small YAML source list.

The default mode is deterministic and offline. Network checks happen only when
the caller passes --fetch, which keeps local tests and dry runs cheap.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

DEFAULT_SOURCES = Path("data/research/sources.yml")
DEFAULT_BLOCKLIST = Path("data/research/blocklist.yml")
DEFAULT_CANDIDATES = Path("data/research/candidates.json")
MAX_FETCH_BYTES = 64_000
USER_AGENT = "ai-lab-codex-workbench-research-scout/1.0"

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY-----"),
    re.compile(r"ghp_[A-Za-z0-9_]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk-[A-Za-z0-9]{24,}"),
]


def utc_today() -> str:
    return dt.datetime.now(dt.UTC).date().isoformat()


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if not value:
        return ""
    if value.startswith("#"):
        return ""
    if value[0] in {'"', "'"} and value.endswith(value[0]):
        return value[1:-1]
    lowered = value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    if lowered in {"null", "none"}:
        return None
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_scalar(part.strip()) for part in inner.split(",")]
    return value


def parse_simple_yaml(path: Path) -> dict[str, Any]:
    """Parse the intentionally small YAML subset used by data/research.

    Supported shapes are top-level scalar values, top-level lists, and a
    top-level "sources" list of mappings with optional scalar lists.
    """
    if not path.is_file():
        return {}

    result: dict[str, Any] = {}
    current_section: str | None = None
    current_item: dict[str, Any] | None = None
    current_list_key: str | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        stripped = raw_line.strip()

        if indent == 0 and stripped.endswith(":"):
            if current_section == "sources" and current_item is not None:
                result.setdefault("sources", []).append(current_item)
                current_item = None
            current_section = stripped[:-1]
            result.setdefault(current_section, [])
            current_list_key = None
            continue

        if indent == 0 and ":" in stripped:
            key, value = stripped.split(":", 1)
            result[key.strip()] = parse_scalar(value)
            current_section = None
            current_item = None
            current_list_key = None
            continue

        if current_section == "sources":
            if (
                current_item is not None
                and current_list_key
                and indent >= 4
                and stripped.startswith("- ")
            ):
                current_item.setdefault(current_list_key, []).append(parse_scalar(stripped[2:]))
                continue

            if indent <= 2 and stripped.startswith("- "):
                if current_item is not None:
                    result.setdefault("sources", []).append(current_item)
                current_item = {}
                current_list_key = None
                remainder = stripped[2:].strip()
                if remainder and ":" in remainder:
                    key, value = remainder.split(":", 1)
                    current_item[key.strip()] = parse_scalar(value)
                continue

            if current_item is not None and ":" in stripped:
                key, value = stripped.split(":", 1)
                key = key.strip()
                value = value.strip()
                if value:
                    current_item[key] = parse_scalar(value)
                    current_list_key = None
                else:
                    current_item[key] = []
                    current_list_key = key
                continue

        if current_section and stripped.startswith("- "):
            result.setdefault(current_section, []).append(parse_scalar(stripped[2:]))

    if current_section == "sources" and current_item is not None:
        result.setdefault("sources", []).append(current_item)

    return result


def load_sources(path: Path) -> list[dict[str, Any]]:
    config = parse_simple_yaml(path)
    sources = config.get("sources", [])
    if not isinstance(sources, list):
        return []

    normalized = []
    for source in sources:
        if not isinstance(source, dict):
            continue
        normalized.append(
            {
                "id": str(source.get("id", "")).strip(),
                "name": str(source.get("name", "")).strip(),
                "category": str(source.get("category", "uncategorized")).strip(),
                "url": str(source.get("url", "")).strip(),
                "kind": str(source.get("kind", "source")).strip(),
                "official": bool(source.get("official", False)),
                "source_status": str(source.get("source_status", "unverified")).strip(),
                "license_hint": str(source.get("license_hint", "Unknown; verify before quoting.")).strip(),
                "safety_note": str(source.get("safety_note", "Review before publication.")).strip(),
                "summary": str(source.get("summary", "")).strip(),
                "tags": [str(tag).strip() for tag in source.get("tags", []) if str(tag).strip()],
            }
        )
    return [source for source in normalized if source["id"] and source["url"]]


def load_blocklist(path: Path) -> dict[str, list[str]]:
    config = parse_simple_yaml(path)
    return {
        "blocked_domains": [str(item).lower() for item in config.get("blocked_domains", [])],
        "blocked_url_contains": [str(item).lower() for item in config.get("blocked_url_contains", [])],
        "blocked_terms": [str(item).lower() for item in config.get("blocked_terms", [])],
    }


def redact_secret_text(text: str) -> str:
    redacted = text
    for pattern in SECRET_PATTERNS:
        redacted = pattern.sub("[REDACTED_SECRET_PATTERN]", redacted)
    return redacted


def has_secret_looking_text(text: str) -> bool:
    return any(pattern.search(text) for pattern in SECRET_PATTERNS)


def blocklist_reasons(source: dict[str, Any], blocklist: dict[str, list[str]]) -> list[str]:
    url = str(source.get("url", ""))
    parsed = urllib.parse.urlparse(url)
    host = parsed.netloc.lower()
    searchable = " ".join(
        [
            str(source.get("id", "")),
            str(source.get("name", "")),
            str(source.get("summary", "")),
            str(source.get("safety_note", "")),
            url,
        ]
    ).lower()

    reasons = []
    for domain in blocklist.get("blocked_domains", []):
        if host == domain or host.endswith(f".{domain}"):
            reasons.append(f"blocked domain: {domain}")
    for fragment in blocklist.get("blocked_url_contains", []):
        if fragment and fragment in url.lower():
            reasons.append(f"blocked URL fragment: {fragment}")
    for term in blocklist.get("blocked_terms", []):
        if term and term in searchable:
            reasons.append(f"blocked term: {term}")
    return reasons


def github_api_url(url: str) -> str | None:
    parsed = urllib.parse.urlparse(url)
    if parsed.netloc.lower() != "github.com":
        return None
    parts = [part for part in parsed.path.strip("/").split("/") if part]
    if len(parts) < 2:
        return None
    owner, repo = parts[0], parts[1]
    return f"https://api.github.com/repos/{owner}/{repo}"


def fetch_json(url: str, timeout: float) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/vnd.github+json, application/json;q=0.9, */*;q=0.1",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        data = response.read(MAX_FETCH_BYTES)
    return json.loads(data.decode("utf-8", errors="replace"))


def fetch_page_metadata(url: str, timeout: float) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/json;q=0.8,*/*;q=0.1",
            "Range": f"bytes=0-{MAX_FETCH_BYTES - 1}",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        data = response.read(MAX_FETCH_BYTES)
        text = data.decode("utf-8", errors="replace")
        title_match = re.search(r"<title[^>]*>(.*?)</title>", text, re.I | re.S)
        title = " ".join(title_match.group(1).split()) if title_match else ""
        return {
            "http_status": getattr(response, "status", None),
            "content_type": response.headers.get("Content-Type", ""),
            "title": title,
        }


def fetch_source_metadata(source: dict[str, Any], timeout: float = 10.0) -> dict[str, Any]:
    url = source.get("url", "")
    metadata: dict[str, Any] = {"checked": True}
    try:
        api_url = github_api_url(str(url))
        if api_url:
            payload = fetch_json(api_url, timeout=timeout)
            metadata.update(
                {
                    "http_status": 200,
                    "github_full_name": payload.get("full_name", ""),
                    "github_description": payload.get("description", "") or "",
                    "github_stars": payload.get("stargazers_count", 0),
                    "github_forks": payload.get("forks_count", 0),
                    "github_pushed_at": payload.get("pushed_at", ""),
                    "github_license": (payload.get("license") or {}).get("spdx_id", ""),
                }
            )
            return metadata
        metadata.update(fetch_page_metadata(str(url), timeout=timeout))
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError) as exc:
        metadata.update({"error": exc.__class__.__name__, "error_detail": str(exc)[:180]})
    return metadata


def build_candidate(
    source: dict[str, Any],
    discovered_at: str,
    blocklist: dict[str, list[str]],
    fetch: bool = False,
) -> dict[str, Any]:
    metadata = fetch_source_metadata(source) if fetch else {"checked": False}
    summary = source.get("summary", "")
    if metadata.get("github_description"):
        summary = str(metadata["github_description"])
    elif metadata.get("title"):
        summary = str(metadata["title"])

    reasons = blocklist_reasons({**source, "summary": summary}, blocklist)
    candidate = {
        "id": source["id"],
        "name": redact_secret_text(source["name"]),
        "category": source["category"],
        "url": redact_secret_text(source["url"]),
        "kind": source["kind"],
        "official": source["official"],
        "source_status": source["source_status"],
        "license_hint": redact_secret_text(source["license_hint"]),
        "safety_note": redact_secret_text(source["safety_note"]),
        "summary": redact_secret_text(summary),
        "tags": source["tags"],
        "discovered_at": discovered_at,
        "metadata": metadata,
        "blocked": bool(reasons),
        "block_reasons": reasons,
    }
    if has_secret_looking_text(json.dumps(candidate, sort_keys=True)):
        candidate["blocked"] = True
        candidate.setdefault("block_reasons", []).append("secret-looking text redacted")
    return candidate


def load_candidate_file(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {
            "schema_version": 1,
            "generated_at": "1970-01-01T00:00:00Z",
            "candidates": [],
        }
    return json.loads(path.read_text(encoding="utf-8"))


def merge_candidates(
    existing: dict[str, Any],
    new_candidates: list[dict[str, Any]],
    generated_at: str,
) -> dict[str, Any]:
    by_id = {
        str(candidate.get("id")): candidate
        for candidate in existing.get("candidates", [])
        if isinstance(candidate, dict) and candidate.get("id")
    }
    for candidate in new_candidates:
        by_id[str(candidate["id"])] = candidate
    return {
        "schema_version": 1,
        "generated_at": f"{generated_at}T00:00:00Z",
        "candidates": sorted(by_id.values(), key=lambda item: (item.get("category", ""), item.get("id", ""))),
    }


def discover(
    sources_path: Path,
    blocklist_path: Path,
    candidates_path: Path,
    discovered_at: str,
    fetch: bool,
    max_sources: int,
) -> dict[str, Any]:
    sources = load_sources(sources_path)
    if max_sources > 0:
        sources = sources[:max_sources]
    blocklist = load_blocklist(blocklist_path)
    new_candidates = [
        build_candidate(source, discovered_at=discovered_at, blocklist=blocklist, fetch=fetch)
        for source in sources
    ]
    existing = load_candidate_file(candidates_path)
    return merge_candidates(existing, new_candidates, generated_at=discovered_at)


def write_candidates(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Discover public AI research guide candidates.")
    parser.add_argument("--sources", default=DEFAULT_SOURCES, type=Path)
    parser.add_argument("--blocklist", default=DEFAULT_BLOCKLIST, type=Path)
    parser.add_argument("--candidates", default=DEFAULT_CANDIDATES, type=Path)
    parser.add_argument("--date", default=utc_today())
    parser.add_argument("--fetch", action="store_true", help="Check public URLs with bounded network requests.")
    parser.add_argument("--dry-run", action="store_true", help="Print discovered candidates without writing files.")
    parser.add_argument("--max-sources", default=0, type=int, help="Limit sources for tests or manual dry runs.")
    args = parser.parse_args(argv)

    payload = discover(
        sources_path=args.sources,
        blocklist_path=args.blocklist,
        candidates_path=args.candidates,
        discovered_at=args.date,
        fetch=args.fetch,
        max_sources=args.max_sources,
    )
    if args.dry_run:
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0
    write_candidates(args.candidates, payload)
    print(f"Wrote {args.candidates} with {len(payload.get('candidates', []))} candidate(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
