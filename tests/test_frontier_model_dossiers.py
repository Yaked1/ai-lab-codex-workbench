"""Structural regression tests for the expanded frontier-model guide."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
GUIDES = ROOT / "docs" / "guides"
GUIDE = GUIDES / "frontier-overview-and-selection.md"
FRONTIER_PAGES = (
    "frontier-overview-and-selection.md",
    "frontier-openai-and-anthropic.md",
    "frontier-google-and-media.md",
    "frontier-open-and-specialist-models.md",
    "frontier-evaluation-and-deployment.md",
    "frontier-sources-and-method.md",
)

CORE_DOSSIER_PREFIXES = {
    "GPT-5.6 Sol",
    "Claude Fable 5",
    "DeepSeek-V4-Pro",
    "Mistral Small 4",
    "Gemma 4 12B",
    "Gemini 3.5 Flash",
    "GPT-Live-1",
    "GPT Image 2",
    "Veo 3.1 Lite Preview",
    "Gemini Robotics-ER 1.6",
}

EPISTEMIC_BOUNDARY_PATTERN = re.compile(
    r"(?i)\b(?:undisclosed|(?:does|do) not disclose|not disclosed|"
    r"(?:does|do) not publish|not published|no public|unknown|"
    r"does not (?:by itself )?establish|not established|not inferred|"
    r"does not imply|"
    r"(?:does|do) not guarantee|not guaranteed|(?:does|do) not support|"
    r"unsupported|explicit constraint|failure (?:mode|case|boundary)|cannot prove|does not prove|"
    r"areas to verify|remain incomplete|require explicit current documentation|"
    r"not evidence|not identical|unless documented|should not be used to promise|"
    r"trade \w+ for)\b"
)


def guide_text() -> str:
    return "\n".join((GUIDES / name).read_text(encoding="utf-8") for name in FRONTIER_PAGES)


def announcement_dossiers(text: str) -> dict[str, str]:
    overview = GUIDE.read_text(encoding="utf-8")
    start = overview.index("## Announcement-Style Release Dossiers")
    end = overview.index("## How to Choose Without Chasing a Single Winner", start)
    block = overview[start:end]
    matches = list(re.finditer(r"(?m)^### (.+)$", block))
    dossiers: dict[str, str] = {}
    for index, match in enumerate(matches):
        title = match.group(1)
        if title == "How to read each release dossier":
            continue
        section_end = matches[index + 1].start() if index + 1 < len(matches) else len(block)
        dossiers[title] = block[match.start():section_end]
    return dossiers


def dossier_subsection(dossier: str, heading: str) -> str:
    start_match = re.search(rf"(?m)^{re.escape(heading)}\s*$", dossier)
    if start_match is None:
        raise AssertionError(f"missing subsection {heading}")
    next_heading = re.search(r"(?m)^####\s+.+$", dossier[start_match.end() :])
    end = start_match.end() + next_heading.start() if next_heading else len(dossier)
    return dossier[start_match.end() : end].strip()


def has_epistemic_boundary(text: str) -> bool:
    return EPISTEMIC_BOUNDARY_PATTERN.search(" ".join(text.split())) is not None


class FrontierModelDossierTests(unittest.TestCase):
    """Keep broad model coverage deep and evidence-conscious."""

    def test_every_announcement_dossier_uses_the_full_schema(self) -> None:
        dossiers = announcement_dossiers(guide_text())
        missing_core = {
            prefix
            for prefix in CORE_DOSSIER_PREFIXES
            if not any(title.startswith(prefix) for title in dossiers)
        }
        self.assertEqual(set(), missing_core, f"missing core dossier(s): {sorted(missing_core)}")
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
                self.assertIn("| Release field | Evidence-conscious record |", dossier)
                for subsection in required_subsections:
                    self.assertIn(subsection, dossier)

    def test_every_dossier_limits_subsection_states_an_epistemic_boundary(self) -> None:
        for title, dossier in announcement_dossiers(guide_text()).items():
            limits = dossier_subsection(
                dossier,
                "#### Limits, unknowns, and misleading shortcuts to avoid",
            )
            with self.subTest(title=title):
                self.assertTrue(limits, f"{title} has an empty limits subsection")
                self.assertTrue(
                    has_epistemic_boundary(limits),
                    f"{title} has no explicit epistemic boundary: {limits}",
                )

    def test_limits_boundary_helper_rejects_heading_only_and_generic_prose(self) -> None:
        heading = "#### Limits, unknowns, and misleading shortcuts to avoid"
        with self.assertRaisesRegex(AssertionError, "missing subsection"):
            dossier_subsection("#### Practical verdict\nUse it carefully.\n", heading)
        self.assertEqual("", dossier_subsection(f"{heading}\n\n#### Practical verdict\nStop.\n", heading))
        self.assertFalse(has_epistemic_boundary("Use the model carefully."))
        self.assertFalse(has_epistemic_boundary("Failure is possible."))
        self.assertTrue(has_epistemic_boundary("The architecture is not published."))

    def test_guide_has_named_cross_model_reference_surfaces_and_sources(self) -> None:
        text = guide_text()
        for heading in (
            "## How the Expanded Technical Dossiers Are Structured",
            "## Comprehensive Architecture, Performance, and Deployment Dossiers",
            "### Open-Weight Quantization and Deployment Reference",
            "### Model-Guide Completeness Matrix",
            "## Uncertainties and Known Limits",
            "## Sources",
            "## Method",
        ):
            with self.subTest(heading=heading):
                self.assertIn(heading, text)
        first_party_sources = {
            "OpenAI": "https://openai.com/index/gpt-5-6/",
            "Anthropic": "https://www.anthropic.com/news/claude-fable-5-mythos-5",
            "DeepSeek": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro",
            "Mistral": "https://mistral.ai/news/",
            "Google": "https://ai.google.dev/gemma/docs/core",
        }
        for family, source in first_party_sources.items():
            with self.subTest(family=family):
                self.assertIn(source, text)

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
