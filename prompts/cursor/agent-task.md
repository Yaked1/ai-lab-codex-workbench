# Cursor Agent Task Template

## Target Tool

Cursor Agent (in Agent mode) or Cursor's Plan mode, used from the Cursor IDE
chat/agent panel. This template assumes the human can see and approve the
proposed plan and diff inside the editor before anything is applied.

## Purpose

Use this template for a focused IDE-based task where the user can inspect
plans and diffs before accepting changes. It is built for small,
well-scoped documentation, prompt-template, or script edits in this
repository, not for open-ended refactors.

## Inputs To Fill

| Input | Description | Example |
| --- | --- | --- |
| `{task}` | The specific, one-sentence task. | `Expand docs/workflows/public-repo-safety.md with a checklist` |
| `{mode}` | Plan-first or direct agent edit. | `Plan first, then edit after approval` |
| `{files}` | Exact files or globs in scope. | `docs/workflows/public-repo-safety.md` |
| `{checks}` | Local checks to run after edits. | `repo health, safe autofix, unit tests` |
| `{context_files}` | Files Cursor should read before proposing anything. | `AGENTS.md`, `README.md` |

## Full Prompt

```text
Target tool:
Cursor

Mode:
{mode}

Goal:
Make this focused change:
{task}

Required context:
- Read AGENTS.md before proposing a plan.
- Read {context_files} to match existing structure, tone, and heading style.
- Inspect the relevant files in {files} before editing.
- Keep the change scoped to {files}; do not expand scope mid-task.
- If the task touches more than one file, produce a plan first and wait for
  my approval before applying any edit.

Boundaries:
- Do not edit .env, .env.*, credentials, browser profiles, private
  documents, private links, private paths, or any folder outside {files}.
- Do not install dependencies or modify lock files.
- Do not run destructive commands (no git reset --hard, no force-push, no
  recursive deletes) without asking first.
- Do not modify GitHub Actions workflow YAML unless explicitly requested.
- Do not accept or apply broad, repository-wide rewrites unless the task
  explicitly asks for them.
- Do not state exact pricing, model, or platform claims for any AI tool
  unless verified against official docs in this session; use conservative,
  "verify in official docs" language instead.

Success criteria:
- The task described in {task} is fully complete.
- The diff touches only {files} and is small and reviewable in the Cursor
  diff view.
- External tool claims are conservative and flagged where unverified.
- Local checks pass, or failures are reported with their output.

Validation if files changed (run in PowerShell):
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests
- git diff --check

Final response:
- Summary of what changed and why
- Files changed
- Commands run
- Checks run and their result
- Claims needing manual verification
- Remaining risks
```

## Short Version

```text
Use Cursor ({mode}) to {task}. Read AGENTS.md, plan first if multi-file,
edit only {files}, avoid secrets/dependencies/workflow changes, no invented
tool claims, run the checks, and report files, commands, checks, claims to
verify, and risks.
```

## Included Scope

- Files or repository areas explicitly listed in `{files}`.
- Adjacent docs needed to preserve navigation and cross-link consistency
  (for example updating a table of contents entry when a heading changes).
- A written plan artifact (Cursor's Plan mode output or an inline task
  list) before any multi-file edit.
- Local checks named in `{checks}` or in this repository's AGENTS.md, run
  from the integrated terminal or PowerShell.

## Excluded Scope

- Any file not listed in `{files}`, including files Cursor suggests adding
  mid-task without being asked first.
- Secrets, `.env` files, credentials, browser profiles, private links, and
  private machine paths.
- Dependency installation, GitHub Actions workflow YAML, generated
  archives, and destructive commands, unless explicitly approved for this
  task.
- Unsupported or exact current product claims about any AI tool.

## Success Criteria

- The plan (if produced) is understandable to a reviewer with no other
  context.
- The applied diff matches the approved scope exactly.
- No private data, secrets, or credentials are added anywhere in the diff.
- Local checks pass after edits, or failures are reported honestly.

## Safety Boundaries

- No hidden broad rewrites: reject any Cursor-proposed diff that touches
  files outside `{files}` without a prior, explicit approval step.
- No private files, browser profiles, or credentials in context or output.
- No unapproved dependency additions or lock file changes.
- No GitHub Actions workflow YAML changes unless the task explicitly
  requests one.
- No exact external tool claims (pricing, model access, platform support)
  unless freshly verified and noted as such.
- Cursor's Agent mode can call terminal commands; review each proposed
  command before allowing it to run, especially anything destructive.

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
## Files changed
## Commands run
## Checks/tests
## Claims needing manual verification
## Remaining risks
```

## Failure Cases

| Failure | What to do |
| --- | --- |
| Cursor proposes edits to more files than `{files}` | Reject the plan or diff and ask for a narrower scope limited to the approved files. |
| The plan depends on an unverified product fact (pricing, model support, platform availability) | Mark the claim for official-doc verification instead of accepting the wording as-is. |
| Local checks cannot run inside the Cursor terminal panel | Open a separate PowerShell window and run the same commands before merging. |
| The diff includes unrelated edits (formatting churn, unrelated files) | Revert those specific hunks before committing or opening a PR. |
| Cursor's agent wants to run a destructive terminal command | Deny it, ask for the non-destructive alternative, and only proceed with explicit human confirmation. |
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **agent prompt template** surface. During broad
maintenance, reviewers should treat `prompts/cursor/agent-task.md` as a contract-bearing artifact
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
