# Windsurf Agent Task Template

## Target Tool

Windsurf's Cascade agent (or the current vendor-supported IDE agent surface
if the product has since been rebranded or replaced). Used from the
Windsurf IDE's agent chat panel, where the agent can read, propose, and
apply file edits directly in the editor. Product features and surface
names change quickly; verify current official documentation before
teaching exact UI steps.

## Purpose

Use this template for a small IDE-agent task where the agent explains the
relevant files first, proposes a plan, and only edits after approval. Built
for documentation, prompt-template, or small script changes in this
repository.

## Inputs To Fill

| Input | Description | Example |
| --- | --- | --- |
| `{task}` | The specific, focused task. | `Explain docs/tools and improve one page` |
| `{files}` | Exact files or globs in scope. | `docs/tools/windsurf.md` |
| `{mode}` | Explain-first or direct edit. | `Explain first, edit after approval` |
| `{checks}` | Local checks to run after edits. | `repo health, safe autofix, unit tests` |
| `{context_files}` | Files to read for house style before editing. | `AGENTS.md`, `README.md` |

## Full Prompt

```text
Target tool:
Windsurf (Cascade agent)

Goal:
{task}

First step:
Explain the relevant folder or files ({files}) before editing. Read
{context_files} to match existing structure and tone. Propose a short plan
and wait for explicit approval before applying any changes.

Boundaries:
- Read AGENTS.md before proposing a plan.
- Keep edits inside this repository; do not reference external repositories
  or private systems.
- Do not edit .env, .env.*, credentials, browser profiles, private links,
  private paths, or any file outside {files}.
- Do not install dependencies or modify lock files.
- Do not run destructive commands (no git reset --hard, no force-push, no
  recursive deletes) without explicit confirmation.
- Do not modify GitHub Actions workflow YAML unless explicitly requested.
- Do not accept or apply large generated diffs without review; if the
  proposed diff is large, ask for it to be split into smaller steps.
- Do not state exact pricing, model, ownership, or platform claims for any
  AI tool unless verified in official docs; use conservative wording
  otherwise.

Success criteria:
- The relevant files in {files} are explained accurately before any edit.
- A clear, numbered plan exists before edits are applied.
- The diff is focused and matches the approved plan.
- Local checks pass, or failures are reported with their output.

Validation (PowerShell):
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests
- git diff --check

Final response:
- Summary of what changed and why
- Files changed
- Commands run
- Checks run and their result
- Tool claims needing manual verification
- Remaining risks
```

## Short Version

```text
Use Windsurf ({mode}) to {task}. Explain {files} first, wait for approval,
edit only those files, avoid secrets/dependencies/workflow changes, reject
oversized diffs, run the checks, and report files, commands, checks, claims
to verify, and risks.
```

## Included Scope

- Files or repository areas explicitly selected in `{files}`.
- The requested task in `{task}` plus directly related docs or tests needed
  for cross-link and terminology consistency.
- A written explanation of the relevant files and a short plan, produced
  before any edit.
- Safe local checks named in `{checks}` or in this repository's AGENTS.md.

## Excluded Scope

- Any file outside `{files}` that was not named and approved in the plan.
- Secrets, `.env` / `.env.*` files, credentials, browser profiles, private
  links, and private machine paths.
- Dependency installation, GitHub Actions workflow YAML, generated
  archives, and destructive commands, unless explicitly approved for this
  task.
- Exact current product claims (pricing, ownership, platform support) for
  Windsurf or any other AI tool, unless freshly verified and dated.
- Large, unreviewed generated diffs applied in one step without a prior
  explanation and plan.

## Success Criteria

- Explanation of the relevant files precedes any editing.
- The applied diff is visible, reviewed, and matches the approved plan.
- No private data, secrets, or credentials appear anywhere in the diff.
- Local checks pass after edits, or failures are reported honestly.
- Any product claim about an AI tool is conservative and marked for
  verification where relevant.

## Safety Boundaries

- No private files or browser profiles in context or output.
- No broad, unreviewed generated diffs; require an explanation and plan
  before any multi-file change is applied.
- No dependency installation or lock file changes.
- No GitHub Actions workflow YAML changes unless explicitly requested.
- No exact product claims (pricing, ownership, platform availability)
  without verification against official docs.
- If Cascade proposes running a terminal command, review it before allowing
  execution, especially anything destructive.

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
## Tool claims needing manual verification
## Remaining risks
```

## Failure Cases

| Failure | What to do |
| --- | --- |
| Product docs, feature names, or the agent's surface have changed since this template was written | Verify current official Windsurf docs and update the wording before teaching exact steps. |
| The proposed diff is too large to review in one pass | Reject it and ask for the change to be split into smaller, sequential steps. |
| Local checks cannot be run from inside the Windsurf IDE terminal | Open a separate PowerShell window and run the same commands before merging. |
| Private data or a secret-looking string appears in the explanation or diff | Stop immediately, remove it, and follow this repository's security policy (rotate any exposed credential). |
| The agent's explanation of the relevant files is inaccurate or incomplete | Ask for a corrected explanation before approving any plan based on it. |
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **agent prompt template** surface. During broad
maintenance, reviewers should treat `prompts/windsurf/agent-task.md` as a contract-bearing artifact
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
