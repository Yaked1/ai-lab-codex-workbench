# Repository Autopilot

Repository Autopilot is a no-API-key maintenance layer for routine generated research updates. It combines the existing cheap research scout, scoring, report generation, local curator prompt prep, deterministic autofix, health checks, and tests into one GitHub Actions workflow.

It is designed for repository maintenance, not unattended guide writing.

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
- Edit core guides, README content, Hermes Agent docs, image-generation docs, scripts, tests, or workflow policy files.
- Run Codex inside GitHub Actions.
- Call paid LLMs or model-provider APIs.
- Publish releases.
- Merge AI-written guide content.
- Replace branch, pull request, checks, review, and controlled merge for curated documentation.

## Why No OpenAI API Keys

This repository is meant to teach public, beginner-friendly AI-assisted repo work. GitHub automation stays cheap and auditable by collecting metadata and preparing local prompts only. The maintainer can then run a local agent (Codex through ChatGPT sign-in, or Claude Code), review the diff, and open a normal pull request.

Keeping the workflow free of model-provider secrets also reduces the risk of accidental secret exposure, unexpected spend, and unattended AI-written changes.

## Why GitHub Actions Does Not Run Codex

The repository separates mechanical automation from AI curation. GitHub Actions can run deterministic scripts and tests. Codex curation remains local/manual so the maintainer sees the prompt, reviews source status, verifies official docs, and decides what changes belong in the guide.

This keeps the guide-writing path:

```text
scout -> curator prompt -> local Codex -> branch -> PR -> checks -> review -> merge
```

For source-inspired prompting-guide work, use the same preview-first shape:

```text
source inventory -> pattern extraction -> public-safe synthesis -> anti-slop review -> local checks -> diff review -> changelog -> release notes
```

The automation may prepare source candidates and curator prompts, but a human must decide which source patterns become repository content. Do not let GitHub Actions bulk-import external prompt text, publish AI-written guide content, or convert archived downloads into docs without local review.

## Generated-File Pull Requests

The autopilot branch is intentionally narrow. It may contain candidate metadata, inbox reports, and local curator prompts. It must not contain finished guide content.

Generated-file PRs are useful because they give maintainers a safe queue of candidate sources and a prompt they can copy into a local Codex session.

## Safe Automerge

Generated-file PRs can be checked by `automerge-safe-generated.yml`. That workflow refuses branches outside `autopilot/` and refuses any changed file outside the generated-file allowlist.

If the PR touches content docs, scripts, tests, workflows, policies, Hermes Agent docs, image-generation docs, skills docs, or release policy files, it must be reviewed and merged by a human through the normal process.

## Manual Run

From PowerShell:

```powershell
gh workflow run repo-autopilot.yml -f scope=hermes-agent -f dry_run=true -f max_sources=5 -f create_pr=true
gh run list --workflow repo-autopilot.yml
gh run view <RUN_ID> --log-failed
```

Then review the generated pull request before relying on the generated prompt.
