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
AUTOMERGE_WORKFLOW = ROOT / ".github" / "workflows" / "automerge-safe-generated.yml"
SAFE_AUTOMERGE_POLICY = ROOT / "docs" / "automation" / "safe-automerge-policy.md"
PUBLICATION_WORKFLOWS = {
    "autofix": ROOT / ".github" / "workflows" / "autofix.yml",
    "monthly": ROOT / ".github" / "workflows" / "monthly-release-draft.yml",
    "daily": ROOT / ".github" / "workflows" / "daily-research-scout.yml",
    "curator": ROOT / ".github" / "workflows" / "curator-prompt-prep.yml",
    "autopilot": ROOT / ".github" / "workflows" / "repo-autopilot.yml",
}
PUBLICATION_POLICY = ROOT / "docs" / "publication-policy.md"
REPOSITORY_AUTOPILOT_GUIDE = ROOT / "docs" / "automation" / "repository-autopilot.md"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))


def load_script(name):
    script = ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def workflow_job_section(workflow: str, job_name: str) -> str:
    match = re.search(
        rf"(?ms)^  {re.escape(job_name)}:\r?\n(.*?)(?=^  [A-Za-z0-9_-]+:\r?\n|\Z)",
        workflow,
    )
    if match is None:
        raise AssertionError(f"workflow job {job_name!r} is missing")
    return match.group(0)


def workflow_run_blocks(job: str) -> list[str]:
    return re.findall(
        r"(?m)^        run: \|\r?\n((?:          .*\r?\n?)*)",
        job,
    )


def workflow_steps(workflow: str) -> list[str]:
    return re.findall(
        r"(?ms)^      - .*?(?=^      - |^  [A-Za-z0-9_-]+:\r?$|\Z)",
        workflow,
    )


def workflow_run_bodies(workflow: str) -> list[str]:
    bodies = []
    lines = workflow.splitlines()
    for index, line in enumerate(lines):
        match = re.match(r"^(?P<indent>\s*)run:\s*(?P<value>.*)$", line)
        if match is None:
            continue

        value = match.group("value").strip()
        if value.startswith("|"):
            indent = len(match.group("indent"))
            block = []
            for next_line in lines[index + 1 :]:
                if next_line and len(next_line) - len(next_line.lstrip()) <= indent:
                    break
                block.append(next_line)
            bodies.append("\n".join(block))
        else:
            bodies.append(value)
    return bodies


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


class SafeGeneratedAutomergeTrustBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = AUTOMERGE_WORKFLOW.read_text(encoding="utf-8")
        cls.policy = SAFE_AUTOMERGE_POLICY.read_text(encoding="utf-8")

    def test_validation_job_is_read_only_and_merge_is_separate(self):
        validation = workflow_job_section(self.workflow, "validate")
        merge = workflow_job_section(self.workflow, "merge")

        self.assertRegex(self.workflow, r"(?m)^  pull_request_target:\r?$")
        self.assertIsNone(re.search(r"(?m)^  pull_request:\r?$", self.workflow))
        self.assertIn("workflow_dispatch:", self.workflow)
        self.assertIn("if: >-", validation)
        self.assertIn(
            "github.ref == format('refs/heads/{0}', "
            "github.event.repository.default_branch)",
            validation,
        )
        self.assertRegex(
            validation,
            r"(?ms)^    permissions:\r?\n"
            r"      contents: read\r?\n"
            r"      pull-requests: read\r?\n"
            r"      checks: read\r?$",
        )
        self.assertNotIn("secrets.", validation)
        self.assertNotRegex(
            validation,
            r"(?m)^      (?:contents|pull-requests|checks): write\r?$",
        )
        self.assertIn("needs: validate", merge)
        self.assertIn("contents: write", merge)
        self.assertIn("pull-requests: write", merge)

    def test_validation_runs_the_base_owned_checker_from_runner_temp(self):
        validation = workflow_job_section(self.workflow, "validate")

        self.assertIn("GH_REPO: ${{ github.repository }}", validation)
        self.assertIn("headRefOid", validation)
        self.assertIn("baseRefOid", validation)
        self.assertIn('if [[ "$head_ref" != autopilot/* ]]', validation)
        self.assertIn('if [ "$head_owner" != "$REPOSITORY_OWNER" ]', validation)
        self.assertIn('if [ "$is_draft" = "true" ]', validation)
        checkout_index = validation.index("Checkout recorded PR head")
        for gate in (
            'if [[ "$head_ref" != autopilot/* ]]',
            'if [ "$head_owner" != "$REPOSITORY_OWNER" ]',
            'if [ "$is_draft" = "true" ]',
        ):
            self.assertLess(validation.index(gate), checkout_index)
        self.assertIn(
            "actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065 # v5.6.0",
            validation,
        )
        self.assertIn('python-version: "3.12"', validation)
        self.assertIn("persist-credentials: false", validation)
        self.assertIn(
            "TRUSTED_CHECKER: ${{ runner.temp }}/safe-generated-checker/"
            "check_safe_generated_diff.py",
            validation,
        )
        self.assertIn(
            'git show "$BASE_SHA:scripts/check_safe_generated_diff.py" '
            '> "$TRUSTED_CHECKER"',
            validation,
        )
        self.assertIn(
            'python "$TRUSTED_CHECKER" --base "$BASE_SHA" --head "$HEAD_SHA"',
            validation,
        )
        self.assertNotIn("python scripts/check_safe_generated_diff.py", validation)
        self.assertIn("python scripts/repo_health_check.py --ci", validation)
        self.assertIn("python scripts/safe_autofix.py --check", validation)
        self.assertIn("python -m unittest discover -s tests", validation)

    def test_merge_job_does_not_check_out_or_run_pr_code(self):
        merge = workflow_job_section(self.workflow, "merge")

        self.assertNotIn("actions/checkout", merge)
        self.assertNotIn("uses:", merge)
        self.assertEqual(1, len(re.findall(r"(?m)^        run:", merge)))
        run_blocks = workflow_run_blocks(merge)
        self.assertEqual(1, len(run_blocks))
        normalized_lines = [
            line.strip().rstrip("\\").strip()
            for line in run_blocks[0].splitlines()
            if line.strip()
        ]
        self.assertEqual(
            [
                'gh pr merge "$PR_NUMBER"',
                "--squash",
                "--auto",
                '--match-head-commit "$HEAD_SHA"',
                '--subject "Autopilot generated research updates"',
            ],
            normalized_lines,
        )
        self.assertNotRegex(
            merge,
            r"(?m)^\s*(?:python|git|bash|sh|node|curl|wget|\./|\.\./)\b",
        )
        self.assertIn("GH_REPO: ${{ github.repository }}", merge)
        self.assertIn("PR_NUMBER: ${{ needs.validate.outputs.pr_number }}", merge)
        self.assertIn("HEAD_SHA: ${{ needs.validate.outputs.head_sha }}", merge)
        self.assertIn('--match-head-commit "$HEAD_SHA"', merge)

    def test_policy_documents_the_trusted_checker_flow_and_evidence(self):
        self.assertIn("## Workflow Trust Boundary", self.policy)
        self.assertIn("recorded base commit", self.policy)
        self.assertIn("RUNNER_TEMP", self.policy)
        self.assertIn("--match-head-commit", self.policy)
        self.assertIn("| Evidence | Source |", self.policy)
        self.assertIn(
            "```bash\nset -euo pipefail\npython \"$RUNNER_TEMP/",
            self.policy,
        )
        self.assertIn("pull_request_target", self.policy)
        self.assertIn("ubuntu-latest", self.policy)
        self.assertIn("Bash", self.policy)
        self.assertIn("set -euo pipefail", self.policy)
        self.assertIn("nonzero", self.policy)
        self.assertIn("no secrets", self.policy)
        self.assertIn("persist-credentials: false", self.policy)
        self.assertIn("workflow execution protection controls", self.policy)
        self.assertIn("actor and event", self.policy)
        self.assertIn("trusted maintainers", self.policy)
        self.assertRegex(self.policy, r"must select\s+the default branch")
        self.assertIn("does not restrict ref selection", self.policy)
        self.assertIn(
            "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/"
            "actions-policies/workflow-execution-protections",
            self.policy,
        )
        self.assertIn("curated or non-allowlisted documentation", self.policy)


class GeneratedPublicationWorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflows = {
            name: path.read_text(encoding="utf-8")
            for name, path in PUBLICATION_WORKFLOWS.items()
        }
        cls.publication_policy = PUBLICATION_POLICY.read_text(encoding="utf-8")
        cls.autopilot_guide = REPOSITORY_AUTOPILOT_GUIDE.read_text(encoding="utf-8")

    def test_dispatch_inputs_enter_shell_only_through_environment(self):
        for name, workflow in self.workflows.items():
            with self.subTest(workflow=name):
                self.assertNotRegex(
                    "\n".join(workflow_run_bodies(workflow)),
                    r"\$\{\{\s*inputs\.",
                )

        self.assertIn("AUTOFIX_REASON: ${{ inputs.reason }}", self.workflows["autofix"])
        self.assertIn("VERSION_INPUT: ${{ inputs.version }}", self.workflows["monthly"])
        self.assertIn("KEEP_DIST_INPUT: ${{ inputs.keep_dist }}", self.workflows["monthly"])
        for name, prefix in (("curator", "CURATOR"), ("autopilot", "AUTOPILOT")):
            with self.subTest(workflow=name):
                workflow = self.workflows[name]
                self.assertIn(f"{prefix}_SCOPE: ${{{{ inputs.scope }}}}", workflow)
                self.assertIn(f"{prefix}_DRY_RUN: ${{{{ inputs.dry_run }}}}", workflow)
                self.assertIn(f"{prefix}_MAX_SOURCES: ${{{{ inputs.max_sources }}}}", workflow)
        self.assertIn("CREATE_PR: ${{ inputs.create_pr }}", self.workflows["autopilot"])

    def test_generated_workflows_publish_only_per_run_review_branches(self):
        for name in ("daily", "curator", "autopilot"):
            with self.subTest(workflow=name):
                workflow = self.workflows[name]
                self.assertIn(
                    "autopilot/generated-${{ github.run_id }}-${{ github.run_attempt }}",
                    workflow,
                )
                self.assertNotIn("autopilot/generated-research-updates", workflow)
                self.assertIn('git switch -c "$GENERATED_BRANCH" "origin/$BASE_BRANCH"', workflow)
                self.assertIn('git push origin "$GENERATED_BRANCH"', workflow)
                self.assertIn("gh pr create", workflow)
                self.assertNotRegex(workflow, r"(?m)^\s*git push\s*$")
                self.assertNotRegex(workflow, r"git push(?:\s+-u)?\s+origin\s+\"?\$BASE_BRANCH")

    def test_generated_workflows_stage_only_allowlisted_paths_then_check_before_push(self):
        expected_staging = {
            "daily": "git add data/research/candidates.json docs/research/inbox/*.md",
            "curator": "git add docs/research/curated/curator-prompt-*.md",
            "autopilot": (
                "git add data/research/candidates.json docs/research/inbox/*.md "
                "docs/research/curated/curator-prompt-*.md"
            ),
        }
        for name, staging in expected_staging.items():
            with self.subTest(workflow=name):
                workflow = self.workflows[name]
                self.assertIn(staging, workflow)
                self.assertNotIn("git add .", workflow)
                self.assertNotIn("if git diff --quiet --", workflow)
                git_add_lines = [
                    line.strip()
                    for body in workflow_run_bodies(workflow)
                    for line in body.splitlines()
                    if re.match(r"^\s*git add(?:\s|$)", line)
                ]
                self.assertEqual([staging], git_add_lines)
                staging_index = workflow.index(staging)
                checker_index = workflow.index("python scripts/check_safe_generated_diff.py --staged", staging_index)
                commit_index = workflow.index("git commit", checker_index)
                push_index = workflow.index("git push origin \"$GENERATED_BRANCH\"", commit_index)
                self.assertLess(staging_index, checker_index)
                self.assertLess(checker_index, commit_index)
                self.assertLess(commit_index, push_index)
                self.assertLess(push_index, workflow.index("gh pr create", push_index))

    def test_repo_autopilot_does_not_publish_when_create_pr_is_false(self):
        workflow = self.workflows["autopilot"]
        publication_body = next(
            body
            for body in workflow_run_bodies(workflow)
            if 'if [ "$CREATE_PR" != "true" ]; then' in body
        )
        false_branch = re.search(
            r'(?ms)if \[ "\$CREATE_PR" != "true" \]; then\r?\n'
            r'(?P<body>.*?)^\s*fi\s*$',
            publication_body,
        )
        self.assertIsNotNone(false_branch)
        self.assertIn("exit 0", false_branch.group("body"))
        gate_index = publication_body.index('if [ "$CREATE_PR" != "true" ]; then')
        for publication_command in (
            "git add data/research/candidates.json",
            "git commit",
            'git push origin "$GENERATED_BRANCH"',
            "gh pr create",
        ):
            with self.subTest(command=publication_command):
                self.assertLess(gate_index, publication_body.index(publication_command))
        self.assertNotIn("gh pr edit", workflow)
        self.assertNotIn("existing_pr=", workflow)

    def test_empty_staged_set_exits_before_commit_and_push(self):
        for name in ("daily", "curator", "autopilot"):
            with self.subTest(workflow=name):
                workflow = self.workflows[name]
                empty_index = workflow.index("if git diff --cached --quiet; then")
                exit_index = workflow.index("exit 0", empty_index)
                commit_index = workflow.index("git commit", empty_index)
                push_index = workflow.index('git push origin "$GENERATED_BRANCH"', empty_index)
                self.assertLess(empty_index, exit_index)
                self.assertLess(exit_index, commit_index)
                self.assertLess(commit_index, push_index)

    def test_gh_steps_have_explicit_repository_context_and_keep_existing_outputs(self):
        for name, workflow in self.workflows.items():
            for step in workflow_steps(workflow):
                if "gh " in step:
                    with self.subTest(workflow=name, step=step.splitlines()[0]):
                        self.assertIn("GH_REPO: ${{ github.repository }}", step)

        self.assertIn("data/research/candidates.json", self.workflows["daily"])
        self.assertIn("docs/research/inbox/*.md", self.workflows["daily"])
        self.assertIn("docs/research/curated/curator-prompt-*.md", self.workflows["curator"])
        self.assertIn("gh issue create", self.workflows["monthly"])
        self.assertIn("gh issue edit", self.workflows["monthly"])

    def test_autofix_stages_only_tracked_changes(self):
        workflow = self.workflows["autofix"]
        self.assertIn("git add --update", workflow)
        self.assertNotIn("git add .", workflow)
        self.assertIn("BASE_BRANCH: ${{ github.event.repository.default_branch }}", workflow)
        checkout_steps = [
            step for step in workflow_steps(workflow) if step.startswith("      - name: Checkout")
        ]
        self.assertEqual(1, len(checkout_steps))
        self.assertIn(
            "ref: ${{ github.event.repository.default_branch }}",
            checkout_steps[0],
        )
        self.assertIn(
            'BRANCH="automation/safe-autofix-${{ github.run_id }}-'
            '${{ github.run_attempt }}"',
            workflow,
        )
        self.assertIn('--base "$BASE_BRANCH"', workflow)
        self.assertNotIn("--base main", workflow)

    def test_write_capable_dispatch_jobs_gate_non_default_refs(self):
        job_names = {
            "autofix": "autofix",
            "monthly": "draft",
            "daily": "scout",
            "curator": "prep",
            "autopilot": "generated-research",
        }
        for name, job_name in job_names.items():
            with self.subTest(workflow=name):
                job = workflow_job_section(self.workflows[name], job_name)
                self.assertRegex(
                    job,
                    r"(?ms)^    if: >-\r?\n"
                    r"      github\.event_name != 'workflow_dispatch' \|\|\r?\n"
                    r"      github\.ref == format\('refs/heads/\{0\}', "
                    r"github\.event\.repository\.default_branch\)\r?\n"
                    r"    runs-on:",
                )

    def test_generated_pr_publishers_have_permissions_and_prepare_the_branch_first(self):
        generation_commands = {
            "daily": "python scripts/discover_ai_sources.py",
            "curator": "python scripts/generate_curator_prompt.py",
            "autopilot": "python scripts/discover_ai_sources.py",
        }
        for name, generation_command in generation_commands.items():
            with self.subTest(workflow=name):
                workflow = self.workflows[name]
                self.assertRegex(
                    workflow,
                    r"(?ms)^permissions:\r?\n.*?^  pull-requests: write$",
                )
                self.assertLess(
                    workflow.index('git switch -c "$GENERATED_BRANCH" "origin/$BASE_BRANCH"'),
                    workflow.index(generation_command),
                )

        self.assertIn("description: \"Open the generated research pull request\"", self.workflows["autopilot"])

    def test_publication_docs_describe_reviewable_per_run_prs(self):
        for document in (self.publication_policy, self.autopilot_guide):
            self.assertIn(
                "autopilot/generated-${{ github.run_id }}-${{ github.run_attempt }}",
                document,
            )
            self.assertIn("GitHub Actions bot", document)
            self.assertIn("human review", document)
            self.assertIn("default branch", document)
            self.assertIn("GITHUB_TOKEN", document)
            self.assertIn("approval-required state", document)
            self.assertIn("write access", document)
            self.assertIn("pull_request_target", document)
            self.assertIn("PR creation fails", document)
            self.assertNotIn("autopilot/generated-research-updates", document)
            self.assertNotIn("update the pull request", document)
            self.assertNotIn("enforced by a script every time", document)
        self.assertIn("data/research/candidates.json", self.publication_policy)
        self.assertIn("docs/research/inbox/*.md", self.publication_policy)
        self.assertIn("docs/research/curated/curator-prompt-*.md", self.publication_policy)
        self.assertIn("create_pr=false", self.autopilot_guide)
        self.assertIn("owner setting or maintainer action", self.autopilot_guide)
        self.assertIn(
            "https://docs.github.com/en/actions/concepts/security/github_token",
            self.autopilot_guide,
        )
        self.assertIn(
            "https://docs.github.com/en/actions/concepts/security/github_token",
            self.publication_policy,
        )


if __name__ == "__main__":
    unittest.main()
