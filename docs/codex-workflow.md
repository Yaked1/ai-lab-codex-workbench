# Codex Workflow For This Repo

This workflow is for safe local Codex use with the AI Lab workbench. It assumes
the repo is already present under `%USERPROFILE%\Documents\AI-Lab\` and should
not be cloned again.

## Start From The Repo

Preferred:

```powershell
cd $env:USERPROFILE\Documents\AI-Lab\ai-lab-codex-workbench-main
codex --sandbox workspace-write
```

If you need the current configured model explicitly:

```powershell
codex --model gpt-5.5 -c model_reasoning_effort='"high"' --sandbox workspace-write
```

Use `xhigh` only when the task genuinely needs extra reasoning:

```powershell
codex --model gpt-5.5 -c model_reasoning_effort='"xhigh"' --sandbox workspace-write
```

## Start From Documents Safely

When launching from `%USERPROFILE%\Documents`, pin Codex to the repo instead of
letting the whole Documents tree become the working surface:

```powershell
cd $env:USERPROFILE\Documents
codex -C .\AI-Lab\ai-lab-codex-workbench-main --sandbox workspace-write
```

Do not run broad cleanup from `Documents`. If a cleanup task starts from
`Documents`, first change into the repo or pass `-C` with the repo path.

## Usage Discipline

- GPT-5.5 medium: mechanical edits, scripts, formatting, obvious fixes.
- GPT-5.5 high: normal repo work, bounded cleanup, tests, moderate debugging.
- GPT-5.5 xhigh: setup orchestration, architecture, hard debugging, final
  high-stakes review.
- Do not use xhigh for bulk file edits or repeated test retries.
- Avoid broad autonomous cleanup and repeated full-repo reads.
- Prefer durable docs and prompt templates over re-explaining the same workflow
  in chat.

## Goal Mode

Use goal mode when the task has multiple phases, clear success criteria, and a
verification gate. Good examples are setup, bounded cleanup, release packaging,
or a multi-file docs update with named files.

Do not use goal mode for one-line edits, simple commands, vague cleanup, or
tasks without a measurable finish line. Short tasks should stay interactive.

Local config currently exposes goals through `[features] goals = true`, but
long objective length is still a practical UI/runtime limit to verify in the
active Codex surface. If a long goal is rejected, use a short objective that
points to a repo doc such as `docs/setup/codex-claude-agent-reach-full-goal.md`.

## Rollout Budget

Do not add `[features.rollout_budget]` to `%USERPROFILE%\.codex\config.toml`.
This machine's local Codex parser rejected that block. Budget discipline is
manual:

- keep scope narrow;
- avoid unnecessary subagents;
- avoid repeated full-repo reads;
- use high or medium for normal repo work;
- stop after verification instead of continuing into unrelated cleanup.

## Sandbox

Codex CLI supports `read-only`, `workspace-write`, and `danger-full-access`
according to local help output. For normal repo work, prefer
`workspace-write`. `danger-full-access` is unnecessary for routine setup,
docs, prompts, scripts, tests, or cleanup, and should require an explicit
reason.

Never use `--dangerously-bypass-approvals-and-sandbox` for normal repository
work.

## Verification Commands

Run the strongest realistic checks for the touched area:

```powershell
git status --short --branch
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
git diff --check
git diff --stat
```

If a suite fails for a reason unrelated to the setup task, report the failure
clearly and do not broaden scope without approval.

## Safe Cleanup Workflow

1. Start in the repo root, not from `Documents`.
2. Run `git status --short --branch`.
3. Read `AGENTS.md` and the specific files in scope.
4. Use `prompts/codex/repo-cleanup-balanced-goal.md`.
5. Prefer deterministic scripts for large mechanical changes.
6. Do not delete outside an explicit approved list.
7. Run checks and inspect `git diff` before claiming completion.

For general cleanup, do not use `danger-full-access`; use a project-scoped
workspace-write session.
