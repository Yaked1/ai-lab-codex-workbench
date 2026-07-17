"""Regression tests for the dated model-guide media set."""

from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as element_tree


REPO_ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = REPO_ROOT / "docs" / "assets" / "model-guides"
FRONTIER_SUBJECT_FILES = (
    "docs/guides/frontier-overview-and-selection.md",
    "docs/guides/frontier-openai-and-anthropic.md",
    "docs/guides/frontier-open-and-specialist-models.md",
    "docs/guides/frontier-evaluation-and-deployment.md",
    "docs/guides/frontier-google-and-media.md",
    "docs/guides/frontier-sources-and-method.md",
)

DEF_FRONTIER_LANDING = "docs/guides/frontier-models-and-multimodal-systems-2026.md"

def frontier_corpus() -> str:
    return "\n".join(
        (REPO_ROOT / relative).read_text(encoding="utf-8")
        for relative in (DEF_FRONTIER_LANDING, *FRONTIER_SUBJECT_FILES)
    )


READER_FACING_MODEL_FILES = {
    "README.md",
    "docs/PLANS/model-media-notes.md",
    "docs/guides/current-models-and-interfaces.md",
    "docs/guides/fable-vs-sol.md",
    "docs/guides/live-audio-and-translation.md",
    "docs/guides/frontier-openai-and-anthropic.md",
    "docs/guides/frontier-open-and-specialist-models.md",
    "docs/guides/frontier-google-and-media.md",
    "docs/research/current-model-claim-ledger-2026-07-11.md",
    "docs/research/model-media-provenance-2026-07-11.md",
}


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
            title = root.find(f"{namespace}title")
            description = root.find(f"{namespace}desc")
            self.assertIsNotNone(title, name)
            self.assertIsNotNone(description, name)
            self.assertTrue((title.text or "").strip(), name)
            self.assertTrue((description.text or "").strip(), name)

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

        essay = frontier_corpus()
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
            "docs/guides/frontier-openai-and-anthropic.md": {
                "xDXX2M5DrO0": "gpt-5-6-family-test",
            },
            "docs/guides/frontier-open-and-specialist-models.md": {
                "5J6HCDEkg64": "grok-4-5-test",
                "XCYYDhG9zKw": "muse-spark-test",
            },
            "docs/guides/frontier-google-and-media.md": {
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
        for relative_path in READER_FACING_MODEL_FILES:
            content = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            self.assertIn("![", content, relative_path)
            self.assertIn("https://i.ytimg.com/vi/", content, relative_path)
            self.assertIn(
                "https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#",
                content,
                relative_path,
            )

    def test_current_plan_is_not_a_reader_facing_media_fixture(self) -> None:
        self.assertNotIn("docs/PLANS/current.md", READER_FACING_MODEL_FILES)

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
        iframe_tags = re.findall(r"<iframe\b[^>]*>", page)
        self.assertEqual(11, len(iframe_tags))
        for iframe in iframe_tags:
            self.assertIn("youtube-nocookie.com", iframe)
            self.assertIn('loading="lazy"', iframe)
            self.assertRegex(iframe, r'title="[^"]+"')
            self.assertIn("allowfullscreen", iframe)

        html_ids = re.findall(r'\bid="([^"]+)"', page)
        self.assertEqual(len(html_ids), len(set(html_ids)))
        for video_id in expected_ids:
            self.assertIn(
                f"https://www.youtube-nocookie.com/embed/{video_id}", page
            )

    def test_video_research_pack_covers_requested_topics(self) -> None:
        pack_path = (
            REPO_ROOT
            / "docs"
            / "research"
            / "video-research-pack-2026-07-11.md"
        )
        self.assertTrue(pack_path.is_file())
        pack = pack_path.read_text(encoding="utf-8")

        required_headings = {
            "## GPT-5.6 Sol, Terra, and Luna launch",
            "## GPT-5.6 effort levels",
            "## Sol Ultra and parallel subagents",
            "## GPT-5.6 in Desktop Codex",
            "## GPT-5.6 in ChatGPT Work",
            "## ChatGPT Work versus Codex",
            "## GPT-5.6 plan availability",
            "## Claude Fable 5 subscription transition",
            "## Claude Opus 4.8",
            "## Grok 4.5",
            "## Grok Build",
            "## Meta Muse Spark 1.1",
            "## Artificial Analysis Intelligence Index",
            "## Artificial Analysis Coding Agent Index",
            "## GPT-Live-1",
            "## GPT-Live-1 Mini",
            "## Gemini 3.5 Flash Live Translate",
            "## Gemini 3.5 Flash",
            "## Gemini Omni Flash",
            "## GPT Image 2",
            "## Nano Banana 2",
            "## Nano Banana Pro",
            "## Nano Banana 2 Lite",
            "## Seedream 5.0 Pro",
            "## Combined frontier-model comparisons",
            "## Combined image-model comparisons",
            "## Google I/O 2026 coverage",
            "## Live voice and translation comparisons",
            "## Video-evaluation checklist",
        }
        for heading in required_headings:
            self.assertIn(heading, pack)

        for query in {
            "Gemini+Omni+Flash+official+demo",
            "Gemini+Omni+Flash+full+test",
            "Gemini+Omni+Flash+vs+Veo",
            "Google+I%2FO+2026+Gemini+Omni+keynote",
        }:
            self.assertIn(query, pack)

    def test_research_pack_is_linked_from_essay_and_provenance(self) -> None:
        link = "video-research-pack-2026-07-11.md"
        essay = frontier_corpus()
        provenance = (
            REPO_ROOT
            / "docs"
            / "research"
            / "model-media-provenance-2026-07-11.md"
        ).read_text(encoding="utf-8")
        self.assertIn(link, essay)
        self.assertIn(link, provenance)

    def test_benchmark_and_model_names_are_not_conflated(self) -> None:
        essay = frontier_corpus()
        pack = (
            REPO_ROOT
            / "docs"
            / "research"
            / "video-research-pack-2026-07-11.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Artificial Analysis Coding Agent Index", pack)
        self.assertNotIn("## Artificial Analysis Codex Index", pack)
        self.assertIn("Nano Banana 2 is not Gemini 3 Pro Image", essay)
        self.assertIn("Nano Banana Pro is Gemini 3 Pro Image", essay)
        for model_id in {
            "gemini-3.1-flash-lite-image",
            "gemini-3.1-flash-image",
            "gemini-3-pro-image",
            "gemini-2.5-flash-image",
        }:
            self.assertIn(model_id, essay)

    def test_image_comparison_is_not_classified_as_omni_video(self) -> None:
        page = (REPO_ROOT / "docs" / "site" / "model-media.html").read_text(
            encoding="utf-8"
        )
        card_match = re.search(
            r'<article class="video-card" id="image-model-comparison">'
            r'.*?FDhx79PU5KQ.*?</article>',
            page,
            flags=re.DOTALL,
        )
        self.assertIsNotNone(card_match)
        card = card_match.group(0)
        self.assertIn("image-generation test", card)
        self.assertIn("not a Gemini Omni Flash demonstration", card)

        pack = (
            REPO_ROOT
            / "docs"
            / "research"
            / "video-research-pack-2026-07-11.md"
        ).read_text(encoding="utf-8")
        self.assertIn(
            "`FDhx79PU5KQ` belongs only to this image-model comparison", pack
        )

    def test_frontier_essay_keeps_product_and_benchmark_corrections(self) -> None:
        essay = frontier_corpus()

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

        self.assertIn('current product label is **Low**, not "Light."', essay)
        self.assertIn("Nano Banana 2 is not Gemini 3 Pro Image", essay)
        self.assertRegex(essay, r"tested\s+GPT-5\.6 Sol Max in Codex")
        self.assertRegex(
            essay, r"No independent\s+Sol Ultra Coding Agent Index result"
        )
        self.assertIn("fully autoregressive", essay)
        self.assertIn("**unconfirmed**", essay)
        self.assertIn("July 19, 2026 at 11:59:59 PM", essay)
        self.assertIn("50% increase to Claude Code weekly usage limits", essay)
        self.assertIn("promotional condition", essay)


if __name__ == "__main__":
    unittest.main()
