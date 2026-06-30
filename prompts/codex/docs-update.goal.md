# Codex Prompt: Documentation Update

## Target Tool

OpenAI Codex CLI or Codex-style coding-agent goal mode.

## Purpose

Use this prompt when a README section, documentation page, workflow guide, tool guide, prompt guide, or public-safety checklist needs a focused public-ready improvement.

## Inputs To Fill

| Input | Description | Example |
| --- | --- | --- |
| `{topic}` | The documentation topic to improve. | `Codex goal workflow` |
| `{audience}` | The reader and prior knowledge. | `Beginner contributors with basic Git knowledge` |
| `{files_to_inspect}` | Files the agent must read before editing. | `README.md`, `docs/codex/00-start-here.md` |
| `{allowed_scope}` | Files or sections that may change. | `README.md and CHANGELOG.md only` |
| `{excluded_scope}` | Files or actions that must not change. | `.github/workflows/`, dependencies, secrets |
| `{claims_to_verify}` | Fast-changing product claims to avoid or mark for manual verification. | `pricing, model availability, connector behavior` |

## Full Prompt

```text
/goal
Objective:
Improve the documentation for {topic} so it is clearer, more public-safe, easier to navigate, and useful to {audience}.

Mandatory first steps:
1. Run git status.
2. Read AGENTS.md fully.
3. Inspect README.md and {files_to_inspect} before editing.
4. Identify any pre-existing working-tree changes and treat them as user work.

Included scope:
- {allowed_scope}
- Update CHANGELOG.md if the change is user-visible.

Excluded scope:
- {excluded_scope}
- Do not edit secrets, .env files, credentials, private links, private paths, browser profiles, or private data.
- Do not add dependencies.
- Do not modify workflow YAML unless explicitly requested.
- Do not invent exact pricing, model availability, benchmark numbers, release timing, or unsupported product behavior.
- Do not publish copied prompt dumps or leaked prompt text.

Safety boundaries:
- Keep the diff reviewable and focused.
- Preserve existing user work.
- Use conservative language for fast-changing tools and mark {claims_to_verify} for official-doc verification.
- Prefer Windows PowerShell examples where commands are needed.

Verification steps:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests
- git diff --stat
- git diff

Success criteria:
- The target docs have a clearer purpose, audience, navigation path, examples/checklists where useful, and explicit failure modes or safety notes.
- Internal links are correct.
- Public-safety rules are preserved.
- The changelog records the visible change if appropriate.
- Required checks pass, or failures are honestly reported with relevant output.

Final report format:
## Summary
## Git state
## Files changed
## Commands run
## Verification results
## Claims needing manual verification
## Remaining risks
```

## Short Version

```text
Improve {topic} docs for {audience}. Run git status, read AGENTS.md, inspect README and target files, edit only {allowed_scope}, avoid secrets/dependencies/workflows/unverified product claims, update changelog if user-visible, run the three local checks, inspect git diff, and report files, commands, check results, manual-verification claims, and risks.
```

## Included Scope

- The documentation files named in `{allowed_scope}`.
- Supporting navigation links when needed.
- CHANGELOG.md for user-visible documentation changes.

## Excluded Scope

- Secrets, credentials, private data, `.env` files, browser profiles, and private links.
- Workflow YAML, dependencies, generated binaries, archives, screenshots, or broad refactors unless explicitly requested.
- Unsupported or exact claims about fast-changing products.

## Safety Boundaries

- Treat pre-existing edits and untracked files as user work.
- Do not delete or move files without explicit approval.
- Do not quote leaked prompts or copied prompt dumps.
- Do not claim tests passed unless run in the current session.

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
## Claims needing manual verification
## Remaining risks
```

## Failure Cases

| Failure | What to do |
| --- | --- |
| Branch has unsafe divergence or unexpected changes | Stop and report the safe commands a human should run. |
| Official tool docs are needed but not checked | Mark the claim for manual verification instead of guessing. |
| Scope grows beyond the requested files | Stop and recommend a separate task. |
| A local check fails | Fix related failures; report unrelated failures clearly. |
| The prompt requests exact product details | Reword conservatively unless freshly verified and dated. |
