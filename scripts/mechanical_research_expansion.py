#!/usr/bin/env python3
"""Deterministically add research-grade review notes across tracked files.

This script is intentionally conservative. It expands files where comments or
documentation sections are syntactically safe, and records strict data, binary,
legal, generated, or placeholder files as skipped instead of corrupting them.
The output manifest is a review aid for broad "touch many files" tasks.
"""
from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

MARKER_BEGIN = "RESEARCH-GRADE-EXPANSION:BEGIN"
MARKER_END = "RESEARCH-GRADE-EXPANSION:END"

REPORT_PATH = Path("docs/review/mechanical-research-expansion-report.md")
MANIFEST_PATH = Path("docs/review/mechanical-research-expansion-manifest.json")

STRICT_JSON = {
    "data/research/candidates.json",
    "skills/manifest.json",
}

SKIP_EXACT = {
    "--watch": "terminal help capture; not public guide source",
    "LICENSE": "legal text should not be rewritten mechanically",
    "docs/research/curated/.gitkeep": "placeholder file has no content surface",
    "docs/research/inbox/.gitkeep": "placeholder file has no content surface",
}


def run_git_ls_files(root: Path) -> list[str]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def category_for(relative: str) -> str:
    if relative.startswith("skills/"):
        return "installable agent skill"
    if relative.startswith("prompts/"):
        return "agent prompt template"
    if relative.startswith("docs/prompting-os/"):
        return "Prompting OS module"
    if relative.startswith("docs/workflows/"):
        return "agent workflow guide"
    if relative.startswith("docs/tools/"):
        return "tool guide"
    if relative.startswith("docs/image-generation/"):
        return "image-generation guide"
    if relative.startswith("docs/hermes/"):
        return "Hermes Agent guide"
    if relative.startswith("docs/site/"):
        return "offline static-site asset"
    if relative.startswith(".github/workflows/"):
        return "GitHub Actions workflow"
    if relative.startswith(".github/ISSUE_TEMPLATE/"):
        return "GitHub issue template"
    if relative.startswith("scripts/"):
        return "repository automation script"
    if relative.startswith("tests/"):
        return "repository regression test"
    if relative.startswith("data/"):
        return "research data configuration"
    if relative in {"README.md", "AGENTS.md", "CONTRIBUTING.md", "SECURITY.md", "CHANGELOG.md"}:
        return "top-level repository policy document"
    return "repository support file"


def display_name(relative: str) -> str:
    stem = Path(relative).stem.replace("-", " ").replace("_", " ").strip()
    if stem.upper() == "README":
        return "README"
    if stem.upper() == "SKILL":
        return Path(relative).parent.name.replace("-", " ")
    return stem or relative


def md_block(relative: str) -> str:
    category = category_for(relative)
    name = display_name(relative)
    return f"""
<!-- {MARKER_BEGIN} -->
## Research-Grade Review Addendum

This file is part of the repository's **{category}** surface. During broad
maintenance, reviewers should treat `{relative}` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `{name}` state what decision, workflow, or reusable behavior it supports?
- Are included scope, excluded scope, and unsafe actions clear enough for an
  agent or contributor to follow?
- Are examples public-safe, repository-relative, and free of private data?
- Are fast-changing product or platform claims phrased conservatively or marked
  for official-doc verification?
- Does the file point to the next artifact a reader should inspect: a command,
  template, test, manifest, package, or deeper guide?
- Could a reviewer cite this file in a PR review and know what evidence proves
  the work is complete?

Keep future edits focused on stronger evidence, clearer failure modes, better
navigation, and safer automation boundaries. Do not add length unless the new
material makes the repository easier to operate, teach, audit, or recover.
<!-- {MARKER_END} -->
"""


def line_comment_block(relative: str, prefix: str = "#") -> str:
    category = category_for(relative)
    lines = [
        f"{prefix} {MARKER_BEGIN}",
        f"{prefix} Research-grade maintenance notes:",
        f"{prefix} - Role: {category}.",
        f"{prefix} - Review this file for clear inputs, outputs, side effects, and failure behavior.",
        f"{prefix} - Keep examples public-safe and repository-relative; avoid secrets or private paths.",
        f"{prefix} - When behavior changes, update adjacent tests, docs, and changelog evidence.",
        f"{prefix} - Prefer deterministic, reviewable operations over hidden or networked side effects.",
        f"{prefix} {MARKER_END}",
        "",
    ]
    return "\n".join(lines)


def ps1_block(relative: str) -> str:
    category = category_for(relative)
    return f"""
<#
{MARKER_BEGIN}
Research-grade maintenance notes:
- Role: {category}.
- Review parameters, side effects, exit behavior, dry-run/apply boundaries, and failure output before changing this script.
- Keep examples public-safe and repository-relative; do not print secrets or inspect private machine state.
- When behavior changes, update tests or documented manual verification steps and record user-visible changes in the changelog.
{MARKER_END}
#>
"""


def css_block(relative: str) -> str:
    return f"""
/* {MARKER_BEGIN}
Research-grade maintenance notes:
- Role: {category_for(relative)}.
- Keep the static site offline-safe: no remote fonts, trackers, analytics, CDNs, or external scripts.
- CSS changes should preserve readable navigation, contrast, responsive layout, and local-only assets.
- Pair visual changes with manual browser inspection or a clear review note.
{MARKER_END} */

.research-grade-addendum {{
  border-top: 1px solid #d8dee8;
  margin-top: 2rem;
  padding-top: 1rem;
}}
"""


def html_section(relative: str) -> str:
    category = category_for(relative)
    return f"""
  <!-- {MARKER_BEGIN} -->
  <section class="research-grade-addendum">
    <h2>Research-Grade Review Notes</h2>
    <p>This page belongs to the repository's {category} surface. Keep it
    offline-safe, public-safe, and useful for a reviewer who opens the file
    without additional context.</p>
    <ul>
      <li>Preserve local-only assets and relative repository links.</li>
      <li>Avoid trackers, analytics, remote fonts, external scripts, private
      paths, and account-specific URLs.</li>
      <li>Make each workflow claim traceable to a guide, prompt, script, test,
      or explicit verification step.</li>
    </ul>
  </section>
  <!-- {MARKER_END} -->
"""


def svg_comment(relative: str) -> str:
    return f"""
  <!-- {MARKER_BEGIN}
  Research-grade maintenance notes:
  - Role: {category_for(relative)}.
  - Keep this diagram source-controlled, text-reviewable, and free of embedded remote assets.
  - Update adjacent docs when visual concepts, labels, or architecture boundaries change.
  {MARKER_END} -->
"""


def normalize_newline(text: str) -> str:
    return text if text.endswith("\n") else text + "\n"


def expand_text(relative: str, text: str) -> tuple[str, str]:
    if MARKER_BEGIN in text:
        return text, "already-expanded"

    suffix = Path(relative).suffix.lower()
    text = normalize_newline(text)

    if suffix == ".md":
        return text + md_block(relative).lstrip(), "markdown-addendum"
    if suffix == ".py":
        return text + "\n" + line_comment_block(relative), "python-comment"
    if suffix == ".ps1":
        return text + ps1_block(relative), "powershell-comment"
    if suffix in {".yml", ".yaml"}:
        return text + "\n" + line_comment_block(relative), "yaml-comment"
    if suffix == ".html":
        section = html_section(relative)
        if "</main>" in text:
            return text.replace("</main>", section + "\n</main>", 1), "html-section"
        if "</body>" in text:
            return text.replace("</body>", section + "\n</body>", 1), "html-section"
        return text + section, "html-section"
    if suffix == ".css":
        return text + css_block(relative), "css-comment"
    if suffix == ".svg":
        comment = svg_comment(relative)
        if "</svg>" in text:
            return text.replace("</svg>", comment + "\n</svg>", 1), "svg-comment"
        return text + comment, "svg-comment"
    if relative in {".gitignore", ".gitattributes", ".editorconfig"}:
        return text + "\n" + line_comment_block(relative), "config-comment"

    return text, "unsupported"


def write_report(root: Path, manifest: dict[str, object]) -> None:
    modified = [entry for entry in manifest["files"] if entry["status"] == "modified"]
    skipped = [entry for entry in manifest["files"] if entry["status"] == "skipped"]
    already = [entry for entry in manifest["files"] if entry["status"] == "already-expanded"]
    marker_covered = modified + already

    lines = [
        "# Mechanical Research Expansion Report",
        "",
        "This report makes the broad mechanical rewrite reviewable. It records",
        "the deterministic expansion strategy, file-class handling, validation",
        "expectations, and skip reasons for tracked repository files.",
        "",
        "## Summary",
        "",
        f"- Tracked files inspected: {manifest['summary']['tracked_files']}",
        f"- Files carrying the expansion marker after this run: {len(marker_covered)}",
        f"- Files changed during the current expansion pass: {len(modified)}",
        f"- Files already carrying the expansion marker before this pass: {len(already)}",
        f"- Files skipped with explicit reasons: {len(skipped)}",
        f"- Manifest: `{MANIFEST_PATH.as_posix()}`",
        "",
        "The current-pass modified count is expected to fall to zero on",
        "idempotent reruns. Use the marker-coverage count, skipped-file list,",
        "and staged `git diff --stat` to audit the full broad rewrite.",
        "",
        f"<!-- {MARKER_BEGIN} -->",
        "## Research-Grade Review Addendum",
        "",
        "This report is itself part of the review evidence for the mechanical",
        "rewrite. It should let a maintainer understand the broad diff without",
        "opening every file first: what transformation ran, which files were",
        "modified, which files were skipped, how to search the inserted markers,",
        "and which validation commands must pass before staging or merging.",
        "",
        "Reviewers should compare this report with the JSON manifest, `git diff",
        "--stat`, and the validation output. If those artifacts disagree, treat",
        "the task as incomplete until the mismatch is explained.",
        f"<!-- {MARKER_END} -->",
        "",
        "## Review Strategy",
        "",
        "- Markdown files receive a visible research-grade review addendum.",
        "- Scripts, tests, workflows, and config files receive comment-only",
        "  maintenance notes so behavior remains unchanged.",
        "- Static HTML receives an offline-safe review section; CSS receives",
        "  supporting local-only styling and notes.",
        "- Strict JSON, legal text, placeholder files, and generated terminal",
        "  captures are not rewritten; they are recorded as skipped.",
        "- Every inserted block is marked with `RESEARCH-GRADE-EXPANSION` so",
        "  reviewers can search and diff the broad pass mechanically.",
        "",
        "## Marker-Covered Surface Classes",
        "",
    ]

    by_category: dict[str, int] = {}
    for entry in marker_covered:
        by_category[entry["category"]] = by_category.get(entry["category"], 0) + 1
    for category, count in sorted(by_category.items()):
        lines.append(f"- {category}: {count}")

    lines.extend(
        [
            "",
            "## Skipped Files",
            "",
        ]
    )
    for entry in skipped:
        lines.append(f"- `{entry['path']}`: {entry['reason']}")

    lines.extend(
        [
            "",
            "## Validation Required After Running",
            "",
            "```powershell",
            "python scripts/repo_health_check.py",
            "python scripts/safe_autofix.py --check",
            "python -m unittest discover -s tests",
            "git diff --check",
            "git diff --cached --check",
            "```",
            "",
            "## Reviewer Search Commands",
            "",
            "```powershell",
            "rg -n \"RESEARCH-GRADE-EXPANSION\" README.md AGENTS.md CONTRIBUTING.md SECURITY.md docs prompts skills scripts tests .github",
            "git diff --stat",
            "git diff --cached --stat",
            "```",
            "",
        ]
    )

    report = "\n".join(lines)
    path = root / REPORT_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report, encoding="utf-8")


def should_skip(relative: str) -> str | None:
    if relative in SKIP_EXACT:
        return SKIP_EXACT[relative]
    if relative in STRICT_JSON:
        return "strict JSON data/manifest; comments are invalid and shape changes risk breaking loaders"
    return None


def expand_repo(root: Path) -> dict[str, object]:
    files = run_git_ls_files(root)
    manifest_entries = []

    for relative in files:
        skip_reason = should_skip(relative)
        entry = {"path": relative, "category": category_for(relative)}
        if skip_reason:
            entry.update({"status": "skipped", "reason": skip_reason})
            manifest_entries.append(entry)
            continue

        path = root / relative
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            entry.update({"status": "skipped", "reason": "not UTF-8 text"})
            manifest_entries.append(entry)
            continue

        expanded, method = expand_text(relative, text)
        if method == "unsupported":
            entry.update({"status": "skipped", "reason": "unsupported syntax for safe mechanical prose/comment expansion"})
        elif method == "already-expanded":
            entry.update({"status": "already-expanded", "method": method})
        else:
            path.write_text(expanded, encoding="utf-8")
            entry.update(
                {
                    "status": "modified",
                    "method": method,
                    "bytes_before": len(text.encode("utf-8")),
                    "bytes_after": len(expanded.encode("utf-8")),
                }
            )
        manifest_entries.append(entry)

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "script": "scripts/mechanical_research_expansion.py",
        "marker_begin": MARKER_BEGIN,
        "marker_end": MARKER_END,
        "research_grade_review_notes": [
            "This manifest is strict JSON, so it carries review notes as data instead of comments.",
            "Use the files array to verify which tracked paths were modified, already expanded, or skipped.",
            "Skipped files are explicit review decisions, not silent omissions.",
            "Pair this manifest with the generated Markdown report and validation command output.",
        ],
        "summary": {
            "tracked_files": len(files),
            "modified": sum(1 for entry in manifest_entries if entry["status"] == "modified"),
            "already_expanded": sum(1 for entry in manifest_entries if entry["status"] == "already-expanded"),
            "marker_covered": sum(1 for entry in manifest_entries if entry["status"] in {"modified", "already-expanded"}),
            "skipped": sum(1 for entry in manifest_entries if entry["status"] == "skipped"),
        },
        "files": manifest_entries,
    }

    manifest_path = root / MANIFEST_PATH
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_report(root, manifest)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Mechanically expand tracked files with research-grade review notes.")
    parser.add_argument("--root", default=Path(__file__).resolve().parents[1], type=Path)
    args = parser.parse_args()

    root = args.root.resolve()
    manifest = expand_repo(root)
    summary = manifest["summary"]
    print(
        "Mechanical research expansion complete: "
        f"{summary['modified']} modified, "
        f"{summary['already_expanded']} already expanded, "
        f"{summary['marker_covered']} marker covered, "
        f"{summary['skipped']} skipped."
    )
    print(f"Wrote {REPORT_PATH.as_posix()}")
    print(f"Wrote {MANIFEST_PATH.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
