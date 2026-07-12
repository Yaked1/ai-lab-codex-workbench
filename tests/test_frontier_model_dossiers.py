"""Structural regression tests for the expanded frontier-model guide."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "docs" / "guides" / "frontier-models-and-multimodal-systems-2026.md"


def guide_text() -> str:
    return GUIDE.read_text(encoding="utf-8")


def announcement_dossiers(text: str) -> dict[str, str]:
    start = text.index("## Announcement-Style Release Dossiers")
    end = text.index("## GPT-5.6 Is a Family", start)
    block = text[start:end]
    matches = list(re.finditer(r"(?m)^### (.+)$", block))
    dossiers: dict[str, str] = {}
    for index, match in enumerate(matches):
        title = match.group(1)
        if title == "How to read each release dossier":
            continue
        section_end = matches[index + 1].start() if index + 1 < len(matches) else len(block)
        dossiers[title] = block[match.start():section_end]
    return dossiers


class FrontierModelDossierTests(unittest.TestCase):
    """Keep broad model coverage deep and evidence-conscious."""

    def test_every_announcement_dossier_uses_the_full_schema(self) -> None:
        dossiers = announcement_dossiers(guide_text())
        self.assertGreaterEqual(len(dossiers), 40)
        required_subsections = (
            "#### Launch story",
            "#### Capabilities and product behavior",
            "#### Benchmarks, results, and what they actually establish",
            "#### Deployment and evaluation consequences",
            "#### Limits, unknowns, and misleading shortcuts to avoid",
            "#### Practical verdict",
        )
        for title, dossier in dossiers.items():
            with self.subTest(title=title):
                self.assertGreaterEqual(len(dossier.split()), 200)
                self.assertIn("| Release field | Evidence-conscious record |", dossier)
                for subsection in required_subsections:
                    self.assertIn(subsection, dossier)

    def test_guide_has_a_large_cross_model_technical_reference(self) -> None:
        text = guide_text()
        self.assertGreaterEqual(len(text.split()), 35_000)
        for heading in (
            "## Comprehensive Architecture, Performance, and Deployment Dossiers",
            "### Open-Weight Quantization and Deployment Reference",
            "### Model-Guide Completeness Matrix",
            "## Uncertainties and Known Limits",
            "## Sources",
        ):
            self.assertIn(heading, text)

    def test_open_weight_models_retain_exact_architecture_fields(self) -> None:
        text = guide_text()
        required_facts = {
            "DeepSeek V4": (
                "1.6T / 49B per token",
                "384 routed experts plus one shared expert",
                "| Transformer layers | 61 |",
                "expert weights FP4 and most other weights FP8",
                "865 GB across 64 Safetensors shards",
                "160 GB across 46 Safetensors shards",
            ),
            "GLM-5.2": (
                "78 transformer layers",
                "256 routed experts plus one shared expert",
                "1,048,576 positions",
                "router computation declared FP32",
            ),
            "Mistral Small 4": (
                "36 layers, hidden size 4,096",
                "128 routed experts plus one shared expert",
                "NVFP4",
                "Hugging Face tree reports roughly 242 GB total",
            ),
            "Mistral Medium 3.5": (
                "| Text layers | 88 |",
                "| Attention heads | 96 |",
                "| KV heads | 8, a grouped-query attention layout |",
                "YaRN-style extension",
                "Vision tower | Pixtral-family encoder, 48 layers",
                "first-party Hugging Face tree reports **267 GB**",
            ),
            "Leanstral 1.5": (
                "119B total",
                "128 experts with 4 routed experts active",
                "Exact Lean version",
                "Final `.lean` file",
                "first-party repository is **121 GB**",
            ),
            "Gemma 4": (
                "128 experts / top 8",
                "Per-Layer Embeddings",
                "Q4_0",
                "Hybrid attention pattern",
            ),
            "DiffusionGemma": (
                "25.2B / 3.8B",
                "Canvas length",
                "256 tokens",
                "Blockwise Discrete Diffusion",
                "51.7 GB across 11 Safetensors shards",
            ),
        }
        for model, facts in required_facts.items():
            for fact in facts:
                with self.subTest(model=model, fact=fact):
                    self.assertIn(fact, text)

    def test_closed_models_do_not_receive_invented_checkpoint_specs(self) -> None:
        text = guide_text()
        for model in (
            "GPT-5.6 Sol",
            "Claude Fable 5",
            "Claude Opus 4.8",
            "Claude Sonnet 5",
            "Grok 4.5",
            "Gemini 3.5 Flash",
            "GPT Image 2",
        ):
            pattern = re.compile(
                rf"(?m)^### {re.escape(model)}[^\n]*\n(?P<body>.*?)(?=^### |^## )",
                re.DOTALL,
            )
            match = pattern.search(text)
            self.assertIsNotNone(match, model)
            body = match.group("body")
            self.assertRegex(body, r"(?i)undisclosed|closed")


if __name__ == "__main__":
    unittest.main()
