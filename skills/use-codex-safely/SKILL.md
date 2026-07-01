---
name: use-codex-safely
description: Use when starting a new OpenAI Codex session against this repository (or a repository following its AGENTS.md convention) and you need a safe first-task workflow -- reading local rules, scoping a task, running checks, and opening a reviewable PR.
category: tools
source:
  - docs/tools/codex.md
  - docs/codex/00-start-here.md
  - docs/codex/01-codex-goal-workflow.md
  - AGENTS.md
---

# Use Codex Safely

## Trigger

Use this skill when a human asks Codex to do real work in this repository
(or a repository with a similar `AGENTS.md`) for the first time in a
session, or whenever the task is broad enough that scope needs to be
established before editing. Do not use it for a single-line read-only
question that needs no file changes -- just answer directly.

## Purpose

Turn "help with the repo" into a bounded, reviewable, checked change: read
the repository's own rules first, agree on scope, edit only what the task
names, verify locally, and hand back a report a human can act on without
re-deriving what happened.

## Inputs

- The task, in one sentence.
- Which files or folders are in scope (ask if not stated).
- Whether the change is docs-only, script-only, or both.

## Scope

Allowed by default: Markdown docs, prompt templates, standard-library Python
scripts already in the repo, and their tests.

Forbidden unless the task explicitly asks for it: `.env` / `.env.*` /
credentials, GitHub Actions workflow YAML, new dependencies, binary or
generated artifacts, and anything outside the files the task named.

## Procedure

1. Run `git status` and read `AGENTS.md` (or the repository's equivalent
   root rules file) in full before touching anything.
2. Read every file the task names before editing any of them.
3. State the scope back in one line: what will change, what will not.
4. Make the smallest edit that satisfies the task.
5. Run the repository's own verification commands (see below).
6. Review the diff yourself before reporting it as done.
7. If the task implies a durable change, create a branch named
   `agent/<short-task-name>`, commit, and open a PR describing what
   changed, why, and what was checked -- do not push directly to `main`
   unless the human explicitly asked for that.

## Verification

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

If a check fails and the failure is related to your change, fix the
smallest likely cause and re-run. If it is unrelated, report it plainly
instead of expanding the task to fix it silently.

## Failure Cases

- The task's scope is ambiguous ("clean up the docs") -- stop and ask which
  files, rather than guessing broadly.
- A step would require a new dependency, editing workflow YAML, or touching
  a secret/credential file -- stop and ask for explicit approval first.
- A verification command fails for a reason unrelated to the task -- report
  it instead of rewriting unrelated code to make it pass.
- The repository has no `AGENTS.md`-equivalent rules file -- say so, and ask
  the human what local conventions (if any) should apply before editing.

## Final Report

- Files changed (exact paths).
- Commands run and whether each passed.
- Any check skipped, and why.
- Claims about Codex's own product behavior (pricing, plan tier, exact
  skill-discovery path) that still need official-doc verification --
  Codex's current skill-discovery path specifically is not settled; see
  [docs/skills/codex.md](../../docs/skills/codex.md).
- Remaining risks.

## Disable Path

Remove this skill's folder from wherever it was installed (see
[skills/README.md](../README.md#installer-behavior) for the exact path per
harness). Removing it does not affect `AGENTS.md` or any other file in this
repository -- this skill only summarizes existing docs, it does not gate
anything.
