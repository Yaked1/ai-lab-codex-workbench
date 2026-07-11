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

    def test_guides_render_clickable_video_thumbnails(self) -> None:
        expected_cards = {
            "docs/guides/current-models-and-interfaces.md": {
                "Y9Wz2PV404E",
                "tV5zXS78HzU",
            },
            "docs/guides/fable-vs-sol.md": {
                "Y9Wz2PV404E",
                "GrdEid8H6H4",
            },
            "docs/guides/live-audio-and-translation.md": {"QjuuTHJKxWI"},
        }

        for relative_path, video_ids in expected_cards.items():
            content = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            for video_id in video_ids:
                thumbnail = f"https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg"
                watch_url = f"https://www.youtube.com/watch?v={video_id}"
                self.assertIn(f"]({watch_url})", content, relative_path)
                self.assertIn(f"]({thumbnail})", content, relative_path)

    def test_every_reader_facing_model_file_has_image_and_video(self) -> None:
        expected_files = {
            "README.md",
            "docs/PLANS/current.md",
            "docs/PLANS/model-media-notes.md",
            "docs/guides/current-models-and-interfaces.md",
            "docs/guides/fable-vs-sol.md",
            "docs/guides/live-audio-and-translation.md",
            "docs/research/current-model-claim-ledger-2026-07-11.md",
            "docs/research/model-media-provenance-2026-07-11.md",
        }

        for relative_path in expected_files:
            content = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            self.assertIn("![", content, relative_path)
            self.assertIn("https://i.ytimg.com/vi/", content, relative_path)
            self.assertIn("https://www.youtube.com/watch?v=", content, relative_path)


if __name__ == "__main__":
    unittest.main()
