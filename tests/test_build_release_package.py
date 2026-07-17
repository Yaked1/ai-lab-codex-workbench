import hashlib
import io
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from contextlib import redirect_stderr
from pathlib import Path
from unittest import mock

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_release_package.py"
spec = importlib.util.spec_from_file_location("build_release_package", SCRIPT)
build_release_package = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_release_package)


def git(root, *args, input_bytes=None):
    return subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        input=input_bytes,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout


def write_file(root, relative, text="sample\n"):
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def commit_all(root, message="fixture"):
    git(root, "add", "-A")
    git(root, "commit", "-m", message)
    return git(root, "rev-parse", "HEAD").decode("ascii").strip()


def make_package_fixture(root):
    git(root, "init")
    git(root, "config", "user.name", "Package Test")
    git(root, "config", "user.email", "package-test@example.invalid")
    for relative in build_release_package.TOP_LEVEL_FILES:
        write_file(root, relative, f"{relative}\n")
    write_file(root, "docs/guide.md", "committed guide\n")
    write_file(root, "data/research/sources.yml")
    write_file(root, "prompts/codex/example.md")
    write_file(root, "scripts/helper.py", "print('helper')\n")
    write_file(root, "tests/test_helper.py", "def test_helper():\n    assert True\n")
    write_file(root, "skills/example/SKILL.md", "# Skill\n")
    write_file(root, "examples/quickstart.md", "# Example\n")
    write_file(root, "starter/README.md", "# Starter\n")
    write_file(root, ".github/workflows/release-package.yml", "name: Release Package\n")
    write_file(root, ".github/codex/prompts/daily-guide-curator.md", "Prompt\n")
    return commit_all(root)


def archive_manifest_hashes(outputs):
    manifest = json.loads(outputs.manifest_path.read_text(encoding="utf-8"))
    with zipfile.ZipFile(outputs.zip_path) as archive:
        extracted = {name: archive.read(name) for name in archive.namelist()}
    hashes = {entry["path"]: entry["sha256"] for entry in manifest["files"]}
    return manifest, extracted, hashes


class BuildReleasePackageTests(unittest.TestCase):
    def test_build_uses_selected_commit_for_dirty_and_untracked_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            commit = make_package_fixture(root)
            write_file(root, "docs/guide.md", "dirty guide\n")
            write_file(root, "docs/untracked.md", "untracked\n")

            outputs = build_release_package.build_package("v0.1.0", root, root / "out")
            manifest, extracted, hashes = archive_manifest_hashes(outputs)

            self.assertEqual(commit, manifest["source_commit"])
            self.assertEqual(b"committed guide\n", extracted["docs/guide.md"])
            self.assertNotIn("docs/untracked.md", extracted)
            self.assertEqual(hashlib.sha256(extracted["docs/guide.md"]).hexdigest(), hashes["docs/guide.md"])

    def test_main_scope_includes_committed_skills_and_examples_and_excludes_unsafe_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_package_fixture(root)
            write_file(root, "docs/private-notes.md", "private\n")
            write_file(root, "docs/cache.zip", "archive\n")
            commit_all(root, "excluded paths")

            outputs = build_release_package.build_package("v0.1.0", root, root / "out")
            _, extracted, _ = archive_manifest_hashes(outputs)

            self.assertIn("skills/example/SKILL.md", extracted)
            self.assertIn("examples/quickstart.md", extracted)
            self.assertIn("starter/README.md", extracted)
            self.assertNotIn("docs/private-notes.md", extracted)
            self.assertNotIn("docs/cache.zip", extracted)

    def test_committed_symlink_is_skipped_and_unicode_space_path_is_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_package_fixture(root)
            write_file(root, "docs/space über.md", "unicode\n")
            commit_all(root, "unicode")
            blob = git(root, "hash-object", "-w", "--stdin", input_bytes=b"docs/guide.md\n").decode().strip()
            git(root, "update-index", "--add", "--cacheinfo", f"120000,{blob},docs/link.md")
            git(root, "commit", "-m", "symlink")
            commit = build_release_package.source_commit(root)

            self.assertIn("docs/space über.md", build_release_package.committed_package_paths(root, commit))
            self.assertNotIn("docs/link.md", build_release_package.committed_package_paths(root, commit))
            outputs = build_release_package.build_package("v0.1.0", root, root / "out")
            _, extracted, _ = archive_manifest_hashes(outputs)
            self.assertEqual(b"unicode\n", extracted["docs/space über.md"])
            self.assertNotIn("docs/link.md", extracted)

    def test_nested_directory_is_rejected_as_repository_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_package_fixture(root)

            with self.assertRaisesRegex(ValueError, "repository top level"):
                build_release_package.build_package("v0.1.0", root / "docs", root / "out")

    def test_second_temp_creation_failure_removes_first_temp(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_package_fixture(root)
            output_dir = root / "out"
            real_temp_path = build_release_package._temp_path
            calls = 0

            def fail_second_temp(directory, suffix):
                nonlocal calls
                calls += 1
                if calls == 2:
                    raise OSError("second temp failed")
                return real_temp_path(directory, suffix)

            with mock.patch.object(build_release_package, "_temp_path", side_effect=fail_second_temp):
                with self.assertRaisesRegex(OSError, "second temp failed"):
                    build_release_package.build_package("v0.1.0", root, output_dir)

            self.assertEqual([], list(output_dir.iterdir()))

    def test_failed_second_publish_preserves_competing_replacement(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_package_fixture(root)
            output_dir = root / "out"
            real_publish = build_release_package._publish_new
            calls = 0

            def replace_then_fail(temp_path, final_path):
                nonlocal calls
                calls += 1
                if calls == 1:
                    identity = real_publish(temp_path, final_path)
                    final_path.unlink()
                    final_path.write_bytes(b"competing output")
                    return identity
                raise OSError("second publish failed")

            with mock.patch.object(build_release_package, "_publish_new", side_effect=replace_then_fail):
                with self.assertRaisesRegex(OSError, "second publish failed"):
                    build_release_package.build_package("v0.1.0", root, output_dir)

            zip_path = output_dir / "ai-agent-coding-workbench-v0.1.0.zip"
            self.assertEqual(b"competing output", zip_path.read_bytes())
            self.assertFalse((output_dir / "package-manifest-v0.1.0.json").exists())
            self.assertEqual([], list(output_dir.glob(".package-*")))

    def test_publish_keeps_temp_identity_anchor_until_pair_is_linked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            temp_path = root / ".package-test"
            final_path = root / "final.zip"
            temp_path.write_bytes(b"package")

            build_release_package._publish_new(temp_path, final_path)

            self.assertTrue(temp_path.exists())
            self.assertEqual(b"package", final_path.read_bytes())

    def test_first_publish_failure_leaves_no_outputs_or_temps(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_package_fixture(root)
            output_dir = root / "out"

            with mock.patch.object(
                build_release_package,
                "_publish_new",
                side_effect=OSError("first publish failed"),
            ):
                with self.assertRaisesRegex(OSError, "first publish failed"):
                    build_release_package.build_package("v0.1.0", root, output_dir)

            self.assertEqual([], list(output_dir.iterdir()))

    def test_temp_cleanup_failure_rolls_back_outputs_and_retries_cleanup(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_package_fixture(root)
            output_dir = root / "out"
            real_cleanup = build_release_package._cleanup_temps
            calls = 0

            def fail_once(paths):
                nonlocal calls
                calls += 1
                if calls == 1:
                    return [OSError("temp cleanup failed")]
                return real_cleanup(paths)

            with mock.patch.object(build_release_package, "_cleanup_temps", side_effect=fail_once):
                with self.assertRaisesRegex(OSError, "cleanup failed"):
                    build_release_package.build_package("v0.1.0", root, output_dir)

            self.assertEqual([], list(output_dir.iterdir()))

    def test_same_commit_builds_byte_identical_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_package_fixture(root)

            first = build_release_package.build_package("v0.1.0", root, root / "out-one")
            second = build_release_package.build_package("v0.1.0", root, root / "out-two")

            self.assertEqual(first.zip_path.read_bytes(), second.zip_path.read_bytes())
            self.assertEqual(first.manifest_path.read_bytes(), second.manifest_path.read_bytes())

    def test_cli_reports_filesystem_errors_without_traceback(self):
        stderr = io.StringIO()
        with mock.patch.object(build_release_package, "build_package", side_effect=OSError("disk failure")):
            with mock.patch.object(sys, "argv", [str(SCRIPT), "--version", "v0.1.0"]):
                with redirect_stderr(stderr):
                    result = build_release_package.main()

        self.assertEqual(2, result)
        self.assertIn("ERROR: disk failure", stderr.getvalue())
        self.assertNotIn("Traceback", stderr.getvalue())

    def test_zip_collision_preserves_existing_zip_and_does_not_create_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_package_fixture(root)
            output_dir = root / "out"
            output_dir.mkdir()
            zip_path = output_dir / "ai-agent-coding-workbench-v0.1.0.zip"
            zip_path.write_bytes(b"keep zip")

            with self.assertRaises(FileExistsError):
                build_release_package.build_package("v0.1.0", root, output_dir)

            self.assertEqual(b"keep zip", zip_path.read_bytes())
            self.assertFalse((output_dir / "package-manifest-v0.1.0.json").exists())

    def test_manifest_collision_preserves_existing_manifest_and_does_not_create_zip(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_package_fixture(root)
            output_dir = root / "out"
            output_dir.mkdir()
            manifest_path = output_dir / "package-manifest-v0.1.0.json"
            manifest_path.write_bytes(b"keep manifest")

            with self.assertRaises(FileExistsError):
                build_release_package.build_package("v0.1.0", root, output_dir)

            self.assertEqual(b"keep manifest", manifest_path.read_bytes())
            self.assertFalse((output_dir / "ai-agent-coding-workbench-v0.1.0.zip").exists())

    def test_package_extracts_with_manifest_hash_and_path_parity(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            commit = make_package_fixture(root)
            outputs = build_release_package.build_package("v0.1.0", root, root / "out")
            manifest, extracted, hashes = archive_manifest_hashes(outputs)
            extract_dir = root / "extracted"
            with zipfile.ZipFile(outputs.zip_path) as archive:
                archive.extractall(extract_dir)

            self.assertEqual(commit, manifest["source_commit"])
            self.assertEqual(set(hashes), set(extracted))
            for relative, data in extracted.items():
                self.assertEqual(data, (extract_dir / relative).read_bytes())
                self.assertEqual(hashlib.sha256(data).hexdigest(), hashes[relative])

    def test_invalid_git_root_fails_plainly(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for relative in build_release_package.TOP_LEVEL_FILES:
                write_file(root, relative)

            with self.assertRaisesRegex(ValueError, "Git repository"):
                build_release_package.build_package("v0.1.0", root, root / "out")

    def test_validate_version_rejects_invalid_version(self):
        with self.assertRaises(ValueError):
            build_release_package.validate_version("v0.1")


if __name__ == "__main__":
    unittest.main()
