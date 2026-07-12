"""Regression tests for the model and effort prompting guide pack."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "docs" / "guides" / "model-prompting"

REQUIRED_FILES = (
    "README.md",
    "surface-and-effort-map.md",
    "sources-and-observations.md",
    "effort-evaluation-playbook.md",
    "gpt-5-6-sol-prompting.md",
    "gpt-5-6-terra-prompting.md",
    "gpt-5-6-luna-prompting.md",
    "claude-fable-5-prompting.md",
    "claude-opus-4-8-prompting.md",
    "grok-4-5-prompting.md",
    "muse-spark-1-1-prompting.md",
    "gemini-3-5-flash-prompting.md",
    "gpt-live-1-prompting.md",
    "gemini-live-translate-prompting.md",
    "gpt-image-2-prompting.md",
    "nano-banana-family-prompting.md",
    "gemini-omni-flash-prompting.md",
    "seedream-5-0-pro-prompting.md",
    "muse-image-video-prompting.md",
)

# Each guide must teach operational prompting, not only product marketing.
CORE_NEEDLES = (
    "Checked:",
    "```text",
    "Failure",
    "Verification",
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class ModelPromptingPackTests(unittest.TestCase):
    def test_required_files_exist(self):
        for name in REQUIRED_FILES:
            with self.subTest(name=name):
                path = PACK / name
                self.assertTrue(path.is_file(), f"missing {path}")
                self.assertTrue(read(path).endswith("\n"))

    def test_guides_have_operational_depth(self):
        for name in REQUIRED_FILES:
            if name in {"README.md", "sources-and-observations.md"}:
                continue
            text = read(PACK / name)
            with self.subTest(name=name):
                for needle in CORE_NEEDLES:
                    self.assertIn(needle, text, f"{name} missing {needle}")

    def test_surface_map_covers_user_effort_facts(self):
        text = read(PACK / "surface-and-effort-map.md")
        for needle in (
            "Light",
            "Ultra",
            "Plus",
            "Pro",
            "Business",
            "0.144.0",
            "0.144.1",
            "Extra High",
            "Ultracode",
            "July 12, 2026",
            "Grok 4.5",
            "Nano Banana Pro",
            "Muse Video",
            "Business",
            "observation",
        ):
            with self.subTest(needle=needle):
                self.assertIn(needle, text)

    def test_sol_guide_covers_all_efforts(self):
        text = read(PACK / "gpt-5-6-sol-prompting.md")
        for needle in (
            "Light / Low",
            "Medium",
            "High",
            "Extra High",
            "Max",
            "Ultra",
            "Plus web Work",
        ):
            with self.subTest(needle=needle):
                self.assertIn(needle, text)

    def test_luna_has_no_ultra_menu(self):
        text = read(PACK / "gpt-5-6-luna-prompting.md")
        self.assertIn("No Ultra", text)
        self.assertIn("local Codex Luna menu", text)

    def test_fable_cutoff_and_ultracode(self):
        text = read(PACK / "claude-fable-5-prompting.md")
        self.assertIn("2026-07-12 11:59:59 PM PT", text)
        self.assertIn("Ultracode", text)
        self.assertIn("2.1.170", text)
        self.assertIn("Extra", text)

    def test_grok_default_high(self):
        text = read(PACK / "grok-4-5-prompting.md")
        self.assertIn("High as the default", text)
        self.assertIn("Grok Build", text)

    def test_nano_banana_mapping(self):
        text = read(PACK / "nano-banana-family-prompting.md")
        self.assertIn("gemini-3-pro-image", text)
        self.assertIn("gemini-3.1-flash-image", text)
        self.assertIn("gemini-3.1-flash-lite-image", text)
        self.assertIn("Nano Banana 2 is not", text)

    def test_muse_video_unavailable(self):
        text = read(PACK / "muse-image-video-prompting.md")
        self.assertIn("coming soon", text)
        self.assertIn("Muse Video", text)
        self.assertIn("Muse Image launched", text)
        self.assertIn("Content Seal", text)

    def test_claude_guides_cover_adaptive_thinking(self):
        fable = read(PACK / "claude-fable-5-prompting.md")
        opus = read(PACK / "claude-opus-4-8-prompting.md")
        self.assertIn("adaptive thinking", fable)
        self.assertIn("Do not add `budget_tokens`", fable)
        self.assertIn("thinking: adaptive", opus)
        self.assertIn("64K", opus)

    def test_sources_ledger_separates_official_and_observed_claims(self):
        text = read(PACK / "sources-and-observations.md")
        self.assertIn("official launch says", text)
        self.assertIn("Business web Work shows Ultra", text)
        self.assertIn("does not establish universal Business eligibility", text)
        self.assertIn("0.144.1", text)

    def test_effort_eval_counts_orchestration_costs(self):
        text = read(PACK / "effort-evaluation-playbook.md")
        self.assertIn("Count all agents", text)
        self.assertIn("human correction", text)
        self.assertIn("frozen baseline prompt", text)

    def test_guide_depth_varies_with_surface_complexity(self):
        sol = len(read(PACK / "gpt-5-6-sol-prompting.md"))
        terra = len(read(PACK / "gpt-5-6-terra-prompting.md"))
        luna = len(read(PACK / "gpt-5-6-luna-prompting.md"))
        self.assertGreater(sol, terra)
        self.assertGreater(terra, luna)
        self.assertGreater(luna, 4000)

    def test_frontier_essay_now_covers_muse_media(self):
        essay = read(
            ROOT
            / "docs"
            / "guides"
            / "frontier-models-and-multimodal-systems-2026.md"
        )
        self.assertIn("### Muse Image and Muse Video", essay)
        self.assertIn("Content Seal", essay)
        self.assertIn("coming soon", essay)

    def test_index_links_every_guide(self):
        index = read(PACK / "README.md")
        for name in REQUIRED_FILES:
            if name == "README.md":
                continue
            with self.subTest(name=name):
                self.assertIn(name, index)

    def test_each_model_guide_links_source_ledger(self):
        exempt = {
            "README.md",
            "sources-and-observations.md",
            "effort-evaluation-playbook.md",
        }
        for name in REQUIRED_FILES:
            if name in exempt:
                continue
            with self.subTest(name=name):
                self.assertIn("sources-and-observations.md", read(PACK / name))

    def test_guides_readme_and_root_readme_link_pack(self):
        guides_readme = read(ROOT / "docs" / "guides" / "README.md")
        root_readme = read(ROOT / "README.md")
        self.assertIn("model-prompting/README.md", guides_readme)
        self.assertIn("docs/guides/model-prompting/README.md", root_readme)

    def test_frontier_essay_links_pack(self):
        essay = read(ROOT / "docs" / "guides" / "frontier-models-and-multimodal-systems-2026.md")
        self.assertIn("model-prompting/README.md", essay)
        self.assertIn("surface-and-effort-map.md", essay)

    def test_no_secret_looking_strings(self):
        import sys

        scripts = ROOT / "scripts"
        if str(scripts) not in sys.path:
            sys.path.insert(0, str(scripts))
        from discover_ai_sources import has_secret_looking_text

        for name in REQUIRED_FILES:
            text = read(PACK / name)
            with self.subTest(name=name):
                self.assertFalse(has_secret_looking_text(text))


if __name__ == "__main__":
    unittest.main()
