"""Regression tests for onboarding, governance, offline site, and starter scope."""

from __future__ import annotations

import re
import subprocess
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
CORE_SITE_PAGES = (
    "docs/site/index.html",
    "docs/site/agent-workflow.html",
    "docs/site/prompt-engineering.html",
    "docs/site/skills-and-tools.html",
)
STARTER_FILES = {
    "starter/README.md",
    "starter/task-template.md",
    "starter/safety-rules.md",
    "starter/evaluation.md",
    "starter/example/task.md",
    "starter/example/expected-report.md",
}
FIRST_TASK_FILES = {
    "examples/first-reviewed-agent-task/README.md",
    "examples/first-reviewed-agent-task/task-input.md",
    "examples/first-reviewed-agent-task/work-order.md",
    "examples/first-reviewed-agent-task/expected-report.md",
    "examples/first-reviewed-agent-task/report.md",
    "examples/first-reviewed-agent-task/check_report.py",
}


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if value and name in {"href", "src"}:
                self.links.append((name, value))


class FirstSuccessTests(unittest.TestCase):
    def test_readme_has_exactly_three_primary_routes(self) -> None:
        section = read("README.md").split("## Start Here", 1)[1].split("## Quick Start", 1)[0]
        rows = re.findall(r"^\| \*\*(.+?)\*\* \|", section, flags=re.MULTILINE)
        self.assertEqual(["Run a task", "Learn prompting", "Contribute"], rows)

    def test_first_task_files_exist_and_checker_passes(self) -> None:
        for relative in FIRST_TASK_FILES:
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / relative).is_file())
        result = subprocess.run(
            [sys.executable, "examples/first-reviewed-agent-task/check_report.py"],
            cwd=ROOT,
            check=True,
            text=True,
            capture_output=True,
        )
        self.assertEqual("PASS: first reviewed agent report satisfies the contract", result.stdout.strip())

    def test_prompting_os_offers_bounded_tracks(self) -> None:
        text = read("docs/prompting-os/README.md")
        for needle in ("First working prompt", "15 minutes", "About one hour", "Maintainer reference"):
            self.assertIn(needle, text)
        self.assertIn("docs/prompting-os/00-first-success.md", read("README.md"))

    def test_redundant_cleanup_prompt_is_retired(self) -> None:
        retired = "prompts/codex/repo-cleanup-balanced-goal.md"
        self.assertFalse((ROOT / retired).exists())
        for path in ROOT.rglob("*"):
            if (
                not path.is_file()
                or ".git" in path.parts
                or path.suffix.lower() in {".pyc", ".zip"}
                or path.name == "gpt_instructions.txt"
                or path == Path(__file__).resolve()
            ):
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            with self.subTest(path=path.relative_to(ROOT).as_posix()):
                self.assertNotIn(retired, text)


class GovernanceTests(unittest.TestCase):
    def test_required_community_files_exist(self) -> None:
        for relative in (
            "CODE_OF_CONDUCT.md",
            "SUPPORT.md",
            "CITATION.cff",
            "docs/maintenance/branch-policy.md",
            "docs/maintenance/github-owner-settings.md",
        ):
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / relative).is_file())

    def test_claude_is_a_thin_adapter_to_agents(self) -> None:
        text = read("CLAUDE.md")
        self.assertLess(len(text.splitlines()), 80)
        self.assertIn("`AGENTS.md` is the authoritative repository instruction file", text)
        for boundary in ("untrusted data", "Preserve unrelated", "dated", "smallest relevant verification"):
            self.assertIn(boundary, text)

    def test_changelog_keeps_unreleased_first(self) -> None:
        headings = re.findall(r"^## (.+)$", read("CHANGELOG.md"), flags=re.MULTILINE)
        self.assertTrue(headings)
        self.assertEqual("Unreleased", headings[0])
        self.assertIn("Repository audit remediation", read("CHANGELOG.md"))

    def test_citation_metadata_has_core_fields(self) -> None:
        text = read("CITATION.cff")
        for line in (
            "cff-version: 1.2.0",
            "title: AI Prompting and Coding Agent Workbench",
            "type: software",
            "repository-code:",
            "license: MIT",
        ):
            self.assertIn(line, text)

    def test_issue_forms_are_bounded_and_good_first_issue_is_reviewable(self) -> None:
        forms = sorted((ROOT / ".github" / "ISSUE_TEMPLATE").glob("*.yml"))
        self.assertGreaterEqual(len(forms), 3)
        self.assertLessEqual(len(forms), 5)
        text = read(".github/ISSUE_TEMPLATE/good_first_issue.yml")
        for field in ("file_scope", "outcome", "acceptance_command", "safety_boundary", "review_effort"):
            self.assertIn(f"id: {field}", text)

    def test_branch_policy_matches_real_namespaces_and_no_delete_command(self) -> None:
        combined = read("docs/maintenance/branch-policy.md") + read("docs/maintenance/github-owner-settings.md")
        for namespace in ("agent/<topic>", "codex/<topic>", "cleanup/<topic>", "autopilot/<run-id>"):
            self.assertIn(namespace, combined)
        owner = read("docs/maintenance/github-owner-settings.md")
        self.assertIn("This table records intended disposition only", owner)
        self.assertNotRegex(owner, r"git\s+(?:branch\s+-[dD]|push\s+[^\n]*--delete)")
        self.assertIn("not verified", owner)

    def test_pull_request_template_demands_evidence_and_boundaries(self) -> None:
        text = read(".github/PULL_REQUEST_TEMPLATE.md")
        for needle in ("Outcome", "Scope", "## Evidence", "Safety and review", "Reviewer focus"):
            self.assertIn(needle, text)


class OfflineSiteAndStarterTests(unittest.TestCase):
    def test_core_site_has_no_network_assets_and_local_links_resolve(self) -> None:
        for relative in CORE_SITE_PAGES:
            path = ROOT / relative
            text = path.read_text(encoding="utf-8")
            self.assertNotRegex(text, r"(?:https?:)?//")
            parser = LinkCollector()
            parser.feed(text)
            for attribute, target in parser.links:
                parts = urlsplit(target)
                if parts.scheme or target.startswith(("#", "mailto:", "javascript:")):
                    continue
                local = (path.parent / parts.path).resolve()
                with self.subTest(page=relative, attribute=attribute, target=target):
                    self.assertTrue(local.exists(), f"missing local target: {local}")

    def test_search_assets_are_local_and_indexed(self) -> None:
        index = read("docs/site/index.html")
        self.assertIn('src="search-index.js"', index)
        self.assertIn('src="search.js"', index)
        self.assertIn('label for="site-search"', index)
        search = read("docs/site/search.js")
        self.assertIn("WORKBENCH_SEARCH_INDEX", search)
        self.assertNotIn("fetch(", search)
        search_index = read("docs/site/search-index.js")
        for route in ("Run a first task", "Learn prompting", "Contribute", "Starter directory"):
            self.assertIn(route, search_index)

    def test_model_media_is_the_explicit_network_exception(self) -> None:
        text = read("docs/site/model-media.html")
        self.assertIn("only core site page that requires a network connection", text)
        self.assertIn("youtube-nocookie.com", text)

    def test_starter_is_small_complete_and_public_safe(self) -> None:
        actual = {
            path.relative_to(ROOT).as_posix()
            for path in (ROOT / "starter").rglob("*")
            if path.is_file()
        }
        self.assertEqual(STARTER_FILES, actual)
        combined = "\n".join(read(relative) for relative in sorted(actual))
        for needle in ("task", "safety", "evaluation", "example"):
            self.assertIn(needle, combined.lower())
        self.assertNotRegex(combined, r"[A-Za-z]:\\|/home/|/Users/")
        self.assertNotRegex(combined, r"https?://")

    def test_release_builder_and_docs_include_starter_and_governance(self) -> None:
        builder = read("scripts/build_release_package.py")
        for needle in ('"CODE_OF_CONDUCT.md"', '"SUPPORT.md"', '"CITATION.cff"', '"starter"'):
            self.assertIn(needle, builder)
        release = read("docs/releases/release-process.md")
        self.assertIn("starter/", release)
        self.assertIn("github-owner-settings.md", release)
        self.assertIn("live github", release.lower())


if __name__ == "__main__":
    unittest.main()
