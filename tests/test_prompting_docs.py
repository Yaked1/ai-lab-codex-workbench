"""Tests for the prompting curriculum docs, their README linkage, and packaging.

These guards keep the prompting guides present, public-safe, linked from the
README, and bundled inside the release package.
"""
import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

GUIDES = (
    "docs/guides/comprehensive-prompt-engineering-guide.md",
    "docs/guides/prompting-ai-coding-agents.md",
    "docs/guides/coding-agent-power-tips.md",
    "docs/guides/prompting-references.md",
    "docs/guides/source-inspired-prompting-curriculum.md",
)

WORKFLOW_GUIDES = (
    "docs/workflows/agent-task-lifecycle.md",
    "docs/workflows/public-repo-safety.md",
    "docs/workflows/research-grade-repository-expansion.md",
)

# Docs that may reference /goal as an example custom slash command.
GOAL_DOCS = (
    "README.md",
    "docs/tools/claude-code.md",
    "docs/automation/local-autopilot.md",
    "docs/guides/coding-agent-power-tips.md",
)

PROMPT_REQUIRED_SECTIONS = {
    "Target tool": ("## Target Tool",),
    "Purpose": ("## Purpose",),
    "Inputs to fill": ("## Inputs To Fill",),
    "Full prompt": ("## Full Prompt", "## Full Prompt / Issue Body"),
    "Short version": ("## Short Version",),
    "Included scope": ("## Included Scope",),
    "Excluded scope": ("## Excluded Scope",),
    "Safety boundaries": ("## Safety Boundaries",),
    "Verification steps": ("## Verification Steps", "## Verification"),
    "Success criteria": ("## Success Criteria",),
    "Final report format": ("## Final Report Format",),
    "Failure cases": ("## Failure Cases",),
}


def load_script(name):
    script = ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


discover_ai_sources = load_script("discover_ai_sources")
build_release_package = load_script("build_release_package")


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


class PromptingGuidesExistTests(unittest.TestCase):
    def test_guides_exist(self):
        for relative in GUIDES:
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / relative).is_file())

    def test_guides_end_with_newline(self):
        for relative in GUIDES:
            with self.subTest(relative=relative):
                self.assertTrue(read(relative).endswith("\n"))

    def test_workflow_guides_exist(self):
        for relative in WORKFLOW_GUIDES:
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / relative).is_file())


class PromptingGuidesContentTests(unittest.TestCase):
    def test_comprehensive_guide_covers_prompt_engineering_system(self):
        text = read("docs/guides/comprehensive-prompt-engineering-guide.md")
        for needle in (
            "Prompt Anatomy",
            "Context Engineering",
            "Reusable Prompt Functions",
            "Agentic Prompting",
            "Evaluation and Regression Testing",
            "Prompt Security",
            "Image Prompting",
            "Prompt Management in Repositories",
        ):
            with self.subTest(needle=needle):
                self.assertIn(needle, text)

    def test_craft_guide_covers_core_techniques(self):
        text = read("docs/guides/prompting-ai-coding-agents.md")
        for needle in ("work order", "Decompose", "Verification", "context window", "Anti-Pattern"):
            with self.subTest(needle=needle):
                self.assertIn(needle, text)

    def test_power_tips_cover_major_agents(self):
        text = read("docs/guides/coding-agent-power-tips.md")
        for agent in ("Claude Code", "Codex", "Cursor", "GitHub Copilot", "Aider", "Windsurf", "MCP"):
            with self.subTest(agent=agent):
                self.assertIn(agent, text)

    def test_references_lead_with_official_and_flag_leaks(self):
        text = read("docs/guides/prompting-references.md")
        self.assertIn("Official Vendor Guides", text)
        self.assertIn("dair-ai", text)
        self.assertIn("promptfoo", text)
        # Leaked-prompt collections must be handled as structural-only, not headlined.
        self.assertIn("never copy the contents", text)
        self.assertIn("source-policy", text)

    def test_guides_have_no_secret_looking_strings(self):
        for relative in GUIDES:
            with self.subTest(relative=relative):
                self.assertFalse(discover_ai_sources.has_secret_looking_text(read(relative)))

    def test_research_grade_expansion_workflow_has_operational_depth(self):
        text = read("docs/workflows/research-grade-repository-expansion.md")
        for needle in (
            "What Research-Grade Means Here",
            "Expansion Scope Model",
            "Evidence Levels",
            "Comprehensiveness Rubric",
            "File-Class Expansion Playbooks",
            "Research-Grade Expansion Procedure",
            "Public-Safety Review For Broad Expansions",
            "Failure Modes",
            "Review Checklist",
            "Final Report Template",
        ):
            with self.subTest(needle=needle):
                self.assertIn(needle, text)


class PromptingGuidesReadmeLinkageTests(unittest.TestCase):
    def test_readme_links_every_guide(self):
        readme = read("README.md")
        for relative in GUIDES:
            with self.subTest(relative=relative):
                self.assertIn(relative, readme)

    def test_readme_has_prompting_section(self):
        readme = read("README.md")
        self.assertIn("Prompting And Agent Mastery", readme)

    def test_research_grade_workflow_is_linked_from_core_policy_docs(self):
        for relative in ("README.md", "AGENTS.md", "CONTRIBUTING.md"):
            with self.subTest(relative=relative):
                self.assertIn("research-grade-repository-expansion.md", read(relative))

    def test_security_has_broad_expansion_review_gate(self):
        security = read("SECURITY.md")
        for needle in (
            "Broad Expansion Security Review",
            "Examples",
            "Agent permissions",
            "Source usage",
            "Staging",
        ):
            with self.subTest(needle=needle):
                self.assertIn(needle, security)

    def test_readme_is_comprehensive_public_manual(self):
        readme_path = ROOT / "README.md"
        readme = read("README.md")
        self.assertGreaterEqual(readme_path.stat().st_size, 50_000)
        for needle in (
            "Table Of Contents",
            "Prompting OS",
            "Core Workflow",
            "Context Engineering",
            "Evaluation And Regression",
            "Automation And Release Packages",
            "Public Safety Rules",
            "Maintainer Playbook",
            "Repository Operating Manual",
            "Package Evidence Model",
            "Evidence Quick Reference",
        ):
            with self.subTest(needle=needle):
                self.assertIn(needle, readme)


class PromptTemplateCompletenessTests(unittest.TestCase):
    def test_prompt_templates_include_operational_sections(self):
        prompt_files = sorted((ROOT / "prompts").rglob("*.md"))
        self.assertGreaterEqual(len(prompt_files), 10)

        for path in prompt_files:
            text = path.read_text(encoding="utf-8")
            relative = path.relative_to(ROOT).as_posix()
            for label, aliases in PROMPT_REQUIRED_SECTIONS.items():
                with self.subTest(prompt=relative, section=label):
                    self.assertTrue(
                        any(alias in text for alias in aliases),
                        f"{relative} is missing {label}",
                    )


class GoalCustomCommandTests(unittest.TestCase):
    """The task asked for /goal-style usage; keep it, but never as a built-in."""

    def test_goal_is_framed_as_user_defined_command(self):
        # Wherever /goal appears it must co-occur with the custom-command
        # directory, proving it is presented as a command you define, not a
        # native Claude Code command.
        for relative in GOAL_DOCS:
            text = read(relative)
            if "/goal" in text:
                with self.subTest(relative=relative):
                    self.assertIn(".claude/commands", text)

    def test_readme_keeps_goal_style_usage(self):
        readme = read("README.md")
        self.assertIn("/goal", readme)
        self.assertIn(".claude/commands", readme)


class PromptingGuidesPackagingTests(unittest.TestCase):
    def test_guides_are_included_in_release_package(self):
        included = {path.relative_to(ROOT).as_posix() for path in build_release_package.iter_package_files(ROOT)}
        for relative in GUIDES:
            with self.subTest(relative=relative):
                self.assertIn(relative, included)


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
