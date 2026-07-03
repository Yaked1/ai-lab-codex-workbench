# Google Antigravity Agent Task Template

## Target Tool

Google Antigravity, the agentic development platform surfaced as an
IDE-integrated agent workspace with plan artifacts, task lists, and
multi-agent orchestration. Product surfaces, agent modes, and artifact
formats change quickly. Verify current official documentation before
relying on any specific feature name, artifact type, or permission model
described below; this template uses generic, conservative language on
purpose.

## Purpose

Use this template for a bounded Antigravity task, run either as a single
agent or as a small set of agents working on clearly separated files. It is
written for documentation, prompt-template, and small script changes in
this repository, where a reviewed plan should exist before any file is
written.

## Inputs To Fill

| Input | Description | Example |
| --- | --- | --- |
| `{task}` | The specific, bounded task. | `Plan a documentation cleanup for docs/tools` |
| `{mode}` | Plan-only, plan-then-edit, or small direct implementation. | `Plan first, edit only after approval` |
| `{files}` | Files or globs the agent may touch. | `docs/tools/*.md` |
| `{agent_count}` | How many agents/tasks are involved, to avoid overlap. | `One agent, one file` |
| `{verification}` | Checks to run after any edit. | `repo health, safe autofix, unit tests` |

## Full Prompt

```text
Target tool:
Google Antigravity

Goal:
Create a reviewed plan, and if approved, a small implementation, for:
{task}

Mode:
{mode}

Agent scope:
{agent_count}
If more than one agent or task is involved, assign each one non-overlapping
files so two agents never propose edits to the same file without a human
merging them.

Instructions:
- Read AGENTS.md first and follow its rules for this repository.
- Keep all work inside this repository; do not reference or fetch content
  from outside repositories or private systems.
- Use one branch for one task.
- Produce a plan artifact (task list, file list, or outline) before editing
  if the task touches more than one file.
- List the exact files you intend to change before making any edit, using
  paths relative to the repository root: {files}
- Prefer documentation, prompt-template, or small testable script changes
  for a first run with this template.
- Keep external AI tool claims conservative; do not state exact pricing,
  model availability, or platform support without a dated, official-doc
  citation, and mark anything uncertain as "needs verification".

Boundaries:
- Do not expose secrets, credentials, tokens, or private links in the plan,
  the diff, or the final report.
- Do not modify GitHub Actions workflow YAML unless explicitly requested.
- Do not add dependencies or new packages.
- Do not run destructive automation (no force-push, no recursive deletes,
  no history rewriting).
- Do not let parallel agents or tasks edit overlapping files without a
  human reviewing and merging the result first.
- Do not silently expand scope beyond {files}; if the task clearly needs
  another file, stop and name it in the plan for approval first.

Validation:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests
- git diff --check

Final response:
- Plan or implementation summary
- Files changed (exact paths)
- Commands/checks run and their results
- Claims needing manual verification against official Antigravity docs
- Remaining risks, including any file-ownership overlap risk
```

## Short Version

```text
Use Antigravity to plan {task}. Read AGENTS.md, list {files} before editing,
do not edit until the plan is approved, keep agents on non-overlapping
files, avoid secrets/dependencies/workflow changes, run the repo checks
after any edit, and report files changed, commands run, verification gaps,
and risks.
```

## Included Scope

- Files, plan artifacts, or repository areas explicitly named in `{files}`.
- The requested task in `{task}` and directly adjacent documentation needed
  to keep cross-links and navigation accurate.
- A written plan (file list, ordered steps, or task breakdown) produced
  before any multi-file edit.
- Local verification commands run after edits are applied.

## Excluded Scope

- Any file outside `{files}` that was not explicitly approved after being
  named in the plan.
- Secrets, `.env` / `.env.*` files, credentials, private links, private
  paths, browser profiles, and account-specific data.
- Dependency installation, GitHub Actions workflow YAML, generated
  archives, release publishing, and destructive automation, unless the task
  explicitly asks for one of these.
- Exact, dated claims about Antigravity's own pricing, plan tiers, model
  routing, or availability, unless freshly verified against official docs
  and dated in the report.

## Success Criteria

- The plan or implementation stays inside the bounds of `{task}` and
  `{files}`.
- File ownership between any concurrent agents or tasks is unambiguous, with
  no two agents proposing edits to the same file unreviewed.
- No secrets or private data appear in the plan, diff, or final report.
- Local checks pass after edits, or failures are reported with output.
- Any claim about Antigravity's own current features is marked for
  official-doc verification rather than stated as fact.

## Safety Boundaries

- Treat Antigravity's multi-agent or parallel-task features as a
  concurrency risk: never approve two agents editing the same file without
  a human merging the result.
- No secrets, tokens, or private links in any plan artifact, chat log, or
  report the agent produces.
- No destructive automation: no force-push, no bulk deletion, no workflow
  YAML edits unless explicitly requested.
- No unverified setup, pricing, or platform-availability claims; use
  "verify in official docs" language instead of asserting specifics.
- Require a human-reviewed plan before any edit that spans more than one
  file, even if the agent's mode allows direct implementation.

## Verification

```powershell
git status
git diff
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
git diff --check
```

## Final Report Format

```markdown
## Summary
## Plan or files changed
## Commands/checks
## Claims needing manual verification
## Remaining risks
```

## Failure Cases

| Failure | What to do |
| --- | --- |
| Product behavior, feature name, or permission model is unclear or seems to have changed | Stop, do not guess, and verify against current official Antigravity docs before continuing. |
| Multiple agents or tasks propose overlapping file edits | Assign explicit file ownership per agent, or fall back to a single agent for this task, and require human merge review. |
| The task grows beyond the files named in `{files}` | Stop, write the additional files into the plan, and get explicit approval before editing them. |
| A required check cannot run in the Antigravity environment | Run the same commands manually in PowerShell and report what could not be verified inside the tool. |
| The agent's final report claims a check passed without showing output | Reject the report and require the actual command output before accepting the result. |
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **agent prompt template** surface. During broad
maintenance, reviewers should treat `prompts/antigravity/agent-task.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `agent task` state what decision, workflow, or reusable behavior it supports?
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
