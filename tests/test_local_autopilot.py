"""Tests for the local autopilot script, public README framing, and deployment files.

These tests read files as text. They guard the behaviors the public workbench
promises without requiring PowerShell, GitHub CLI, or a network connection.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "local_autopilot.ps1"
README = ROOT / "README.md"
LOCAL_AUTOPILOT_DOC = ROOT / "docs" / "automation" / "local-autopilot.md"
WORKFLOWS = ROOT / ".github" / "workflows"

# Owner-specific hardware framing that must not appear in the public README.
BANNED_README_TERMS = (
    "lightweight laptop",
    "weak laptop",
    "weak Windows laptop",
    "student laptop",
    "modest-laptop",
    "MX-class",
    "8 GB RAM",
    "2 GB VRAM",
    "limited Windows laptop",
)


def read(path):
    return path.read_text(encoding="utf-8")


class LocalAutopilotScriptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = read(SCRIPT)

    def test_default_branch_is_curate_research_guides(self):
        # The -Branch parameter must default to the documented branch so
        # local-codex and full-safe work without the caller passing a branch.
        self.assertRegex(
            self.text,
            r'\[string\]\$Branch\s*=\s*"codex/curate-research-guides"',
        )

    def test_does_not_use_branchname_variable(self):
        # The old helper used $BranchName, which masked the real fix and caused
        # confusion with the -Branch parameter. It must be gone entirely.
        self.assertNotIn("$BranchName", self.text)

    def test_does_not_trim_branch_list_result_directly(self):
        # The reported crash was `(& git branch --list ...).Trim()` throwing on a
        # null result. Calling .Trim() on the raw branch-list output is forbidden.
        self.assertIsNone(
            re.search(r"git branch --list[^\n]*\)\s*\.Trim\(", self.text),
            "Do not call .Trim() directly on the git branch --list result.",
        )

    def test_branch_lookup_is_null_safe(self):
        # The replacement must coerce/guard before treating the result as text.
        self.assertIn("Test-BranchExists", self.text)
        self.assertIn("IsNullOrWhiteSpace", self.text)

    def test_supports_required_modes(self):
        for mode in ("status", "scout", "prompt", "local-codex", "local-claude", "full-safe"):
            with self.subTest(mode=mode):
                self.assertIn(f'"{mode}"', self.text)

    def test_mode_validateset_includes_local_claude(self):
        match = re.search(r"\[ValidateSet\(([^)]*)\)\]\s*\r?\n\s*\[string\]\$Mode", self.text)
        self.assertIsNotNone(match, "Could not find the ValidateSet for -Mode.")
        self.assertIn("local-claude", match.group(1))
        self.assertIn("local-codex", match.group(1))

    def test_local_claude_default_branch_documented_in_script(self):
        # local-claude must fall back to its own default branch.
        self.assertIn("claude/curate-research-guides", self.text)

    def test_uses_per_agent_default_branch_resolution(self):
        # Defaults are only applied when the caller omitted -Branch.
        self.assertIn('$PSBoundParameters.ContainsKey("Branch")', self.text)

    def test_merges_main_with_ff_only(self):
        self.assertRegex(self.text, r"git merge --ff-only main")

    def test_does_not_perform_forbidden_git_actions(self):
        # The script must never merge PRs, force-push, or delete branches.
        self.assertNotIn("push --force", self.text)
        self.assertNotIn("--force-with-lease", self.text)
        self.assertNotIn("branch -D", self.text)
        self.assertNotIn("branch -d", self.text)
        self.assertNotIn("pr merge", self.text)

    def test_refuses_dirty_tree_unless_allowed(self):
        self.assertIn("Assert-CleanTree", self.text)
        self.assertIn("AllowDirty", self.text)


class ReadmePublicFramingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = read(README)

    def test_readme_has_no_personal_laptop_constraints(self):
        for term in BANNED_README_TERMS:
            with self.subTest(term=term):
                self.assertNotIn(term, self.text)

    def test_local_autopilot_doc_documents_local_claude_mode(self):
        self.assertIn("-Mode local-claude", read(LOCAL_AUTOPILOT_DOC))

    def test_local_autopilot_doc_documents_claude_code_local_workflow(self):
        text = read(LOCAL_AUTOPILOT_DOC)
        self.assertIn("claude/curate-research-guides", text)
        self.assertIn("Claude Code", text)


class DeploymentAndDocsExistenceTests(unittest.TestCase):
    def test_offline_site_files_exist(self):
        required = [
            "docs/site/index.html",
            "docs/site/agent-workflow.html",
            "docs/site/prompt-engineering.html",
            "docs/site/skills-and-tools.html",
            "docs/site/styles.css",
        ]
        for relative in required:
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / relative).is_file())

    def test_offline_site_has_no_external_assets(self):
        # The site is offline-first by design: no CDN, analytics, or remote fonts.
        index = read(ROOT / "docs" / "site" / "index.html")
        self.assertNotIn("http://", index)
        self.assertNotIn("https://", index)

    def test_automation_docs_exist(self):
        required = [
            "docs/automation/repository-autopilot.md",
            "docs/automation/local-autopilot.md",
            "docs/automation/safe-automerge-policy.md",
            "docs/automation/release-draft-policy.md",
        ]
        for relative in required:
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / relative).is_file())

    def test_claude_code_tool_doc_exists(self):
        self.assertTrue((ROOT / "docs" / "tools" / "claude-code.md").is_file())


class WorkflowSafetyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = "\n".join(
            read(path) for path in sorted(WORKFLOWS.glob("*.yml"))
        )

    def test_no_openai_api_key(self):
        self.assertNotIn("OPENAI" + "_API_KEY", self.text)

    def test_no_codex_action(self):
        self.assertNotIn("openai/" + "codex-action", self.text)

    def test_workflows_do_not_run_codex(self):
        self.assertIsNone(re.search(r"(?im)^\s*run:\s*codex(?:\s|$)", self.text))
        self.assertNotIn("Run Codex", self.text)

    def test_safe_generated_automerge_policy_present(self):
        # The generated-file-only automerge guard must stay in place.
        automerge = read(WORKFLOWS / "automerge-safe-generated.yml")
        self.assertIn("check_safe_generated_diff.py", automerge)
        self.assertTrue((ROOT / "scripts" / "check_safe_generated_diff.py").is_file())


if __name__ == "__main__":
    unittest.main()
