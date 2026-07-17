"""Regression coverage for the Kimi K3 frontier dossier."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DOSSIER = ROOT / "docs" / "guides" / "kimi-k3-frontier-dossier.md"
MANIFEST = ROOT / "repository-manifest.json"


class KimiK3FrontierTests(unittest.TestCase):
    def test_dossier_is_present_and_dated(self) -> None:
        text = DOSSIER.read_text(encoding="utf-8")
        self.assertTrue(text.endswith("\n"))
        self.assertIn("# Kimi K3 Frontier Dossier", text)
        self.assertIn("Checked: 2026-07-17", text)
        self.assertIn("July 16, 2026", text)

    def test_dossier_records_release_and_open_source_boundary(self) -> None:
        text = DOSSIER.read_text(encoding="utf-8")
        self.assertIn("July 27, 2026", text)
        self.assertIn("not yet verified", text)
        self.assertIn("do not label the model open-weight", text)
        self.assertIn("2.8T-parameter", text)

    def test_dossier_does_not_invent_architecture(self) -> None:
        text = DOSSIER.read_text(encoding="utf-8")
        for unknown in (
            "dense or MoE",
            "active per token",
            "layer count",
            "expert count",
            "attention topology",
            "serving precision",
        ):
            with self.subTest(unknown=unknown):
                self.assertIn(unknown, text)

    def test_dossier_has_full_operational_schema(self) -> None:
        text = DOSSIER.read_text(encoding="utf-8")
        for heading in (
            "## Release card",
            "## Launch story",
            "## Capabilities and product behavior",
            "## Benchmarks, results, and what they establish",
            "## Deployment and evaluation consequences",
            "## Limits, unknowns, and misleading shortcuts to avoid",
            "## Practical verdict",
            "## Verification",
        ):
            with self.subTest(heading=heading):
                self.assertIn(heading, text)

    def test_manifest_declares_dossier_and_test(self) -> None:
        text = MANIFEST.read_text(encoding="utf-8")
        self.assertIn("docs/guides/kimi-k3-frontier-dossier.md", text)
        self.assertIn("tests/test_kimi_k3_frontier.py", text)


if __name__ == "__main__":
    unittest.main()
