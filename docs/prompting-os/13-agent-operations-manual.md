# Agent Operations Manual

This manual explains how to run coding agents and tool-using agents in a way
that is scoped, observable, reversible, and safe for public repositories. It
applies to Codex, Claude Code, and comparable local or cloud-assisted agents.

The purpose is operational discipline. A good agent is not one that touches many
files quickly. A good agent produces a reviewable result that satisfies the
requested task, preserves local work, runs checks, and reports risk honestly.

## Operating Principles

1. Inspect before editing.
2. Treat the repository as the source of truth.
3. Keep the task boundary visible.
4. Use tools deliberately.
5. Preserve unrelated local changes.
6. Verify with commands or reviewable artifacts.
7. Report what happened, not what the agent intended.
8. Avoid destructive actions unless explicitly approved.

## Agent Runbook

### 1. Receive The Task

Capture:

- Objective.
- Audience.
- Files likely in scope.
- Files out of scope.
- Safety rules.
- Required checks.
- Whether staging, committing, or pushing is requested.

If the task says "make it comprehensive," convert that into measurable targets:

- README size or sections.
- Package Markdown file count.
- Package byte count.
- Required topics.
- Tests that prevent regression.
- Package manifest evidence.

### 2. Inspect State

Run:

```powershell
git status --short --branch
```

Read:

- `AGENTS.md`.
- Target files.
- Tests for touched scripts.
- Package docs if package behavior changes.

Do not assume the worktree is clean. If it contains staged or unstaged changes,
work with them unless the user explicitly asks to reset.

### 3. Select Permission Profile

| Profile | Allowed | Use when |
| --- | --- | --- |
| Observe | Read, search, summarize. | Review, audit, diagnostics. |
| Draft | Produce proposed text or plan. | User asked for advice or design. |
| Edit docs | Modify Markdown, templates, static HTML. | Documentation or prompt changes. |
| Edit code | Modify scoped scripts/tests. | Bug fixes or features. |
| Package | Build local artifacts and inspect manifests. | Release/package work. |
| Publish | Push, release, send, delete. | Only with explicit approval. |

### 4. Execute

Good execution loop:

```text
inspect -> update plan -> edit -> focused check -> repair -> full check -> status -> report
```

Do not:

- Edit unrelated files.
- Install dependencies without approval.
- Rewrite style across the repo without request.
- Delete files without explicit request.
- Claim checks passed before running them.
- Hide failures.

### 5. Verify

Verification should match the blast radius.

| Change | Verification |
| --- | --- |
| Markdown only | Health check, safe autofix check, relevant tests. |
| Prompt package source | Build package, inspect manifest, run package tests. |
| Script change | Unit tests plus focused manual command. |
| Workflow docs | Link/path review and CI policy check. |
| Static site | Offline-safety review and link sanity. |

### 6. Report

Final report fields:

- Summary.
- Files changed.
- Commands run.
- Checks passed or failed.
- Package evidence, if relevant.
- Risks.
- Unverified items.
- Staging/commit state.

## Dirty Worktree Rules

Agents often work in dirty repositories. The safe rule is simple:

- Do not reset.
- Do not checkout files.
- Do not clean.
- Do not delete.
- Do not overwrite unrelated changes.
- Do not assume existing changes are yours.

If a touched file has prior edits, read the file and make a compatible patch.
If unrelated files are dirty, ignore them and report that they existed.

## Staging Rules

Stage only when the user asks. When staging:

```powershell
git add -A
git status --short --branch
git diff --cached --stat
git diff --cached --check
```

Staging is not a substitute for verification. It only updates the index.

## Tool Use Discipline

Treat every tool call as an operation with a purpose.

| Tool action | Safe default |
| --- | --- |
| Read file | Allowed when in repo and relevant. |
| Search | Prefer `rg` for files and text. |
| Browse web | Use when facts may be current or user requested it. |
| Run tests | Use relevant checks. |
| Build package | Use ignored output directories for validation. |
| Network command | Justify need and scope. |
| Delete/move | Avoid unless explicit and verified. |
| Publish/push | Requires explicit user request. |

## Agent Prompt Template

```text
Objective:
[specific deliverable]

Context:
- Current repo:
- User constraints:
- Relevant files:

Allowed changes:
- [paths]

Forbidden changes:
- [paths/actions]

Procedure:
1. Run git status.
2. Read local instructions and target files.
3. Make a focused change.
4. Run checks.
5. Stage changes only if requested.
6. Report summary, files, commands, checks, and risks.

Failure behavior:
If blocked, report the blocker and the safest next action.
Do not widen scope silently.
```

## Review Questions

Before accepting agent work:

- Does the diff match the task?
- Are unrelated files untouched?
- Are new claims supported?
- Are private paths absent?
- Are secrets absent?
- Did checks run?
- Did tests actually cover the touched area?
- Did package manifests prove package contents?
- Did the final report identify remaining risk?

## Common Agent Failures

| Failure | Symptom | Prevention |
| --- | --- | --- |
| Premature success | Agent reports done after editing but before checks. | Require verification evidence. |
| Scope creep | Many unrelated docs change. | Name allowed paths. |
| Unsafe source use | Leak-derived content appears in docs. | Use structural-only source policy. |
| Hidden dependency | Agent adds package or lock file. | Require approval for dependencies. |
| Dirty-tree damage | User changes disappear. | No reset or checkout; preserve local work. |
| Weak final report | Summary lacks commands or risks. | Use required final report fields. |

## Long-Running Work

For multi-turn work:

1. Maintain a plan.
2. Update plan status as work changes.
3. Keep a context ledger.
4. Re-run current-state checks before claiming completion.
5. Do not mark complete from memory.

Completion means the current state proves the objective. It does not mean the
agent remembers having done something.

## Package-Oriented Agent Work

When the task involves a ZIP or release package:

- Identify the source directory.
- Identify included files.
- Build into an ignored output directory.
- Inspect the manifest.
- Record file count, byte count, hashes, and required files.
- Add tests for package expectations.
- Do not commit generated ZIPs unless explicitly requested.

Example:

```powershell
python scripts/create_prompting_os_package.py --version v1 --output-dir .\.tmp\prompting-os-package-check
Get-Content .\.tmp\prompting-os-package-check\prompting-os-v1-manifest.json -TotalCount 80
```

## Agent Definition Of Done

An agent task is done only when:

- The requested change exists in current files.
- The diff is scoped.
- Relevant checks ran.
- Failing checks are fixed or reported.
- Public-safety rules are preserved.
- Package artifacts are rebuilt when package source changed.
- The final state is staged if the user requested staging.
- The final report is factual.

## Final Rule

Autonomy without audit is just risk with a progress bar. Keep every agent action
connected to evidence.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **Prompting OS module** surface. During broad
maintenance, reviewers should treat `docs/prompting-os/13-agent-operations-manual.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `13 agent operations manual` state what decision, workflow, or reusable behavior it supports?
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
