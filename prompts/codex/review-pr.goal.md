# Codex Prompt: Review Pull Request

## Target Tool

OpenAI Codex CLI or Codex-style coding-agent goal mode used as a reviewer.

## Purpose

Use this prompt when Codex should review a current branch, pull request, or proposed diff. The default mode is read-only: the agent should inspect and report, not implement fixes. This is the reviewer's-hat prompt, distinct from `fix-bug.goal.md` (which implements a fix) and `repository-cleanup.goal.md` (which performs conservative tidying). If review findings turn into an approved fix task, hand the results to a separate implementation prompt instead of blending review and edit in the same run.

## Inputs To Fill

| Input | Description | Example |
| --- | --- | --- |
| `{base_branch}` | Branch or ref to compare against. | `origin/main` |
| `{pr_goal}` | What the PR is supposed to accomplish. | `Improve prompt templates` |
| `{areas_of_concern}` | Review priorities. | `public safety, unsupported claims, tests` |
| `{allowed_edits}` | Whether edits are allowed. | `None; review only` |
| `{checks_available}` | Checks or CI results to inspect/run. | `repo health, safe autofix, unittest` |
| `{pr_source}` | Where the branch/PR came from. | `Fork contributor, first-time submitter` |

## Full Prompt

```text
/goal
Objective:
Review the current branch or PR diff against {base_branch} for correctness, public safety, documentation quality, maintainability, and task fit.

PR goal:
{pr_goal}

Areas of concern:
{areas_of_concern}

Allowed edits:
{allowed_edits}

PR source:
{pr_source}

Mandatory first steps:
1. Run git status.
2. Read AGENTS.md fully.
3. Inspect the diff with git diff --stat {base_branch} and git diff {base_branch}.
4. Treat the review as read-only unless {allowed_edits} explicitly permits fixes.
5. Check whether the diff conflicts with {base_branch} (git merge-tree or a
   local merge dry run) before reviewing content, so a stale branch is
   flagged early instead of discovered after a full read.
6. Note whether {pr_source} implies restricted CI credentials (fork PRs
   commonly cannot access repository secrets); if so, expect certain checks
   to be skipped rather than failed, and say so in the report.

Review checklist:
- Does the diff solve {pr_goal}? Are there unrelated edits?
- Are secrets, private links, private paths, token-like strings, or private files included?
- Are generated files, archives, binaries, or dependency changes present unexpectedly?
- Does the diff touch anything under .github/workflows/? If so, flag it as
  requiring explicit maintainer approval regardless of intent.
- Does the diff add a new dependency or lock-file change? If so, flag it
  even if the PR goal seems to justify it; that decision belongs to a human.
- Are external AI tool claims conservative and marked for official-doc verification?
- Are prompt templates scoped, safe, and operational? Are docs navigable
  for beginners and auditable by maintainers?
- Were {checks_available} run, and do results support the claims?
- Is CHANGELOG.md updated when the change is user-visible, including for a
  public API, CLI flag, or documented script interface change?
- Does the diff include or modify tests for the behavior it changes? A
  behavior change with zero test coverage is a finding, not a footnote.
- Are any changed files generated output (built HTML, packaged release
  archives, compiled artifacts) rather than source? Hand-edited generated
  files are themselves a finding.

Safety boundaries:
- Do not edit files unless explicitly allowed.
- Do not run destructive commands.
- Do not quote secrets if found; identify the file and type of issue only.
- Do not approve based only on the PR summary.
- Do not invent missing CI or test results.
- Do not approve a diff that touches .github/workflows/ without explicitly
  flagging it for maintainer sign-off, even if {allowed_edits} permits fixes.
- Do not approve a new dependency addition without flagging it for explicit
  maintainer approval, even if it looks small or well-justified.

Useful verification commands if command execution is allowed:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests
- git diff --check {base_branch}
- git merge-tree $(git merge-base HEAD {base_branch}) HEAD {base_branch}

Success criteria:
- Findings are specific, severity-ordered, and actionable.
- The verdict is clear: approve, request changes, or comment only.
- Missing checks and unverified claims are reported.
- Public-safety concerns are prioritized.
- Merge conflicts, missing tests, undocumented API changes, and
  workflow/dependency changes are called out explicitly when present.

Final report format:
## Verdict
approve | request changes | comment only

## Findings
Severity-ordered findings with file references where possible.

## Summary

## Risks

## Required fixes

## Optional improvements

## Commands inspected or run

## Checks not run
```

### Worked Example

```text
/goal
Objective:
Review the current branch or PR diff against origin/main for correctness,
public safety, documentation quality, maintainability, and task fit.

PR goal:
Add a --json output flag to scripts/repo_health_check.py.

Areas of concern:
public safety, whether the default text output changed, test coverage for
the new flag, whether CHANGELOG.md was updated.

Allowed edits:
None; review only.

PR source:
First-time external contributor via a fork.

Mandatory first steps:
1-4. Standard (git status, read AGENTS.md, inspect git diff --stat and git
     diff against origin/main, treat this as read-only review).
5. Run a merge dry run against origin/main to check for conflicts before
   reading further.
6. Because this is a fork PR, expect any workflow step requiring repository
   secrets to have been skipped in CI, not failed; note this instead of
   treating a skipped check as a red flag.

Review checklist:
- Does the diff add --json without changing default text output?
- Are there unrelated edits to other scripts?
- Any secrets, tokens, or private paths introduced?
- Any new dependency added to parse or emit JSON (there should not be; the
  standard library json module is sufficient)?
- Does the diff touch .github/workflows/? (It should not for this task.)
- Is there a test covering both --json and default output?
- Is CHANGELOG.md updated for this user-visible CLI change?
- Does the diff change the documented CLI interface without a changelog
  entry?

Safety boundaries:
- Do not edit scripts/repo_health_check.py or its test.
- Do not run destructive commands.
- Do not quote any secret-looking string found; describe the finding only.
- Do not approve solely because the PR description says "tests pass."

Useful verification commands:
- python scripts/repo_health_check.py / --json
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests
- git diff --check origin/main

Success criteria:
- Verdict reflects whether default output is unchanged and --json is valid
  JSON with documented keys.
- Missing test coverage or a missing CHANGELOG entry is called out as a
  required fix, not an optional one.
- Fork-restricted CI gaps are explained rather than treated as failures.

Final report format: same as above.
```

## Short Version

```text
Review this branch against {base_branch} for {pr_goal}. Run git status, read AGENTS.md, inspect diff stat and diff, check for merge conflicts, do not edit unless allowed, prioritize {areas_of_concern}, flag workflow/dependency changes and missing tests/changelog entries explicitly, report severity-ordered findings, verdict, risks, required fixes, optional improvements, commands run, and checks not run.
```

## Included Scope

- Read-only inspection of the current branch or PR diff.
- Optional local checks when command execution is allowed.
- File edits only if `{allowed_edits}` explicitly permits them.

## Excluded Scope

- Implementing fixes by default.
- Any approval of changes under `.github/workflows/` without explicit
  maintainer sign-off flagged in the findings.
- Any approval of a new dependency or lock-file change without explicit
  maintainer sign-off flagged in the findings.
- Destructive git operations, dependency installs, workflow edits, private
  folder inspection, and quoting secret values.

## Safety Boundaries

- Review the actual diff, not only summaries.
- Treat secrets and private data as blockers.
- Treat unsupported exact product claims as issues needing verification.
- Do not claim checks passed unless run or observed in current CI output.
- Treat any diff under `.github/workflows/` as requiring explicit
  maintainer approval, regardless of how small it looks.
- Treat any new dependency as requiring explicit maintainer approval,
  regardless of how justified it looks in the PR description.
- Do not conflate a skipped check (common on fork PRs with restricted
  secrets) with a failed check; report which one actually happened.

## Verification Steps

```powershell
git status
git diff --stat {base_branch}
git diff {base_branch}
git diff --check {base_branch}
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

Only run checks if review scope allows command execution. Task-specific
check: run `git merge-tree $(git merge-base HEAD {base_branch}) HEAD
{base_branch}` (or attempt a local merge dry run) to surface conflicts with
`{base_branch}` before finalizing the verdict, since a clean-looking diff
can still fail to merge.

## Success Criteria

- Findings are ordered by severity and grounded in specific files or lines.
- Behavioral regressions, safety risks, and missing tests are prioritized.
- The review is clear when no issues are found.
- Open questions, checks run, checks not run, and residual risks are reported.
- Workflow changes, new dependencies, missing tests, undocumented public-API
  changes, and merge conflicts are each named explicitly when present, not
  buried inside a general comment.

## Final Report Format

```markdown
## Verdict
approve | request changes | comment only

## Findings

## Summary

## Risks

## Required fixes

## Optional improvements

## Commands inspected or run

## Checks not run
```

## Failure Cases

| Failure | What to do |
| --- | --- |
| Base branch is unclear | Ask for the base branch or inspect tracking information. |
| Diff is too large | Recommend splitting the PR. |
| Secrets are present | Request changes and do not quote the value. |
| Checks were not run | Mark as a review gap. |
| Product claims are exact but unverified | Request conservative wording or official-doc evidence. |
| PR touches generated files (built output, packaged archives) instead of source | Request changes; generated files should come from the generator, not hand edits. |
| PR has no tests for the behavior it changes | Mark as a required fix unless truly untestable, and say why if so. |
| PR changes a public API, CLI flag, or documented interface without a changelog entry | Request a CHANGELOG.md entry before approval. |
| PR is from a fork with restricted CI secrets | Note which checks could not run due to permissions; do not treat a skipped check as failed. |
| PR conflicts with {base_branch} | Flag the conflict and recommend a rebase before further review; do not review a diff that cannot cleanly apply. |

## Anti-Patterns

- Approving based on the PR description or commit message instead of the
  actual diff. The description says what the author intended; the diff
  says what happened.
- Silently fixing a small issue found during review instead of reporting
  it. Review mode stays read-only unless `{allowed_edits}` says otherwise.
- Treating a skipped CI check (common on forked PRs without secret access)
  as equivalent to a passing check. Say explicitly that it did not run.
- Burying a workflow-file change or a new dependency inside "optional
  improvements" instead of calling it out as a required, separate decision.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **agent prompt template** surface. During broad
maintenance, reviewers should treat `prompts/codex/review-pr.goal.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `review pr.goal` state what decision, workflow, or reusable behavior it supports?
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
