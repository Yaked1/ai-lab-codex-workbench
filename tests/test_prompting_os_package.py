import importlib.util
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "create_prompting_os_package.py"
spec = importlib.util.spec_from_file_location("create_prompting_os_package", SCRIPT)
create_prompting_os_package = importlib.util.module_from_spec(spec)
spec.loader.exec_module(create_prompting_os_package)


def write_file(root, relative, text="sample\n"):
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def make_prompting_os_fixture(root):
    write_file(root, "docs/prompting-os/README.md", "# Prompting OS\n")
    write_file(root, "docs/prompting-os/01-kernel.md", "# Kernel\n")
    write_file(root, "docs/prompting-os/templates/master-prompt-template.md", "# Template\n")
    write_file(root, "docs/prompting-os/evals/prompt-quality-rubric.md", "# Rubric\n")
    write_file(root, "docs/prompting-os/visuals/prompting-os-architecture.svg", "<svg></svg>\n")


class PromptingOsPackageTests(unittest.TestCase):
    def test_build_package_creates_deterministic_zip_and_public_safe_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_prompting_os_fixture(root)

            outputs = create_prompting_os_package.build_package(root=root, version="1")

            self.assertEqual(outputs.zip_path.name, "prompting-os-v1.zip")
            self.assertEqual(outputs.manifest_path.name, "prompting-os-v1-manifest.json")
            self.assertTrue(outputs.zip_path.is_file())
            self.assertTrue(outputs.manifest_path.is_file())

            with zipfile.ZipFile(outputs.zip_path) as archive:
                names = set(archive.namelist())
                info = archive.getinfo("Prompting_OS_v1/README.md")

            self.assertIn("Prompting_OS_v1/README.md", names)
            self.assertIn("Prompting_OS_v1/01-kernel.md", names)
            self.assertIn("Prompting_OS_v1/templates/master-prompt-template.md", names)
            self.assertEqual(info.date_time, create_prompting_os_package.FIXED_ZIP_TIMESTAMP)

            manifest_text = outputs.manifest_path.read_text(encoding="utf-8")
            manifest = json.loads(manifest_text)
            self.assertEqual(manifest["package_name"], "prompting-os")
            self.assertEqual(manifest["version"], "v1")
            self.assertEqual(manifest["source_dir"], "docs/prompting-os")
            self.assertEqual(manifest["archive"]["name"], outputs.zip_path.name)
            self.assertIn("Prompting_OS_v1/README.md", {entry["archive_path"] for entry in manifest["files"]})
            self.assertNotIn(str(root), manifest_text)

    def test_build_package_excludes_private_cache_and_archive_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_prompting_os_fixture(root)
            write_file(root, "docs/prompting-os/.env", "TOKEN=nope\n")
            write_file(root, "docs/prompting-os/private-notes.md", "private\n")
            write_file(root, "docs/prompting-os/secret-plan.md", "secret\n")
            write_file(root, "docs/prompting-os/__pycache__/cached.pyc", "cached\n")
            write_file(root, "docs/prompting-os/archive.zip", "not a real zip\n")

            outputs = create_prompting_os_package.build_package(root=root, version="v1")

            with zipfile.ZipFile(outputs.zip_path) as archive:
                names = set(archive.namelist())

            self.assertNotIn("Prompting_OS_v1/.env", names)
            self.assertNotIn("Prompting_OS_v1/private-notes.md", names)
            self.assertNotIn("Prompting_OS_v1/secret-plan.md", names)
            self.assertFalse(any("__pycache__" in name for name in names))
            self.assertNotIn("Prompting_OS_v1/archive.zip", names)

    def test_normalize_version_rejects_invalid_values(self):
        with self.assertRaises(ValueError):
            create_prompting_os_package.normalize_version("v1..0")
        with self.assertRaises(ValueError):
            create_prompting_os_package.normalize_version("latest")

    def test_repository_prompting_os_source_is_substantial(self):
        source_dir = ROOT / "docs" / "prompting-os"
        files = create_prompting_os_package.iter_source_files(source_dir)
        markdown_files = [path for path in files if path.suffix.lower() == ".md"]
        markdown_bytes = sum(path.stat().st_size for path in markdown_files)
        large_markdown_files = [path for path in markdown_files if path.stat().st_size >= 5_000]

        required = {
            "08-production-prompt-architecture.md",
            "09-security-and-governance.md",
            "10-evaluation-cookbook.md",
            "11-comprehensiveness-benchmark.md",
            "templates/master-prompt-template.md",
            "evals/prompt-quality-rubric.md",
        }
        relative_paths = {path.relative_to(source_dir).as_posix() for path in markdown_files}

        self.assertGreaterEqual(len(markdown_files), 14)
        self.assertGreaterEqual(len(large_markdown_files), 14)
        self.assertGreaterEqual(markdown_bytes, 100_000)
        self.assertTrue(required.issubset(relative_paths))
        self.assertGreaterEqual((source_dir / "templates" / "master-prompt-template.md").stat().st_size, 4_000)
        self.assertGreaterEqual((source_dir / "evals" / "prompt-quality-rubric.md").stat().st_size, 4_000)

    def test_real_package_manifest_shows_substantial_markdown_payload(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "package"
            outputs = create_prompting_os_package.build_package(
                root=ROOT,
                version="v1",
                output_dir=output_dir,
            )
            manifest = json.loads(outputs.manifest_path.read_text(encoding="utf-8"))
            markdown_entries = [entry for entry in manifest["files"] if entry["path"].endswith(".md")]
            markdown_bytes = sum(entry["size_bytes"] for entry in markdown_entries)

            self.assertGreaterEqual(len(markdown_entries), 14)
            self.assertGreaterEqual(markdown_bytes, 100_000)
            self.assertIn(
                "Prompting_OS_v1/08-production-prompt-architecture.md",
                {entry["archive_path"] for entry in markdown_entries},
            )
            self.assertIn(
                "Prompting_OS_v1/09-security-and-governance.md",
                {entry["archive_path"] for entry in markdown_entries},
            )
            self.assertIn(
                "Prompting_OS_v1/10-evaluation-cookbook.md",
                {entry["archive_path"] for entry in markdown_entries},
            )
            self.assertIn(
                "Prompting_OS_v1/11-comprehensiveness-benchmark.md",
                {entry["archive_path"] for entry in markdown_entries},
            )


if __name__ == "__main__":
    unittest.main()
