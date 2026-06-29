# Agentic Coding Playbook

This playbook describes a safe branch-to-review workflow for AI coding agents. It is intended for public repositories, student laptops, and maintainers who want useful agent help without losing control of the diff.

## Beginner Path

Start with a small documentation task before asking an agent to edit code.

1. Read `AGENTS.md`.
2. Run `git status`.
3. Create a short branch name.
4. Give the agent one focused task.
5. Require file inspection before editing.
6. Run local checks.
7. Review the diff.
8. Open a PR only when the change is understandable.

Safe branch setup:

```powershell
git status
git switch -c agent/docs-small-edit
```

Safe validation:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

## Advanced Path

Use this path for multi-file docs, scripts, or workflow changes that still need to stay reviewable.

1. Confirm the branch is clean or every existing change is understood.
2. Write a task spec with included paths, excluded paths, and verification commands.
3. Ask the agent to inspect relevant files and report the intended edit plan.
4. Let the agent edit only after the plan matches the request.
5. Run focused checks first, then full repo checks.
6. Review `git diff --stat` before reading the full diff.
7. Update `CHANGELOG.md` for user-visible changes.
8. Keep the PR description factual: what changed, why, commands run, checks run, and known limitations.

## Lifecycle

| Phase | Goal | Evidence |
| --- | --- | --- |
| Intake | Understand the request. | Task objective, scope, success criteria. |
| Branch | Isolate the work. | `git status`, branch name. |
| Agent work | Produce a focused diff. | Changed files match scope. |
| Checks | Catch basic failures. | Check command output. |
| PR | Make review easy. | Summary, commands, risks. |
| Review | Find regressions and safety issues. | Comments, requested changes, approval. |
| Merge | Land only reviewed work. | Passing CI and human decision. |
| Rollback | Recover from bad changes. | Known commit or PR to revert. |

## Agent Prompt Example

```text
Read AGENTS.md and inspect the relevant files before editing.

Objective:
Add a beginner-friendly section to docs/workflows/agent-task-lifecycle.md that explains how to review an agent-generated diff.

Scope:
- Include: docs/workflows/agent-task-lifecycle.md, CHANGELOG.md
- Exclude: workflow YAML, dependencies, generated files, private paths

Safety:
- Keep the change public-safe.
- Do not add external links unless necessary.
- Mark fast-changing tool behavior as "verify in official documentation."

Verification:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check

Final report:
- Summary
- Files changed
- Commands run
- Checks run
- Remaining risks
```

## Code Change Prompt Example

Use this only after a beginner has completed docs-only practice.

```text
Read AGENTS.md, scripts/repo_health_check.py, scripts/safe_autofix.py, and tests/.

Objective:
Fix BUG_DESCRIPTION with the smallest code change and add or update focused tests.

Scope:
- Include: scripts/, tests/
- Exclude: dependencies, workflow YAML, unrelated docs

Rules:
- Prefer Python standard library.
- Do not add dependencies.
- Do not rewrite unrelated functions.
- If a failing test is unrelated, report it instead of broad refactoring.

Verification:
- python -m unittest discover -s tests
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
```

## PR Review Checklist

- [ ] The branch has one task.
- [ ] The diff matches the requested scope.
- [ ] The agent inspected relevant files before editing.
- [ ] No secrets, private links, private paths, or personal data were added.
- [ ] No dependency or lock file was added without approval.
- [ ] Workflow YAML was not changed unless requested.
- [ ] Local checks were run and results are reported.
- [ ] CI passed or failures are documented.
- [ ] User-visible changes are recorded in `CHANGELOG.md`.
- [ ] Fast-changing external claims are marked for official-doc verification.

## Public Repository Safety Gate

Before merge, run:

```powershell
git status
git diff --stat
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

Then manually check:

- No `.env`, credentials, private keys, browser cookies, or token-like strings.
- No private URLs, private account IDs, personal emails, or private machine paths.
- No exact pricing, plan limits, model availability, or platform support claims unless verified.
- No external trackers, analytics, CDNs, or remote fonts in static HTML.

## Common Mistakes

| Mistake | Why it is risky | Safer habit |
| --- | --- | --- |
| Working on `main` for agent tasks | Harder to review or revert. | Use `agent/<short-task-name>` branches. |
| Asking the agent to edit before reading files | Breaks local conventions. | Require inspection first. |
| Accepting a diff without reading it | Regressions and secrets can land. | Review every changed file. |
| Skipping checks for docs | Formatting or public-safety issues can slip in. | Run repo health and safe autofix checks. |
| Combining multiple goals | PR becomes hard to review. | One task, one branch, one PR. |

## Failure Modes

| Failure mode | Signal | Response |
| --- | --- | --- |
| Cherry-pick or merge conflict | Git reports unmerged paths. | Inspect conflicted files, preserve useful changes, remove markers, stage, continue. |
| Test failure after docs-only change | Tests fail outside touched area. | Report clearly; do not rewrite unrelated code unless asked. |
| Agent adds dependency | New package file or install instruction appears. | Remove or ask for explicit approval. |
| Agent changes workflow YAML | `.github/workflows` diff appears. | Stop unless the task explicitly requested automation changes. |
| Agent uses private context | Private path or link appears. | Remove it and tighten prompt boundaries. |

## Branch And PR Naming

Use short public-safe names:

```text
agent/docs-guide-update
agent/fix-health-check
agent/prompt-template-review
```

Avoid private project names, school portals, account IDs, internal ticket numbers, or sensitive context.

## Definition Of Done

A task is done when:

- The requested change is complete.
- The diff is minimal and reviewable.
- Relevant checks were run.
- Failures are fixed or honestly reported.
- Public-safety constraints are preserved.
- The final report lists changed files, commands, checks, and risks.
