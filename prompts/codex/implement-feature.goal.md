# Codex Prompt: Implement Feature

## Target Tool

OpenAI Codex CLI or Codex-style coding-agent goal mode.

## Purpose

Use this prompt when adding one small feature to a lightweight documentation, script, test, prompt-template, or workflow-teaching repository while keeping the change reviewable.

## Inputs To Fill

| Input | Description | Example |
| --- | --- | --- |
| `{feature}` | The feature to add. | `Add a docs freshness checklist` |
| `{user_value}` | What users can do after the feature exists. | `Maintainers can audit stale product claims` |
| `{files_to_inspect}` | Files the agent should read first. | `README.md`, `scripts/repo_health_check.py` |
| `{allowed_scope}` | Files or modules that may change. | `docs/`, `scripts/repo_health_check.py`, related tests |
| `{excluded_scope}` | Explicitly forbidden files/actions. | `No workflow YAML or dependencies` |
| `{checks}` | Required validation. | `repo health, safe autofix, unittest` |

## Full Prompt

```text
/goal
Objective:
Implement this small feature: {feature}

User value:
{user_value}

Mandatory first steps:
1. Run git status.
2. Read AGENTS.md fully.
3. Inspect {files_to_inspect} before editing.
4. Identify pre-existing modified or untracked files and preserve user work.

Included scope:
- {allowed_scope}
- Tests or docs directly needed to prove the feature.
- CHANGELOG.md if the feature is user-visible.

Excluded scope:
- {excluded_scope}
- Do not edit secrets, credentials, .env files, private links, private paths, browser profiles, or private data.
- Do not delete files.
- Do not install dependencies without explicit approval.
- Do not modify workflow YAML unless explicitly requested.
- Do not modify system settings.
- Do not add exact external product claims unless they are verified and dated.

Safety boundaries:
- Implement the smallest useful version.
- Prefer Python standard library and existing project patterns.
- Do not refactor unrelated code.
- Keep public docs conservative about fast-changing tools.
- Stop if branch divergence or existing changes make safe editing ambiguous.

Verification steps:
- Run a focused test or script check if one applies.
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests
- git diff --stat
- git diff

Success criteria:
- {feature} works or is documented clearly.
- {user_value} is satisfied.
- Related tests/docs are updated when practical.
- No unrelated files changed.
- {checks} pass or failures are honestly reported.

Final report format:
## Summary
## Git state
## Files changed
## Commands run
## Verification results
## Remaining risks
```

## Short Version

```text
Implement {feature} with the smallest safe diff. Run git status, read AGENTS.md, inspect {files_to_inspect}, preserve existing work, edit only {allowed_scope}, avoid {excluded_scope}, update docs/tests/changelog when useful, run required checks, inspect git diff, and report files, commands, checks, and risks.
```

## Included Scope

- Files named in `{allowed_scope}`.
- Focused tests, docs, and changelog entries needed to make the feature reviewable.

## Excluded Scope

- Secrets, private data, dependencies, workflow YAML, system settings, broad refactors, and unrelated cleanup.
- Exact external product claims without official-doc verification.

## Safety Boundaries

- Do not use destructive git operations.
- Do not overwrite untracked or modified user work.
- Do not expand the feature into a platform redesign.
- Do not claim behavior is verified unless a command or manual inspection proves it.

## Verification Steps

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
git diff --stat
git diff
```

## Final Report Format

```markdown
## Summary
## Git state
## Files changed
## Commands run
## Verification results
## Remaining risks
```

## Failure Cases

| Failure | What to do |
| --- | --- |
| Feature is too broad | Split it into smaller goals. |
| A dependency seems necessary | Stop and ask for approval. |
| Existing tests do not cover the area | Add a focused test if practical, otherwise explain the gap. |
| Branch has unrelated changes | Preserve them and report the risk. |
| Implementation requires workflow changes | Stop unless workflow edits were explicitly requested. |
