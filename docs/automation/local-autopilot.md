# Local Autopilot

`scripts/local_autopilot.ps1` is a Windows PowerShell helper for the common
maintainer loop. It wraps safe Git and GitHub CLI commands, copies the latest
curator prompt to the clipboard, and starts a local agent (Codex or Claude
Code) when requested.

It never commits automatically, never force-pushes, never merges pull
requests, never deletes branches, and never runs destructive cleanup. Every
write action it performs is a plain `git switch`, `git pull --ff-only`, or
`git merge --ff-only` -- nothing history-rewriting, nothing that touches
`main` directly.

## Requirements

- Run from the repository root.
- Use Windows PowerShell or PowerShell 7.
- Install and authenticate GitHub CLI for modes that call GitHub Actions
  (`status`, `scout`, `prompt`, `full-safe`).
- Install and sign into Codex locally for `local-codex` and `full-safe`.
- Install and sign into Claude Code locally for `local-claude`.
- Keep the working tree clean unless you intentionally pass `-AllowDirty`.

## Quick Command Chooser

Use the smallest mode that matches what you are trying to do.

| Goal | Command | Writes anything? | Needs `gh`? | Needs local agent sign-in? |
| --- | --- | --- | --- | --- |
| See current repo/autopilot state | `.\scripts\local_autopilot.ps1 -Mode status` | No | Optional | No |
| Run the cheap public research scout | `.\scripts\local_autopilot.ps1 -Mode scout` | Workflow may update generated research files | Yes | No |
| Prepare a copyable curator prompt | `.\scripts\local_autopilot.ps1 -Mode prompt -DryRun $true` | Workflow may update generated prompt files | Yes | No |
| Start Codex on a review branch | `.\scripts\local_autopilot.ps1 -Mode local-codex` | Only branch switching/pulling before agent starts | No | Codex |
| Start Claude Code on a review branch | `.\scripts\local_autopilot.ps1 -Mode local-claude` | Only branch switching/pulling before agent starts | No | Claude Code |
| Do the whole safe local loop | `.\scripts\local_autopilot.ps1 -Mode full-safe -DryRun $true` | Generated workflow files plus branch prep | Yes | Codex |

For a first run, start with `status`. It is read-only and gives you the
state you need before choosing a workflow-triggering or agent-starting mode.

## Parameters

| Parameter | Default | Meaning |
| --- | --- | --- |
| `-Mode` | `status` | One of `status`, `scout`, `prompt`, `local-codex`, `local-claude`, `full-safe`. |
| `-Scope` | `hermes-agent` | Passed to `curator-prompt-prep.yml` in `prompt` and `full-safe` modes. |
| `-DryRun` | `$true` | Passed to `curator-prompt-prep.yml`. Keep `$true` unless you intend a real prompt-prep run. |
| `-MaxSources` | `5` | Passed to `curator-prompt-prep.yml` to cap how many sources are considered. |
| `-Branch` | mode-specific | Overrides the branch used by `local-codex`, `local-claude`, or `full-safe`. If omitted, each mode falls back to its own default branch. |
| `-AllowDirty` | off (switch) | Skips the clean-tree check. Only use this after reviewing `git status` yourself. |

## Preflight Checklist

Before using any mode that can switch branches or trigger a workflow:

1. Open PowerShell from the repository root.
2. Run `git status --short --branch`.
3. Confirm the changed files are expected. If you are not sure, stop and ask
   a maintainer before using `-AllowDirty`.
4. Confirm `main` is the intended base branch for this run.
5. For `scout`, `prompt`, or `full-safe`, run `gh auth status`.
6. For `local-codex`, run `codex login status` or the current official Codex
   sign-in/status command documented by OpenAI.
7. For `local-claude`, use the current official Claude Code sign-in/status
   command documented by Anthropic.

Tool setup commands and sign-in behavior can change. If a command here does
not match the current vendor docs, follow the vendor's official docs and then
update this page in a reviewed PR.

## Modes

### `status` -- read-only

```powershell
.\scripts\local_autopilot.ps1 -Mode status
```

Preconditions: none. Safe to run on a dirty tree at any time.

It shows:

- `git status --short --branch`
- Current branch
- Latest five GitHub workflow runs, when `gh` is available
- Latest research inbox files
- Latest curator prompt files
- Open issues, when `gh` is available

If `gh` is not installed, it skips the workflow-run and issue sections and
says so instead of failing.

### `scout` -- trigger the daily research scout

```powershell
.\scripts\local_autopilot.ps1 -Mode scout
```

Preconditions: clean tree (unless `-AllowDirty`), `gh` installed and
authenticated.

It switches to `main`, pulls the latest `main` with `--ff-only`, triggers
`daily-research-scout.yml`, watches the run to completion, pulls `main`
again, and prints the latest generated report path under
`docs/research/inbox/`.

### `prompt` -- prepare a local curator prompt

```powershell
.\scripts\local_autopilot.ps1 -Mode prompt -Scope hermes-agent -DryRun $true -MaxSources 5
```

Preconditions: clean tree (unless `-AllowDirty`), `gh` installed and
authenticated.

It switches to `main`, pulls the latest `main`, triggers
`curator-prompt-prep.yml` with the given `-Scope`, `-DryRun`, and
`-MaxSources`, watches the run, pulls `main` again, copies the latest curator
prompt to the clipboard, and prints the prompt path.

### `local-codex` -- start a local Codex session

```powershell
.\scripts\local_autopilot.ps1 -Mode local-codex
.\scripts\local_autopilot.ps1 -Mode local-codex -Branch codex/curate-research-guides
```

Preconditions: clean tree (unless `-AllowDirty`), `codex` on `PATH` and
signed in.

Default branch: `codex/curate-research-guides` (used automatically if
`-Branch` is omitted).

### `local-claude` -- start a local Claude Code session

```powershell
.\scripts\local_autopilot.ps1 -Mode local-claude
.\scripts\local_autopilot.ps1 -Mode local-claude -Branch claude/curate-research-guides
```

Preconditions: clean tree (unless `-AllowDirty`), `claude` on `PATH` and
signed in.

Default branch: `claude/curate-research-guides` (used automatically if
`-Branch` is omitted).

### `full-safe` -- scout, then prompt, then local Codex

```powershell
.\scripts\local_autopilot.ps1 -Mode full-safe -Scope hermes-agent -DryRun $true -MaxSources 5
```

Preconditions: same as `scout` and `prompt` combined, plus Codex installed and
signed in (this mode always finishes on `local-codex`, using
`codex/curate-research-guides` unless `-Branch` is given).

Runs, in order: `Invoke-Scout`, `Invoke-Prompt`, then `Invoke-LocalAgent` with
`codex`.

## What `local-codex` And `local-claude` Actually Do

Both local agent modes, in order:

1. Refuse to run on a dirty tree unless you pass `-AllowDirty`
   (`Assert-CleanTree`).
2. Confirm the target CLI (`codex` or `claude`) is on `PATH`.
3. Switch to `main` and pull it with `--ff-only`.
4. Create the target branch from `main` if it does not exist, or switch to it
   if it does (`Use-AgentBranch` / `Test-BranchExists`). A missing branch does
   not throw.
5. Try to fast-forward the latest `main` into the branch
   (`git merge --ff-only main`). If the branch has diverged from `main` (for
   example after a previous squash merge), the fast-forward is skipped with a
   warning and the run continues -- this is expected, not fatal.
6. Copy the latest curator prompt to the clipboard.
7. Start the agent (`codex` or `claude`) as the final step.

The script itself makes no commits, never merges pull requests, never
force-pushes, and never deletes branches. Everything after step 7 -- editing
files, running checks, committing, opening a PR -- is the local agent's and
the maintainer's responsibility.

After the agent edits, review the diff and run checks manually. With Claude
Code you can paste the curator prompt directly or save it as a reusable
custom slash command under `.claude/commands/` (for example a `/goal` command
defined in `.claude/commands/goal.md` -- see
[docs/skills/claude-code.md](../skills/claude-code.md) for a worked example).

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

## Source-Inspired Prompting Guide Loop

When using downloaded or archived prompting repositories as inspiration, keep
the local loop explicit:

1. Inventory source names and categories.
2. Extract reusable patterns, not passages.
3. Write original public-safe examples.
4. Add or update navigation so readers can find the new material.
5. Run an anti-slop pass for unsupported claims, hype, copied text, and
   private paths.
6. Run local checks and inspect the diff.
7. Update changelog and release notes when the change is user-visible.

Do not paste local archive paths into public docs. The public page may name
source families or upstream projects, but exact local filesystem locations
belong only in maintainer notes or task context.

## Beginner Workflow With Evidence

Use this sequence when you want a complete, reviewable run:

| Step | Command or action | Evidence to keep |
| --- | --- | --- |
| 1 | `.\scripts\local_autopilot.ps1 -Mode status` | Current branch, dirty/clean state, latest generated files. |
| 2 | `.\scripts\local_autopilot.ps1 -Mode scout` | Workflow run URL or run ID, latest inbox report path. |
| 3 | `.\scripts\local_autopilot.ps1 -Mode prompt -Scope hermes-agent -DryRun $true -MaxSources 5` | Curator prompt path, workflow run result. |
| 4 | Read the generated curator prompt before using it. | Notes on sources rejected or claims to verify. |
| 5 | `.\scripts\local_autopilot.ps1 -Mode local-codex` or `-Mode local-claude` | Branch name and local agent used. |
| 6 | Review the diff before committing. | `git diff --stat` and a short summary of changed files. |
| 7 | Run repository checks. | Command names and pass/fail results. |
| 8 | Open a PR. | PR link, checks, review notes, known limitations. |

The evidence does not need to be noisy. A short PR note with command names,
results, branch name, and generated prompt path is usually enough.

## Safety Boundaries

| Boundary | Why it exists | What to do instead |
| --- | --- | --- |
| No automatic commits | A generated prompt or local agent edit still needs human review. | Review `git diff`, run checks, then commit manually. |
| No direct writes to `main` | Public docs need branch review and rollback history. | Use a focused branch and PR. |
| No force-push or history rewrite | Beginners can lose work when history is rewritten unexpectedly. | Create a new branch or ask a maintainer for recovery help. |
| No destructive cleanup | The script should not remove evidence needed for review. | Clean generated files manually only after reading the diff. |
| No paid LLM calls in GitHub Actions | Avoids secrets, surprise cost, and unattended guide writing. | Run Codex or Claude Code locally with human supervision. |
| Dirty tree requires opt-in | Prevents branch switches from mixing unrelated edits. | Commit, stash, or intentionally rerun with `-AllowDirty` after review. |

## Verification After A Local Agent Run

After `local-codex`, `local-claude`, or `full-safe` starts an agent and the
agent finishes editing, verify the normal repository state yourself:

```powershell
git status --short --branch
git diff --stat
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

For public docs, also skim the changed text for:

- Secrets, token-like values, account IDs, and private links.
- Private machine paths or archive paths.
- Exact product pricing, hosted feature availability, model availability, or
  setup behavior that was not checked against official docs that day.
- Recommendations to run heavy local models, training, or paid automation as
  beginner defaults.

## Rollback And Recovery

The script avoids destructive actions, so most recovery is normal Git work.

| Situation | Recovery |
| --- | --- |
| You started the wrong local branch | Stop the agent, run `git status --short --branch`, and switch back only after confirming no edits would be lost. |
| Generated workflow output is not useful | Leave it unmerged, close the generated PR, or rerun with a narrower scope. |
| The agent edited unrelated files | Do not commit the mixed diff. Move the intended changes to a clean branch or ask for help splitting the work. |
| A fast-forward pull fails | Stop and inspect branch history. Do not force-pull or reset unless a maintainer explicitly approves. |
| A PR was merged with a bad generated file | Open a normal follow-up PR or revert the merge commit, then rerun the deterministic workflow. |
| Clipboard copy failed | Open the latest curator prompt file directly and copy only the public-safe prompt content. |

For published releases or security-sensitive mistakes, follow the repository
release and security policies rather than relying only on this helper.

## Official Documentation To Recheck

Some facts in this guide can drift. Recheck the official docs before making a
public claim about:

| Topic | Why it can drift |
| --- | --- |
| GitHub CLI authentication and workflow-dispatch flags | CLI flags and auth messages may change. |
| Codex CLI install, sign-in, model names, and availability | Product behavior and model access can change. |
| Claude Code install and sign-in behavior | CLI setup and authentication flow can change. |
| GitHub Actions permissions and branch protection behavior | Repository and platform settings can affect results. |

When in doubt, phrase the docs as "verify in official docs" instead of
locking the guide to an exact current behavior.

## Troubleshooting

| Symptom | Likely cause | First response |
| --- | --- | --- |
| Working tree is dirty (`Refusing to continue`) | Local edits are present and `-AllowDirty` was not passed. | Run `git status --short`, then commit, stash, or discard the edits. If the edits are intentional and reviewed, rerun with `-AllowDirty`. |
| `Required command 'gh' was not found` | GitHub CLI is missing or not on `PATH`. | Install GitHub CLI, restart PowerShell, and run `gh auth status`. |
| `Required command 'codex' was not found` | Codex CLI is missing or not on `PATH`. | Install or repair the local Codex CLI and confirm sign-in before rerunning. |
| `Required command 'claude' was not found` | Claude Code CLI is missing or not on `PATH`. | Install or repair the local Claude Code CLI and confirm sign-in before rerunning. |
| `No curator prompt was found in docs/research/curated` | `curator-prompt-prep.yml` has not run yet, or the file was moved/deleted. | Run `-Mode prompt` first, or check `docs/research/curated/` directly. |
| `Could not find a recent run` | GitHub Actions did not start, or `gh` cannot see the repository. | Run `gh run list --limit 5` and verify the repository remote with `gh repo view`. |
| Workflow run fails | CI failed, or a source fetch failed. | Run `gh run view <RUN_ID> --log-failed`. |
| Clipboard copy fails | PowerShell clipboard access is unavailable (for example, over a remote session). | Open the latest file in `docs/research/curated/` and copy it manually. |
| Fast-forward into the branch was skipped | The branch has diverged from `main`, usually after a prior squash merge. | Expected; rebase onto `main` or recreate the branch if you need the latest `main`. |
| Branch already exists with unrelated history | A stale branch from an earlier run was never cleaned up. | Delete the stale local branch yourself after confirming it is merged or abandoned, then rerun the mode. |
| Agent starts but never commits | This is by design -- the script never commits for you. | Review the diff, run local checks, then commit and push yourself. |

## Safety Guarantees Recap

- No automatic commits.
- No force-push.
- No pull request merges.
- No branch deletion.
- No destructive cleanup (`git clean`, `git reset --hard`, etc.).
- Dirty-tree runs require an explicit `-AllowDirty` opt-in.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `docs/automation/local-autopilot.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `local autopilot` state what decision, workflow, or reusable behavior it supports?
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
