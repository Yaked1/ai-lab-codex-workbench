# Codex Prompt: Documentation Update

## Target Tool

OpenAI Codex.

## Purpose

Use this prompt when a documentation page, README section, workflow guide, tool guide, or public-safety checklist needs a focused improvement.

## Inputs To Fill

| Input | Example |
| --- | --- |
| Topic | "Codex goal workflow" |
| Files | `docs/codex/01-codex-goal-workflow.md` |
| Audience | "Beginner Windows users with basic Git knowledge" |
| Required sections | "Setup, examples, safety risks, verification" |
| Claims to avoid or verify | "Exact pricing, model availability, platform support" |

## Full Prompt

```text
/goal
Objective:
Improve or add documentation for:
[TOPIC]

Audience:
[AUDIENCE]

Files to inspect first:
- AGENTS.md
- README.md
- [TARGET FILES]

Included scope:
- [FILES OR SECTIONS ALLOWED]

Excluded scope:
- Do not edit code unless documentation cannot be accurate without it.
- Do not modify workflow YAML.
- Do not add dependencies.
- Do not touch secrets, .env files, private links, or private data.
- Do not invent exact pricing, model availability, release timing, or unsupported product features.

Success criteria:
- Documentation is clear for beginners and still useful to advanced users.
- Structure includes practical headings, tables, checklists, examples, and failure modes where useful.
- Windows PowerShell commands are used where commands are needed.
- Hardware limits are stated if relevant.
- Fast-changing tool claims say to verify in official documentation.
- Internal links are correct.
- Local checks pass:
  - python scripts/repo_health_check.py
  - python scripts/safe_autofix.py --check
  - python -m unittest discover -s tests

Workflow:
1. Run git status.
2. Inspect relevant files before editing.
3. Make the smallest complete documentation change.
4. Update CHANGELOG.md if the change is user-visible.
5. Run checks.
6. Fix related failures.

Final response:
- Summary
- Files changed
- Commands run
- Checks/tests run
- Claims needing manual verification
- Remaining risks
```

## Short Version

```text
Update [FILE] for [AUDIENCE]. Read AGENTS.md first, keep the diff focused, avoid unverified tool claims, run the three local checks, and report files changed, commands run, checks, manual-verification claims, and remaining risks.
```

## Success Criteria

- The target documentation is longer, clearer, and more practical.
- The change is scoped to the requested files.
- Public-safety rules are preserved.
- External claims are conservative.
- Local checks pass or failures are clearly reported.

## Safety Boundaries

- Keep work inside this repository.
- Do not expose secrets or private links.
- Do not add dependencies.
- Do not edit workflow YAML unless requested.
- Do not convert a docs task into a broad refactor.

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
## Checks/tests
## Claims needing manual verification
## Remaining risks
```

## Failure Cases

| Failure | What to do |
| --- | --- |
| Official tool docs are needed but not checked | Mark the claim for manual verification instead of guessing. |
| Scope grows beyond requested files | Stop and ask or split into a new task. |
| Local check fails | Fix the related cause or report it clearly. |
| Prompt asks for exact pricing | Avoid exact pricing unless freshly verified and dated. |
