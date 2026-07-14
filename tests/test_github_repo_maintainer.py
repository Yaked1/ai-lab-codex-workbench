"""Regression tests for the staged-index safety gate in the maintainer script."""
from __future__ import annotations

import shutil
import subprocess
import tempfile
import unittest
import os
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "github_repo_maintainer.ps1"
GIT = shutil.which("git")
PWSH = shutil.which("pwsh")
ANSI_ESCAPE = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")


def normalized_process_output(result: subprocess.CompletedProcess[str]) -> str:
    """Return stable diagnostic text across Windows console encodings and ANSI rendering."""
    combined = (result.stdout or "") + (result.stderr or "")
    # PowerShell's formatted error renderer inserts an isolated ``|`` gutter
    # when a long message wraps. It is presentation noise, not message content.
    return " ".join(token for token in ANSI_ESCAPE.sub("", combined).split() if token != "|")


@unittest.skipUnless(GIT and PWSH, "git and PowerShell are required")
class GitHubRepoMaintainerStagedIndexTests(unittest.TestCase):
    def test_windows_command_line_quoting_preserves_argument_boundaries(self):
        script_text = SCRIPT.read_text(encoding="utf-8")
        start = script_text.index("function ConvertTo-WindowsCommandLineArgument")
        end = script_text.index("function Invoke-GitBytes")
        helper = script_text[start:end]
        command = (
            "Invoke-Expression @'\n"
            + helper
            + "'@\n"
            + "@('plain', 'has space', 'quote\"here', 'trailing\\', "
            + "'space trailing\\', '') | "
            + "ForEach-Object { ConvertTo-WindowsCommandLineArgument $_ } | "
            + "ConvertTo-Json -Compress"
        )

        result = subprocess.run(
            [PWSH, "-NoProfile", "-Command", command],
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(
            json.loads(result.stdout),
            [
                "plain",
                '"has space"',
                '"quote\\"here"',
                "trailing\\",
                '"space trailing\\\\"',
                '""',
            ],
        )

    def run_git(self, root: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [GIT, *args],
            cwd=root,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )

    def run_git_bytes(self, root: Path, *args: str) -> subprocess.CompletedProcess[bytes]:
        return subprocess.run(
            [GIT, *args],
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )

    def make_repo(self) -> tempfile.TemporaryDirectory[str]:
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        self.addCleanup(temporary.cleanup)
        self.run_git(root, "init", "-b", "work")
        self.run_git(root, "config", "user.name", "Maintainer Test")
        self.run_git(root, "config", "user.email", "maintainer-test@example.invalid")
        (root / "baseline.md").write_text("baseline\n", encoding="utf-8")
        self.run_git(root, "add", "baseline.md")
        self.run_git(root, "commit", "-m", "baseline")
        return temporary

    def run_maintainer(
        self,
        root: Path,
        *extra: str,
        include: str = "approved.md",
    ) -> subprocess.CompletedProcess[str]:
        command = [
            PWSH,
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(SCRIPT),
            "-Mode",
            "commit",
            "-Apply",
            "-BaseBranch",
            "main",
            "-Include",
            include,
            "-CommitMessage",
            "test: staged index gate",
            "-SkipChecks",
            "-SkipAutofix",
            *extra,
        ]
        return subprocess.run(
            command,
            cwd=root,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

    def test_refuses_forbidden_pre_staged_path_before_staging_approved_file(self):
        temporary = self.make_repo()
        root = Path(temporary.name)
        (root / "approved.md").write_text("approved\n", encoding="utf-8")
        (root / "forbidden.txt").write_text("not approved\n", encoding="utf-8")
        self.run_git(root, "add", "forbidden.txt")

        result = self.run_maintainer(root)

        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("staged index", (result.stdout + result.stderr).lower())
        staged = self.run_git(root, "diff", "--cached", "--name-only").stdout.splitlines()
        self.assertEqual(staged, ["forbidden.txt"])

    def test_refuses_cached_secret_when_worktree_copy_is_safe(self):
        temporary = self.make_repo()
        root = Path(temporary.name)
        secret_fixture = "sk-" + ("1" * 24)
        (root / "approved.md").write_text(secret_fixture + "\n", encoding="utf-8")
        self.run_git(root, "add", "approved.md")
        (root / "approved.md").write_text("safe worktree copy\n", encoding="utf-8")

        result = self.run_maintainer(root)

        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("secret-looking staged content", (result.stdout + result.stderr).lower())

    def test_refuses_oversized_cached_blob(self):
        temporary = self.make_repo()
        root = Path(temporary.name)
        (root / "approved.md").write_text("x" * 32, encoding="utf-8")
        self.run_git(root, "add", "approved.md")
        (root / "approved.md").write_text("safe worktree copy\n", encoding="utf-8")

        result = self.run_maintainer(root, "-MaxSecretScanBytes", "16")

        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("exceeds -maxsecretscanbytes", (result.stdout + result.stderr).lower())

    def test_allow_deleted_files_commits_exact_approved_deletion(self):
        temporary = self.make_repo()
        root = Path(temporary.name)
        deleted = root / "obsolete.md"
        deleted.write_text("obsolete\n", encoding="utf-8")
        self.run_git(root, "add", deleted.name)
        self.run_git(root, "commit", "-m", "add obsolete file")
        deleted.unlink()

        result = self.run_maintainer(
            root,
            "-AllowDeletedFiles",
            include=deleted.name,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        names = self.run_git(root, "show", "--format=", "--name-only", "HEAD").stdout.splitlines()
        self.assertEqual(names, [deleted.name])
        self.assertNotIn(deleted.name, self.run_git(root, "ls-tree", "-r", "--name-only", "HEAD").stdout.splitlines())

    def test_allow_deleted_files_commits_rename_as_deletion_and_addition(self):
        temporary = self.make_repo()
        root = Path(temporary.name)
        old_path = root / "old-name.md"
        new_path = root / "new-name.md"
        old_path.write_text("rename me\n", encoding="utf-8")
        self.run_git(root, "add", old_path.name)
        self.run_git(root, "commit", "-m", "add old path")
        old_path.rename(new_path)

        result = self.run_maintainer(root, "-AllowDeletedFiles", include="*.md")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        names = [
            name.decode("utf-8")
            for name in self.run_git_bytes(
                root,
                "diff-tree",
                "--no-commit-id",
                "--name-only",
                "-r",
                "--no-renames",
                "-z",
                "HEAD",
            ).stdout.split(b"\0")
            if name
        ]
        self.assertEqual(set(names), {new_path.name, old_path.name})
        tree = self.run_git(root, "ls-tree", "-r", "--name-only", "HEAD").stdout.splitlines()
        self.assertIn(new_path.name, tree)
        self.assertNotIn(old_path.name, tree)

    def test_refuses_binary_cached_blob_with_text_extension(self):
        temporary = self.make_repo()
        root = Path(temporary.name)
        approved = root / "approved.txt"
        approved.write_bytes(b"binary\x00payload\n")
        self.run_git(root, "add", approved.name)
        approved.write_text("safe worktree copy\n", encoding="utf-8")

        result = self.run_maintainer(root, include=approved.name)

        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("binary control byte", (result.stdout + result.stderr).lower())

    def test_allows_tab_lf_and_cr_in_cached_text_blob(self):
        temporary = self.make_repo()
        root = Path(temporary.name)
        approved = root / "approved.txt"
        approved.write_bytes(b"column\tvalue\r\nnext\tline\n")

        result = self.run_maintainer(root, include=approved.name)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_refuses_invalid_utf8_cached_blob_with_text_extension(self):
        temporary = self.make_repo()
        root = Path(temporary.name)
        approved = root / "approved.txt"
        approved.write_bytes(b"invalid\xffutf8\n")
        self.run_git(root, "add", approved.name)
        approved.write_text("safe worktree copy\n", encoding="utf-8")

        result = self.run_maintainer(root, include=approved.name)

        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("could not decode cached staged content", (result.stdout + result.stderr).lower())

    def test_refuses_pre_commit_hook_index_mutation(self):
        temporary = self.make_repo()
        root = Path(temporary.name)
        (root / "approved.md").write_text("approved\n", encoding="utf-8")
        hook = root / ".git" / "hooks" / "pre-commit"
        hook.write_text(
            "#!/bin/sh\nprintf 'hook mutation\\n' > hook-forbidden.md\ngit add hook-forbidden.md\n",
            encoding="utf-8",
        )
        os.chmod(hook, 0o755)

        result = self.run_maintainer(root)

        output = normalized_process_output(result)
        self.assertNotEqual(result.returncode, 0, output)
        self.assertIn("local commit may exist", output.lower())
        self.assertNotIn("== Final report ==", result.stdout)
        self.assertNotIn("Actions:", result.stdout)
        committed_paths = self.run_git(root, "show", "--format=", "--name-only", "HEAD").stdout.splitlines()
        self.assertEqual(committed_paths, ["approved.md", "hook-forbidden.md"])

    def test_commits_exact_unicode_and_space_path_set(self):
        temporary = self.make_repo()
        root = Path(temporary.name)
        approved = "approved space ü.md"
        (root / approved).write_text("approved\n", encoding="utf-8")

        result = self.run_maintainer(root, include=approved)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        names = self.run_git_bytes(
            root,
            "diff-tree",
            "--no-commit-id",
            "--name-only",
            "-r",
            "-z",
            "HEAD",
        ).stdout.split(b"\0")
        self.assertEqual([name.decode("utf-8") for name in names if name], [approved])

    def test_uses_nul_delimited_git_path_interfaces(self):
        text = SCRIPT.read_text(encoding="utf-8")
        self.assertIn('"--cached", "--name-only", "-z", "--no-renames"', text)
        self.assertIn('"--name-status", "-z", "--no-renames"', text)
        self.assertIn("ConvertFrom-NulDelimitedGitOutput", text)
        self.assertNotIn(".ArgumentList", text)
        self.assertNotIn('Trim().Replace("\\\\", "/")', text)


if __name__ == "__main__":
    unittest.main()
