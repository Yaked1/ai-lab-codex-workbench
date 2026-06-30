import tempfile
import unittest
from pathlib import Path
import importlib.util

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "repo_health_check.py"
spec = importlib.util.spec_from_file_location("repo_health_check", SCRIPT)
repo_health_check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(repo_health_check)


class RepoHealthTests(unittest.TestCase):
    def test_missing_required_files_are_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            errors = repo_health_check.check_required_files(Path(tmp))
            self.assertTrue(any("README.md" in error for error in errors))

    def test_secret_pattern_detects_private_key(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bad = root / "bad.md"
            bad.write_text("-----BEGIN " + "PRIVATE KEY-----\nnope\n", encoding="utf-8")
            errors = repo_health_check.check_secret_patterns(root)
            self.assertTrue(errors)


class PowerShellHelperTests(unittest.TestCase):
    def test_create_task_branch_reuses_existing_branch(self):
        script = (Path(__file__).resolve().parents[1] / "scripts" / "create_task_branch.ps1").read_text(
            encoding="utf-8"
        )
        self.assertIn("git branch --list $Branch", script)
        self.assertIn("git checkout $Branch", script)
        self.assertIn("git checkout -b $Branch", script)
        self.assertIn("Using branch: $Branch", script)


if __name__ == "__main__":
    unittest.main()
