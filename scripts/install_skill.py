#!/usr/bin/env python3
"""Install one or more skills from skills/ into an agent harness.

Standard library only -- no new dependency was added to run this. Works
two ways:

1. Run from inside a clone of this repository: copies files straight out
   of the local skills/ folder.
2. Run standalone (for example after downloading just this script): fetches
   the specific skill's files over plain HTTPS from the public GitHub repo,
   nothing more. This script never executes anything it downloads -- it
   only reads Markdown/JSON text and writes it to the target path.
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
import urllib.request
from pathlib import Path
from typing import Optional

RAW_BASE = "https://raw.githubusercontent.com/Yaked1/ai-lab-codex-workbench/main"

# Harnesses with a documented native skill-bundle folder this installer can
# target directly. See skills/README.md's "Installer Behavior" table for the
# reasoning -- these lists must stay in sync with that table.
CLAUDE_CODE_HARNESSES = {"claude-code", "claude-code-cli", "claude-code-desktop"}
CODEX_HARNESSES = {"codex", "codex-cli", "codex-desktop"}
HERMES_HARNESSES = {"hermes"}
NATIVE_SKILL_HARNESSES = CLAUDE_CODE_HARNESSES | CODEX_HARNESSES | HERMES_HARNESSES

# Harnesses with no native skill-loading mechanism today. The installer stages
# a flattened copy and tells the human where to paste it manually instead of
# claiming an auto-install path that does not exist.
FLATTENED_STAGED_HARNESSES = {
    "cursor",
    "windsurf",
    "aider",
    "antigravity",
    "github-copilot",
    "opencode",
    "kilo-code",
    "mcp",
}

ALL_HARNESSES = sorted(NATIVE_SKILL_HARNESSES | FLATTENED_STAGED_HARNESSES)


def repo_root() -> Optional[Path]:
    here = Path(__file__).resolve().parent.parent
    if (here / "skills" / "manifest.json").is_file():
        return here
    return None


def load_manifest(root: Optional[Path]) -> dict:
    if root is not None:
        return json.loads((root / "skills" / "manifest.json").read_text(encoding="utf-8"))
    with urllib.request.urlopen(f"{RAW_BASE}/skills/manifest.json") as response:  # noqa: S310
        return json.loads(response.read().decode("utf-8"))


def read_skill_file(root: Optional[Path], relative_path: str) -> str:
    if root is not None:
        return (root / relative_path).read_text(encoding="utf-8")
    with urllib.request.urlopen(f"{RAW_BASE}/{relative_path}") as response:  # noqa: S310
        return response.read().decode("utf-8")


def strip_frontmatter(skill_md_text: str) -> str:
    """Return SKILL.md body without the leading YAML frontmatter block."""
    if not skill_md_text.startswith("---\n"):
        return skill_md_text
    end = skill_md_text.find("\n---\n", 4)
    if end == -1:
        return skill_md_text
    return skill_md_text[end + 5 :].lstrip("\n")


def target_path(harness: str, scope: str, slug: str) -> Path:
    if harness in CLAUDE_CODE_HARNESSES:
        if scope == "user":
            return Path.home() / ".claude" / "skills" / slug / "SKILL.md"
        return Path(".claude") / "skills" / slug / "SKILL.md"
    if harness in CODEX_HARNESSES:
        if scope == "user":
            return Path.home() / ".agents" / "skills" / slug / "SKILL.md"
        return Path(".agents") / "skills" / slug / "SKILL.md"
    if harness in HERMES_HARNESSES:
        if scope == "user":
            return Path.home() / ".hermes" / "skills" / slug / "SKILL.md"
        return Path(".agent-skills") / "hermes" / slug / "SKILL.md"
    return Path(".agent-skills") / harness / f"{slug}.md"


def install_one(root: Optional[Path], slug: str, harness: str, scope: str, force: bool, dry_run: bool) -> None:
    skill_md_relpath = f"skills/{slug}/SKILL.md"
    text = read_skill_file(root, skill_md_relpath)
    dest = target_path(harness, scope, slug)

    if harness in FLATTENED_STAGED_HARNESSES:
        text = strip_frontmatter(text)

    if dest.exists() and not force and not dry_run:
        print(f"SKIP  {slug}: {dest} already exists (use --force to overwrite)")
        return

    if dry_run:
        print(f"WOULD WRITE  {slug} -> {dest}")
        return

    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8", newline="\n")
    print(f"OK    {slug} -> {dest}")

    if harness in FLATTENED_STAGED_HARNESSES:
        print(
            f"      {harness} has no confirmed native skill-loading path. "
            f"Paste the staged file above into {harness}'s own custom-"
            f"instructions/rules mechanism -- see docs/tools/{harness}.md "
            "for its current location."
        )
    elif harness in CODEX_HARNESSES:
        print(
            "      Codex reads local skills from .agents/skills (project) "
            "or ~/.agents/skills (user). The same skill files are available "
            "to Codex CLI, IDE extension, and Codex app sessions that scan "
            "that location."
        )
    elif harness in CLAUDE_CODE_HARNESSES:
        print(
            "      Claude Code reads skills from .claude/skills (project) "
            "or ~/.claude/skills (user). Start or refresh Claude Code from "
            "the target repo and invoke the skill by name if needed."
        )
    elif harness in HERMES_HARNESSES:
        if scope == "user":
            print(
                "      Hermes reads local skills from ~/.hermes/skills. "
                "Use /skills list or /<skill-name> in Hermes to confirm it "
                "is available."
            )
        else:
            print(
                "      Hermes project scope is staged as a real SKILL.md "
                "folder. Add this directory to skills.external_dirs in "
                "~/.hermes/config.yaml, or install the public repo path with "
                f"'hermes skills install Yaked1/ai-lab-codex-workbench/skills/{slug}' "
                "after the skill is published."
            )


def cmd_list(root: Optional[Path]) -> int:
    manifest = load_manifest(root)
    for entry in manifest["skills"]:
        print(f"{entry['slug']:40} [{entry['category']:16}] {entry['description']}")
    print(f"\n{len(manifest['skills'])} skills. Harnesses: {', '.join(ALL_HARNESSES)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", action="store_true", help="List every available skill and exit")
    parser.add_argument("--skill", help="Slug of the skill to install (see --list)")
    parser.add_argument("--all", action="store_true", help="Install every skill for the given harness")
    parser.add_argument("--harness", choices=ALL_HARNESSES, help="Target agent harness")
    parser.add_argument(
        "--scope",
        choices=["project", "user"],
        default="project",
        help="Install scope for harnesses with documented project/user locations",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite an existing installed skill")
    parser.add_argument("--dry-run", action="store_true", help="Preview the target path without writing")
    args = parser.parse_args()

    root = repo_root()

    if args.list:
        return cmd_list(root)

    if not args.harness:
        parser.error("--harness is required unless --list is given")
    if not args.skill and not args.all:
        parser.error("either --skill <slug> or --all is required")

    manifest = load_manifest(root)
    slugs = [entry["slug"] for entry in manifest["skills"]] if args.all else [args.skill]

    known = {entry["slug"] for entry in manifest["skills"]}
    unknown = [slug for slug in slugs if slug not in known]
    if unknown:
        print(f"Unknown skill slug(s): {', '.join(unknown)}. Run --list to see valid slugs.", file=sys.stderr)
        return 1

    for slug in slugs:
        install_one(root, slug, args.harness, args.scope, args.force, args.dry_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# RESEARCH-GRADE-EXPANSION:BEGIN
# Research-grade maintenance notes:
# - Role: repository automation script.
# - Review this file for clear inputs, outputs, side effects, and failure behavior.
# - Keep examples public-safe and repository-relative; avoid secrets or private paths.
# - When behavior changes, update adjacent tests, docs, and changelog evidence.
# - Prefer deterministic, reviewable operations over hidden or networked side effects.
# RESEARCH-GRADE-EXPANSION:END
