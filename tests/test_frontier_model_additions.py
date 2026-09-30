"""Coverage contracts for the dated frontier-model additions supplement."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "docs" / "guides" / "frontier-model-additions-2026-09.md"
MODEL_LIST = ROOT / "docs" / "guides" / "frontier-model-list.md"


class FrontierModelAdditionsTests(unittest.TestCase):
    def test_current_hosted_families_are_documented_and_indexed(self) -> None:
        guide = GUIDE.read_text(encoding="utf-8")
        index = MODEL_LIST.read_text(encoding="utf-8")
        models = (
            "GPT-6 Astra",
            "GPT-6.1 Sol",
            "GPT-6 Luna",
            "Claude Fable 5.1",
            "Claude Opus 5.5",
            "Claude Sonnet 5.5",
            "Claude Haiku 4.5",
            "Gemini 3.8 Flash",
            "DeepSeek-V4.1-Flash",
            "GLM-5.3",
        )
        for model in models:
            with self.subTest(model=model):
                self.assertIn(model, guide)
                self.assertIn(model, index)

    def test_open_model_ecosystems_have_sources_and_operational_limits(self) -> None:
        text = GUIDE.read_text(encoding="utf-8")
        for model in (
            "gpt-oss-120b",
            "Llama 4 Scout",
            "Qwen3-235B-A22B",
            "Qwen3-Coder-480B-A35B-Instruct",
            "Mistral Large 3",
            "OLMo 3.1 Think 32B",
        ):
            with self.subTest(model=model):
                self.assertIn(model, text)
        for heading in (
            "## Scope and Evidence Rules",
            "## Selection by Workload",
            "## Evaluation and Deployment Checklist",
            "## Known Limits and Refresh Triggers",
            "## First-Party Source Index",
        ):
            self.assertIn(heading, text)
        self.assertGreaterEqual(text.count("https://"), 15)

    def test_superseded_index_entries_are_not_presented_as_current(self) -> None:
        index = MODEL_LIST.read_text(encoding="utf-8")
        self.assertIn("| GPT-5.6 Sol | Earlier hosted generation", index)
        self.assertIn("| Gemini 3.5 Flash | Legacy hosted generation", index)
        self.assertIn("| DeepSeek-V4-Flash | Retired", index)


if __name__ == "__main__":
    unittest.main()
