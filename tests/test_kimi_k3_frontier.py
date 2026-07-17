"""Regression coverage for the Kimi K3 frontier dossier and model list."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DOSSIER = ROOT / "docs" / "guides" / "kimi-k3-frontier-dossier.md"
MODEL_LIST = ROOT / "docs" / "guides" / "frontier-model-list.md"
MANIFEST = ROOT / "repository-manifest.json"


class KimiK3FrontierTests(unittest.TestCase):
    def test_dossier_is_present_and_dated(self) -> None:
        text = DOSSIER.read_text(encoding="utf-8")
        self.assertTrue(text.endswith("\n"))
        self.assertIn("# Kimi K3 Frontier Dossier", text)
        self.assertIn("Checked: 2026-07-17", text)
        self.assertIn("July 17, 2026", text)

    def test_dossier_records_hosted_and_weight_release_boundary(self) -> None:
        text = DOSSIER.read_text(encoding="utf-8")
        self.assertIn("July 27, 2026", text)
        self.assertIn("not yet inspectable", text)
        self.assertIn("license", text.lower())
        self.assertIn("full model weights", text)

    def test_dossier_records_disclosed_architecture(self) -> None:
        text = DOSSIER.read_text(encoding="utf-8")
        for fact in (
            "2.8T-parameter",
            "Mixture-of-Experts",
            "16 of 896 experts active",
            "Kimi Delta Attention",
            "Attention Residuals",
            "Stable LatentMoE",
            "MXFP4",
            "MXFP8",
            "1 million tokens",
        ):
            with self.subTest(fact=fact):
                self.assertIn(fact, text)

    def test_dossier_records_current_api_surface_and_pricing(self) -> None:
        text = DOSSIER.read_text(encoding="utf-8")
        for fact in (
            "`kimi-k3`",
            "$0.30/MTok cache-hit input",
            "$3.00/MTok cache-miss input",
            "$15.00/MTok output",
            "`max` at launch",
        ):
            with self.subTest(fact=fact):
                self.assertIn(fact, text)

    def test_dossier_has_full_operational_schema(self) -> None:
        text = DOSSIER.read_text(encoding="utf-8")
        for heading in (
            "## Release card",
            "## Launch story",
            "## Architecture and infrastructure",
            "## Capabilities and product behavior",
            "## Benchmarks, results, and what they establish",
            "## Deployment and evaluation consequences",
            "## Limits, unknowns, and misleading shortcuts to avoid",
            "## Practical verdict",
            "## Sources and recheck triggers",
            "## Verification",
        ):
            with self.subTest(heading=heading):
                self.assertIn(heading, text)

    def test_frontier_model_list_includes_kimi_k3(self) -> None:
        text = MODEL_LIST.read_text(encoding="utf-8")
        self.assertIn("Kimi K3", text)
        self.assertIn("kimi-k3-frontier-dossier.md", text)
        self.assertIn("2.8T", text)
        self.assertIn("16 / 896", text)
        self.assertIn("July 27, 2026", text)

    def test_manifest_declares_dossier_list_and_test(self) -> None:
        text = MANIFEST.read_text(encoding="utf-8")
        for path in (
            "docs/guides/kimi-k3-frontier-dossier.md",
            "docs/guides/frontier-model-list.md",
            "tests/test_kimi_k3_frontier.py",
        ):
            with self.subTest(path=path):
                self.assertIn(path, text)


if __name__ == "__main__":
    unittest.main()
