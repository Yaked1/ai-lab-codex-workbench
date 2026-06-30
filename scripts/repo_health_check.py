#!/usr/bin/env python3
"""Repository health checks for the Codex workbench."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CHANGELOG.md",
    ".gitignore",
    ".editorconfig",
    "docs/releases/release-process.md",
    "docs/releases/v0.1.0.md",
    ".github/workflows/ci.yml",
    ".github/workflows/autofix.yml",
    ".github/workflows/merge-pr.yml",
    ".github/workflows/release-package.yml",
    ".github/workflows/daily-research-scout.yml",
    ".github/workflows/curator-prompt-prep.yml",
    ".github/workflows/repo-autopilot.yml",
    ".github/workflows/automerge-safe-generated.yml",
    ".github/workflows/monthly-release-draft.yml",
    ".github/codex/prompts/daily-guide-curator.md",
    ".github/codex/prompts/source-safety-review.md",
    ".github/codex/prompts/skill-guide-generator.md",
    ".github/codex/prompts/image-prompting-guide-generator.md",
    ".github/codex/prompts/hermes-agent-guide-generator.md",
    "docs/guides/prompting-ai-coding-agents.md",
    "docs/guides/coding-agent-power-tips.md",
    "docs/guides/prompting-references.md",
    "docs/guides/source-inspired-prompting-curriculum.md",
    "docs/prompting-os/README.md",
    "docs/prompting-os/01-kernel.md",
    "docs/prompting-os/02-model-family-drivers.md",
    "docs/prompting-os/03-context-engineering.md",
    "docs/prompting-os/04-agent-skills.md",
    "docs/prompting-os/05-image-prompting-engine.md",
    "docs/prompting-os/06-evaluation-and-optimization.md",
    "docs/prompting-os/07-source-map.md",
    "docs/prompting-os/08-production-prompt-architecture.md",
    "docs/prompting-os/09-security-and-governance.md",
    "docs/prompting-os/10-evaluation-cookbook.md",
    "docs/prompting-os/11-comprehensiveness-benchmark.md",
    "docs/prompting-os/12-prompt-pattern-library.md",
    "docs/prompting-os/13-agent-operations-manual.md",
    "docs/prompting-os/14-rag-and-tool-use-field-guide.md",
    "docs/prompting-os/15-maintenance-and-release-manual.md",
    "docs/prompting-os/16-comprehensive-examples.md",
    "docs/prompting-os/17-curriculum-and-workshops.md",
    "docs/prompting-os/18-troubleshooting-and-debugging.md",
    "docs/prompting-os/19-model-specific-adaptation.md",
    "docs/prompting-os/20-prompt-library-governance.md",
    "docs/prompting-os/21-checklists-and-templates.md",
    "docs/prompting-os/22-risk-register.md",
    "docs/prompting-os/23-quality-assurance-matrix.md",
    "docs/prompting-os/24-archive-corpus-source-map.md",
    "docs/prompting-os/25-repository-expansion-playbook.md",
    "docs/prompting-os/26-offline-package-reader-guide.md",
    "docs/prompting-os/27-prompt-evaluation-datasets.md",
    "docs/prompting-os/28-tool-permission-model.md",
    "docs/prompting-os/29-source-grounded-writing-lab.md",
    "docs/prompting-os/30-agent-review-and-red-team.md",
    "docs/prompting-os/31-workbench-maintainer-runbook.md",
    "docs/prompting-os/32-completion-evidence-manual.md",
    "docs/prompting-os/33-prompt-library-indexing.md",
    "docs/prompting-os/34-static-site-and-release-docs.md",
    "docs/prompting-os/35-workshop-assessment-bank.md",
    "docs/prompting-os/36-prompt-metrics-and-telemetry.md",
    "docs/prompting-os/37-failure-mode-catalog.md",
    "docs/prompting-os/evals/prompt-quality-rubric.md",
    "docs/prompting-os/templates/master-prompt-template.md",
    "docs/prompting-os/visuals/prompting-os-architecture.svg",
    "docs/publication-policy.md",
    "docs/automation/repository-autopilot.md",
    "docs/automation/local-autopilot.md",
    "docs/automation/safe-automerge-policy.md",
    "docs/automation/release-draft-policy.md",
    "docs/research/source-policy.md",
    "docs/skills/README.md",
    "docs/image-generation/README.md",
    "docs/hermes/README.md",
    "data/research/sources.yml",
    "data/research/candidates.json",
    "data/research/blocklist.yml",
    "scripts/discover_ai_sources.py",
    "scripts/score_research_candidates.py",
    "scripts/generate_research_report.py",
    "scripts/generate_curator_prompt.py",
    "scripts/check_safe_generated_diff.py",
    "scripts/repo_autopilot_status.py",
    "scripts/local_autopilot.ps1",
    "tests/test_research_discovery.py",
    "scripts/build_release_package.py",
    "tests/test_build_release_package.py",
    "scripts/create_prompting_os_package.py",
    "tests/test_prompting_os_package.py",
    "scripts/safe_autofix.py",
    "scripts/repo_health_check.py",
]

SKIP_DIRS = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".cache",
    "dist",
    "build",
    "logs",
    "outputs",
    # Local scratch, editor, and agent-tool state directories. These are
    # gitignored and never part of a release, so the checks skip them.
    ".tmp",
    ".idea",
    ".vscode",
    ".omc",
}

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY-----"),
    re.compile(r"ghp_[A-Za-z0-9_]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk-[A-Za-z0-9]{24,}"),
]

TEXT_SUFFIXES = {".md", ".txt", ".py", ".ps1", ".yml", ".yaml", ".json", ".toml", ".svg"}


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def iter_text_files(root: Path):
    for path in root.rglob("*"):
        if should_skip(path) or not path.is_file():
            continue
        if path.name in {"LICENSE", ".gitignore", ".editorconfig"} or path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def check_required_files(root: Path) -> list[str]:
    errors = []
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"Missing required file: {relative}")
    return errors


def check_secret_patterns(root: Path) -> list[str]:
    errors = []
    for path in iter_text_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"Possible secret pattern in {path.relative_to(root)}")
    return errors


def check_large_files(root: Path) -> list[str]:
    warnings = []
    for path in root.rglob("*"):
        if should_skip(path) or not path.is_file():
            continue
        size = path.stat().st_size
        if size > 5_000_000:
            warnings.append(f"Large file over 5 MB: {path.relative_to(root)} ({size} bytes)")
    return warnings


def check_final_newlines(root: Path) -> list[str]:
    errors = []
    for path in iter_text_files(root):
        try:
            data = path.read_bytes()
        except OSError:
            continue
        if data and not data.endswith(b"\n"):
            errors.append(f"Missing final newline: {path.relative_to(root)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Repository health check")
    parser.add_argument("--root", default=".")
    parser.add_argument("--ci", action="store_true", help="CI mode")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors = []
    warnings = []

    errors.extend(check_required_files(root))
    errors.extend(check_secret_patterns(root))
    errors.extend(check_final_newlines(root))
    warnings.extend(check_large_files(root))

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    if errors:
        print(f"Repository health check failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print("Repository health check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
