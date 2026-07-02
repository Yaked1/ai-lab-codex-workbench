import tempfile
import unittest
from pathlib import Path
import importlib.util

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "safe_autofix.py"
spec = importlib.util.spec_from_file_location("safe_autofix", SCRIPT)
safe_autofix = importlib.util.module_from_spec(spec)
spec.loader.exec_module(safe_autofix)


class SafeAutofixTests(unittest.TestCase):
    def test_normalize_text_trims_trailing_whitespace_and_final_newline(self):
        raw = "hello   \r\nworld\t\r\n\r\n"
        self.assertEqual(safe_autofix.normalize_text(raw), "hello\nworld\n")

    def test_process_file_reports_change(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.md"
            path.write_text("Title   ", encoding="utf-8")
            changed = safe_autofix.process_file(path, write=True)
            self.assertTrue(changed)
            self.assertEqual(path.read_text(encoding="utf-8"), "Title\n")


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
