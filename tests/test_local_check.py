"""Behavior tests for the local PowerShell verification gate."""

from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "local_check.ps1"
PWSH = shutil.which("pwsh")


@unittest.skipUnless(PWSH, "PowerShell is required")
class LocalCheckTests(unittest.TestCase):
    def run_local_check(
        self, health_exit: int = 0, autofix_exit: int = 0, tests_exit: int = 0
    ) -> tuple[subprocess.CompletedProcess[str], list[str]]:
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary = Path(temporary_directory)
            log_path = temporary / "python-invocations.log"
            shim_path = temporary / "python.cmd"
            shim_path.write_text(
                "\r\n".join(
                    (
                        "@echo off",
                        "setlocal DisableDelayedExpansion",
                        'echo %*>> "%LOCAL_CHECK_SHIM_LOG%"',
                        'if "%~1"=="scripts/repo_health_check.py" exit /b %LOCAL_CHECK_HEALTH_EXIT%',
                        'if "%~1"=="scripts/safe_autofix.py" exit /b %LOCAL_CHECK_AUTOFIX_EXIT%',
                        'if "%~1"=="-m" exit /b %LOCAL_CHECK_TESTS_EXIT%',
                        "exit /b 99",
                    )
                ),
                encoding="ascii",
            )

            environment = os.environ.copy()
            environment.update(
                {
                    "LOCAL_CHECK_SHIM_LOG": str(log_path),
                    "LOCAL_CHECK_HEALTH_EXIT": str(health_exit),
                    "LOCAL_CHECK_AUTOFIX_EXIT": str(autofix_exit),
                    "LOCAL_CHECK_TESTS_EXIT": str(tests_exit),
                    "PATH": str(temporary) + os.pathsep + environment["PATH"],
                }
            )
            result = subprocess.run(
                [
                    PWSH,
                    "-NoProfile",
                    "-ExecutionPolicy",
                    "Bypass",
                    "-File",
                    str(SCRIPT),
                ],
                cwd=ROOT,
                env=environment,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )
            invocations = (
                log_path.read_text(encoding="utf-8").splitlines()
                if log_path.exists()
                else []
            )
        return result, invocations

    def assert_failed_command(
        self, result: subprocess.CompletedProcess[str], invocations: list[str], exit_code: int, expected_invocations: list[str]
    ) -> None:
        self.assertEqual(exit_code, result.returncode, result.stdout + result.stderr)
        self.assertEqual(expected_invocations, invocations)
        self.assertNotIn("All local checks passed.", result.stdout)

    def test_stops_after_first_child_failure(self) -> None:
        result, invocations = self.run_local_check(health_exit=17)

        self.assert_failed_command(
            result,
            invocations,
            17,
            ["scripts/repo_health_check.py"],
        )

    def test_stops_after_second_child_failure(self) -> None:
        result, invocations = self.run_local_check(autofix_exit=18)

        self.assert_failed_command(
            result,
            invocations,
            18,
            ["scripts/repo_health_check.py", "scripts/safe_autofix.py --check"],
        )

    def test_stops_after_third_child_failure(self) -> None:
        result, invocations = self.run_local_check(tests_exit=19)

        self.assert_failed_command(
            result,
            invocations,
            19,
            [
                "scripts/repo_health_check.py",
                "scripts/safe_autofix.py --check",
                "-m unittest discover -s tests",
            ],
        )

    def test_runs_all_commands_then_reports_success_once(self) -> None:
        result, invocations = self.run_local_check()

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual(
            [
                "scripts/repo_health_check.py",
                "scripts/safe_autofix.py --check",
                "-m unittest discover -s tests",
            ],
            invocations,
        )
        self.assertEqual(1, result.stdout.count("All local checks passed."))


if __name__ == "__main__":
    unittest.main()
