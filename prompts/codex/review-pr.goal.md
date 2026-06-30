# Codex Prompt: Review Pull Request

## Target Tool

OpenAI Codex CLI or Codex-style coding-agent goal mode used as a reviewer.

## Purpose

Use this prompt when Codex should review a current branch, pull request, or proposed diff. The default mode is read-only: the agent should inspect and report, not implement fixes.

## Inputs To Fill

| Input | Description | Example |
| --- | --- | --- |
| `{base_branch}` | Branch or ref to compare against. | `origin/main` |
| `{pr_goal}` | What the PR is supposed to accomplish. | `Improve prompt templates` |
| `{areas_of_concern}` | Review priorities. | `public safety, unsupported claims, tests` |
| `{allowed_edits}` | Whether edits are allowed. | `None; review only` |
| `{checks_available}` | Checks or CI results to inspect/run. | `repo health, safe autofix, unittest` |

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

Mandatory first steps:
1. Run git status.
2. Read AGENTS.md fully.
3. Inspect the diff with git diff --stat {base_branch} and git diff {base_branch}.
4. Treat the review as read-only unless {allowed_edits} explicitly permits fixes.

Review checklist:
- Does the diff solve {pr_goal}?
- Are there unrelated edits?
- Are secrets, private links, private paths, token-like strings, or private files included?
- Are generated files, archives, binaries, or dependency changes present unexpectedly?
- Are external AI tool claims conservative and marked for official-doc verification?
- Are prompt templates scoped, safe, and operational?
- Are docs navigable for beginners and auditable by maintainers?
- Were {checks_available} run, and do results support the claims?
- Is CHANGELOG.md updated when the change is user-visible?

Safety boundaries:
- Do not edit files unless explicitly allowed.
- Do not run destructive commands.
- Do not quote secrets if found; identify the file and type of issue only.
- Do not approve based only on the PR summary.
- Do not invent missing CI or test results.

Useful verification commands if command execution is allowed:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests

Success criteria:
- Findings are specific, severity-ordered, and actionable.
- The verdict is clear: approve, request changes, or comment only.
- Missing checks and unverified claims are reported.
- Public-safety concerns are prioritized.

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

## Short Version

```text
Review this branch against {base_branch} for {pr_goal}. Run git status, read AGENTS.md, inspect diff stat and diff, do not edit unless allowed, prioritize {areas_of_concern}, report severity-ordered findings, verdict, risks, required fixes, optional improvements, commands run, and checks not run.
```

## Included Scope

- Read-only inspection of the current branch or PR diff.
- Optional local checks when command execution is allowed.
- File edits only if `{allowed_edits}` explicitly permits them.

## Excluded Scope

- Implementing fixes by default.
- Destructive git operations, dependency installs, workflow edits, private folder inspection, and quoting secret values.

## Safety Boundaries

- Review the actual diff, not only summaries.
- Treat secrets and private data as blockers.
- Treat unsupported exact product claims as issues needing verification.
- Do not claim checks passed unless run or observed in current CI output.

## Verification Steps

```powershell
git status
git diff --stat {base_branch}
git diff {base_branch}
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

Only run checks if review scope allows command execution.

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
