"""Tests for the canonical repository and release manifest."""

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "repository-manifest.json"


def load_module(name: str, relative: str):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RepositoryManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        cls.builder = load_module("manifest_build_release_package", "scripts/build_release_package.py")
        cls.health = load_module("manifest_repo_health_check", "scripts/repo_health_check.py")

    def test_manifest_has_unique_required_files_that_exist(self) -> None:
        required = self.manifest["required_files"]
        self.assertEqual(len(required), len(set(required)))
        for relative in required:
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / relative).is_file(), relative)

    def test_release_builder_uses_manifest_scope(self) -> None:
        release = self.manifest["release"]
        self.assertEqual(tuple(release["top_level_files"]), self.builder.TOP_LEVEL_FILES)
        self.assertEqual(tuple(release["package_directories"]), self.builder.PACKAGE_DIRS)
        self.assertEqual(
            tuple(release["package_subdirectories"]),
            tuple(path.as_posix() for path in self.builder.PACKAGE_SUBDIRS),
        )
        self.assertIn("starter", self.builder.PACKAGE_DIRS)
        self.assertIn("repository-manifest.json", self.builder.TOP_LEVEL_FILES)

    def test_health_checker_uses_manifest_required_files_and_suffixes(self) -> None:
        self.assertEqual(
            self.manifest["required_files"],
            self.health.required_files(ROOT),
        )
        self.assertEqual(
            set(self.manifest["text_suffixes"]),
            self.health.text_suffixes(ROOT),
        )
        for suffix in (".html", ".css", ".js", ".sh", ".xml", ".ini"):
            with self.subTest(suffix=suffix):
                self.assertIn(suffix, self.health.text_suffixes(ROOT))

    def test_secret_scanner_reads_web_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest = {
                "required_files": [],
                "release": {
                    "top_level_files": [],
                    "package_directories": [],
                    "package_subdirectories": [],
                },
                "text_suffixes": [".html", ".js"],
            }
            (root / "repository-manifest.json").write_text(
                json.dumps(manifest) + "\n",
                encoding="utf-8",
            )
            (root / "page.html").write_text(
                "<p>AKIAABCDEFGHIJKLMNOP</p>\n",
                encoding="utf-8",
            )
            (root / "safe.js").write_text(
                "const label = 'public example';\n",
                encoding="utf-8",
            )
            errors = self.health.check_secret_patterns(root)
            self.assertEqual(1, len(errors))
            self.assertIn("page.html", errors[0])

    def test_manifest_covers_frontier_kimi_assets(self) -> None:
        required = set(self.manifest["required_files"])
        for relative in (
            "docs/guides/frontier-model-list.md",
            "docs/guides/kimi-k3-frontier-dossier.md",
            "tests/test_kimi_k3_frontier.py",
        ):
            with self.subTest(relative=relative):
                self.assertIn(relative, required)


if __name__ == "__main__":
    unittest.main()
