# Codex Skills

Source status: official-doc anchored. Current path and surface claims were
checked against OpenAI Codex skills documentation on 2026-07-02; re-check the
same page before future product-specific edits:
<https://developers.openai.com/codex/skills>

## What It Is

Codex skills package task-specific instructions, resources, and optional scripts
so Codex can follow repeatable workflows. They are useful for recurring
documentation, review, testing, or research workflows when the boundaries are
clear.

## What "Skill" Means In This Repo's Codex Workflow

This repository now ships a 100+ item `skills/` catalog with native
`SKILL.md` bundles, plus two repo-local conventions that function as the
practical skill layer for Codex sessions here. Keep the packaging boundaries
clear: the skill catalog is ordinary repository content that can be copied by
the installer, while product behavior should be re-checked in official docs
before future setup claims are broadened.

| Convention | What it is | Where it lives | Official Codex feature? |
| --- | --- | --- | --- |
| `AGENTS.md` | Always-on repository rules Codex (and other agents) should read before any edit. | Repo root: [AGENTS.md](../../AGENTS.md) | Yes -- `AGENTS.md` is a recognized convention Codex looks for; verify exact discovery behavior in official docs. |
| `skills/*/SKILL.md` | Installable procedures for the repository's docs, prompt templates, safe Codex work, bounded goal-running, skill creation, and skill installation. | [skills/](../../skills/), installed to `.agents/skills/<slug>/SKILL.md` or `~/.agents/skills/<slug>/SKILL.md` | Yes -- OpenAI docs describe `.agents/skills` repo/user locations and say skills are available in Codex CLI, IDE extension, and Codex app. |
| `.goal.md` prompt files | Repo-local, human-authored prompt templates that structure a Codex "goal mode" task end to end (objective, scope, safety, verification, report format). | [prompts/codex/*.goal.md](../../prompts/codex/) | No -- this is a repo convention, not a Codex product feature. The `.goal.md` suffix and folder location are choices this repository made, not something Codex requires. |
| `.github/codex/prompts/*.md` | Prompt bodies used by this repo's own automation (for example the daily curator prompt) rather than by an interactive user. | [.github/codex/prompts/](../../.github/codex/prompts/) | No -- also repo-local, consumed by this repo's scripts/workflows, not a Codex product mechanism. |

The common thread with a native `SKILL.md` bundle (see
[claude-code.md](claude-code.md)) is real: both are "a documented,
bounded procedure with a trigger, scope, and verification steps." The
difference is packaging and authority. A `skills/*/SKILL.md` file is a native
skill-bundle shape that the installer copies into Codex's documented
`.agents/skills` location. A `.goal.md` file in this repo is plain Markdown
that a human pastes into a Codex session (or a maintainer script assembles
into a prompt) -- it
has no special loading mechanism of its own. Never describe
`prompts/codex/*.goal.md` as something Codex auto-discovers or auto-runs; it
is invoked because a person copies it in, the same way `/goal` in Claude Code
is a user-authored custom command, not a built-in feature (see
[claude-code.md](claude-code.md) for that distinction).

## Worked Example: This Repo's Own `.goal.md` Convention

[prompts/codex/docs-update.goal.md](../../prompts/codex/docs-update.goal.md)
is a real file in this repo and a good model for what a Codex "skill-like"
prompt looks like here. Its shape:

```text
## Target Tool          -- OpenAI Codex CLI or Codex-style goal mode.
## Purpose               -- one sentence, what recurring task this covers.
## Inputs To Fill        -- {topic}, {audience}, {files_to_inspect}, etc.
## Full Prompt           -- the complete /goal-style prompt, with mandatory
                            first steps (git status, read AGENTS.md, read
                            target files), included/excluded scope, safety
                            boundaries, verification commands, success
                            criteria, and a final report format.
## Short Version         -- a compressed one-paragraph version of the same
                            prompt for quick reuse.
## Included Scope / Excluded Scope
## Safety Boundaries
## Verification Steps    -- the same three repo-wide commands used everywhere:
                            repo_health_check.py, safe_autofix.py --check,
                            unittest discover.
## Success Criteria
## Final Report Format
## Failure Cases
## Anti-Patterns
```

The other files in [prompts/codex/](../../prompts/codex/) --
`fix-bug.goal.md`, `implement-feature.goal.md`, `repository-cleanup.goal.md`,
and `review-pr.goal.md` -- follow the same template. This is what "authoring
a Codex skill safely in this repo" means in practice: writing one more
`.goal.md` file with the same required sections (this repo's test suite,
`tests/test_prompting_docs.py`, actually checks that every file under
`prompts/` includes headings such as `## Target Tool`, `## Full Prompt`,
`## Included Scope`, `## Excluded Scope`, `## Safety Boundaries`,
`## Verification Steps` or `## Verification`, `## Success Criteria`,
`## Final Report Format`, and `## Failure Cases`).

For installable bundles, see [skills/README.md](../../skills/README.md) and
[skills/INDEX.md](../../skills/INDEX.md). For a new task-specific prompt,
use the `.goal.md` convention instead. Keep the two conventions separate in
the docs: a `SKILL.md` bundle is a product feature Codex can load per its own
discovery rules (re-check current docs before broadening claims), while a
`.goal.md` file in `prompts/codex/` is always manually pasted in by a person.

## Beginner Friendliness

Medium. A learner should understand `AGENTS.md`, Git branches, local checks, and
PR review before creating write-capable skills.

## Installation

Use the repository installer to copy a concrete `SKILL.md` bundle from
[skills/](../../skills/) into the local Codex skill path:

```powershell
python scripts/install_skill.py --list
python scripts/install_skill.py --skill use-codex-safely --harness codex-cli
python scripts/install_skill.py --all --harness codex-cli
python scripts/install_skill.py --all --harness codex-desktop
```

PowerShell users can run the equivalent native script:

```powershell
.\scripts\install_skill.ps1 -List
.\scripts\install_skill.ps1 -Skill use-codex-safely -Harness codex-cli
.\scripts\install_skill.ps1 -All -Harness codex-cli
.\scripts\install_skill.ps1 -All -Harness codex-desktop
```

The installer writes actual files under `.agents/skills/<slug>/SKILL.md` for
project scope, or `~/.agents/skills/<slug>/SKILL.md` with `--scope user` /
`-Scope user`. Use the `codex` harness name as a shorter alias if you do not
need to distinguish CLI from app in command examples.

For this repo's own `.goal.md` convention, no special directory creation is
needed -- it is just a new Markdown file:

```powershell
New-Item -ItemType File -Path .\prompts\codex\new-task.goal.md -Force
```

## Required Files And Folder Shape

```text
docs-review/
  SKILL.md
  references/
  scripts/
```

Keep `references/` and `scripts/` optional. If a script is included, document how
to run it, how to test it, and what files it may touch.

This repo's `.goal.md` convention is flatter -- one file per task family,
no subfolders:

```text
prompts/codex/
  docs-update.goal.md
  fix-bug.goal.md
  implement-feature.goal.md
  repository-cleanup.goal.md
  review-pr.goal.md
```

## How To Test

```powershell
git status
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

For a skill-specific test, ask Codex to run a read-only explanation task before
allowing edits. For a new `.goal.md` file specifically, also run:

```powershell
python -m unittest tests.test_prompting_docs
```

That module (`tests/test_prompting_docs.py`) enumerates every file under
`prompts/` and fails if a required section heading is missing, so it is the
fastest way to confirm a new goal file matches the repo's own template
before the full suite runs.

## Safe Use Cases

- Public documentation curation.
- Prompt-template review.
- Source-safety review.
- Small script testing.
- PR summary drafting.

## Unsafe Or Inappropriate Use Cases

- Unrestricted daily publishing.
- Direct pushes to `main`.
- Secret scanning that prints secrets.
- Private folder indexing.
- Prompt leaking or jailbreak guidance.
- Broad workflow rewrites without a dedicated automation task.

## Common Errors

| Error | Likely cause | Response |
| --- | --- | --- |
| Codex edits too much | Skill lacks excluded scope. | Add explicit allowed and forbidden paths. |
| Commands are stale | Product behavior changed. | Mark as official-doc verification items. |
| Checks are skipped | Skill ends at drafting. | Require validation and final reporting. |

## Troubleshooting Table

| Symptom | Likely cause | Response |
| --- | --- | --- |
| Skill or goal file not picked up | For a native `SKILL.md`, the file is outside Codex's `.agents/skills` discovery path or the Codex session has not refreshed. For a `.goal.md` file in this repo, it was never pasted into the session -- there is no auto-discovery for repo-local prompt files. | Move the bundle under `.agents/skills/<slug>/SKILL.md` or `~/.agents/skills/<slug>/SKILL.md` and restart or refresh Codex if needed; for `.goal.md` files, paste the prompt body into the session explicitly, since that is the entire mechanism. |
| Wrong skill triggered | Trigger wording overlaps with another skill's description, or two `.goal.md` files cover near-identical objectives. | Narrow the trigger language; check `prompts/codex/` for an existing overlapping template before adding a new one. |
| Codex edits files outside the intended `.goal.md` scope | The `## Included Scope` / `## Excluded Scope` sections were vague or missing specific paths. | Rewrite scope sections with explicit file paths, following `docs-update.goal.md` as the template. |
| Prompt guide or goal file followed inconsistently across sessions | The prompt lacks an explicit "mandatory first steps" ordering, so different sessions read files in a different order and drift. | Add numbered mandatory first steps (git status, read AGENTS.md, read target files) as `docs-update.goal.md` does. |
| Final report is missing required evidence | The `.goal.md` file's `## Final Report Format` section was skipped or the model ignored it. | Re-state the exact report headings in the prompt and re-run; treat a missing report as an incomplete task, not a done one. |
| `tests.test_prompting_docs` fails on a new goal file | A required section heading (see the list above) is missing or misspelled. | Compare headings against `docs-update.goal.md` exactly, including the `##` level. |

## Disable Or Uninstall

Move or remove the skill folder from the active Codex skill location. For a repo
example, remove it through a normal branch and PR. For this repo's `.goal.md`
convention, delete the specific file under `prompts/codex/` through a normal
branch and PR -- there is no separate "disable" step because nothing is
auto-loaded.

## Public Repository Safety

- Keep skill docs public-safe.
- Do not commit private memories or hidden local config.
- Do not add dependencies unless explicitly approved.
- Keep generated guide updates behind branch, PR, checks, and review.

## Checklist: Writing A New Skill Or Goal File Safely In This Repo

- [ ] Decide which convention fits: a native `SKILL.md` bundle under
      `.agents/skills` (official Codex feature) or a `.goal.md` prompt
      file (repo-local, manually pasted, no auto-loading).
- [ ] Read `AGENTS.md` in full before drafting.
- [ ] Name the trigger: what recurring task does this cover, and what should
      *not* trigger it?
- [ ] Name `## Included Scope` and `## Excluded Scope` with explicit file
      paths, not general descriptions.
- [ ] Include mandatory first steps: `git status`, read `AGENTS.md`, read
      every file named in scope before editing.
- [ ] Add `## Safety Boundaries` that explicitly forbid secrets, `.env`
      files, credentials, private links, private paths, dependency
      additions, and workflow YAML edits unless the task explicitly asks
      for them.
- [ ] Add `## Verification Steps` using this repo's real commands:
      `python scripts/repo_health_check.py`,
      `python scripts/safe_autofix.py --check`,
      `python -m unittest discover -s tests`.
- [ ] Add `## Success Criteria`, `## Final Report Format`, and
      `## Failure Cases` sections, matching the headings
      `tests/test_prompting_docs.py` checks for.
- [ ] Confirm no exact pricing, plan tier, or model-availability claim is
      hardcoded -- mark it "verify current details in official docs"
      instead.
- [ ] Run the new or edited file through the full local check suite before
      opening a PR.
- [ ] Confirm the diff only touches the intended skill/prompt file (plus
      `CHANGELOG.md` if the change is user-visible).

## Skill Authoring Checklist

- [ ] The skill name describes a repeatable task.
- [ ] `SKILL.md` states trigger conditions.
- [ ] Required files are public-safe.
- [ ] Optional scripts are documented and testable.
- [ ] The skill says what it may read.
- [ ] The skill says what it may edit.
- [ ] The skill says what requires approval.
- [ ] The final report format includes files, commands, checks, and risks.
- [ ] Current product behavior is marked for official-doc verification.

## Minimal Public Skill Skeleton

```markdown
# Documentation Review Skill

Use when the user asks for a public documentation review.

Read:
- AGENTS.md
- README.md
- The requested docs

Do:
- Identify clarity, safety, source, and verification issues.
- Return findings ordered by severity.

Do not:
- Edit files unless explicitly asked.
- Read secrets or private folders.
- Make exact current product claims without official docs.

Final report:
- Findings
- Files reviewed
- Checks run or not run
- Claims needing verification
```

## Review Questions

- Does the skill duplicate an existing prompt template, or does it add real
  reusable procedure?
- Would a new user know when it triggers?
- Could it accidentally read private data?
- Could it edit files outside the intended scope?
- Are scripts optional, safe, and covered by tests?
- Is disabling or removing the skill straightforward?
- If this is a `.goal.md` file, does it match the section headings
  `tests/test_prompting_docs.py` already enforces for everything under
  `prompts/`?

## Claims To Verify In Official Docs

The following are fast-changing or product-specific and must not be stated
as settled fact without a fresh check against
<https://developers.openai.com/codex/skills> or the relevant Codex product
docs:

- Whether `SKILL.md` folder locations and discovery rules have changed for a
  given Codex surface (CLI, IDE extension, app, web, cloud).
- Whether Codex auto-loads skills versus requiring explicit invocation.
- Plan tier, subscription, or pricing requirements for any Codex surface.
- Model availability or default model behavior inside Codex sessions.
- Any claim about how `AGENTS.md` is merged with other instruction sources
  (for example nested `AGENTS.md` files or IDE-specific settings).
- Sandbox, approval-mode, or permission-prompt defaults for local, IDE, web,
  or cloud Codex workflows.

## Maintenance

Review public skill docs when:

- Codex skill behavior changes in official docs.
- Repository checks change.
- Prompt-template section requirements change.
- A skill starts producing broad diffs.
- A security or public-safety rule changes.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `docs/skills/codex.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `codex` state what decision, workflow, or reusable behavior it supports?
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
<!-- RESEARCH-GRADE-EXPANSION:END -->
