"""Tests for the prompting curriculum docs, their README linkage, and packaging.

These guards keep the prompting guides present, public-safe, linked from the
README, and bundled inside the release package.
"""
import importlib.util
import subprocess
import sys
import tempfile
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

CORE_PROMPTS = {
    "prompts/aider/agent-task.md",
    "prompts/antigravity/agent-task.md",
    "prompts/claude/agent-reach-search.md",
    "prompts/claude-code/review-docs.goal.md",
    "prompts/codex/docs-update.goal.md",
    "prompts/codex/fix-bug.goal.md",
    "prompts/codex/implement-feature.goal.md",
    "prompts/codex/review-pr.goal.md",
    "prompts/cursor/agent-task.md",
    "prompts/github-copilot/agent-task.md",
    "prompts/opencode/agent-task.md",
    "prompts/windsurf/agent-task.md",
}


def load_script(name):
    script = ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


discover_ai_sources = load_script("discover_ai_sources")
build_release_package = load_script("build_release_package")
mechanical_research_expansion = load_script("mechanical_research_expansion")


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

    def test_readme_is_focused_public_entry_point(self):
        readme = read("README.md")
        for needle in (
            "Start Here",
            "Quick Start",
            "Prompting And Agent Mastery",
            "Prompting OS",
            "Coding-agent workflow",
            "Source-grounded writing",
            "Evaluation",
            "Current Model Guides",
            "Repository Map",
            "Automation",
            "Public Safety",
            "Troubleshooting",
            "Contributing",
        ):
            with self.subTest(needle=needle):
                self.assertIn(needle, readme)


class PromptTemplateCompletenessTests(unittest.TestCase):
    def test_prompt_templates_include_operational_sections(self):
        prompt_files = sorted((ROOT / "prompts").rglob("*.md"))
        prompt_paths = {path.relative_to(ROOT).as_posix() for path in prompt_files}
        self.assertTrue(
            CORE_PROMPTS.issubset(prompt_paths),
            f"missing core prompt(s): {sorted(CORE_PROMPTS - prompt_paths)}",
        )

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


class MechanicalResearchExpansionStripTests(unittest.TestCase):
    begin = mechanical_research_expansion.MARKER_BEGIN
    end = mechanical_research_expansion.MARKER_END

    def marked(self, opening: str, closing: str, body: str = "generated note") -> str:
        return f"{opening}{self.begin}{body}{self.end}{closing}"

    def test_markdown_strip_preserves_unique_content(self):
        text = (
            "# Keep this heading\n\n"
            + self.marked("<!-- ", " -->", " -->\n## Generated\n\nGenerated only\n<!-- ")
            + "\n\nUnique tail\n"
        )

        stripped = mechanical_research_expansion.strip_text("guide.md", text)

        self.assertEqual("# Keep this heading\n\nUnique tail\n", stripped)

    def test_python_and_yaml_line_comment_blocks_strip(self):
        for relative in ("script.py", "workflow.yml"):
            with self.subTest(relative=relative):
                text = (
                    "keep_before\n\n"
                    f"# {self.begin}\n"
                    "# generated only\n"
                    f"# {self.end}\n\n"
                    "keep_after\n"
                )

                stripped = mechanical_research_expansion.strip_text(relative, text)

                self.assertEqual("keep_before\n\nkeep_after\n", stripped)

    def test_powershell_block_comment_strips(self):
        text = (
            "Write-Host 'keep'\n\n"
            "<#\n"
            f"{self.begin}\n"
            "Generated only\n"
            f"{self.end}\n"
            "#>\n"
        )

        stripped = mechanical_research_expansion.strip_text("check.ps1", text)

        self.assertEqual("Write-Host 'keep'\n", stripped)

    def test_html_section_and_svg_comment_strip(self):
        html = (
            "<main>\n"
            "  <p>keep</p>\n\n"
            f"  <!-- {self.begin} -->\n"
            "  <section class=\"research-grade-addendum\">generated</section>\n"
            f"  <!-- {self.end} -->\n\n"
            "</main>\n"
        )
        svg = (
            "<svg>\n"
            f"  <!-- {self.begin}\n"
            "  generated\n"
            f"  {self.end} -->\n\n"
            "  <rect />\n"
            "</svg>\n"
        )

        self.assertEqual(
            "<main>\n  <p>keep</p>\n\n</main>\n",
            mechanical_research_expansion.strip_text("page.html", html),
        )
        self.assertEqual(
            "<svg>\n  <rect />\n</svg>\n",
            mechanical_research_expansion.strip_text("diagram.svg", svg),
        )

    def test_css_removes_only_exact_generated_rule(self):
        text = (
            "body { color: black; }\n\n"
            f"/* {self.begin}\n"
            "generated\n"
            f"{self.end} */\n\n"
            ".research-grade-addendum {\n"
            "  border-top: 1px solid #d8dee8;\n"
            "  margin-top: 2rem;\n"
            "  padding-top: 1rem;\n"
            "}\n\n"
            ".research-grade-addendum { color: red; }\n"
        )

        stripped = mechanical_research_expansion.strip_text("styles.css", text)

        self.assertEqual(
            "body { color: black; }\n\n.research-grade-addendum { color: red; }\n",
            stripped,
        )

    def test_css_terminal_generated_content_does_not_leave_blank_eof(self):
        text = (
            "body { color: black; }\n\n"
            f"/* {self.begin}\n"
            "generated\n"
            f"{self.end} */\n\n"
            ".research-grade-addendum {\n"
            "  border-top: 1px solid #d8dee8;\n"
            "  margin-top: 2rem;\n"
            "  padding-top: 1rem;\n"
            "}\n"
        )

        stripped = mechanical_research_expansion.strip_text("styles.css", text)

        self.assertEqual("body { color: black; }\n", stripped)
        self.assertFalse(stripped.endswith("\n\n"))

    def test_malformed_markers_fail_closed_and_name_path(self):
        for relative, text in (
            ("unclosed.md", f"before\n<!-- {self.begin} -->\n"),
            ("out-of-order.py", f"# {self.end}\n# {self.begin}\n"),
        ):
            with self.subTest(relative=relative):
                with self.assertRaisesRegex(ValueError, relative):
                    mechanical_research_expansion.strip_text(relative, text)

    def test_strip_is_idempotent_and_preserves_final_newline_state(self):
        for ending in ("\n", ""):
            with self.subTest(ending=repr(ending)):
                text = (
                    "before\n\n"
                    f"<!-- {self.begin} -->\nGenerated\n<!-- {self.end} -->\n\n"
                    f"after{ending}"
                )
                stripped = mechanical_research_expansion.strip_text("guide.md", text)

                self.assertEqual(f"before\n\nafter{ending}", stripped)
                self.assertEqual(stripped, mechanical_research_expansion.strip_text("guide.md", stripped))

    def test_default_check_is_read_only_and_write_then_check_is_clean(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "README.md").write_text(
                f"keep\n<!-- {self.begin} -->\nGenerated\n<!-- {self.end} -->\n",
                encoding="utf-8",
            )
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            subprocess.run(["git", "add", "README.md"], cwd=root, check=True)

            command = [sys.executable, str(ROOT / "scripts" / "mechanical_research_expansion.py"), "--root", str(root)]
            before = (root / "README.md").read_text(encoding="utf-8")
            audit = subprocess.run(command, text=True, capture_output=True, check=False)

            self.assertNotEqual(0, audit.returncode)
            self.assertIn("README.md", audit.stdout + audit.stderr)
            self.assertEqual(before, (root / "README.md").read_text(encoding="utf-8"))

            write = subprocess.run(command + ["--write"], text=True, capture_output=True, check=False)
            self.assertEqual(0, write.returncode, write.stdout + write.stderr)
            self.assertNotIn(self.begin, (root / "README.md").read_text(encoding="utf-8"))

            second_write = subprocess.run(command + ["--write"], text=True, capture_output=True, check=False)
            self.assertEqual(0, second_write.returncode, second_write.stdout + second_write.stderr)
            self.assertIn("0 changed", second_write.stdout)

            clean_audit = subprocess.run(command + ["--check"], text=True, capture_output=True, check=False)
            self.assertEqual(0, clean_audit.returncode, clean_audit.stdout + clean_audit.stderr)

    def test_live_root_scan_is_clean_across_all_approved_tracked_paths(self):
        errors, changes = mechanical_research_expansion.scan_repo(ROOT)

        self.assertEqual([], errors)
        self.assertEqual([], changes)

    def test_cli_malformed_marker_fails_without_mutating_bytes(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            malformed = root / "malformed.md"
            original = f"keep\n<!-- {self.begin} -->\n".encode("utf-8")
            malformed.write_bytes(original)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            subprocess.run(["git", "add", "malformed.md"], cwd=root, check=True)

            base_command = [
                sys.executable,
                str(ROOT / "scripts" / "mechanical_research_expansion.py"),
                "--root",
                str(root),
            ]
            for suffix in ([], ["--check"]):
                with self.subTest(suffix=suffix):
                    result = subprocess.run(
                        base_command + suffix,
                        text=True,
                        capture_output=True,
                        check=False,
                    )

                    self.assertNotEqual(0, result.returncode)
                    self.assertIn("malformed.md", result.stdout + result.stderr)
                    self.assertEqual(original, malformed.read_bytes())

    def test_deleted_mechanical_expansion_artifacts_are_absent(self):
        for relative in (
            "docs/review/mechanical-research-expansion-report.md",
            "docs/review/mechanical-research-expansion-manifest.json",
        ):
            with self.subTest(relative=relative):
                self.assertFalse((ROOT / relative).exists())


if __name__ == "__main__":
    unittest.main()
