# Codex Prompt: Repository Cleanup

## Target Tool

OpenAI Codex CLI or Codex-style coding-agent goal mode.

## Purpose

Use this prompt for conservative repository cleanup that improves consistency, navigation, or validation without changing project meaning, architecture, dependencies, or workflow behavior.

## Inputs To Fill

| Input | Description | Example |
| --- | --- | --- |
| `{cleanup_goal}` | The exact cleanup objective. | `Fix Markdown navigation and obvious broken internal references` |
| `{allowed_scope}` | Files or folders that may change. | `README.md`, `docs/guides/`, `prompts/codex/` |
| `{excluded_scope}` | Files, folders, or actions that must not change. | `.github/workflows/`, dependencies, generated archives |
| `{validation}` | Required checks. | `repo_health_check`, `safe_autofix`, `unittest` |

## Full Prompt

```text
/goal
Objective:
Perform this conservative repository cleanup: {cleanup_goal}

Mandatory first steps:
1. Run git status.
2. Read AGENTS.md fully.
3. Inspect {allowed_scope} before editing.
4. Identify pre-existing modified or untracked files and preserve user work.

Included scope:
- {allowed_scope}
- Deterministic whitespace/final-newline cleanup when reported by safe_autofix.
- CHANGELOG.md if the cleanup is visible to readers.

Excluded scope:
- {excluded_scope}
- Do not delete files.
- Do not install dependencies.
- Do not edit secrets, .env files, private links, private paths, browser profiles, credentials, or private data.
- Do not modify workflow YAML unless explicitly requested.
- Do not rewrite large sections just to make them sound different.
- Do not introduce exact pricing, model, benchmark, or unsupported tool claims.

Safety boundaries:
- Cleanup must be predictable, reviewable, and tied to the stated objective.
- Prefer safe_autofix.py for whitespace cleanup.
- Do not mix broad editorial rewrites with deterministic cleanup.
- Ask or stop if a file appears obsolete but deletion was not explicitly approved.

Verification steps:
- python scripts/safe_autofix.py --check
- python scripts/repo_health_check.py
- python -m unittest discover -s tests
- git diff --stat
- git diff

Success criteria:
- Repository meaning and behavior are preserved.
- The diff is small enough to review.
- No unrelated files change.
- Public-safety rules still hold.
- {validation} pass or failures are honestly reported.

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
Clean up {allowed_scope} for {cleanup_goal}. Run git status, read AGENTS.md, preserve existing user work, do not delete files/add dependencies/change workflows/touch secrets, prefer safe_autofix for whitespace, run required checks, inspect git diff, and report files, commands, checks, and risks.
```

## Included Scope

- Files and folders named in `{allowed_scope}`.
- Obvious broken navigation or deterministic formatting issues.
- CHANGELOG.md if readers will notice the cleanup.

## Excluded Scope

- File deletion, broad restructuring, dependency changes, workflow YAML, generated binary artifacts, and unrelated prose rewrites.
- Secrets, credentials, private data, private paths, and private links.

## Safety Boundaries

- Treat untracked files as user work unless explicitly told otherwise.
- Do not use `git clean`, `git reset`, stash, rebase, or force-push.
- Do not claim cleanup is safe until the diff is inspected.

## Verification Steps

```powershell
python scripts/safe_autofix.py --check
python scripts/repo_health_check.py
python -m unittest discover -s tests
git diff --stat
git diff
```

If safe autofix reports formatting issues and the task allows it:

```powershell
python scripts/safe_autofix.py --write
python scripts/safe_autofix.py --check
```

## Success Criteria

- Cleanup is scoped, reversible where practical, and preserves user data.
- No files are deleted or moved unless the task explicitly allows it.
- Manifests, logs, or reports exist when organization work affects many files.
- Checks pass or failures are reported with the changed-file list.

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
| Cleanup becomes a rewrite | Stop and split into a documentation task. |
| Unexpected files changed | Report them and avoid staging/committing until reviewed. |
| A file seems safe to delete | Ask for explicit approval instead of deleting it. |
| Safe autofix changes many files | Review the full diff before claiming success. |
| Tests fail outside cleanup scope | Report the pre-existing or unrelated failure clearly. |
