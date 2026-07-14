import tempfile
import unittest
from pathlib import Path
import importlib.util
import re
import shutil
import subprocess

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "repo_health_check.py"
ROOT = Path(__file__).resolve().parents[1]
PWSH = shutil.which("pwsh")
GIT = shutil.which("git")
CHECKOUT_SHA = "34e114876b0b11c390a56381ad16ebd13914f8d5"
SETUP_PYTHON_SHA = "a26af69be951a213d495a4c3e4e4022e16d87065"
spec = importlib.util.spec_from_file_location("repo_health_check", SCRIPT)
repo_health_check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(repo_health_check)


class RepoHealthTests(unittest.TestCase):
    def test_missing_required_files_are_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            errors = repo_health_check.check_required_files(Path(tmp))
            self.assertTrue(any("README.md" in error for error in errors))

    def test_stale_mechanical_expansion_artifacts_are_not_required(self):
        self.assertNotIn("docs/review/mechanical-research-expansion-report.md", repo_health_check.REQUIRED_FILES)
        self.assertNotIn(
            "docs/review/mechanical-research-expansion-manifest.json",
            repo_health_check.REQUIRED_FILES,
        )

    def test_secret_pattern_detects_private_key(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bad = root / "bad.md"
            bad.write_text("-----BEGIN " + "PRIVATE KEY-----\nnope\n", encoding="utf-8")
            errors = repo_health_check.check_secret_patterns(root)
            self.assertTrue(errors)


class PowerShellHelperTests(unittest.TestCase):
    @unittest.skipUnless(PWSH, "PowerShell is required")
    def test_powershell_skill_installer_writes_expected_project_skill(self):
        installer = ROOT / "scripts" / "install_skill.ps1"
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [
                    PWSH,
                    "-NoProfile",
                    "-ExecutionPolicy",
                    "Bypass",
                    "-File",
                    str(installer),
                    "-Skill",
                    "use-codex-safely",
                    "-Harness",
                    "codex-cli",
                ],
                cwd=tmp,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )

            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            installed = Path(tmp) / ".agents" / "skills" / "use-codex-safely" / "SKILL.md"
            self.assertTrue(installed.is_file())
            text = installed.read_text(encoding="utf-8-sig")
            self.assertTrue(text.startswith("---\n") or text.startswith("---\r\n"))
            self.assertIn("name: use-codex-safely", text)

    @unittest.skipUnless(PWSH and GIT, "PowerShell and Git are required")
    def test_create_task_branch_creates_then_reuses_branch_in_temp_repo(self):
        branch_script = ROOT / "scripts" / "create_task_branch.ps1"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            subprocess.run([GIT, "init", "-b", "main"], cwd=root, check=True, capture_output=True)
            subprocess.run(
                [GIT, "config", "user.name", "Branch Helper Test"],
                cwd=root,
                check=True,
                capture_output=True,
            )
            subprocess.run(
                [GIT, "config", "user.email", "branch-helper@example.invalid"],
                cwd=root,
                check=True,
                capture_output=True,
            )
            (root / "README.md").write_text("baseline\n", encoding="utf-8")
            subprocess.run([GIT, "add", "README.md"], cwd=root, check=True, capture_output=True)
            subprocess.run(
                [GIT, "commit", "-m", "baseline"], cwd=root, check=True, capture_output=True
            )

            command = [
                PWSH,
                "-NoProfile",
                "-ExecutionPolicy",
                "Bypass",
                "-File",
                str(branch_script),
                "-Name",
                "My reviewed task",
            ]
            first = subprocess.run(
                command,
                cwd=root,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )
            second = subprocess.run(
                command,
                cwd=root,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )

            self.assertEqual(0, first.returncode, first.stdout + first.stderr)
            self.assertEqual(0, second.returncode, second.stdout + second.stderr)
            branch = subprocess.run(
                [GIT, "branch", "--show-current"],
                cwd=root,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
            ).stdout.strip()
            self.assertEqual("agent/my-reviewed-task", branch)
            self.assertIn("already exists", second.stdout)
            self.assertIn("Using branch: agent/my-reviewed-task", second.stdout)


class WorkflowRuntimeTests(unittest.TestCase):
    def test_ci_has_windows_local_powershell_gate(self):
        workflow = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
        windows_job = re.search(
            r"(?ms)^  windows-runtime:\r?\n(.*?)(?=^  [A-Za-z0-9_-]+:\r?\n|\Z)",
            workflow,
        )
        self.assertIsNotNone(windows_job)
        section = windows_job.group(0)
        self.assertRegex(section, r"(?m)^    runs-on: windows-latest\s*$")
        run_commands = re.findall(r"(?m)^        run:\s*([^#\r\n]+?)\s*$", section)
        self.assertIn("pwsh -NoProfile -File scripts/local_check.ps1", run_commands)

    def test_all_first_party_actions_are_immutable_and_version_commented(self):
        expected = {
            "actions/checkout": (CHECKOUT_SHA, "v4.3.1"),
            "actions/setup-python": (SETUP_PYTHON_SHA, "v5.6.0"),
        }
        uses_pattern = re.compile(
            r"(?m)^\s*uses:\s+(actions/(?:checkout|setup-python))@([^\s#]+)\s+#\s+(v\d+\.\d+\.\d+)\s*$"
        )
        found = 0
        workflow_root = ROOT / ".github" / "workflows"
        workflows = sorted({*workflow_root.glob("*.yml"), *workflow_root.glob("*.yaml")})
        for workflow in workflows:
            text = workflow.read_text(encoding="utf-8")
            action_lines = [
                line
                for line in text.splitlines()
                if re.search(r"uses:\s+actions/(?:checkout|setup-python)@", line)
            ]
            matches = list(uses_pattern.finditer(text))
            self.assertEqual(
                len(action_lines),
                len(matches),
                f"mutable or unversioned action reference in {workflow.name}",
            )
            for match in matches:
                action, sha, version = match.groups()
                with self.subTest(workflow=workflow.name, action=action):
                    self.assertRegex(sha, r"^[0-9a-f]{40}$")
                    self.assertEqual(expected[action], (sha, version))
                found += 1
        self.assertGreater(found, 0)


if __name__ == "__main__":
    unittest.main()
