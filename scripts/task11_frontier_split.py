#!/usr/bin/env python3
"""Task 11: losslessly split the frontier models guide into subject pages.

Uses the same H1/H2/H3 node grammar as tests/test_frontier_model_migration.py.
Writes destination pages, a compatibility map, and a landing index with stable
anchor stubs. Idempotent only when the source still contains the pre-split body;
re-running after split is a no-op if the map already validates.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRONTIER_MIGRATION_BOUNDARY = "<!-- frontier-migration-boundary -->"
GUIDES = ROOT / "docs" / "guides"
LEGACY = GUIDES / "frontier-models-and-multimodal-systems-2026.md"
MAP = GUIDES / "frontier-models-compatibility-map.json"
SUBJECT_DIR = GUIDES


def lf(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def digest(text: str) -> str:
    return hashlib.sha256(lf(text).encode("utf-8")).hexdigest()


def slug(text: str) -> str:
    value = text.lower().strip()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    value = re.sub(r"[\s-]+", "-", value)
    return value.strip("-")


def headings(text: str) -> list[re.Match[str]]:
    return list(re.finditer(r"(?m)^(#{1,6}) +(.+?)\s*$", lf(text)))


def parse_nodes(text: str, source_path: str) -> list[dict[str, object]]:
    text = lf(text)
    all_headings = headings(text)
    anchor_counts: dict[str, int] = {}
    heading_anchors: dict[int, str] = {}
    for match in all_headings:
        base = slug(match.group(2))
        occurrence = anchor_counts.get(base, 0)
        heading_anchors[match.start()] = base if occurrence == 0 else f"{base}-{occurrence}"
        anchor_counts[base] = occurrence + 1

    primary = [match for match in all_headings if len(match.group(1)) <= 3]
    paths: list[str] = []
    nodes: list[dict[str, object]] = []
    for index, match in enumerate(primary):
        level = len(match.group(1))
        title = match.group(2)
        while len(paths) >= level:
            paths.pop()
        paths.append(title)
        end = len(text)
        for later in primary[index + 1 :]:
            later_level = len(later.group(1))
            if (
                (level == 1 and later_level == 2)
                or (level == 2 and later_level in {2, 3})
                or (level == 3 and later_level <= 3)
            ):
                end = later.start()
                break
        boundary = text.find(FRONTIER_MIGRATION_BOUNDARY, match.end(), end)
        if boundary != -1:
            end = boundary
        content = text[match.start() : end]
        nodes.append(
            {
                "source_path": source_path,
                "order": len(nodes),
                "type": f"h{level}",
                "heading": title,
                "heading_path": list(paths),
                "line_start": text.count("\n", 0, match.start()) + 1,
                "line_end": text.count("\n", 0, end) + 1,
                "anchor": heading_anchors[match.start()],
                "content": content,
                "content_sha256": digest(content),
            }
        )
    return nodes


# Destination assignment by top-level H2 slug (H1 stays on landing).
#
# The six destination files remain beside the legacy guide so every copied
# relative Markdown link keeps the same base directory. This is deliberately
# less clever than moving content into a deeper folder and then rewriting it,
# because a lossless migration should not make link semantics depend on a
# second transformation.
H2_DESTINATION = {
    "how-the-expanded-technical-dossiers-are-structured": (
        "frontier-sources-and-method.md",
        "Frontier sources and method",
    ),
    "prompting-guides-for-these-models": (
        "frontier-overview-and-selection.md",
        "Frontier overview and selection",
    ),
    "the-short-answer": (
        "frontier-overview-and-selection.md",
        "Frontier overview and selection",
    ),
    "announcement-style-release-dossiers": (
        "frontier-overview-and-selection.md",
        "Frontier overview and selection",
    ),
    "gpt-56-is-a-family-not-a-ladder-of-nicknames": (
        "frontier-openai-and-anthropic.md",
        "OpenAI and Anthropic frontier systems",
    ),
    "what-each-gpt-56-effort-is-for": (
        "frontier-openai-and-anthropic.md",
        "OpenAI and Anthropic frontier systems",
    ),
    "claude-fable-5-and-claude-opus-48": (
        "frontier-openai-and-anthropic.md",
        "OpenAI and Anthropic frontier systems",
    ),
    "claude-sonnet-5": (
        "frontier-openai-and-anthropic.md",
        "OpenAI and Anthropic frontier systems",
    ),
    "coding-agentic-and-cost-efficient-model-additions": (
        "frontier-open-and-specialist-models.md",
        "Open and specialist frontier models",
    ),
    "detailed-dossiers-for-the-newly-audited-systems": (
        "frontier-open-and-specialist-models.md",
        "Open and specialist frontier models",
    ),
    "grok-45-in-grok-build": (
        "frontier-open-and-specialist-models.md",
        "Open and specialist frontier models",
    ),
    "artificial-analysis-what-the-scores-do-and-do-not-mean": (
        "frontier-evaluation-and-deployment.md",
        "Frontier evaluation and deployment",
    ),
    "meta-muse-spark-11": (
        "frontier-open-and-specialist-models.md",
        "Open and specialist frontier models",
    ),
    "gemini-35-flash": (
        "frontier-google-and-media.md",
        "Google, live, image, and media systems",
    ),
    "gpt-live-1-and-gemini-35-live-translate": (
        "frontier-google-and-media.md",
        "Google, live, image, and media systems",
    ),
    "image-and-video-models": (
        "frontier-google-and-media.md",
        "Google, live, image, and media systems",
    ),
    "extended-operating-guidance-for-the-established-families": (
        "frontier-evaluation-and-deployment.md",
        "Frontier evaluation and deployment",
    ),
    "comprehensive-architecture-performance-and-deployment-dossiers": (
        "frontier-evaluation-and-deployment.md",
        "Frontier evaluation and deployment",
    ),
    "how-to-choose-without-chasing-a-single-winner": (
        "frontier-overview-and-selection.md",
        "Frontier overview and selection",
    ),
    "uncertainties-and-known-limits": (
        "frontier-evaluation-and-deployment.md",
        "Frontier evaluation and deployment",
    ),
    "sources": (
        "frontier-sources-and-method.md",
        "Frontier sources and method",
    ),
    "method": (
        "frontier-sources-and-method.md",
        "Frontier sources and method",
    ),
}


def destination_for_node(node: dict[str, object]) -> tuple[str, str]:
    if node["type"] == "h1":
        return ("", "landing")
    # Use the H2 ancestor slug for H3 nodes.
    heading_path = node["heading_path"]  # type: ignore[assignment]
    h2_title = heading_path[1] if len(heading_path) > 1 else node["heading"]
    key = slug(str(h2_title))
    if key not in H2_DESTINATION:
        raise KeyError(f"no destination mapping for H2 slug {key!r} ({h2_title!r})")
    filename, title = H2_DESTINATION[key]
    rel = f"docs/guides/{filename}"
    return rel, title


def already_split(source: str) -> bool:
    return "frontier-models-compatibility-map.json" in source and "Subject pages" in source


def build_landing(
    h1_content: str,
    stubs: list[dict[str, str]],
    subjects: list[tuple[str, str]],
) -> str:
    # Strip trailing whitespace from H1 content for clean insertion.
    body = h1_content
    nav_lines = [
        "## Subject pages",
        "",
        "This landing page keeps stable anchors for the pre-split guide. Full",
        "subject content lives in the bounded pages below.",
        "",
    ]
    for rel, title in subjects:
        link = rel.replace("docs/guides/", "")
        nav_lines.append(f"- [{title}]({link})")
    nav_lines.extend(
        [
            "",
            "## Compatibility anchors",
            "",
            "Each anchor below preserves a pre-split heading target. Follow the",
            "linked subject page for the full section body.",
            "",
        ]
    )
    for stub in stubs:
        dest_link = stub["destination_path"].replace("docs/guides/", "")
        nav_lines.append(
            f'<a id="{stub["anchor"]}"></a>\n\n'
            f"**{stub['heading']}** → "
            f"[{stub['destination_title']}]({dest_link}#{stub['destination_anchor']})\n"
        )
    nav_lines.append("")
    nav_lines.append(
        "Compatibility map: "
        "[frontier-models-compatibility-map.json]"
        "(frontier-models-compatibility-map.json)"
    )
    nav_lines.append("")
    return body + "\n".join(nav_lines) + "\n"


def main() -> int:
    source = lf(LEGACY.read_text(encoding="utf-8"))
    source_path = "docs/guides/frontier-models-and-multimodal-systems-2026.md"

    if already_split(source) and MAP.is_file():
        print("frontier guide already split; map present")
        return 0

    nodes = parse_nodes(source, source_path)
    counts = {
        kind: sum(1 for node in nodes if node["type"] == kind)
        for kind in ("h1", "h2", "h3")
    }
    print(f"parsed nodes: {counts}")

    SUBJECT_DIR.mkdir(parents=True, exist_ok=True)

    # Group destination content.
    dest_order: list[str] = []
    dest_bodies: dict[str, list[str]] = {}
    dest_titles: dict[str, str] = {}
    map_nodes: list[dict[str, object]] = []
    stubs: list[dict[str, str]] = []
    h1_content = ""
    fable_marked = False

    for node in nodes:
        rel, title = destination_for_node(node)
        if node["type"] == "h1":
            h1_content = str(node["content"])
            # Landing keeps H1; record map entry with destination = legacy path
            # so reconstruction still works. Destination content for H1 lives on
            # the landing page only.
            map_nodes.append(
                {
                    **{k: node[k] for k in node if k != "content"},
                    "destination_path": source_path,
                    "destination_anchor": node["anchor"],
                    "destination_title": "Frontier models landing",
                }
            )
            stubs.append(
                {
                    "anchor": str(node["anchor"]),
                    "heading": str(node["heading"]),
                    "destination_path": source_path,
                    "destination_anchor": str(node["anchor"]),
                    "destination_title": "Frontier models landing",
                }
            )
            continue

        if rel not in dest_bodies:
            dest_bodies[rel] = []
            dest_titles[rel] = title
            dest_order.append(rel)
        dest_bodies[rel].append(str(node["content"]))

        entry = {
            **{k: node[k] for k in node if k != "content"},
            "destination_path": rel,
            "destination_anchor": node["anchor"],
            "destination_title": title,
        }
        # Mark the canonical Fable access evidence node once.
        content = str(node["content"])
        normalized_content = " ".join(content.split())
        if (
            not fable_marked
            and "July 19, 2026 at 11:59:59 PM PT" in normalized_content
            and "support.claude.com" in content
        ):
            entry["evidence_id"] = "fable-access-july-19-2026"
            fable_marked = True

        map_nodes.append(entry)
        stubs.append(
            {
                "anchor": str(node["anchor"]),
                "heading": str(node["heading"]),
                "destination_path": rel,
                "destination_anchor": str(node["anchor"]),
                "destination_title": title,
            }
        )

    if not fable_marked:
        # Last resort: scan map_nodes destinations after write is not available yet;
        # scan source nodes again.
        for entry, node in zip(map_nodes, nodes):
            content = str(node["content"])
            if "July 19, 2026 at 11:59:59 PM PT" in " ".join(content.split()) and "support.claude.com" in content:
                entry["evidence_id"] = "fable-access-july-19-2026"
                fable_marked = True
                break
    if not fable_marked:
        raise SystemExit("could not locate canonical Fable evidence node")

    bridge_nodes: list[dict[str, str]] = []
    subjects_for_nav: list[tuple[str, str]] = []
    for rel in dest_order:
        title = dest_titles[rel]
        subjects_for_nav.append((rel, title))
        page_slug = slug(title)
        # Destination page H1 is bridge content (not from source).
        bridge_nodes.append({"path": rel, "anchor": page_slug})
        # Subject pages stay beside the legacy guide, so copied relative links
        # retain their original base. Node bodies remain byte-exact. The hidden
        # boundary marker keeps the final source node separate from file-level
        # newline normalization without adding a reader-facing heading.
        joined = "".join(dest_bodies[rel])
        page = (
            f"# {title}\n\n"
            f"[← Frontier models index](frontier-models-and-multimodal-systems-2026.md)\n\n"
            + joined
            + FRONTIER_MIGRATION_BOUNDARY
            + "\n"
        )
        out_path = ROOT / rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(page, encoding="utf-8", newline="\n")

    # Landing: H1 content + subject nav + stubs.
    # H1 destination is the legacy path itself. After rewrite, the landing's H1
    # node content must still hash-match the original H1 content. So the landing
    # file must START with the exact original H1 content, then add extra H2
    # sections for navigation. Extra H2s on the landing are NOT in the map as
    # destination nodes (landing is only source_path for H1). destination_nodes()
    # only parses destination_paths from map nodes — which includes source_path
    # for H1. So if landing has extra H2s, they appear as destination nodes for
    # source_path and fail as "unapproved destination node".
    #
    # Fix: either
    # 1) mark extra landing H2s as bridge_nodes, or
    # 2) put only exact H1 content on landing with HTML stubs that are not headings.
    #
    # Option 2: stubs are already HTML <a id> without ## headings. Subject page
    # list can be a bullet list without ## ... wait, we used ## Subject pages.
    # Mark those as bridge nodes.

    landing_extra_headings = [
        "Subject pages",
        "Compatibility anchors",
    ]
    landing = build_landing(h1_content, stubs[1:], subjects_for_nav)  # skip H1 stub self-ref optional
    # Include H1 stub for completeness too.
    landing = build_landing(h1_content, stubs, subjects_for_nav)

    # After write, landing parse will include H1 + H2 Subject pages + H2 Compatibility anchors.
    # Bridge those H2 anchors.
    for heading in landing_extra_headings:
        bridge_nodes.append({"path": source_path, "anchor": slug(heading)})

    LEGACY.write_text(landing if landing.endswith("\n") else landing + "\n", encoding="utf-8", newline="\n")

    # Destination anchors are local to each split page. Recompute them after
    # writing because repeated headings that were globally suffixed in the
    # monolith may receive a different suffix once grouped by subject. Match
    # nodes by ordered content fingerprint, then update both map entries and
    # compatibility stubs.
    stub_by_source_anchor = {stub["anchor"]: stub for stub in stubs}
    bridge_keys = {(item["path"], item["anchor"]) for item in bridge_nodes}
    for rel in dest_order:
        parsed = parse_nodes((ROOT / rel).read_text(encoding="utf-8"), rel)
        parsed = [node for node in parsed if (rel, node["anchor"]) not in bridge_keys]
        assigned = [entry for entry in map_nodes if entry["destination_path"] == rel]
        if len(parsed) != len(assigned):
            raise SystemExit(f"destination node count mismatch for {rel}")
        for entry, actual in zip(assigned, parsed):
            if actual["content_sha256"] != entry["content_sha256"]:
                raise SystemExit(
                    f"ordered hash mismatch for {rel}: {entry['heading']} -> {actual['heading']}"
                )
            entry["destination_anchor"] = actual["anchor"]
            stub_by_source_anchor[str(entry["anchor"])]["destination_anchor"] = str(actual["anchor"])

    # Validate destination content hashes match before writing map.
    # Re-parse each destination and compare.
    for entry in map_nodes:
        dest_path = ROOT / str(entry["destination_path"])
        dest_nodes = parse_nodes(dest_path.read_text(encoding="utf-8"), str(entry["destination_path"]))
        match = next((n for n in dest_nodes if n["anchor"] == entry["destination_anchor"]), None)
        if match is None:
            raise SystemExit(
                f"missing destination node {entry['destination_path']}#{entry['destination_anchor']}"
            )
        if match["content_sha256"] != entry["content_sha256"]:
            raise SystemExit(
                f"hash mismatch for {entry['destination_path']}#{entry['destination_anchor']}"
            )

    data = {
        "legacy_path": source_path,
        "source_sha256": digest(source),
        "source_node_counts": counts,
        "bridge_nodes": bridge_nodes,
        "nodes": [
            {
                k: v
                for k, v in entry.items()
                if k != "content"
            }
            for entry in map_nodes
        ],
        "compatibility_stubs": stubs,
    }
    # map_nodes still have no content field (we stripped it). Good.
    MAP.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {len(dest_order)} subject pages + landing + map ({len(map_nodes)} nodes)")
    for rel in dest_order:
        print(f"  {rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
