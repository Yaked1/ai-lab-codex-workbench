import importlib.util
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_release_package.py"
spec = importlib.util.spec_from_file_location("build_release_package", SCRIPT)
build_release_package = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_release_package)


def write_file(root, relative, text="sample\n"):
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def make_package_fixture(root):
    for relative in build_release_package.TOP_LEVEL_FILES:
        write_file(root, relative, f"{relative}\n")

    write_file(root, "docs/guide.md")
    write_file(root, "data/research/sources.yml")
    write_file(root, "prompts/codex/example.md")
    write_file(root, "scripts/helper.py", "print('helper')\n")
    write_file(root, "tests/test_helper.py", "def test_helper():\n    assert True\n")
    write_file(root, ".github/workflows/release-package.yml", "name: Release Package\n")
    write_file(root, ".github/codex/prompts/daily-guide-curator.md", "Prompt\n")


class BuildReleasePackageTests(unittest.TestCase):
    def test_build_package_creates_zip_and_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_package_fixture(root)

            outputs = build_release_package.build_package("v0.1.0", root)

            self.assertEqual(outputs.zip_path.name, "ai-agent-coding-workbench-v0.1.0.zip")
            self.assertEqual(outputs.manifest_path.name, "package-manifest-v0.1.0.json")
            self.assertTrue(outputs.zip_path.is_file())
            self.assertTrue(outputs.manifest_path.is_file())

            with zipfile.ZipFile(outputs.zip_path) as archive:
                names = set(archive.namelist())

            self.assertIn("README.md", names)
            self.assertIn("AGENTS.md", names)
            self.assertIn("data/research/sources.yml", names)
            self.assertIn("docs/guide.md", names)
            self.assertIn("prompts/codex/example.md", names)
            self.assertIn("scripts/helper.py", names)
            self.assertIn("tests/test_helper.py", names)
            self.assertIn(".github/workflows/release-package.yml", names)
            self.assertIn(".github/codex/prompts/daily-guide-curator.md", names)

            manifest = json.loads(outputs.manifest_path.read_text(encoding="utf-8"))
            self.assertEqual(manifest["package_name"], "ai-agent-coding-workbench")
            self.assertEqual(manifest["version"], "v0.1.0")
            self.assertEqual(manifest["archive"]["name"], outputs.zip_path.name)
            self.assertTrue(manifest["archive"]["sha256"])

    def test_build_package_excludes_generated_private_and_dependency_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_package_fixture(root)
            write_file(root, ".env", "TOKEN=nope\n")
            write_file(root, ".env.local", "TOKEN=nope\n")
            write_file(root, "dist/old.txt")
            write_file(root, "docs/__pycache__/cached.pyc")
            write_file(root, "docs/.pytest_cache/cache.txt")
            write_file(root, "docs/.venv/activate.ps1")
            write_file(root, "docs/node_modules/package/index.js")

            outputs = build_release_package.build_package("v0.1.0", root)

            with zipfile.ZipFile(outputs.zip_path) as archive:
                names = set(archive.namelist())

            self.assertNotIn(".env", names)
            self.assertNotIn(".env.local", names)
            self.assertFalse(any(name.startswith("dist/") for name in names))
            self.assertFalse(any("__pycache__" in name for name in names))
            self.assertFalse(any(".pytest_cache" in name for name in names))
            self.assertFalse(any(".venv" in name for name in names))
            self.assertFalse(any("node_modules" in name for name in names))

    def test_validate_version_rejects_invalid_version(self):
        with self.assertRaises(ValueError):
            build_release_package.validate_version("v0.1")


if __name__ == "__main__":
    unittest.main()

# RESEARCH-GRADE-EXPANSION:BEGIN
# Research-grade maintenance notes:
# - Role: repository regression test.
# - Review this file for clear inputs, outputs, side effects, and failure behavior.
# - Keep examples public-safe and repository-relative; avoid secrets or private paths.
# - When behavior changes, update adjacent tests, docs, and changelog evidence.
# - Prefer deterministic, reviewable operations over hidden or networked side effects.
# RESEARCH-GRADE-EXPANSION:END
