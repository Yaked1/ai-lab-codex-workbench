"""Lossless migration contracts for the frontier-model reference."""

from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
FRONTIER_MIGRATION_BOUNDARY = "<!-- frontier-migration-boundary -->"
GUIDES = ROOT / "docs" / "guides"
LEGACY = GUIDES / "frontier-models-and-multimodal-systems-2026.md"
MAP = GUIDES / "frontier-models-compatibility-map.json"


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
    """Parse the task's H1/H2/H3 source-node grammar without rewrapping."""
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
            if (level == 1 and later_level == 2) or (level == 2 and later_level in {2, 3}) or (level == 3 and later_level <= 3):
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


def load_map() -> dict[str, object]:
    return json.loads(MAP.read_text(encoding="utf-8"))


def destination_nodes(repo: Path, data: dict[str, object]) -> tuple[dict[tuple[str, str], dict[str, object]], list[tuple[str, dict[str, object]]]]:
    bridges = {
        (entry["path"], entry["anchor"])
        for entry in data["bridge_nodes"]
    }
    result: dict[tuple[str, str], dict[str, object]] = {}
    extras: list[tuple[str, dict[str, object]]] = []
    destination_paths = {entry["destination_path"] for entry in data["nodes"]}
    for relative in destination_paths:
        parsed = parse_nodes((repo / relative).read_text(encoding="utf-8"), relative)
        for node in parsed:
            key = (relative, node["anchor"])
            if key in bridges:
                continue
            if key in result:
                raise AssertionError(f"duplicate destination anchor: {relative}#{node['anchor']}")
            result[key] = node
    expected = {(entry["destination_path"], entry["destination_anchor"]) for entry in data["nodes"]}
    for key, node in result.items():
        if key not in expected:
            extras.append((key[0], node))
    return result, extras


def verify(data: dict[str, object], repo: Path = ROOT) -> None:
    nodes = data["nodes"]
    if len({entry["order"] for entry in nodes}) != len(nodes):
        raise AssertionError("duplicate source node order")
    if len({entry["anchor"] for entry in nodes}) != len(nodes):
        raise AssertionError("duplicate source anchor")
    counts: dict[str, int] = {}
    for entry in nodes:
        counts[entry["type"]] = counts.get(entry["type"], 0) + 1
    if counts != data["source_node_counts"]:
        raise AssertionError("source node count mismatch")
    destinations, extras = destination_nodes(repo, data)
    if extras:
        raise AssertionError(f"unapproved destination node: {extras[0][0]}#{extras[0][1]['anchor']}")
    reconstructed: list[str] = []
    for entry in sorted(nodes, key=lambda item: item["order"]):
        key = (entry["destination_path"], entry["destination_anchor"])
        node = destinations.get(key)
        if node is None:
            raise AssertionError(f"missing destination node: {key[0]}#{key[1]}")
        if node["content_sha256"] != entry["content_sha256"]:
            raise AssertionError(f"content hash mismatch: {key[0]}#{key[1]}")
        reconstructed.append(node["content"])
    reconstructed_text = "".join(reconstructed)
    if digest(reconstructed_text) != data["source_sha256"]:
        raise AssertionError("ordered reconstruction hash mismatch")
    fable = [entry for entry in nodes if entry.get("evidence_id") == "fable-access-july-19-2026"]
    if len(fable) != 1:
        raise AssertionError("canonical Fable node missing or duplicated")
    canonical = destinations[(fable[0]["destination_path"], fable[0]["destination_anchor"])]["content"]
    normalized_canonical = " ".join(canonical.split())
    if "July 19, 2026 at 11:59:59 PM PT" not in normalized_canonical or "support.claude.com" not in canonical:
        raise AssertionError("canonical Fable evidence changed")
    landing = (repo / data["legacy_path"]).read_text(encoding="utf-8")
    for stub in data["compatibility_stubs"]:
        marker = f'<a id="{stub["anchor"]}"></a>'
        if marker not in landing:
            raise AssertionError(f"missing compatibility anchor: {stub['anchor']}")


class FrontierMigrationTests(unittest.TestCase):
    def test_manifest_records_the_complete_pre_split_source(self) -> None:
        data = load_map()
        self.assertEqual({"h1": 1, "h2": 22, "h3": 124}, data["source_node_counts"])
        self.assertEqual(147, len(data["nodes"]))
        self.assertEqual(147, len(data["compatibility_stubs"]))
        self.assertRegex(data["source_sha256"], r"^[0-9a-f]{64}$")

    def test_landing_is_a_bounded_compatibility_index(self) -> None:
        text = LEGACY.read_text(encoding="utf-8")
        self.assertIn("## Subject pages", text)
        self.assertIn("## Compatibility anchors", text)
        self.assertIn("frontier-models-compatibility-map.json", text)
        self.assertLess(len(text.splitlines()), 800)

    def test_split_uses_six_bounded_subject_pages(self) -> None:
        data = load_map()
        destinations = sorted(
            {entry["destination_path"] for entry in data["nodes"] if entry["type"] != "h1"}
        )
        self.assertEqual(6, len(destinations))
        for relative in destinations:
            with self.subTest(relative=relative):
                path = ROOT / relative
                self.assertTrue(path.is_file())
                self.assertLess(len(path.read_text(encoding="utf-8").splitlines()), 2300)
    def test_map_reconstructs_every_source_node_in_order(self) -> None:
        verify(load_map())

    def test_compatibility_stubs_cover_every_old_anchor(self) -> None:
        data = load_map()
        self.assertEqual(len(data["nodes"]), len(data["compatibility_stubs"]))
        verify(data)

    def test_mutations_fail_closed(self) -> None:
        data = load_map()
        cases = []
        missing = deepcopy(data); missing["nodes"].pop(); cases.append((missing, "source node count mismatch"))
        duplicated = deepcopy(data); duplicated["nodes"].append(deepcopy(duplicated["nodes"][0])); cases.append((duplicated, "duplicate source node order"))
        no_fable = deepcopy(data); no_fable["nodes"] = [n for n in no_fable["nodes"] if n.get("evidence_id") != "fable-access-july-19-2026"]; cases.append((no_fable, "source node count mismatch"))
        for broken, message in cases:
            with self.subTest(message=message):
                with self.assertRaisesRegex(AssertionError, message):
                    verify(broken)


if __name__ == "__main__":
    unittest.main()
