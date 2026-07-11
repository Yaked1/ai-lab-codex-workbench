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
            "aa-frontier-benchmark-2026-07-11.svg",
            "gpt-5-6-effort-surfaces.svg",
            "live-architecture.svg",
            "multimodal-model-map-2026.svg",
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

        essay = (
            REPO_ROOT
            / "docs"
            / "guides"
            / "frontier-models-and-multimodal-systems-2026.md"
        ).read_text(encoding="utf-8")
        for link in {
            "../assets/model-guides/gpt-5-6-effort-surfaces.svg",
            "../assets/model-guides/aa-frontier-benchmark-2026-07-11.svg",
            "../assets/model-guides/multimodal-model-map-2026.svg",
        }:
            self.assertIn(f"]({link})", essay)

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
                "Y9Wz2PV404E": "fable-official",
                "tV5zXS78HzU": "gpt-sol-explainer",
            },
            "docs/guides/fable-vs-sol.md": {
                "Y9Wz2PV404E": "fable-official",
                "GrdEid8H6H4": "fable-hands-on",
            },
            "docs/guides/live-audio-and-translation.md": {
                "QjuuTHJKxWI": "launch-discussion"
            },
            "docs/guides/frontier-models-and-multimodal-systems-2026.md": {
                "xDXX2M5DrO0": "gpt-5-6-family-test",
                "5J6HCDEkg64": "grok-4-5-test",
                "XCYYDhG9zKw": "muse-spark-test",
                "TdN-YdFLWvY": "gemini-3-5-flash-test",
                "FDhx79PU5KQ": "image-model-comparison",
                "sWkGomJ3TLI": "gpt-image-2-official",
                "EAN5Cj347PY": "gpt-live-official",
            },
        }

        page_url = (
            "https://yaked1.github.io/ai-lab-codex-workbench/"
            "site/model-media.html"
        )
        for relative_path, cards in expected_cards.items():
            content = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            for video_id, anchor in cards.items():
                thumbnail = f"https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg"
                self.assertIn(f"]({thumbnail})", content, relative_path)
                self.assertIn(f"]({page_url}#{anchor})", content, relative_path)

    def test_every_reader_facing_model_file_has_image_and_video(self) -> None:
        expected_files = {
            "README.md",
            "docs/PLANS/current.md",
            "docs/PLANS/model-media-notes.md",
            "docs/guides/current-models-and-interfaces.md",
            "docs/guides/fable-vs-sol.md",
            "docs/guides/live-audio-and-translation.md",
            "docs/guides/frontier-models-and-multimodal-systems-2026.md",
            "docs/research/current-model-claim-ledger-2026-07-11.md",
            "docs/research/model-media-provenance-2026-07-11.md",
        }

        for relative_path in expected_files:
            content = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            self.assertIn("![", content, relative_path)
            self.assertIn("https://i.ytimg.com/vi/", content, relative_path)
            self.assertIn(
                "https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#",
                content,
                relative_path,
            )

    def test_embedded_media_page_uses_privacy_enhanced_players(self) -> None:
        page = (REPO_ROOT / "docs" / "site" / "model-media.html").read_text(
            encoding="utf-8"
        )
        expected_ids = {
            "Y9Wz2PV404E",
            "GrdEid8H6H4",
            "tV5zXS78HzU",
            "QjuuTHJKxWI",
            "xDXX2M5DrO0",
            "TdN-YdFLWvY",
            "5J6HCDEkg64",
            "XCYYDhG9zKw",
            "FDhx79PU5KQ",
            "sWkGomJ3TLI",
            "EAN5Cj347PY",
        }

        self.assertEqual(11, page.count("<iframe"))
        self.assertEqual(11, page.count("allowfullscreen"))
        for video_id in expected_ids:
            self.assertIn(
                f"https://www.youtube-nocookie.com/embed/{video_id}", page
            )

    def test_frontier_essay_keeps_product_and_benchmark_corrections(self) -> None:
        essay = (
            REPO_ROOT
            / "docs"
            / "guides"
            / "frontier-models-and-multimodal-systems-2026.md"
        ).read_text(encoding="utf-8")

        expected_sections = {
            "## GPT-5.6 Is a Family, Not a Ladder of Nicknames",
            "## Claude Fable 5 and Claude Opus 4.8",
            "## Grok 4.5 in Grok Build",
            "## Artificial Analysis: What the Scores Do and Do Not Mean",
            "## Meta Muse Spark 1.1",
            "## Gemini 3.5 Flash",
            "## GPT-Live-1 and Gemini 3.5 Live Translate",
            "## Image and Video Models",
            "## Uncertainties and Known Limits",
            "## Sources",
            "## Method",
        }
        for heading in expected_sections:
            self.assertIn(heading, essay)

        self.assertIn("current label is `low`, not “light.”", essay)
        self.assertIn("Nano Banana 2 is not Gemini 3 Pro Image", essay)
        self.assertIn("tested Sol Max, not Sol Ultra", essay)
        self.assertIn("fully autoregressive", essay)
        self.assertIn("**unconfirmed**", essay)
        self.assertIn("July 12, 2026 at 11:59:59 PM Pacific Time", essay)


if __name__ == "__main__":
    unittest.main()
