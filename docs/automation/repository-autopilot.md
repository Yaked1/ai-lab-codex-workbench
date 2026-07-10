# Repository Autopilot

Repository Autopilot is a no-API-key maintenance layer for routine generated
research updates. It combines the existing cheap research scout, scoring,
report generation, local curator prompt prep, deterministic autofix, health
checks, and tests into one GitHub Actions workflow.

It is designed for repository maintenance, not unattended guide writing. No
step in this flow calls a paid LLM API, and no step publishes finished guide
content to `main` on its own.

## End-To-End Flow

The full loop, from daily scouting to a merged guide update, looks like this:

```text
daily-research-scout.yml (scheduled, cheap, public-safe)
        |
        v
data/research/candidates.json (scored candidate list)
        |
        v
curator-prompt-prep.yml (manual trigger)
        |
        v
docs/research/curated/curator-prompt-*.md (ready-to-paste local prompt)
        |
        v
local human-reviewed agent curation
(Codex via ChatGPT sign-in, or Claude Code, run on your machine)
        |
        v
local branch (for example codex/curate-research-guides)
        |
        v
pull request opened by the maintainer
        |
        v
required checks: repo_health_check.py, safe_autofix.py --check, unit tests
        |
        v
human review (diff read, source verification, public-safety check)
        |
        v
controlled merge to main
```

Every arrow in that chain is either a deterministic script/workflow step or an
explicit human action. There is no arrow where a GitHub Actions job silently
writes guide prose and merges it.

### Stage by stage

1. **Daily scout.** `daily-research-scout.yml` runs on a schedule (or manual
   dispatch) and fetches a small number of public source records from
   `data/research/sources.yml`. It scores them and writes
   `data/research/candidates.json` plus a dated report under
   `docs/research/inbox/`. This step is cheap, uses no model-provider API key,
   and never runs Codex.
2. **Candidate scoring.** `data/research/candidates.json` is deterministic
   output: scores, categories, and blocked flags computed by a script, not an
   LLM. `scripts/repo_autopilot_status.py` can summarize it locally without
   `gh`:

   ```powershell
   python scripts/repo_autopilot_status.py
   ```

3. **Curator prompt prep.** `curator-prompt-prep.yml` is a manually triggered,
   cheap workflow. It prepares a ready-to-copy Markdown prompt in
   `docs/research/curated/curator-prompt-*.md`. It does not write guide
   content itself; it writes the *prompt* a human will hand to a local agent.
4. **Local human-reviewed curation.** A maintainer runs `local_autopilot.ps1`
   in `local-codex`, `local-claude`, or `full-safe` mode. The script copies the
   latest curator prompt to the clipboard and starts a local agent (Codex CLI
   through ChatGPT sign-in, or the Claude Code CLI) on a dedicated branch. All
   guide writing happens locally, under the maintainer's own agent session and
   review.
5. **Pull request.** The maintainer (or the local agent, non-destructively)
   pushes the branch and opens a PR. Nothing in this flow pushes directly to
   `main`.
6. **Review and checks.** The PR runs the same checks a contributor would run
   locally: `scripts/repo_health_check.py`, `scripts/safe_autofix.py --check`,
   and `python -m unittest discover -s tests`.
7. **Controlled merge.** A human merges after reading the diff. For curated
   guide content this is always a normal, human-approved merge -- never an
   automatic one.

## What It Does

`repo-autopilot.yml` can:

- Fetch a small number of public source records from `data/research/sources.yml`.
- Score candidates in `data/research/candidates.json`.
- Generate a research inbox report in `docs/research/inbox/`.
- Generate a ready-to-copy local curator prompt in `docs/research/curated/`.
- Run deterministic safe autofix.
- Run repository health checks, formatting checks, and unit tests.
- Create or update the branch `autopilot/generated-research-updates`.
- Open or update the pull request titled `Autopilot generated research updates`.

The workflow commits only these generated files:

- `data/research/candidates.json`
- `docs/research/inbox/*.md`
- `docs/research/curated/curator-prompt-*.md`

## What It Does Not Do

Repository Autopilot does not:

- Commit directly to `main`.
- Edit core guides, README content, Hermes Agent docs, image-generation docs,
  scripts, tests, or workflow policy files.
- Run Codex inside GitHub Actions.
- Call paid LLMs or model-provider APIs.
- Publish releases.
- Merge AI-written guide content.
- Replace branch, pull request, checks, review, and controlled merge for
  curated documentation.

## Which Files The Safe Automerge Workflow May Touch

`automerge-safe-generated.yml` only evaluates PRs from branches starting with
`autopilot/`, and only squash-merges when every changed file matches the
allowlist below. See
[safe-automerge-policy.md](safe-automerge-policy.md) for the full decision
table and a worked rejection example.

| Path pattern | Automerge eligible? | Notes |
| --- | --- | --- |
| `data/research/candidates.json` | Yes | Exact path match only. |
| `docs/research/inbox/*.md` | Yes | Any Markdown file directly in this folder. |
| `docs/research/curated/curator-prompt-*.md` | Yes | Must start with `curator-prompt-` and end in `.md`. |
| `README.md`, `AGENTS.md`, `CHANGELOG.md` | No | Human review required. |
| `scripts/*`, `tests/*` | No | Human review required. |
| `.github/workflows/*` | No | Human review required. |
| `docs/skills/*`, `docs/hermes/*`, `docs/image-generation/*` | No | Human review required. |
| Any other guide or content doc | No | Human review required. |
| Any file outside `docs/research/` and `data/research/` | No | Human review required. |

The check is deterministic, implemented in
`scripts/check_safe_generated_diff.py`, and re-run in CI, so this table is not
just documentation -- it is enforced by a script every time.

## Why No OpenAI API Keys

This repository is meant to teach public, beginner-friendly AI-assisted repo
work. GitHub automation stays cheap and auditable by collecting metadata and
preparing local prompts only. The maintainer can then run a local agent (Codex
through ChatGPT sign-in, or Claude Code), review the diff, and open a normal
pull request.

Keeping the workflow free of model-provider secrets also reduces the risk of
accidental secret exposure, unexpected spend, and unattended AI-written
changes.

## Why GitHub Actions Does Not Run Codex

The repository separates mechanical automation from AI curation. GitHub
Actions can run deterministic scripts and tests. Codex curation remains
local/manual so the maintainer sees the prompt, reviews source status,
verifies official docs, and decides what changes belong in the guide.

This keeps the guide-writing path:

```text
scout -> curator prompt -> local Codex -> branch -> PR -> checks -> review -> merge
```

For source-inspired prompting-guide work, use the same preview-first shape:

```text
source inventory -> pattern extraction -> public-safe synthesis -> anti-slop review -> local checks -> diff review -> changelog -> release notes
```

The automation may prepare source candidates and curator prompts, but a human
must decide which source patterns become repository content. Do not let
GitHub Actions bulk-import external prompt text, publish AI-written guide
content, or convert archived downloads into docs without local review.

## Generated-File Pull Requests

The autopilot branch is intentionally narrow. It may contain candidate
metadata, inbox reports, and local curator prompts. It must not contain
finished guide content.

Generated-file PRs are useful because they give maintainers a safe queue of
candidate sources and a prompt they can copy into a local Codex session.

## Safe Automerge

Generated-file PRs can be checked by `automerge-safe-generated.yml`. That
workflow refuses branches outside `autopilot/` and refuses any changed file
outside the generated-file allowlist.

If the PR touches content docs, scripts, tests, workflows, policies, Hermes
Agent docs, image-generation docs, skills docs, or release policy files, it
must be reviewed and merged by a human through the normal process.

## Manual Run

From PowerShell:

```powershell
gh workflow run repo-autopilot.yml -f scope=hermes-agent -f dry_run=true -f max_sources=5 -f create_pr=true
gh run list --workflow repo-autopilot.yml
gh run view <RUN_ID> --log-failed
```

Then review the generated pull request before relying on the generated
prompt.

## Local Status Check Without `gh`

If GitHub CLI is not installed or you just want a quick local snapshot,
`scripts/repo_autopilot_status.py` reads the same generated files directly
from disk:

```powershell
python scripts/repo_autopilot_status.py
```

It prints the current branch, `git status --short --branch`, the latest
research inbox files, the latest curator prompt files, and a summary of
`data/research/candidates.json` (candidate count, blocked count, and the top
five scored candidates). This is read-only and safe to run at any time.

## Failure Modes

| Symptom | Likely cause | Response |
| --- | --- | --- |
| `repo-autopilot.yml` run fails on source fetch | A source in `data/research/sources.yml` is unreachable or malformed. | Inspect the run log; fix or temporarily skip the failing source. |
| Automerge refuses a generated PR | The PR touched a file outside the allowlist. | Treat it as a normal content PR; route through human review. |
| Candidates file is missing or invalid JSON | The scout has not run yet, or a manual edit broke the JSON. | Run the scout workflow again, or fix the JSON and re-validate with `python scripts/repo_autopilot_status.py`. |
| Curator prompt folder is empty | `curator-prompt-prep.yml` has not been run. | Trigger it manually, then rerun `local_autopilot.ps1 -Mode prompt`. |
| PR contains both generated files and guide edits | A local agent branch mixed autopilot output with manual edits. | Split into two PRs: one generated-only, one reviewed normally. |
