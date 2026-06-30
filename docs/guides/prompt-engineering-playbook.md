# Prompt Engineering Playbook

Use this playbook to turn a loose request into a prompt that an AI coding agent can execute safely. It is written for public repositories, Windows-friendly workflows, and reviewable pull requests.

For the full curriculum, start with [Comprehensive Prompt Engineering Guide](comprehensive-prompt-engineering-guide.md). Use this playbook as the shorter operational reference.

The main rule: a prompt is a work order, not a wish. It should define the goal, scope, safety boundaries, verification steps, and final report.

## Beginner Path

1. Pick a docs-only task that affects one or two files.
2. Run `git status` before asking the agent to work.
3. Tell the agent to read `AGENTS.md` and the target files before editing.
4. State the files in scope and the files out of scope.
5. Include the exact checks the agent should run.
6. Ask for a final report with changed files, commands run, checks run, and remaining risks.
7. Review the diff yourself before committing or opening a PR.

Safe beginner prompt:

```text
Read AGENTS.md and README.md before editing.

Objective:
Add one short beginner-friendly paragraph to README.md explaining why local checks matter.

Scope:
- Include: README.md
- Exclude: workflow YAML, dependencies, scripts, private files

Safety:
- Do not add external links unless they are already used in this repo.
- Do not include secrets, personal data, or private machine paths.

Verification:
- Run: python scripts/repo_health_check.py
- Run: python scripts/safe_autofix.py --check

Final report:
- Summary
- Files changed
- Commands run
- Checks run
- Risks or skipped verification
```

## Advanced Path

Use the advanced path when the task spans multiple files or several tools.

1. Define the public audience and the repository purpose.
2. Split the task into phases: inspect, edit, validate, review.
3. Add explicit stop conditions for risky commands, unexpected conflicts, or unrelated failing tests.
4. Require conservative language for fast-changing tools.
5. Require a changelog entry for user-visible documentation or workflow changes.
6. Require the agent to distinguish verified facts from claims that need official documentation.
7. Ask for a small diff even when the task is broad.

Advanced prompt skeleton:

```text
Objective:
Complete REQUEST as a reviewable public-repository change.

Context:
- Audience:
- Repository purpose:
- Current branch:
- Relevant docs:

Required workflow:
1. Run git status.
2. Inspect relevant files.
3. Make the smallest correct change.
4. Update CHANGELOG.md if the change is user-visible.
5. Run the listed checks.
6. Report unverified claims and remaining risks.

Safety boundaries:
- Do not edit .env, credentials, private documents, browser profiles, or secrets.
- Do not add dependencies.
- Do not modify workflow YAML unless explicitly required.
- Do not state exact pricing, plan access, model availability, or platform support unless verified in official documentation.

Verification:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests
```

## Core Prompt Patterns

| Pattern | When to use it | Prompt phrase |
| --- | --- | --- |
| Inspect then edit | The agent needs repo conventions. | "Read AGENTS.md and the target files before editing." |
| Smallest correct change | The task is focused. | "Keep the diff minimal and avoid unrelated refactors." |
| Scope fence | Risk of broad edits. | "Include these paths; exclude these paths." |
| Verification contract | You need a reliable finish. | "Run these checks and report exact results." |
| Claims control | External tools are mentioned. | "Mark fast-changing behavior as verify in official documentation." |
| Recovery rule | Conflicts or test failures are possible. | "If failures are unrelated, report them instead of rewriting the repo." |

## Examples

### Weak Prompt

```text
Improve the docs and make the repo look professional.
```

Why it is weak:

- No file scope.
- No safety boundaries.
- No audience.
- No verification.
- No final report format.

### Strong Prompt

```text
Read AGENTS.md, README.md, and docs/workflows/public-repo-safety.md.

Objective:
Add a practical checklist section to docs/workflows/public-repo-safety.md for reviewing static HTML pages in a public repo.

Scope:
- Include: docs/workflows/public-repo-safety.md, CHANGELOG.md
- Exclude: workflow YAML, dependencies, scripts, private paths

Content rules:
- Mention no external trackers, analytics, CDNs, remote fonts, private links, or secrets.
- Keep claims evergreen.
- Use Windows-friendly examples if commands are needed.

Verification:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check

Final report:
- Summary
- Files changed
- Commands run
- Checks run
- Claims needing manual verification
- Remaining risks
```

## Safe Commands

These commands are safe for this repository when run from the repository root.

```powershell
git status
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
git diff --stat
```

Commands that need extra care:

```powershell
# Verify this command in official docs before running.
# Replace placeholders before use.
# Do not paste secrets into commands.
npx TOOL_NAME@latest --help
```

Do not ask a beginner agent task to run install, delete, force-push, system settings, or credential commands.

## Common Mistakes

| Mistake | Consequence | Safer alternative |
| --- | --- | --- |
| "Fix everything" prompt | Large unrelated diff. | Give one objective and exact scope. |
| No verification command | False confidence. | List checks and require exact results. |
| No excluded paths | Agent may edit workflows or generated files. | Include an explicit "Exclude" list. |
| Exact product claims | Docs become stale or wrong. | Say "verify in official documentation." |
| Secret-like examples | Public repo risk. | Use placeholders such as `YOUR_TOKEN_HERE`. |
| Tool setup guessing | Broken instructions. | Link or point to official docs for current setup. |

## Review Checklist

- [ ] Does the prompt have one primary objective?
- [ ] Does it name the audience or user?
- [ ] Does it tell the agent what to inspect first?
- [ ] Does it include files or folders in scope?
- [ ] Does it exclude secrets, private files, dependencies, and workflow YAML when appropriate?
- [ ] Does it include verification commands?
- [ ] Does it require a final report?
- [ ] Does it avoid exact pricing, plan, model, or platform claims?
- [ ] Does it tell the agent what to do if checks fail?

## Failure Modes

| Failure mode | Likely cause | Recovery |
| --- | --- | --- |
| Agent edits too many files | Scope was vague. | Stop, review diff, tighten file scope, restart from clean state if needed. |
| Agent makes unsupported product claims | Prompt allowed guessing. | Replace claims with conservative wording and official-doc verification notes. |
| Agent skips tests | Verification was optional or unclear. | Add exact commands and require reporting skipped checks. |
| Agent exposes private context | Prompt allowed broad filesystem access. | Restrict work to repository root and remove private details from the prompt. |
| Agent keeps fixing unrelated failures | No stop rule. | Tell the agent to report unrelated failures instead of rewriting unrelated areas. |

## Final Report Template

```text
Summary:
- What changed and why.

Files changed:
- path/to/file.md

Commands run:
- command and result

Checks run:
- check name: pass/fail/not run

Claims needing manual verification:
- Tool behavior, pricing, setup, platform support, or model availability.

Remaining risks:
- Anything not verified or intentionally left out.
```
