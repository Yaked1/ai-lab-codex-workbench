# Claude Code Goal: Review Documentation

## Target Tool

Claude Code.

## Purpose

Use this prompt for read-only documentation review. Claude Code should identify clarity, safety, consistency, and verification issues before a maintainer edits or merges docs.

## Inputs To Fill

| Input | Example |
| --- | --- |
| Docs to review | `README.md`, `docs/tools/*.md` |
| Audience | "Beginner Windows users" |
| Main risks | "Unverified AI tool claims" |
| Allowed edits | "None" |

## Full Prompt

```text
Target tool:
Claude Code

Objective:
Review this repository's documentation for beginner clarity, public repository safety, and consistency with AGENTS.md.

Files to read first:
- AGENTS.md
- README.md
- CONTRIBUTING.md
- SECURITY.md
- [DOCS TO REVIEW]

Boundaries:
- Do not edit files unless explicitly asked after the review.
- Do not add dependencies.
- Do not inspect files outside this repository.
- Do not include secrets, private links, personal account details, or private machine paths.
- Do not make exact pricing, model, or platform claims.

Review tasks:
1. Identify unclear beginner instructions.
2. Identify claims about external tools that should be verified against official docs.
3. Identify missing safety warnings.
4. Identify workflow steps that could encourage unsafe automation.
5. Identify outdated, vague, or unsupported guidance.
6. Recommend the smallest useful documentation changes.

Final response:
- Verdict
- Findings ordered by severity
- Suggested edits
- Files reviewed
- Checks not run
- Tool claims that should be manually verified before public release
```

## Short Version

```text
Review [DOCS] for beginner clarity, public safety, AGENTS.md consistency, and unverified tool claims. Do not edit. Return severity-ordered findings, suggested edits, files reviewed, checks not run, and claims to verify.
```

## Success Criteria

- Findings are specific and actionable.
- Review is read-only.
- Public safety issues are prioritized.
- External tool claims needing verification are identified.

## Safety Boundaries

- No edits.
- No dependency installation.
- No private folders.
- No secret values in output.
- No unsupported product claims.

## Verification

This is usually a review-only task. If command execution is allowed, optional checks are:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

## Final Report Format

```markdown
## Verdict
## Findings
## Suggested edits
## Files reviewed
## Checks not run
## Claims needing manual verification
```

## Failure Cases

| Failure | What to do |
| --- | --- |
| Review starts editing | Stop and return findings only. |
| Claim needs current docs | Mark it for manual verification. |
| File scope is unclear | Ask which docs to review. |
| Secret appears in context | Do not quote it; flag the issue safely. |
