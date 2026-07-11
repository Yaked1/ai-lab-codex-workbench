"""Regression tests for the dated model-guide media set."""

from pathlib import Path
import unittest
import xml.etree.ElementTree as element_tree


REPO_ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = REPO_ROOT / "docs" / "assets" / "model-guides"


class ModelMediaTests(unittest.TestCase):
    """Keep visual assets local, accessible, and connected to their guides."""

    def test_expected_svg_assets_are_valid_and_accessible(self) -> None:
        expected = {
            "availability-map.svg",
            "aa-benchmark-comparison.svg",
            "live-architecture.svg",
        }

        self.assertEqual(expected, {path.name for path in ASSET_DIR.glob("*.svg")})
        for name in expected:
            root = element_tree.parse(ASSET_DIR / name).getroot()
            namespace = "{http://www.w3.org/2000/svg}"
            self.assertIsNotNone(root.find(f"{namespace}title"), name)
            self.assertIsNotNone(root.find(f"{namespace}desc"), name)

    def test_important_guides_embed_local_visuals(self) -> None:
        expected_links = {
            "docs/guides/current-models-and-interfaces.md": "../assets/model-guides/availability-map.svg",
            "docs/guides/fable-vs-sol.md": "../assets/model-guides/aa-benchmark-comparison.svg",
            "docs/guides/live-audio-and-translation.md": "../assets/model-guides/live-architecture.svg",
            "docs/research/current-model-claim-ledger-2026-07-11.md": "../assets/model-guides/aa-benchmark-comparison.svg",
        }

        for relative_path, link in expected_links.items():
            content = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            self.assertIn(f"]({link})", content, relative_path)

    def test_provenance_ledger_records_reuse_limits(self) -> None:
        ledger = (
            REPO_ROOT / "docs" / "research" / "model-media-provenance-2026-07-11.md"
        ).read_text(encoding="utf-8")

        self.assertIn("## Uncertainties", ledger)
        self.assertIn("Artificial Analysis Terms of Use", ledger)
        self.assertIn("screenshot permission not found", ledger)


if __name__ == "__main__":
    unittest.main()
