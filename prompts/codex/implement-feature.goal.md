# Codex Prompt: Implement Feature

## Target Tool

OpenAI Codex.

## Purpose

Use this prompt when adding a small feature to a lightweight documentation, script, test, or GitHub workflow teaching repository.

## Inputs To Fill

| Input | Example |
| --- | --- |
| Feature | "Add a checklist to the merge report template" |
| User-facing behavior | "Maintainers see a rollback section" |
| Files likely touched | `docs/templates/merge-report.md` |
| Out of scope | "No workflow YAML changes" |
| Checks | Repo health, safe autofix, unit tests |

## Full Prompt

```text
/goal
Objective:
Implement this small feature:
[FEATURE DESCRIPTION]

User context:
This project is a low-setup, cross-platform learning repository. Prefer lightweight Markdown docs, PowerShell commands, Python standard-library scripts, and GitHub Actions already present in the repo. Avoid Docker, WSL, heavy local models, and large dependencies unless explicitly approved.

Files to inspect first:
- AGENTS.md
- README.md
- [RELEVANT FILES]

Included scope:
- [FILES OR MODULES ALLOWED]

Excluded scope:
- Do not edit secrets, credentials, .env files, private links, or private data.
- Do not delete files.
- Do not install dependencies without approval.
- Do not modify system settings.
- Do not modify workflow YAML unless explicitly requested.

Success criteria:
- Feature is implemented in the smallest reasonable way.
- README or docs are updated if user-facing behavior changes.
- Tests/checks are added or updated when practical.
- Local checks pass:
  - python scripts/repo_health_check.py
  - python scripts/safe_autofix.py --check
  - python -m unittest discover -s tests
- No unrelated files changed.

Workflow:
1. Run git status.
2. Read AGENTS.md.
3. Inspect relevant files.
4. Make a brief plan.
5. Implement the smallest useful change.
6. Update docs and changelog if needed.
7. Run checks.
8. Fix related failures.
9. Report results and remaining risks.
```

## Short Version

```text
Implement [FEATURE] with the smallest safe diff. Read AGENTS.md, inspect relevant files, avoid dependencies and workflow changes unless requested, update docs/tests when useful, run the three local checks, and report files, commands, checks, and risks.
```

## Success Criteria

- Feature works or documentation clearly reflects the new behavior.
- Tests or docs are updated when appropriate.
- No unrelated files changed.
- Local checks pass or failures are explained.

## Safety Boundaries

- No secrets or private data.
- No deletion.
- No unapproved dependencies.
- No system settings.
- No broad refactors.
- No exact external product claims unless verified.

## Verification

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

## Final Report Format

```markdown
## Summary
## Files changed
## Commands run
## Tests/checks
## Remaining risks
```

## Failure Cases

| Failure | What to do |
| --- | --- |
| Feature is too broad | Split into smaller goals. |
| Dependency seems necessary | Ask before adding it. |
| Tests are impractical | Explain why and run available checks. |
| Existing code is unclear | Inspect more context and keep the change conservative. |
