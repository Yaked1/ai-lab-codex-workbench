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

import re

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "create_prompting_os_package.py"
spec = importlib.util.spec_from_file_location("create_prompting_os_package", SCRIPT)
create_prompting_os_package = importlib.util.module_from_spec(spec)
spec.loader.exec_module(create_prompting_os_package)

CORE_PROMPTING_OS_ARTIFACTS = {
    "README.md",
    "01-kernel.md",
    "08-production-prompt-architecture.md",
    "09-security-and-governance.md",
    "10-evaluation-cookbook.md",
    "16-comprehensive-examples.md",
    "18-troubleshooting-and-debugging.md",
    "24-archive-corpus-source-map.md",
    "templates/master-prompt-template.md",
    "evals/prompt-quality-rubric.md",
}

VOLUME_POLICY_PATTERN = re.compile(
    r"(?i)\b(?:byte floor|file and byte floors|count and byte floor|"
    r"markdown depth targets|package-depth targets)\b"
)
NORMATIVE_VOLUME_PATTERN = re.compile(
    r"(?ix)"
    r"(?=.*\b(?:at\s+least|minimum(?:\s+of)?|must|needs?|requires?|"
    r"qualif(?:y|ies)|readiness|before\s+release|floor|threshold|target)\b)"
    r"(?=.*\b(?:\d[\d,]*(?:\.\d+)?\s*(?:(?:Markdown|content)\s+)?"
    r"(?:KB|MB|GB|bytes?|words?|files?)|"
    r"file\s+count|byte\s+count|word\s+count|content\s+target)\b)"
)
PER_FILE_SIZE_QUALITY_PATTERN = re.compile(
    r"(?ix)"
    r"(?=.*\bper[- ]file\b)"
    r"(?=.*\b(?:byte\s+)?size\b)"
    r"(?=.*\bquality\b)"
    r"(?=.*\b(?:determine|determines|grade|graded|grading|prove|proof|qualify|qualifies)\b)"
)
INVENTORY_METADATA_ALLOWANCE = re.compile(
    r"(?ix)"
    r"(?=.*\b(?:inventory|telemetry|audit\s+metadata)\b)"
    r"(?=.*\b(?:not\s+(?:a\s+)?quality\s+proof|does\s+not\s+grade\s+quality|"
    r"does\s+not\s+determine\s+quality|not\s+used\s+to\s+prove\s+quality)\b)"
)
FILE_POLICY_PATTERNS = {
    "22-risk-register.md": re.compile(
        r"(?i)\b(?:README size|minimum useful size|package-depth tests)\b"
    ),
    "23-quality-assurance-matrix.md": re.compile(
        r"(?i)\b(?:size check|package-depth tests)\b"
    ),
    "24-archive-corpus-source-map.md": re.compile(r"(?i)\bdepth promise\b"),
    "25-repository-expansion-playbook.md": re.compile(
        r"(?i)\b(?:enough depth|depth or completeness claims)\b"
    ),
    "34-static-site-and-release-docs.md": re.compile(r"(?i)\bdeep enough to teach\b"),
}


def write_file(root, relative, text="sample\n"):
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def git(root, *args, input_bytes=None):
    return subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        input=input_bytes,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout


def commit_all(root, message="fixture"):
    git(root, "add", "-A")
    git(root, "commit", "-m", message)
    return git(root, "rev-parse", "HEAD").decode("ascii").strip()


def make_prompting_os_fixture(root):
    git(root, "init")
    git(root, "config", "user.name", "Package Test")
    git(root, "config", "user.email", "package-test@example.invalid")
    write_file(root, "docs/prompting-os/README.md", "# Prompting OS\n")
    write_file(root, "docs/prompting-os/01-kernel.md", "# Kernel\n")
    write_file(root, "docs/prompting-os/templates/master-prompt-template.md", "# Template\n")
    write_file(root, "docs/prompting-os/evals/prompt-quality-rubric.md", "# Rubric\n")
    write_file(root, "docs/prompting-os/visuals/prompting-os-architecture.svg", "<svg></svg>\n")


def markdown_section(text, heading):
    level = len(heading) - len(heading.lstrip("#"))
    start = text.find(f"{heading}\n")
    if start < 0:
        raise AssertionError(f"missing section {heading}")
    match = re.search(
        rf"(?m)^#{{1,{level}}}\s+.+$", text[start + len(heading) + 1 :]
    )
    end = start + len(heading) + 1 + match.start() if match else len(text)
    return " ".join(text[start:end].split())


def duplicate_values(values):
    seen = set()
    duplicates = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return sorted(duplicates)


def ordered_sequences_match(expected, actual):
    return list(expected) == list(actual)


def is_normative_volume_proxy(line):
    if INVENTORY_METADATA_ALLOWANCE.search(line):
        return False
    return bool(
        VOLUME_POLICY_PATTERN.search(line)
        or NORMATIVE_VOLUME_PATTERN.search(line)
        or PER_FILE_SIZE_QUALITY_PATTERN.search(line)
    )


def volume_policy_matches(prompting_os):
    matches = []
    for path in sorted(prompting_os.rglob("*.md")):
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            file_policy = FILE_POLICY_PATTERNS.get(path.name)
            if is_normative_volume_proxy(line) or (
                file_policy is not None and file_policy.search(line)
            ):
                relative = path.relative_to(prompting_os).as_posix()
                matches.append(f"{relative}:{line_number}: {line.strip()}")
    return matches


class PromptingOsPackageTests(unittest.TestCase):
    def test_build_package_creates_deterministic_zip_and_public_safe_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_prompting_os_fixture(root)
            commit_all(root)

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
            commit_all(root)

            outputs = create_prompting_os_package.build_package(root=root, version="v1")

            with zipfile.ZipFile(outputs.zip_path) as archive:
                names = set(archive.namelist())

            self.assertNotIn("Prompting_OS_v1/.env", names)
            self.assertNotIn("Prompting_OS_v1/private-notes.md", names)
            self.assertNotIn("Prompting_OS_v1/secret-plan.md", names)
            self.assertFalse(any("__pycache__" in name for name in names))
            self.assertNotIn("Prompting_OS_v1/archive.zip", names)

    def test_build_uses_committed_custom_prefix_and_excludes_dirty_untracked_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_prompting_os_fixture(root)
            write_file(root, "docs/custom/guide.md", "committed\n")
            commit = commit_all(root)
            write_file(root, "docs/custom/guide.md", "dirty\n")
            write_file(root, "docs/custom/untracked.md", "untracked\n")

            outputs = create_prompting_os_package.build_package(
                root=root,
                version="v1",
                source_dir=Path("docs/custom"),
                output_dir=root / "out",
            )
            manifest = json.loads(outputs.manifest_path.read_text(encoding="utf-8"))
            with zipfile.ZipFile(outputs.zip_path) as archive:
                names = set(archive.namelist())
                data = archive.read("Prompting_OS_v1/guide.md")

            self.assertEqual(commit, manifest["source_commit"])
            self.assertEqual(b"committed\n", data)
            self.assertNotIn("Prompting_OS_v1/untracked.md", names)
            self.assertEqual("docs/custom", manifest["source_dir"])

    def test_custom_source_prefix_requires_committed_files_and_stays_inside_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_prompting_os_fixture(root)
            commit_all(root)
            write_file(root, "docs/uncommitted-source/readme.md", "local only\n")

            with self.assertRaisesRegex(FileNotFoundError, "committed source prefix"):
                create_prompting_os_package.build_package(
                    root=root,
                    source_dir=Path("docs/uncommitted-source"),
                    output_dir=root / "out",
                )
            with self.assertRaisesRegex(ValueError, "inside the repository root"):
                create_prompting_os_package.build_package(
                    root=root,
                    source_dir=root.parent,
                    output_dir=root / "out",
                )

    def test_invalid_git_root_fails_plainly(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_file(root, "docs/prompting-os/README.md", "local only\n")

            with self.assertRaisesRegex(ValueError, "Git repository"):
                create_prompting_os_package.build_package(root=root, output_dir=root / "out")

    def test_committed_symlink_is_skipped_and_unicode_space_path_is_packaged(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_prompting_os_fixture(root)
            write_file(root, "docs/prompting-os/space über.md", "unicode\n")
            commit_all(root, "unicode")
            blob = git(root, "hash-object", "-w", "--stdin", input_bytes=b"README.md\n").decode().strip()
            git(root, "update-index", "--add", "--cacheinfo", f"120000,{blob},docs/prompting-os/link.md")
            git(root, "commit", "-m", "symlink")
            commit = create_prompting_os_package.source_commit(root)

            self.assertIn("docs/prompting-os/space über.md", create_prompting_os_package.committed_package_paths(root, commit))
            self.assertNotIn("docs/prompting-os/link.md", create_prompting_os_package.committed_package_paths(root, commit))
            outputs = create_prompting_os_package.build_package(root=root, output_dir=root / "out")
            with zipfile.ZipFile(outputs.zip_path) as archive:
                self.assertEqual(b"unicode\n", archive.read("Prompting_OS_v1/space über.md"))
                self.assertNotIn("Prompting_OS_v1/link.md", archive.namelist())

    def test_nested_directory_is_rejected_as_repository_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_prompting_os_fixture(root)
            commit_all(root)

            with self.assertRaisesRegex(ValueError, "repository top level"):
                create_prompting_os_package.build_package(
                    root=root / "docs",
                    output_dir=root / "out",
                )

    def test_second_temp_creation_failure_removes_first_temp(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_prompting_os_fixture(root)
            commit_all(root)
            output_dir = root / "out"
            real_temp_path = create_prompting_os_package._temp_path
            calls = 0

            def fail_second_temp(directory, suffix):
                nonlocal calls
                calls += 1
                if calls == 2:
                    raise OSError("second temp failed")
                return real_temp_path(directory, suffix)

            with mock.patch.object(create_prompting_os_package, "_temp_path", side_effect=fail_second_temp):
                with self.assertRaisesRegex(OSError, "second temp failed"):
                    create_prompting_os_package.build_package(root=root, output_dir=output_dir)

            self.assertEqual([], list(output_dir.iterdir()))

    def test_failed_second_publish_preserves_competing_replacement(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_prompting_os_fixture(root)
            commit_all(root)
            output_dir = root / "out"
            real_publish = create_prompting_os_package._publish_new
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

            with mock.patch.object(create_prompting_os_package, "_publish_new", side_effect=replace_then_fail):
                with self.assertRaisesRegex(OSError, "second publish failed"):
                    create_prompting_os_package.build_package(root=root, output_dir=output_dir)

            zip_path = output_dir / "prompting-os-v1.zip"
            self.assertEqual(b"competing output", zip_path.read_bytes())
            self.assertFalse((output_dir / "prompting-os-v1-manifest.json").exists())
            self.assertEqual([], list(output_dir.glob(".package-*")))

    def test_publish_keeps_temp_identity_anchor_until_pair_is_linked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            temp_path = root / ".package-test"
            final_path = root / "final.zip"
            temp_path.write_bytes(b"package")

            create_prompting_os_package._publish_new(temp_path, final_path)

            self.assertTrue(temp_path.exists())
            self.assertEqual(b"package", final_path.read_bytes())

    def test_first_publish_failure_leaves_no_outputs_or_temps(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_prompting_os_fixture(root)
            commit_all(root)
            output_dir = root / "out"

            with mock.patch.object(
                create_prompting_os_package,
                "_publish_new",
                side_effect=OSError("first publish failed"),
            ):
                with self.assertRaisesRegex(OSError, "first publish failed"):
                    create_prompting_os_package.build_package(root=root, output_dir=output_dir)

            self.assertEqual([], list(output_dir.iterdir()))

    def test_temp_cleanup_failure_rolls_back_outputs_and_retries_cleanup(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_prompting_os_fixture(root)
            commit_all(root)
            output_dir = root / "out"
            real_cleanup = create_prompting_os_package._cleanup_temps
            calls = 0

            def fail_once(paths):
                nonlocal calls
                calls += 1
                if calls == 1:
                    return [OSError("temp cleanup failed")]
                return real_cleanup(paths)

            with mock.patch.object(create_prompting_os_package, "_cleanup_temps", side_effect=fail_once):
                with self.assertRaisesRegex(OSError, "cleanup failed"):
                    create_prompting_os_package.build_package(root=root, output_dir=output_dir)

            self.assertEqual([], list(output_dir.iterdir()))

    def test_repository_root_is_supported_as_custom_source_prefix(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_prompting_os_fixture(root)
            commit_all(root)

            outputs = create_prompting_os_package.build_package(
                root=root,
                source_dir=root,
                output_dir=root / "out",
            )
            manifest = json.loads(outputs.manifest_path.read_text(encoding="utf-8"))
            with zipfile.ZipFile(outputs.zip_path) as archive:
                names = set(archive.namelist())

            self.assertEqual(".", manifest["source_dir"])
            self.assertIn("Prompting_OS_v1/docs/prompting-os/README.md", names)

    def test_same_commit_builds_byte_identical_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_prompting_os_fixture(root)
            commit_all(root)

            first = create_prompting_os_package.build_package(root=root, output_dir=root / "out-one")
            second = create_prompting_os_package.build_package(root=root, output_dir=root / "out-two")

            self.assertEqual(first.zip_path.read_bytes(), second.zip_path.read_bytes())
            self.assertEqual(first.manifest_path.read_bytes(), second.manifest_path.read_bytes())

    def test_cli_reports_filesystem_errors_without_traceback(self):
        stderr = io.StringIO()
        with mock.patch.object(create_prompting_os_package, "build_package", side_effect=OSError("disk failure")):
            with mock.patch.object(sys, "argv", [str(SCRIPT)]):
                with redirect_stderr(stderr):
                    result = create_prompting_os_package.main()

        self.assertEqual(2, result)
        self.assertIn("ERROR: disk failure", stderr.getvalue())
        self.assertNotIn("Traceback", stderr.getvalue())

    def test_collisions_preserve_existing_package_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_prompting_os_fixture(root)
            commit_all(root)
            output_dir = root / "out"
            output_dir.mkdir()
            zip_path = output_dir / "prompting-os-v1.zip"
            zip_path.write_bytes(b"zip sentinel")

            with self.assertRaises(FileExistsError):
                create_prompting_os_package.build_package(root=root, output_dir=output_dir)

            self.assertEqual(b"zip sentinel", zip_path.read_bytes())
            self.assertFalse((output_dir / "prompting-os-v1-manifest.json").exists())
            zip_path.unlink()
            manifest_path = output_dir / "prompting-os-v1-manifest.json"
            manifest_path.write_bytes(b"manifest sentinel")

            with self.assertRaises(FileExistsError):
                create_prompting_os_package.build_package(root=root, output_dir=output_dir)

            self.assertEqual(b"manifest sentinel", manifest_path.read_bytes())
            self.assertFalse(zip_path.exists())

    def test_package_extracts_with_manifest_hash_and_path_parity(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_prompting_os_fixture(root)
            commit = commit_all(root)
            outputs = create_prompting_os_package.build_package(root=root, output_dir=root / "out")
            manifest = json.loads(outputs.manifest_path.read_text(encoding="utf-8"))
            extract_dir = root / "extracted"
            with zipfile.ZipFile(outputs.zip_path) as archive:
                archive.extractall(extract_dir)
                archive_entries = {name: archive.read(name) for name in archive.namelist()}

            self.assertEqual(commit, manifest["source_commit"])
            manifest_entries = {entry["archive_path"]: entry for entry in manifest["files"]}
            self.assertEqual(set(archive_entries), set(manifest_entries))
            for archive_path, data in archive_entries.items():
                self.assertEqual(data, (extract_dir / archive_path).read_bytes())
                self.assertEqual(hashlib.sha256(data).hexdigest(), manifest_entries[archive_path]["sha256"])

    def test_normalize_version_rejects_invalid_values(self):
        with self.assertRaises(ValueError):
            create_prompting_os_package.normalize_version("v1..0")
        with self.assertRaises(ValueError):
            create_prompting_os_package.normalize_version("latest")

    def test_prompting_os_quality_contract_uses_behavior_evidence_and_parity(self):
        readme = (ROOT / "docs" / "prompting-os" / "README.md").read_text(encoding="utf-8")
        section = markdown_section(readme, "## Package Quality Contract")
        for contract in (
            "Named core artifacts",
            "Worked example",
            "Failure case",
            "Verification command",
            "Source, manifest, and archive parity",
            "source_commit",
            "python -m unittest tests.test_prompting_os_package",
        ):
            with self.subTest(contract=contract):
                self.assertIn(contract, section)
        self.assertNotRegex(section, r"(?i)(?:at least|minimum)\s+(?:35|300\s*KB|\d+\s+Markdown files)")

    def test_prompting_os_policy_does_not_use_volume_quality_floors(self):
        prompting_os = ROOT / "docs" / "prompting-os"
        matches = volume_policy_matches(prompting_os)
        self.assertEqual([], matches, "volume quality proxy remains:\n" + "\n".join(matches))

    def test_volume_policy_scan_recurses_and_reports_relative_file_identity(self):
        with tempfile.TemporaryDirectory() as tmp:
            prompting_os = Path(tmp)
            nested = prompting_os / "nested" / "policy.md"
            nested.parent.mkdir()
            nested.write_text("Require a byte floor for quality.\n", encoding="utf-8")
            self.assertEqual(
                ["nested/policy.md:1: Require a byte floor for quality."],
                volume_policy_matches(prompting_os),
            )

    def test_volume_policy_scan_detects_semantic_normative_proxies(self):
        with tempfile.TemporaryDirectory() as tmp:
            prompting_os = Path(tmp)
            policy = prompting_os / "policy.md"
            policy.write_text(
                "A package needs at least 40 Markdown files to qualify as complete.\n"
                "Require a minimum of 300 KB of Markdown before release.\n"
                "Release readiness requires a 10,000-word content target.\n",
                encoding="utf-8",
            )
            self.assertEqual(
                [
                    "policy.md:1: A package needs at least 40 Markdown files to qualify as complete.",
                    "policy.md:2: Require a minimum of 300 KB of Markdown before release.",
                    "policy.md:3: Release readiness requires a 10,000-word content target.",
                ],
                volume_policy_matches(prompting_os),
            )

    def test_volume_policy_detector_rejects_per_file_size_as_quality(self):
        self.assertTrue(is_normative_volume_proxy("Per-file size metrics determine quality."))
        self.assertTrue(is_normative_volume_proxy("Quality is graded by per-file byte size."))
        self.assertFalse(is_normative_volume_proxy("The manifest records per-file size metadata."))
        self.assertFalse(
            is_normative_volume_proxy(
                "Inventory metadata: per-file size does not determine quality."
            )
        )

    def test_volume_policy_scan_allows_descriptive_and_disclaimed_inventory_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            prompting_os = Path(tmp)
            (prompting_os / "inventory.md").write_text(
                "The archive contains 40 Markdown files.\n"
                "Inventory metadata (not quality proof): 40 Markdown files.\n"
                "Telemetry inventory count is 40 files and does not grade quality.\n",
                encoding="utf-8",
            )
            self.assertEqual([], volume_policy_matches(prompting_os))

    def test_static_release_policy_separates_behavior_from_inventory_metadata(self):
        text = (ROOT / "docs" / "prompting-os" / "34-static-site-and-release-docs.md").read_text(
            encoding="utf-8"
        )
        section = markdown_section(text, "## Focused Prompting OS Package")
        for contract in (
            "Behavior and evidence review",
            "Inventory metadata (not quality proof)",
            "Named core artifacts",
            "Worked example",
            "Failure or counterexample",
            "Executable verification",
            "Source, manifest, and archive parity",
            "Markdown file count",
            "Markdown byte count",
        ):
            with self.subTest(contract=contract):
                self.assertIn(contract, section)

    def test_duplicate_sequence_guard_detects_collisions(self):
        self.assertEqual(["same"], duplicate_values(["same", "other", "same"]))

    def test_ordered_sequence_guard_detects_reordering(self):
        expected = ["first.md", "second.md"]
        self.assertTrue(ordered_sequences_match(expected, list(expected)))
        self.assertFalse(ordered_sequences_match(expected, list(reversed(expected))))

    def test_repository_prompting_os_has_named_core_artifacts_and_examples(self):
        source_dir = ROOT / "docs" / "prompting-os"
        files = create_prompting_os_package.iter_source_files(source_dir)
        relative_paths = {path.relative_to(source_dir).as_posix() for path in files}
        self.assertTrue(
            CORE_PROMPTING_OS_ARTIFACTS.issubset(relative_paths),
            f"missing core artifact(s): {sorted(CORE_PROMPTING_OS_ARTIFACTS - relative_paths)}",
        )

        examples = (source_dir / "16-comprehensive-examples.md").read_text(encoding="utf-8")
        worked = markdown_section(examples, "## Example 1: Documentation Update")
        failure = markdown_section(examples, "## Example 2: Source-Grounded Research Summary")
        self.assertIn("### Strong Prompt", worked)
        self.assertIn("python scripts/repo_health_check.py", worked)
        self.assertIn("### Failure Case", failure)
        self.assertIn("Expected behavior", failure)

    def test_archive_inventory_rows_have_source_identity_status_and_safe_use(self):
        source_map = (ROOT / "docs" / "prompting-os" / "24-archive-corpus-source-map.md").read_text(encoding="utf-8")
        start = source_map.index("## Top-Level Archive Inventory")
        end = source_map.index("## Extracted Folder Findings", start)
        rows = [line for line in source_map[start:end].splitlines() if line.startswith("| `")]
        identities = set()
        for row in rows:
            cells = [cell.strip() for cell in row.strip("|").split("|")]
            with self.subTest(row=row):
                self.assertEqual(3, len(cells))
                self.assertRegex(cells[0], r"^`[^`]+\.zip`$")
                self.assertIn(cells[1], {"Readable", "Central directory unreadable in local scan"})
                self.assertTrue(cells[2])
                identities.add(cells[0])
        for identity in ("`agent-coworker-main.zip`", "`openai-openai-cookbook.zip`", "`superpowers-main.zip`"):
            self.assertIn(identity, identities)

    def test_real_package_matches_committed_source_manifest_and_archive_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "package"
            outputs = create_prompting_os_package.build_package(
                root=ROOT,
                version="v1",
                output_dir=output_dir,
            )
            manifest = json.loads(outputs.manifest_path.read_text(encoding="utf-8"))
            commit = git(ROOT, "rev-parse", "HEAD").decode("ascii").strip()
            source_path_sequence = [
                path.decode("utf-8", "surrogateescape")
                for path in git(
                    ROOT,
                    "ls-tree",
                    "-rz",
                    "--name-only",
                    commit,
                    "--",
                    "docs/prompting-os",
                ).split(b"\0")
                if path
            ]
            manifest_path_sequence = [entry["path"] for entry in manifest["files"]]
            manifest_archive_path_sequence = [entry["archive_path"] for entry in manifest["files"]]
            with zipfile.ZipFile(outputs.zip_path) as archive:
                archive_path_sequence = archive.namelist()
                archive_bytes = {path: archive.read(path) for path in archive_path_sequence}

            self.assertEqual(commit, manifest["source_commit"])
            for label, sequence in (
                ("source paths", source_path_sequence),
                ("manifest paths", manifest_path_sequence),
                ("manifest archive paths", manifest_archive_path_sequence),
                ("ZIP names", archive_path_sequence),
            ):
                with self.subTest(sequence=label):
                    self.assertEqual([], duplicate_values(sequence), f"duplicate {label}")
            expected_archive_path_sequence = [
                f"Prompting_OS_v1/{path.removeprefix('docs/prompting-os/')}"
                for path in source_path_sequence
            ]
            self.assertTrue(ordered_sequences_match(source_path_sequence, manifest_path_sequence))
            self.assertTrue(
                ordered_sequences_match(expected_archive_path_sequence, manifest_archive_path_sequence)
            )
            self.assertTrue(
                ordered_sequences_match(manifest_archive_path_sequence, archive_path_sequence)
            )
            manifest_by_archive = {entry["archive_path"]: entry for entry in manifest["files"]}
            for archive_path, data in archive_bytes.items():
                entry = manifest_by_archive[archive_path]
                self.assertEqual(hashlib.sha256(data).hexdigest(), entry["sha256"])
                self.assertEqual(data, git(ROOT, "cat-file", "blob", f"{commit}:{entry['path']}"))
            for artifact in CORE_PROMPTING_OS_ARTIFACTS:
                self.assertIn(f"docs/prompting-os/{artifact}", source_path_sequence)


if __name__ == "__main__":
    unittest.main()
