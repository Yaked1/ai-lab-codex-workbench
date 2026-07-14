"""Behavior tests for the GitHub repository bootstrap safety boundary."""

from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "bootstrap_github_repo.ps1"
GIT = shutil.which("git")
PWSH = shutil.which("pwsh")


@unittest.skipUnless(GIT and PWSH, "git and PowerShell are required")
class BootstrapGitHubRepoTests(unittest.TestCase):
    def run_git(self, root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [GIT, *args],
            cwd=root,
            encoding="utf-8",
            errors="strict",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=check,
        )

    def make_repo(self) -> tuple[tempfile.TemporaryDirectory[str], Path, Path, Path]:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        base = Path(temporary.name)
        root = base / "repo"
        shims = base / "shims"
        root.mkdir()
        shims.mkdir()
        (root / "scripts").mkdir()
        (root / "scripts" / "repo_health_check.py").write_text(
            "# replaced by the test command shim\n", encoding="utf-8"
        )
        self.run_git(root, "init", "-b", "main")
        self.run_git(root, "config", "user.name", "Bootstrap Test")
        self.run_git(root, "config", "user.email", "bootstrap@example.invalid")
        (root / "README.md").write_text("baseline\n", encoding="utf-8")
        self.run_git(root, "add", "README.md", "scripts/repo_health_check.py")
        self.run_git(root, "commit", "-m", "baseline")
        log = base / "commands.log"
        self.write_shims(shims)
        return temporary, root, shims, log

    @staticmethod
    def write_shims(shims: Path) -> None:
        (shims / "python.cmd").write_text(
            "\r\n".join(
                (
                    "@echo off",
                    'echo python %*>> "%BOOTSTRAP_COMMAND_LOG%"',
                    "echo BOOTSTRAP_HEALTH_DIAGNOSTIC",
                    'if defined BOOTSTRAP_HEALTH_MUTATE_PATH echo changed-after-scan>"%BOOTSTRAP_HEALTH_MUTATE_PATH%"',
                    "exit /b %BOOTSTRAP_HEALTH_EXIT%",
                )
            ),
            encoding="ascii",
        )
        (shims / "gh.cmd").write_text(
            "\r\n".join(
                (
                    "@echo off",
                    'echo gh %*>> "%BOOTSTRAP_COMMAND_LOG%"',
                    "exit /b %BOOTSTRAP_GH_EXIT%",
                )
            ),
            encoding="ascii",
        )

    def run_bootstrap(
        self,
        root: Path,
        shims: Path,
        log: Path,
        *extra: str,
        health_exit: int = 0,
        gh_exit: int = 0,
        health_mutate_path: Path | None = None,
    ) -> subprocess.CompletedProcess[str]:
        environment = os.environ.copy()
        environment.update(
            {
                "BOOTSTRAP_COMMAND_LOG": str(log),
                "BOOTSTRAP_HEALTH_EXIT": str(health_exit),
                "BOOTSTRAP_GH_EXIT": str(gh_exit),
                "GIT_CONFIG_GLOBAL": str(shims / "empty.gitconfig"),
                "PATH": str(shims) + os.pathsep + environment["PATH"],
            }
        )
        if health_mutate_path is not None:
            environment["BOOTSTRAP_HEALTH_MUTATE_PATH"] = str(health_mutate_path)
        (shims / "empty.gitconfig").write_text("", encoding="utf-8")
        return subprocess.run(
            [
                PWSH,
                "-NoProfile",
                "-ExecutionPolicy",
                "Bypass",
                "-File",
                str(SCRIPT),
                *extra,
            ],
            cwd=root,
            env=environment,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

    @staticmethod
    def read_log(log: Path) -> list[str]:
        return log.read_text(encoding="utf-8").splitlines() if log.exists() else []

    def test_preview_lists_dirty_candidates_without_staging_or_contacting_github(self) -> None:
        _, root, shims, log = self.make_repo()
        (root / "README.md").write_text("modified\n", encoding="utf-8")
        (root / "notes with spaces.md").write_text("new\n", encoding="utf-8")

        result = self.run_bootstrap(root, shims, log)

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("Candidate paths", result.stdout)
        self.assertIn("README.md", result.stdout)
        self.assertIn("notes with spaces.md", result.stdout)
        self.assertIn("Preview only", result.stdout)
        self.assertEqual([], self.run_git(root, "diff", "--cached", "--name-only").stdout.splitlines())
        self.assertFalse(any(line.startswith("gh ") for line in self.read_log(log)))
        self.assertEqual("baseline", self.run_git(root, "log", "-1", "--pretty=%s").stdout.strip())

    def test_apply_stages_only_the_displayed_candidates(self) -> None:
        _, root, shims, log = self.make_repo()
        (root / "README.md").write_text("modified\n", encoding="utf-8")
        (root / "approved.md").write_text("approved\n", encoding="utf-8")
        hook = root / ".git" / "hooks" / "pre-commit"
        hook.write_text(
            "#!/bin/sh\nprintf 'hook-created\\n' > forbidden.md\nexit 29\n",
            encoding="utf-8",
        )

        result = self.run_bootstrap(root, shims, log, "-Apply")

        self.assertNotEqual(0, result.returncode, result.stdout + result.stderr)
        combined = result.stdout + result.stderr
        self.assertIn("git commit failed", combined)
        self.assertNotIn("Nothing to commit", combined)
        self.assertEqual(
            ["README.md", "approved.md"],
            self.run_git(root, "diff", "--cached", "--name-only").stdout.splitlines(),
        )
        self.assertNotIn("forbidden.md", self.run_git(root, "diff", "--cached", "--name-only").stdout)
        self.assertFalse(any("gh repo create" in line for line in self.read_log(log)))

    def test_health_or_secret_failure_stops_before_staging(self) -> None:
        _, root, shims, log = self.make_repo()
        (root / "unsafe.md").write_text("candidate\n", encoding="utf-8")

        result = self.run_bootstrap(root, shims, log, "-Apply", health_exit=17)

        self.assertNotEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("health and secret", (result.stdout + result.stderr).lower())
        self.assertIn("BOOTSTRAP_HEALTH_DIAGNOSTIC", result.stdout + result.stderr)
        self.assertEqual([], self.run_git(root, "diff", "--cached", "--name-only").stdout.splitlines())
        self.assertFalse(any(line.startswith("gh ") for line in self.read_log(log)))

    def test_corrupt_git_metadata_fails_closed_without_initializing(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        base = Path(temporary.name)
        root = base / "repo"
        shims = base / "shims"
        root.mkdir()
        shims.mkdir()
        (root / "scripts").mkdir()
        (root / "scripts" / "repo_health_check.py").write_text("# shimmed\n", encoding="utf-8")
        corrupt_git = root / ".git"
        corrupt_git.mkdir()
        marker = corrupt_git / "corrupt-marker"
        marker.write_text("do not replace\n", encoding="utf-8")
        self.write_shims(shims)

        result = self.run_bootstrap(root, shims, base / "commands.log", "-Apply")

        self.assertNotEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("existing Git metadata", result.stdout + result.stderr)
        self.assertEqual("do not replace\n", marker.read_text(encoding="utf-8"))
        self.assertFalse((corrupt_git / "HEAD").exists())
        self.assertEqual([], self.read_log(base / "commands.log"))

    def test_existing_origin_apply_does_not_require_github_cli_auth(self) -> None:
        temporary, root, shims, log = self.make_repo()
        bare = Path(temporary.name) / "remote.git"
        self.run_git(Path(temporary.name), "init", "--bare", str(bare))
        self.run_git(root, "remote", "add", "origin", str(bare))
        (root / "README.md").write_text("reviewed update\n", encoding="utf-8")

        result = self.run_bootstrap(root, shims, log, "-Apply", gh_exit=41)

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertFalse(any(line.startswith("gh ") for line in self.read_log(log)))
        remote_subject = self.run_git(
            bare, "log", "-1", "--pretty=%s", "refs/heads/main"
        ).stdout.strip()
        self.assertEqual("Initial Codex automation workbench", remote_subject)

    def test_candidate_change_during_health_check_fails_before_staging(self) -> None:
        _, root, shims, log = self.make_repo()
        candidate = root / "README.md"
        candidate.write_text("reviewed update\n", encoding="utf-8")

        result = self.run_bootstrap(
            root,
            shims,
            log,
            "-Apply",
            health_mutate_path=candidate,
        )

        self.assertNotEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("changed while health", (result.stdout + result.stderr).lower())
        self.assertEqual([], self.run_git(root, "diff", "--cached", "--name-only").stdout.splitlines())
        self.assertFalse(any(line.startswith("gh ") for line in self.read_log(log)))

    def test_new_repository_without_git_identity_fails_before_staging_or_github(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        base = Path(temporary.name)
        root = base / "repo"
        shims = base / "shims"
        root.mkdir()
        shims.mkdir()
        (root / "scripts").mkdir()
        (root / "scripts" / "repo_health_check.py").write_text("# shimmed\n", encoding="utf-8")
        (root / "README.md").write_text("new repository\n", encoding="utf-8")
        self.write_shims(shims)
        log = base / "commands.log"

        result = self.run_bootstrap(root, shims, log, "-Apply")

        self.assertNotEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("Git commit identity is not configured", result.stdout + result.stderr)
        self.assertTrue((root / ".git").is_dir())
        self.assertEqual([], self.run_git(root, "diff", "--cached", "--name-only").stdout.splitlines())
        self.assertFalse(any(line.startswith("gh ") for line in self.read_log(log)))

    def test_apply_handles_staged_rename_unicode_and_leading_dash_path(self) -> None:
        temporary, root, shims, log = self.make_repo()
        bare = Path(temporary.name) / "remote.git"
        self.run_git(Path(temporary.name), "init", "--bare", str(bare))
        self.run_git(root, "remote", "add", "origin", str(bare))
        unicode_name = "renamed " + chr(0xFC) + "ber.md"
        self.run_git(root, "mv", "README.md", unicode_name)
        (root / "-leading.md").write_text("leading dash\n", encoding="utf-8")

        result = self.run_bootstrap(root, shims, log, "-Apply")

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("README.md", result.stdout)
        self.assertIn("renamed", result.stdout)
        self.assertIn("-leading.md", result.stdout)
        remote_paths = self.run_git(
            bare,
            "-c",
            "core.quotepath=false",
            "ls-tree",
            "-r",
            "--name-only",
            "refs/heads/main",
        ).stdout.splitlines()
        self.assertIn(unicode_name, remote_paths)
        self.assertIn("-leading.md", remote_paths)
        self.assertNotIn("README.md", remote_paths)
        self.assertFalse(any(line.startswith("gh ") for line in self.read_log(log)))

    def test_clean_apply_reports_empty_staged_set_without_commit_failure(self) -> None:
        temporary, root, shims, log = self.make_repo()
        bare = Path(temporary.name) / "remote.git"
        self.run_git(Path(temporary.name), "init", "--bare", str(bare))
        self.run_git(root, "remote", "add", "origin", str(bare))
        self.run_git(root, "push", "-u", "origin", "main")

        result = self.run_bootstrap(root, shims, log, "-Apply")

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("No staged changes to commit", result.stdout)
        self.assertNotIn("commit failed", (result.stdout + result.stderr).lower())
        self.assertEqual("baseline", self.run_git(root, "log", "-1", "--pretty=%s").stdout.strip())

    def test_apply_gate_is_explicit_in_help_and_source(self) -> None:
        source = SCRIPT.read_text(encoding="utf-8")
        self.assertIn("[switch]$Apply", source)
        self.assertNotIn("git add .", source)
        self.assertIn('@("add", "-A", "--")', source)
        self.assertGreaterEqual(source.count("ReadToEndAsync()"), 2)
        self.assertNotIn(".StandardOutput.ReadToEnd()", source)
        self.assertNotIn(".StandardError.ReadToEnd()", source)
        self.assertLess(
            source.index("$reviewedBlobSnapshot = if ($hasRepository)"),
            source.index("$health = Invoke-ToolCommand"),
        )
        self.assertIn("Assert-BlobSnapshotUnchanged", source)


if __name__ == "__main__":
    unittest.main()
