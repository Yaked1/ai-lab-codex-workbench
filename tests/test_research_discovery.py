import contextlib
import importlib.util
import io
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))


def load_script(name):
    script = ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


discover_ai_sources = load_script("discover_ai_sources")
score_research_candidates = load_script("score_research_candidates")
generate_research_report = load_script("generate_research_report")
generate_curator_prompt = load_script("generate_curator_prompt")
safe_autofix = load_script("safe_autofix")
check_safe_generated_diff = load_script("check_safe_generated_diff")
repo_autopilot_status = load_script("repo_autopilot_status")


class ResearchDiscoveryTests(unittest.TestCase):
    def write_sources(self, root):
        sources = root / "sources.yml"
        sources.write_text(
            "\n".join(
                [
                    "version: 1",
                    "categories:",
                    "  - official_docs",
                    "sources:",
                    "  - id: official-example",
                    "    name: Official Example Docs",
                    "    category: official_docs",
                    "    url: https://example.com/docs",
                    "    kind: official_docs",
                    "    official: true",
                    "    source_status: official-docs",
                    "    license_hint: Official docs; link only.",
                    "    safety_note: Verify commands before publishing.",
                    "    summary: Public docs for a safe tool.",
                    "    tags:",
                    "      - docs",
                    "      - safety",
                    "  - id: blocked-example",
                    "    name: Blocked Example",
                    "    category: official_docs",
                    "    url: https://pastebin.com/example",
                    "    kind: public_page",
                    "    official: false",
                    "    source_status: unverified",
                    "    license_hint: Unknown",
                    "    safety_note: Review before use.",
                    "    summary: Should be blocked by domain.",
                    "    tags:",
                    "      - blocked",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        return sources

    def write_blocklist(self, root):
        blocklist = root / "blocklist.yml"
        blocklist.write_text(
            "\n".join(
                [
                    "version: 1",
                    "blocked_domains:",
                    "  - pastebin.com",
                    "blocked_url_contains:",
                    "  - /private/",
                    "blocked_terms:",
                    "  - token dump",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        return blocklist

    def test_source_config_parsing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            sources = self.write_sources(root)
            parsed = discover_ai_sources.load_sources(sources)
            self.assertEqual(len(parsed), 2)
            self.assertEqual(parsed[0]["id"], "official-example")
            self.assertTrue(parsed[0]["official"])
            self.assertEqual(parsed[0]["tags"], ["docs", "safety"])

    def test_candidate_scoring(self):
        candidate = {
            "official": True,
            "source_status": "official-docs",
            "license_hint": "Official docs",
            "summary": "Useful source",
            "safety_note": "Verify before publishing",
            "metadata": {"http_status": 200},
        }
        score = score_research_candidates.score_candidate(candidate)
        self.assertGreaterEqual(score, 70)

    def test_blocklist_behavior(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            sources = self.write_sources(root)
            blocklist = self.write_blocklist(root)
            payload = discover_ai_sources.discover(
                sources_path=sources,
                blocklist_path=blocklist,
                candidates_path=root / "missing.json",
                discovered_at="2026-06-29",
                fetch=False,
                max_sources=0,
            )
            blocked = [item for item in payload["candidates"] if item["blocked"]]
            self.assertEqual(len(blocked), 1)
            self.assertIn("blocked domain", blocked[0]["block_reasons"][0])

    def test_report_generation_and_path_formatting(self):
        candidates = [
            {
                "id": "official-example",
                "name": "Official Example Docs",
                "category": "official_docs",
                "url": "https://example.com/docs",
                "source_status": "official-docs",
                "license_hint": "Official docs",
                "safety_note": "Verify commands before publishing.",
                "summary": "Useful source",
                "tags": ["docs"],
                "score": 90,
                "quality": "high",
            }
        ]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            report_path = generate_research_report.write_report(root, "2026-06-29", candidates, 10)
            self.assertEqual(report_path.as_posix().endswith("docs/research/inbox/2026-06-29.md"), True)
            text = report_path.read_text(encoding="utf-8")
            self.assertIn("Daily AI Skills And Prompt Guide Candidates - 2026-06-29", text)
            self.assertIn("Official Example Docs", text)
            self.assertTrue(text.endswith("\n"))
            self.assertEqual(text, safe_autofix.normalize_text(text))

    def test_no_secret_looking_strings_in_generated_reports(self):
        candidates = [
            {
                "id": "bad",
                "name": "Bad " + "sk-" + "abcdefghijklmnopqrstuvwxyz",
                "category": "official_docs",
                "url": "https://example.com",
                "source_status": "unverified",
                "license_hint": "Unknown",
                "safety_note": "Review.",
                "summary": "No secret should survive.",
                "tags": [],
                "score": 1,
                "quality": "low",
            }
        ]
        text = generate_research_report.render_report(candidates, "2026-06-29", 10)
        self.assertNotIn("sk-" + "abcdefghijklmnopqrstuvwxyz", text)
        self.assertFalse(discover_ai_sources.has_secret_looking_text(text))

    def test_scout_dry_run_does_not_write_candidate_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            sources = self.write_sources(root)
            blocklist = self.write_blocklist(root)
            candidates = root / "candidates.json"
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                exit_code = discover_ai_sources.main(
                    [
                        "--sources",
                        str(sources),
                        "--blocklist",
                        str(blocklist),
                        "--candidates",
                        str(candidates),
                        "--date",
                        "2026-06-29",
                        "--dry-run",
                    ]
                )
            self.assertEqual(exit_code, 0)
            self.assertFalse(candidates.exists())
            self.assertIn("official-example", output.getvalue())

    def test_curator_prompt_generation_is_local_and_no_api_key(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            candidates_path = root / "data" / "research" / "candidates.json"
            candidates_path.parent.mkdir(parents=True, exist_ok=True)
            candidates_path.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "generated_at": "2026-06-29T00:00:00Z",
                        "candidates": [
                            {
                                "id": "hermes",
                                "name": "Hermes Agent Docs",
                                "category": "hermes_agent",
                                "url": "https://hermes-agent.nousresearch.com/docs/",
                                "source_status": "official-docs",
                                "license_hint": "Official docs",
                                "safety_note": "Agent workflows only.",
                                "summary": "Official Hermes Agent docs.",
                                "tags": ["hermes-agent"],
                                "score": 90,
                                "quality": "high",
                                "blocked": False,
                            }
                        ],
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            inbox = root / "docs" / "research" / "inbox"
            inbox.mkdir(parents=True, exist_ok=True)
            (inbox / "2026-06-29.md").write_text("Scout report\n", encoding="utf-8")

            prompt_path = generate_curator_prompt.write_prompt(
                root,
                report_date="2026-06-29",
                scope="hermes-agent",
                dry_run=True,
                max_sources=5,
            )
            text = prompt_path.read_text(encoding="utf-8")
            self.assertIn("Run Codex locally using ChatGPT sign-in", text)
            self.assertIn("Hermes Agent Docs", text)
            self.assertNotIn("OPENAI" + "_API_KEY", text)
            self.assertNotIn("openai/" + "codex-action", text)

    def test_github_workflows_do_not_run_codex_or_require_openai_api_key(self):
        workflows = ROOT / ".github" / "workflows"
        workflow_text = "\n".join(
            path.read_text(encoding="utf-8") for path in sorted(workflows.glob("*.yml"))
        )
        self.assertNotIn("openai/" + "codex-action", workflow_text)
        self.assertNotIn("openai-" + "api-key", workflow_text)
        self.assertNotIn("OPENAI" + "_API_KEY", workflow_text)
        self.assertNotIn("Run Codex", workflow_text)
        self.assertIsNone(re.search(r"(?im)^\s*run:\s*codex(?:\s|$)", workflow_text))
        self.assertIsNone(re.search(r"(?im)^\s*codex(?:\s|$)", workflow_text))

    def test_safe_generated_diff_allows_only_generated_files(self):
        report = check_safe_generated_diff.classify_changed_files(
            [
                "data/research/candidates.json",
                "docs/research/inbox/2026-06-29.md",
                "docs/research/curated/curator-prompt-2026-06-29.md",
            ]
        )
        self.assertTrue(report.is_safe)
        self.assertEqual(report.refused, [])

    def test_safe_generated_diff_rejects_forbidden_files(self):
        report = check_safe_generated_diff.classify_changed_files(
            [
                "docs/research/inbox/2026-06-29.md",
                "README.md",
                ".github/workflows/repo-autopilot.yml",
                "scripts/repo_health_check.py",
                "docs/hermes/hermes-agent.md",
            ]
        )
        self.assertFalse(report.is_safe)
        self.assertIn("README.md", report.refused)
        self.assertIn(".github/workflows/repo-autopilot.yml", report.refused)
        self.assertIn("scripts/repo_health_check.py", report.refused)
        self.assertIn("docs/hermes/hermes-agent.md", report.refused)

    def test_repo_autopilot_status_candidate_summary(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            candidates_path = root / "data" / "research" / "candidates.json"
            candidates_path.parent.mkdir(parents=True, exist_ok=True)
            candidates_path.write_text(
                json.dumps(
                    {
                        "generated_at": "2026-06-29T00:00:00Z",
                        "candidates": [
                            {
                                "id": "safe",
                                "category": "hermes_agent",
                                "score": 91,
                                "blocked": False,
                            },
                            {
                                "id": "blocked",
                                "category": "prompt_engineering",
                                "score": 0,
                                "blocked": True,
                            },
                        ],
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            (root / "docs" / "research" / "inbox").mkdir(parents=True)
            (root / "docs" / "research" / "inbox" / "2026-06-29.md").write_text("report\n", encoding="utf-8")
            (root / "docs" / "research" / "curated").mkdir(parents=True)
            (root / "docs" / "research" / "curated" / "curator-prompt-2026-06-29.md").write_text(
                "prompt\n",
                encoding="utf-8",
            )

            status = repo_autopilot_status.build_status(root)
            self.assertEqual(status["candidate_count"], 2)
            self.assertEqual(status["blocked_count"], 1)
            self.assertEqual(status["generated_at"], "2026-06-29T00:00:00Z")
            self.assertEqual(status["top_candidates"][0]["id"], "safe")
            rendered = repo_autopilot_status.render_status(status)
            self.assertIn("candidate_count: 2", rendered)
            self.assertIn("docs/research/inbox/2026-06-29.md", rendered)

    def test_autopilot_docs_and_workflows_exist(self):
        required = [
            "docs/automation/repository-autopilot.md",
            "docs/automation/local-autopilot.md",
            "docs/automation/safe-automerge-policy.md",
            "docs/automation/release-draft-policy.md",
            ".github/workflows/repo-autopilot.yml",
            ".github/workflows/automerge-safe-generated.yml",
            ".github/workflows/monthly-release-draft.yml",
            "scripts/local_autopilot.ps1",
            "scripts/repo_autopilot_status.py",
            "scripts/check_safe_generated_diff.py",
        ]
        for relative in required:
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / relative).is_file())


if __name__ == "__main__":
    unittest.main()
