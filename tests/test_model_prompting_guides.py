"""Regression tests for the model and effort prompting guide pack."""
import re
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "docs" / "guides" / "model-prompting"
FABLE_PROMOTION_SOURCE = (
    "https://support.claude.com/en/articles/15424964-claude-fable-5-promotional-access"
)

REQUIRED_FILES = (
    "README.md",
    "surface-and-effort-map.md",
    "shared-execution-contract.md",
    "sources-and-observations.md",
    "effort-evaluation-playbook.md",
    "gpt-5-6-sol-prompting.md",
    "gpt-5-6-terra-prompting.md",
    "gpt-5-6-luna-prompting.md",
    "claude-fable-5-prompting.md",
    "claude-opus-4-8-prompting.md",
    "claude-sonnet-5-prompting.md",
    "deepseek-v4-prompting.md",
    "glm-5-2-prompting.md",
    "mistral-current-models-prompting.md",
    "google-open-media-robotics-prompting.md",
    "grok-4-5-prompting.md",
    "muse-spark-1-1-prompting.md",
    "gemini-3-5-flash-prompting.md",
    "gpt-live-1-prompting.md",
    "gemini-live-translate-prompting.md",
    "gpt-image-2-prompting.md",
    "nano-banana-family-prompting.md",
    "gemini-omni-flash-prompting.md",
    "seedream-5-0-pro-prompting.md",
    "muse-image-video-prompting.md",
)

# Each guide must teach operational prompting, not only product marketing.
CORE_NEEDLES = (
    "Checked:",
    "```text",
    "Failure",
    "Verification",
)


FRONTIER_FILES = (
    "frontier-models-and-multimodal-systems-2026.md",
    "frontier-overview-and-selection.md",
    "frontier-openai-and-anthropic.md",
    "frontier-google-and-media.md",
    "frontier-open-and-specialist-models.md",
    "frontier-evaluation-and-deployment.md",
    "frontier-sources-and-method.md",
)

SHARED_FILES = {
    "README.md",
    "surface-and-effort-map.md",
    "sources-and-observations.md",
    "effort-evaluation-playbook.md",
    "shared-execution-contract.md",
}

PRECISION_HEADINGS = (
    "## Precision Execution Contract",
    "### Model and version identity",
    "### Surface, plan, effort, and harness matrix",
    "### Tool and permission boundary",
    "### Pricing, limits, and benchmark context",
    "### Production prompt template",
    "### Evaluation rubric",
    "### Auto-fail conditions",
    "### Failure protocol",
    "### Run record",
)

PRECISION_FIELDS = (
    "Model ID:",
    "Release / availability:",
    "Plan:",
    "Surface:",
    "Harness / client version:",
    "Effort / thinking:",
    "Tools enabled:",
    "Permission boundary:",
    "Objective:",
    "Context:",
    "Constraints:",
    "Output contract:",
    "Verification:",
    "Stop conditions:",
    "Retry / escalation:",
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")



def frontier_corpus() -> str:
    return "\n".join(read(ROOT / "docs" / "guides" / name) for name in FRONTIER_FILES)


def normalize_markdown(text: str) -> str:
    """Collapse Markdown wrapping without changing claim text."""
    return " ".join(text.split())


def markdown_section(text: str, heading: str) -> str:
    """Return one heading-bounded Markdown section, including subheadings."""
    level = len(heading) - len(heading.lstrip("#"))
    start_match = re.search(rf"(?m)^{re.escape(heading)}\s*$", text)
    if start_match is None:
        raise AssertionError(f"missing section {heading}")
    next_heading = re.search(
        rf"(?m)^#{{1,{level}}}\s+.+$", text[start_match.end() :]
    )
    end = (
        start_match.end() + next_heading.start()
        if next_heading is not None
        else len(text)
    )
    return normalize_markdown(text[start_match.start() : end])


def raw_markdown_section(text: str, heading: str) -> str:
    """Return a heading-bounded section while preserving table line breaks."""
    level = len(heading) - len(heading.lstrip("#"))
    start_match = re.search(rf"(?m)^{re.escape(heading)}\s*$", text)
    if start_match is None:
        raise AssertionError(f"missing section {heading}")
    next_heading = re.search(
        rf"(?m)^#{{1,{level}}}\s+.+$", text[start_match.end() :]
    )
    end = (
        start_match.end() + next_heading.start()
        if next_heading is not None
        else len(text)
    )
    return text[start_match.start() : end]


def paragraph_containing(text: str, marker: str) -> str:
    """Return the single Markdown paragraph containing a historical marker."""
    paragraphs = re.split(r"\n\s*\n", text)
    matches = [paragraph for paragraph in paragraphs if marker in paragraph]
    if len(matches) != 1:
        raise AssertionError(
            f"expected one paragraph containing {marker!r}, found {len(matches)}"
        )
    return normalize_markdown(matches[0])


def markdown_table(section: str) -> tuple[list[str], list[dict[str, str]]]:
    """Parse the first pipe table in a bounded Markdown section."""
    table_lines = [line.strip() for line in section.splitlines() if line.strip().startswith("|")]
    if len(table_lines) < 3:
        raise AssertionError("bounded section has no Markdown table")
    headers = [cell.strip() for cell in table_lines[0].strip("|").split("|")]
    rows = []
    for line in table_lines[2:]:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != len(headers):
            raise AssertionError(f"table row has {len(cells)} cells; expected {len(headers)}")
        rows.append(dict(zip(headers, cells)))
    return headers, rows


class ModelPromptingPackTests(unittest.TestCase):
    def test_required_files_exist(self):
        for name in REQUIRED_FILES:
            with self.subTest(name=name):
                path = PACK / name
                self.assertTrue(path.is_file(), f"missing {path}")
                self.assertTrue(read(path).endswith("\n"))

    def test_model_pages_link_to_the_single_shared_execution_contract(self):
        contract = PACK / "shared-execution-contract.md"
        self.assertTrue(contract.is_file())
        for name in REQUIRED_FILES:
            if name in SHARED_FILES:
                continue
            with self.subTest(name=name):
                self.assertIn(
                    "shared-execution-contract.md",
                    read(PACK / name),
                )

    def test_guides_have_operational_depth(self):
        for name in REQUIRED_FILES:
            if name in {"README.md", "sources-and-observations.md"}:
                continue
            text = read(PACK / name)
            with self.subTest(name=name):
                for needle in CORE_NEEDLES:
                    self.assertIn(needle, text, f"{name} missing {needle}")

    def test_shared_contract_owns_the_precision_contract(self):
        text = read(PACK / "shared-execution-contract.md")
        for heading in PRECISION_HEADINGS:
            with self.subTest(heading=heading):
                self.assertIn(heading, text)
        for field in PRECISION_FIELDS:
            with self.subTest(field=field):
                self.assertIn(field, text)

    def test_model_pages_do_not_repeat_the_shared_contract(self):
        forbidden = {
            "## Precision Execution Contract",
            "### Surface, plan, effort, and harness matrix",
            "### Tool and permission boundary",
            "### Evaluation rubric",
            "### Failure protocol",
            "### Run record",
        }
        for name in REQUIRED_FILES:
            if name in SHARED_FILES:
                continue
            text = read(PACK / name)
            with self.subTest(name=name):
                for heading in forbidden:
                    self.assertNotIn(heading, text)
                self.assertIn("shared-execution-contract.md", text)
    def test_precision_contract_identifies_unknowns_and_evidence(self):
        text = read(PACK / "shared-execution-contract.md")
        self.assertIn("Unknown or unverified:", text)
        self.assertIn("Evidence class:", text)
        self.assertIn("Auto-fail", text)
    def test_surface_map_covers_user_effort_facts(self):
        text = normalize_markdown(read(PACK / "surface-and-effort-map.md"))
        for needle in (
            "Light",
            "Ultra",
            "Plus",
            "Pro",
            "Business",
            "0.144.0",
            "0.144.1",
            "Extra High",
            "Ultracode",
            "July 19, 2026",
            "Grok 4.5",
            "Nano Banana Pro",
            "Muse Video",
            "Business",
            "observation",
        ):
            with self.subTest(needle=needle):
                self.assertIn(needle, text)

    def test_sol_guide_covers_all_efforts(self):
        text = read(PACK / "gpt-5-6-sol-prompting.md")
        for needle in (
            "Light / Low",
            "Medium",
            "High",
            "Extra High",
            "Max",
            "Ultra",
            "Plus web Work",
        ):
            with self.subTest(needle=needle):
                self.assertIn(needle, text)

    def test_sol_precision_addendum_records_current_surface_identity(self):
        surface = read(PACK / "surface-and-effort-map.md")
        for needle in (
            "0.145.0-alpha.4",
            "ChatGPT Desktop Work",
            "ChatGPT Desktop Codex",
            "Plus | Medium, High",
            "Pro, Business, Enterprise | Medium, High, Extra High, Sol Pro",
            "no `ultra` reasoning value",
            "1.05M-token context window",
            "Sol **$5/$30**",
            "Agents Last Exam | 52.7 | 50.4 | 50.3",
        ):
            with self.subTest(needle=needle):
                self.assertIn(needle, surface)

        sol = read(PACK / "gpt-5-6-sol-prompting.md")
        for needle in (
            "installed 0.144.0, stable 0.144.1, alpha 0.145.0-alpha.4",
            "Sol Pro path",
            "API: none through max, never ultra",
            "universal Business Work Ultra eligibility",
            "Vendor launch chart: Agents Last Exam 52.7",
        ):
            with self.subTest(sol_needle=needle):
                self.assertIn(needle, sol)

    def test_luna_has_no_ultra_menu(self):
        text = read(PACK / "gpt-5-6-luna-prompting.md")
        self.assertIn("No Ultra", text)
        self.assertIn("local Codex Luna menu", text)

    def test_fable_cutoff_and_ultracode(self):
        text = read(PACK / "claude-fable-5-prompting.md")
        promotion_row = next(
            normalize_markdown(line)
            for line in text.splitlines()
            if line.startswith("| Subscription promo end |")
        )
        self.assertIn("July 19, 2026 at 11:59:59 PM PT", promotion_row)
        self.assertIn(FABLE_PROMOTION_SOURCE, promotion_row)
        self.assertIn("Ultracode", text)
        self.assertIn("2.1.170", text)
        self.assertIn("Extra", text)

    def test_current_fable_sections_use_exact_july_19_claim(self):
        sections = {
            "README.md": "## Current Model Guides",
            "docs/PLANS/current.md": "## Decisions",
            "docs/guides/current-models-and-interfaces.md": "## Claude Fable 5",
            "docs/guides/frontier-openai-and-anthropic.md": "## Claude Fable 5 and Claude Opus 4.8",
            "docs/guides/model-prompting/claude-fable-5-prompting.md": "# Claude Fable 5 Prompting Guide",
            "docs/guides/model-prompting/sources-and-observations.md": "## Anthropic and Claude",
            "docs/guides/model-prompting/surface-and-effort-map.md": "### Fable 5 subscription cutoff",
        }
        for relative, heading in sections.items():
            with self.subTest(relative=relative):
                section = markdown_section(read(ROOT / relative), heading)
                self.assertIn("July 19, 2026", section)
                self.assertIn("11:59:59 PM PT", section)
                self.assertIn(FABLE_PROMOTION_SOURCE, section)

    def test_current_fable_sections_separate_access_and_limit_promotions(self):
        sections = {
            "docs/PLANS/current.md": "## Decisions",
            "docs/guides/current-models-and-interfaces.md": "## Claude Fable 5",
            "docs/guides/frontier-openai-and-anthropic.md": "## Claude Fable 5 and Claude Opus 4.8",
            "docs/guides/model-prompting/claude-fable-5-prompting.md": "# Claude Fable 5 Prompting Guide",
            "docs/guides/model-prompting/sources-and-observations.md": "## Anthropic and Claude",
            "docs/guides/model-prompting/surface-and-effort-map.md": "### Fable 5 subscription cutoff",
        }
        for relative, heading in sections.items():
            with self.subTest(relative=relative):
                section = markdown_section(read(ROOT / relative), heading)
                self.assertIn("included promotional access", section)
                self.assertIn("separate", section.lower())
                self.assertIn("50%", section)
                self.assertIn("weekly", section.lower())
                self.assertIn("usage credits", section)

    def test_fable_access_update_does_not_infer_api_availability(self):
        essay = frontier_corpus()
        section = markdown_section(
            essay, "### The July 19 Subscription Access Update"
        )

        self.assertNotIn("through the API at API rates", section)
        self.assertIn("API availability and pricing are separate surfaces", section)
        self.assertIn("require current API documentation", section)
        self.assertIn(FABLE_PROMOTION_SOURCE, section)
        self.assertIn("July 19, 2026 at 11:59:59 PM PT", section)
        self.assertIn("50%", section)
        self.assertIn("usage credits", section)

    def test_fable_evidence_row_records_current_promotion_scope(self):
        ledger = read(PACK / "sources-and-observations.md")
        rows = [
            normalize_markdown(line)
            for line in ledger.splitlines()
            if line.startswith("|") and FABLE_PROMOTION_SOURCE in line
        ]
        self.assertEqual(1, len(rows), "expected one Fable promotion evidence row")
        row = rows[0]
        for exact in (
            "July 19, 2026 at 11:59:59 PM PT",
            "50%",
            "usage credits",
            "Official",
            "2026-07-13",
            "subscription weekly limits",
            "Help Center",
        ):
            with self.subTest(exact=exact):
                self.assertIn(exact, row)

    def test_superseded_fable_dates_are_labeled_as_history(self):
        historical_surfaces = {
            "docs/PLANS/frontier-model-essay-notes.md": "Historical snapshot:",
            "docs/PLANS/model-prompting-guide-notes.md": "Historical snapshot:",
            "docs/research/current-model-claim-ledger-2026-07-11.md": "Superseded historical observation:",
            "docs/research/video-research-pack-2026-07-11.md": "The July 12 query is a superseded historical discovery search",
        }
        for relative, marker in historical_surfaces.items():
            with self.subTest(relative=relative):
                paragraph = paragraph_containing(read(ROOT / relative), marker)
                self.assertIn("superseded", paragraph.lower())
                self.assertIn("July 19, 2026", paragraph)
                self.assertIn("11:59:59 PM PT", paragraph)
                self.assertIn(FABLE_PROMOTION_SOURCE, paragraph)

    def test_grok_default_high(self):
        text = read(PACK / "grok-4-5-prompting.md")
        self.assertIn("High as the default", text)
        self.assertIn("Grok Build", text)

    def test_nano_banana_mapping(self):
        text = read(PACK / "nano-banana-family-prompting.md")
        self.assertIn("gemini-3-pro-image", text)
        self.assertIn("gemini-3.1-flash-image", text)
        self.assertIn("gemini-3.1-flash-lite-image", text)
        self.assertIn("Nano Banana 2 is not", text)

    def test_muse_video_unavailable(self):
        text = read(PACK / "muse-image-video-prompting.md")
        self.assertIn("coming soon", text)
        self.assertIn("Muse Video", text)
        self.assertIn("Muse Image launched", text)
        self.assertIn("Content Seal", text)

    def test_claude_guides_cover_adaptive_thinking(self):
        fable = read(PACK / "claude-fable-5-prompting.md")
        opus = read(PACK / "claude-opus-4-8-prompting.md")
        self.assertIn("adaptive thinking", fable)
        self.assertIn("Do not add `budget_tokens`", fable)
        self.assertIn("thinking: adaptive", opus)
        self.assertIn("64K", opus)

    def test_sources_ledger_separates_official_and_observed_claims(self):
        text = read(PACK / "sources-and-observations.md")
        self.assertIn("official launch says", text)
        self.assertIn("Business web Work shows Ultra", text)
        self.assertIn("does not establish universal Business eligibility", text)
        self.assertIn("0.144.1", text)

    def test_effort_eval_counts_orchestration_costs(self):
        text = read(PACK / "effort-evaluation-playbook.md")
        self.assertIn("Count all agents", text)
        self.assertIn("human correction", text)
        self.assertIn("frozen baseline prompt", text)

    def test_effort_eval_has_one_compact_observed_worked_example(self):
        section = markdown_section(
            read(PACK / "effort-evaluation-playbook.md"),
            "## Compact Worked Example",
        )
        for heading in (
            "### Filled baseline and candidate",
            "### Observed validation",
            "### Counterexample and failure",
            "### Executable verification",
        ):
            with self.subTest(heading=heading):
                self.assertIn(heading, section)
        self.assertIn("Baseline |", section)
        self.assertIn("Candidate |", section)
        self.assertIn("Result |", section)
        self.assertIn("python -m unittest tests.test_model_prompting_guides", section)
        self.assertIn("planned model comparison", section.lower())
        self.assertIn("not executed", section.lower())
        self.assertIn("deterministic Task 10 document-contract evidence", section)
        self.assertNotIn("| Result | FAIL | PASS |", section)
        self.assertNotRegex(section, r"<(?:fill|model|result|command)[^>]*>")

    def test_gpt_5_6_claim_ledger_has_row_level_source_identity(self):
        section = raw_markdown_section(
            read(PACK / "sources-and-observations.md"),
            "## Claim-Level GPT-5.6 Ledger",
        )
        headers, rows = markdown_table(section)
        self.assertEqual(
            [
                "Claim",
                "Evidence class",
                "Source identity",
                "Scope",
                "Checked",
                "Recheck trigger",
            ],
            headers,
        )
        self.assertTrue(rows)
        first_party_https = re.compile(
            r"https://(?:help\.openai\.com/|developers\.openai\.com/|"
            r"www\.npmjs\.com/package/@openai/codex)"
        )
        for row_number, row in enumerate(rows, 1):
            with self.subTest(row=row_number, claim=row.get("Claim")):
                for column in headers:
                    self.assertTrue(row[column].strip(), f"row {row_number} has empty {column}")
                self.assertRegex(row["Checked"], r"^\d{4}-\d{2}-\d{2}$")
                try:
                    parsed_date = date.fromisoformat(row["Checked"])
                except ValueError as exc:
                    self.fail(f"row {row_number} has invalid ISO date: {exc}")
                self.assertEqual(row["Checked"], parsed_date.isoformat())
                evidence_class = row["Evidence class"]
                if evidence_class in {"Official", "Package registry"}:
                    self.assertRegex(row["Source identity"], first_party_https)
                elif evidence_class == "Local evidence":
                    self.assertRegex(row["Source identity"], r"`codex(?:\.cmd)?\s+[^`]+`")
                elif evidence_class == "User observation":
                    self.assertRegex(row["Source identity"], r"(?i)ChatGPT.+(?:picker|surface|observation)")
                else:
                    self.fail(f"unsupported evidence class in row {row_number}: {evidence_class}")
        expected_sources = {
            "Codex CLI minimum": "https://help.openai.com/en/articles/20001275",
            "Installed CLI": "`codex --version`",
            "Stable npm": "https://www.npmjs.com/package/@openai/codex",
            "Sol/Terra local menu": "`codex debug models`",
            "Plus Chat": "https://help.openai.com/en/articles/20001354",
            "API uses": "https://developers.openai.com/api/docs/models",
            "list prices": "https://developers.openai.com/api/docs/models",
        }
        for marker, source in expected_sources.items():
            matching = [row for row in rows if marker in row["Claim"]]
            with self.subTest(claim=marker):
                self.assertEqual(1, len(matching))
                self.assertIn(source, matching[0]["Source identity"])
                self.assertEqual("2026-07-12", matching[0]["Checked"])
                self.assertTrue(matching[0]["Scope"])

    def test_frontier_essay_now_covers_muse_media(self):
        essay = frontier_corpus()
        self.assertIn("### Muse Image and Muse Video", essay)
        self.assertIn("Content Seal", essay)
        self.assertIn("coming soon", essay)

    def test_frontier_essay_records_all_new_audit_outcomes(self):
        essay = frontier_corpus()
        for needle in (
            "Claude Sonnet 5",
            "DeepSeek-V4-Pro and DeepSeek-V4-Flash",
            "GLM-5.2",
            "Current Mistral Family by Workload",
            "Gemma 4",
            "DiffusionGemma",
            "Veo 3.1 Lite",
            "Lyria 3",
            "Gemini Robotics-ER 1.6",
            "Watchlist: Gemini 3.5 Pro",
            "Robostral Navigate",
        ):
            with self.subTest(needle=needle):
                self.assertIn(needle, essay)

    def test_new_guides_preserve_documented_boundaries(self):
        self.assertIn("Preview", read(PACK / "deepseek-v4-prompting.md"))
        self.assertIn("no public identifier", read(PACK / "mistral-current-models-prompting.md"))
        self.assertIn("coming soon", read(PACK / "google-open-media-robotics-prompting.md"))

    def test_index_links_every_guide(self):
        index = read(PACK / "README.md")
        for name in REQUIRED_FILES:
            if name == "README.md":
                continue
            with self.subTest(name=name):
                self.assertIn(name, index)

    def test_each_model_guide_links_source_ledger(self):
        exempt = {
            "README.md",
            "sources-and-observations.md",
            "effort-evaluation-playbook.md",
        }
        for name in REQUIRED_FILES:
            if name in exempt:
                continue
            with self.subTest(name=name):
                self.assertIn("sources-and-observations.md", read(PACK / name))

    def test_guides_readme_and_root_readme_link_pack(self):
        guides_readme = read(ROOT / "docs" / "guides" / "README.md")
        root_readme = read(ROOT / "README.md")
        self.assertIn("model-prompting/README.md", guides_readme)
        self.assertIn("docs/guides/model-prompting/README.md", root_readme)

    def test_frontier_essay_links_pack(self):
        essay = frontier_corpus()
        self.assertIn("model-prompting/README.md", essay)
        self.assertIn("surface-and-effort-map.md", essay)

    def test_no_secret_looking_strings(self):
        import sys

        scripts = ROOT / "scripts"
        if str(scripts) not in sys.path:
            sys.path.insert(0, str(scripts))
        from discover_ai_sources import has_secret_looking_text

        for name in REQUIRED_FILES:
            text = read(PACK / name)
            with self.subTest(name=name):
                self.assertFalse(has_secret_looking_text(text))


if __name__ == "__main__":
    unittest.main()
