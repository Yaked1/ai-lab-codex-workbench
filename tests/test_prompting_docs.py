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
    "docs/guides/prompting-ai-coding-agents.md",
    "docs/guides/coding-agent-power-tips.md",
    "docs/guides/prompting-references.md",
)

# Docs that may reference /goal as an example custom slash command.
GOAL_DOCS = (
    "README.md",
    "docs/tools/claude-code.md",
    "docs/automation/local-autopilot.md",
    "docs/guides/coding-agent-power-tips.md",
)


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


class PromptingGuidesContentTests(unittest.TestCase):
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


class PromptingGuidesReadmeLinkageTests(unittest.TestCase):
    def test_readme_links_every_guide(self):
        readme = read("README.md")
        for relative in GUIDES:
            with self.subTest(relative=relative):
                self.assertIn(relative, readme)

    def test_readme_has_prompting_section(self):
        readme = read("README.md")
        self.assertIn("Prompting And Agent Mastery", readme)


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
