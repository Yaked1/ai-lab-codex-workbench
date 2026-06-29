# Codex Prompt: Review Pull Request

## Target Tool

OpenAI Codex.

## Purpose

Use this prompt when Codex should act as a reviewer, not an implementer. The default mode is read-only.

## Inputs To Fill

| Input | Example |
| --- | --- |
| Base branch | `main` |
| PR task | "Expand tool docs" |
| Areas of concern | "External claims, secret safety, tests" |
| Allowed edits | "None unless explicitly requested" |

## Full Prompt

```text
/goal
Objective:
Review the current branch or PR diff for correctness, safety, documentation quality, and maintainability.

Instructions:
- Read AGENTS.md.
- Run git status.
- Inspect the diff against [BASE BRANCH].
- Do not modify files unless explicitly asked after the review.
- Prioritize findings by severity.
- Include file references where possible.

Review checklist:
- Does the change solve the stated task?
- Are there unrelated edits?
- Are secrets, private links, or private files included?
- Are tests/checks adequate?
- Is the solution too complex?
- Is documentation updated when needed?
- Are external AI tool claims conservative and marked for official-doc verification?
- Do local checks and CI results support the final claim?

Output:
1. Verdict: approve/request changes/comment only
2. Findings ordered by severity
3. Summary
4. Risks
5. Required fixes
6. Optional improvements
7. Commands inspected or run
8. Checks not run
```

## Short Version

```text
Review this branch against [BASE]. Read AGENTS.md, inspect git status and diff, do not edit, lead with severity-ordered findings, and report verdict, risks, required fixes, optional improvements, and commands inspected.
```

## Success Criteria

- Review is read-only.
- Findings are specific and actionable.
- Safety issues are prioritized.
- Missing checks are reported.
- Verdict is clear.

## Safety Boundaries

- Do not edit files.
- Do not run destructive commands.
- Do not inspect private folders.
- Do not approve a diff that includes secrets or private data.
- Do not rely only on the PR summary.

## Verification

Useful commands:

```powershell
git status
git diff --stat main
git diff main
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
| Base branch is unclear | Ask for the base branch or inspect local branch tracking. |
| Diff is too large | Recommend splitting the PR. |
| Secrets are present | Request changes and do not quote the secret value. |
| Checks were not run | Mark as a review gap. |
