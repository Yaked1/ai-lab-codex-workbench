# GitHub Copilot Agent Task Template

## Target Tool

GitHub Copilot coding agent (assigned to a GitHub issue, producing a draft
pull request) or Copilot Chat/agent mode inside VS Code. This template also
works as the basis for a `.github/copilot-instructions.md`-style repository
convention: the same scope, boundary, and checklist language can be copied
into that file so Copilot picks it up automatically for every session in
this repository.

## Purpose

Use this template for a small issue assignment that should produce a
reviewable branch or pull request, or for a bounded Copilot Chat agent-mode
session in the editor. It keeps the task small enough that a human can
review the resulting diff without reading the full agent transcript.

## Inputs To Fill

| Input | Description | Example |
| --- | --- | --- |
| `{issue_title}` | Short, specific issue title. | `Expand public repo safety checklist` |
| `{files_expected}` | Files the change should touch. | `docs/workflows/public-repo-safety.md` |
| `{acceptance_criteria}` | Concrete, checkable criteria. | `Includes secret scan step, working links, and CI log reference` |
| `{checks}` | GitHub Actions and/or local commands to require. | `GitHub Actions and local unittest/repo-health checks` |
| `{reviewer}` | Who reviews and merges the PR. | `Repository maintainer, squash merge only` |

## Full Prompt / Issue Body

```text
Target tool:
GitHub Copilot coding agent (or Copilot Chat agent mode in VS Code)

Issue goal:
{issue_title}

Description:
{one paragraph describing the problem and desired outcome}

Expected files:
- {files_expected}

Scope:
- Work only inside this repository; do not reference or pull in content
  from other repositories.
- Keep the branch focused on this single issue.
- Prefer documentation, tests, or small script changes over broad
  refactors.
- Do not edit .env, .env.*, credentials, private links, browser profiles,
  or any file outside {files_expected}.
- Do not modify GitHub Actions workflow YAML unless this issue explicitly
  asks for a workflow change.
- Do not add dependencies without maintainer approval in the issue thread.
- Do not state exact pricing, model, plan, or platform claims for any AI
  tool unless verified in official docs; use conservative wording and flag
  anything uncertain.

Acceptance criteria:
{acceptance_criteria}
- The diff solves the stated issue goal completely, not partially.
- No unrelated files are changed.
- Public safety rules from AGENTS.md still hold (no secrets, no private
  links, no unsafe automation guidance).
- GitHub Actions checks in {checks} pass.
- The PR description lists changed files, checks run, and known
  limitations.
- A human reviewer ({reviewer}) can understand and approve the PR without
  reading the full agent conversation.

Required checks:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests
- git diff --check

PR review notes:
Before merge, {reviewer} must inspect the diff line by line, read the
GitHub Actions logs, confirm no private data or secrets appear anywhere in
the diff or commit history, and squash merge only after that review.
```

## Short Version

```text
Create a small PR for {issue_title}. Touch only {files_expected}, meet
{acceptance_criteria}, avoid secrets/dependencies/workflow changes, keep AI
tool claims conservative, require {checks} to pass, and include a PR
summary with changed files, checks run, limitations, and verification gaps.
```

## Included Scope

- Files, issue body content, and pull request description explicitly
  selected for the Copilot task (named in `{files_expected}`).
- Local and GitHub Actions checks relevant to the changed files.
- Documentation or tests needed to keep the resulting PR reviewable and
  self-contained.
- Optionally, the same scope/boundary language copied into
  `.github/copilot-instructions.md` so it applies automatically to future
  Copilot sessions in this repository.

## Excluded Scope

- Secrets, `.env` / `.env.*` files, credentials, browser profiles, private
  links, and private machine paths.
- Dependency installation, GitHub Actions workflow YAML edits, generated
  archives, release publishing, and destructive commands, unless the issue
  explicitly approves one of these.
- Exact current product claims (pricing, plan tiers, model availability)
  for Copilot or any other AI tool, unless verified in official docs and
  dated in the PR description.
- Merging without human review, regardless of how confident the agent's
  self-report is.

## Success Criteria

- The PR is focused: one issue, one branch, a diff a reviewer can read in
  one pass.
- GitHub Actions checks in `{checks}` pass, or failures are explained in
  the PR description with the actual log output.
- No private data, secrets, or credentials appear anywhere in the diff or
  commit history.
- The human reviewer named in `{reviewer}` can approve or request changes
  from the diff and PR description alone, without needing the agent
  transcript.

## Safety Boundaries

- No secrets or credentials in code, comments, commit messages, or the PR
  description.
- No private links or private account-specific data.
- No files outside `{files_expected}` without a follow-up issue comment
  explaining and requesting approval for the expanded scope.
- No dependency additions without explicit maintainer approval in the issue
  thread.
- No exact pricing/model/platform claims unless verified and dated.
- No merge without human review; Copilot's coding agent produces a draft
  PR, it does not have merge authority in this workflow.

## Verification

Ask the agent, and independently confirm as reviewer, that these pass:

```powershell
git status
git diff --check
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

Also open the PR's "Checks" tab and read the GitHub Actions logs directly;
do not rely on the agent's summary of whether Actions passed.

## Final Report Format

```markdown
## Summary
## Files changed
## Checks run
## GitHub Actions status
## Claims needing manual verification
## Remaining risks
```

## Failure Cases

| Failure | What to do |
| --- | --- |
| The agent opens a PR broader than `{files_expected}` | Request changes, ask for the extra files to be reverted or split into a separate issue. |
| GitHub Actions checks fail | Open the Actions log, identify the specific failing step, and either ask the agent to fix the smallest related cause or fix it manually. |
| The PR includes private data or a secret-looking string | Do not merge; request removal, and rotate any credential that may have been exposed. |
| Tool availability or a feature claim differs by Copilot plan or is unverifiable from the issue thread alone | Mark it for official-doc verification in the PR description rather than accepting it as fact. |
| The agent's PR description claims checks passed but no Actions run is visible | Treat as unverified; require an actual passing check run before approving. |
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **agent prompt template** surface. During broad
maintenance, reviewers should treat `prompts/github-copilot/agent-task.md` as a contract-bearing artifact
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
