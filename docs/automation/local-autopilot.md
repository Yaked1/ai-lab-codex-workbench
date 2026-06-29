# Local Autopilot

`scripts/local_autopilot.ps1` is a Windows PowerShell helper for the common maintainer loop. It wraps safe Git and GitHub CLI commands, copies the latest curator prompt to the clipboard, and starts a local agent (Codex or Claude Code) when requested.

It never commits automatically, never force-pushes, never merges pull requests, never deletes branches, and never runs destructive cleanup.

## Requirements

- Run from the repository root.
- Use Windows PowerShell or PowerShell 7.
- Install and authenticate GitHub CLI for modes that call GitHub Actions.
- Install and sign into Codex locally for `local-codex` and `full-safe`.
- Install and sign into Claude Code locally for `local-claude`.
- Keep the working tree clean unless you intentionally pass `-AllowDirty`.

## Modes

Status mode is read-only:

```powershell
.\scripts\local_autopilot.ps1 -Mode status
```

It shows:

- `git status`
- Current branch
- Latest five GitHub workflow runs, when `gh` is available
- Latest research inbox files
- Latest curator prompt files
- Open issues, when `gh` is available

Scout mode runs the daily scout workflow:

```powershell
.\scripts\local_autopilot.ps1 -Mode scout
```

It switches to `main`, pulls the latest `main`, triggers `daily-research-scout.yml`, watches the run, pulls `main` again, and prints the latest generated report path.

Prompt mode prepares a local curator prompt:

```powershell
.\scripts\local_autopilot.ps1 -Mode prompt -Scope hermes-agent -DryRun $true -MaxSources 5
```

It switches to `main`, pulls the latest `main`, triggers `curator-prompt-prep.yml`, watches the run, pulls `main` again, copies the latest curator prompt to the clipboard, and prints the prompt path.

Local Codex mode creates or switches to a local branch and starts Codex. The
branch defaults to `codex/curate-research-guides`, so you do not have to pass
one:

```powershell
.\scripts\local_autopilot.ps1 -Mode local-codex
.\scripts\local_autopilot.ps1 -Mode local-codex -Branch codex/curate-research-guides
```

Local Claude Code mode does the same thing for the Claude Code CLI. The branch
defaults to `claude/curate-research-guides`:

```powershell
.\scripts\local_autopilot.ps1 -Mode local-claude
.\scripts\local_autopilot.ps1 -Mode local-claude -Branch claude/curate-research-guides
```

Both local agent modes:

- Refuse to run on a dirty tree unless you pass `-AllowDirty`.
- Switch to `main` and pull it with `--ff-only`.
- Create the target branch from `main` if it does not exist, or switch to it if
  it does. A missing branch no longer throws; the old `.Trim()`-on-null bug is
  fixed.
- Try to fast-forward the latest `main` into the branch. If the branch has
  diverged from `main` (for example after a previous squash merge), the
  fast-forward is skipped with a warning and the run continues.
- Copy the latest curator prompt to the clipboard.
- Start the agent as the final step. They never commit, never merge pull
  requests, never force-push, and never delete branches.

After the agent edits, review the diff and run checks manually. With Claude
Code you can paste the curator prompt directly or save it as a reusable custom
slash command under `.claude/commands/` (for example a `/goal` command defined
in `.claude/commands/goal.md`).

Full safe mode runs scout, prompt prep, prompt copy, branch setup, and local
Codex on `codex/curate-research-guides`:

```powershell
.\scripts\local_autopilot.ps1 -Mode full-safe -Scope hermes-agent -DryRun $true -MaxSources 5
```

## Recommended Beginner Workflow

1. Run status mode.
2. Make sure the working tree is clean.
3. Run scout mode.
4. Run prompt mode with `-DryRun $true`.
5. Review the generated prompt.
6. Run local Codex mode (`-Mode local-codex`) or local Claude Code mode
   (`-Mode local-claude`) on a focused branch.
7. Run local checks.
8. Open a pull request for human review.

## Troubleshooting

| Symptom | Likely cause | First response |
| --- | --- | --- |
| `Required command 'gh' was not found` | GitHub CLI is missing or not on `PATH`. | Install GitHub CLI, restart PowerShell, and run `gh auth status`. |
| `Could not find a recent run` | GitHub Actions did not start or `gh` cannot see the repository. | Run `gh run list --limit 5` and verify the repository remote. |
| Working tree is dirty | Local edits are present. | Commit, stash, or inspect them before running a modifying mode. |
| Workflow run fails | CI or source fetching failed. | Run `gh run view <RUN_ID> --log-failed`. |
| Clipboard copy fails | PowerShell clipboard access is unavailable. | Open the latest file in `docs/research/curated/` and copy it manually. |
| `codex` is not found | Codex CLI is missing or not on `PATH`. | Install or repair the local Codex CLI and confirm sign-in before rerunning. |
| `claude` is not found | Claude Code CLI is missing or not on `PATH`. | Install or repair the local Claude Code CLI and confirm sign-in before rerunning. |
| Fast-forward into the branch was skipped | The branch has diverged from `main`. | Expected after a prior merge; rebase onto `main` or recreate the branch if you need the latest `main`. |
