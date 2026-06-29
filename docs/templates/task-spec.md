# Task Spec

Use this template before asking Codex or another AI coding agent to work.

Copy the sections that matter into an issue, PR description, or agent goal. For a tiny typo fix, this may be too much. For any multi-file, agent-assisted, public-facing, or workflow-sensitive task, use the full template.

## Task Title

```text
[Short public-safe title]
```

## Objective

```text
[One clear outcome. Avoid vague requests such as "improve everything."]
```

## Owner And Review

- Requester:
- Implementer or agent:
- Reviewer:
- Target branch:
- Expected PR size:
- Deadline, if any:

## Background

- Why this change is needed:
- Who benefits:
- Relevant issue or discussion:
- Tool intended for the task:
- Current limitation or pain point:
- Previous related work:

## User Story

```text
As a [learner/contributor/maintainer/instructor],
I want [specific improvement],
so that [observable benefit].
```

## Readiness Checklist

- [ ] The objective is specific.
- [ ] The included scope is listed.
- [ ] The excluded scope is listed.
- [ ] Success criteria are testable.
- [ ] Required checks are listed.
- [ ] Public-safety risks are identified.
- [ ] Fast-changing external claims are marked for official-doc verification.

## Files The Agent Should Inspect First

- `AGENTS.md`
- `README.md`
- `[add relevant docs, scripts, or tests]`

## Current Behavior Or Current Content

```text
[Describe what exists now. Link or name the relevant section, script behavior, prompt template, or workflow.]
```

## Desired Behavior Or Desired Content

```text
[Describe the target state in enough detail that a reviewer can tell whether it was achieved.]
```

## Included Scope

- [ ] `[file or folder]`
- [ ] `[specific behavior or section]`
- [ ] `[tests, docs, prompts, or changelog entry if needed]`

## Excluded Scope

- [ ] Do not edit secrets or `.env` files.
- [ ] Do not install dependencies without approval.
- [ ] Do not delete files.
- [ ] Do not change unrelated folders.
- [ ] Do not modify workflow YAML unless explicitly requested.
- [ ] Do not add exact pricing, model, or platform claims without official-doc verification.
- [ ] Do not rewrite unrelated guides or templates.
- [ ] Do not add generated assets, screenshots, or binaries unless explicitly requested.

## Success Criteria

- [ ] The requested change is complete.
- [ ] The diff is focused.
- [ ] Beginner-facing docs are clear.
- [ ] Advanced users can audit the reasoning, safety boundaries, and verification path.
- [ ] Public-safety rules still hold.
- [ ] External claims are conservative or explicitly marked for official-doc verification.
- [ ] Internal links still point to real files or headings.
- [ ] Checks pass or failures are honestly reported.
- [ ] Final response lists files changed, commands run, checks run, and remaining risks.

## Acceptance Tests Or Review Evidence

| Requirement | Evidence to inspect |
| --- | --- |
| `[requirement]` | `[file section, command output, test result, rendered page, or PR review note]` |
| `[requirement]` | `[evidence]` |

## Safety Boundaries

- Keep work inside this repository.
- Do not inspect private folders.
- Do not print environment variables.
- Do not add secrets, private links, or personal data.
- Ask before destructive commands.
- Ask before dependency installation.

## External Claims

List any claims that could become stale:

- Tool setup:
- Pricing or plan availability:
- Model names:
- Platform support:
- Feature behavior:
- Official docs to verify:

If there are no external claims, write:

```text
No fast-changing external claims added.
```

## Local Checks

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

## Manual Review Steps

- [ ] Review `git diff --stat`.
- [ ] Review the full diff for unrelated changes.
- [ ] Search for private links, paths, credentials, and account details.
- [ ] Check Markdown tables and links where relevant.
- [ ] Open static HTML files directly in a browser if they changed.
- [ ] Confirm changelog entry is present when user-visible docs changed.

## Rollback Plan

```text
[How to revert if this change causes confusion or breaks checks. For a normal PR, "revert the squash commit" is usually enough.]
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

## Example Filled Task

```markdown
## Task Title

Expand Codex review guidance

## Objective

Expand docs/codex/04-review-checklist.md with a clearer PR review sequence, public-safety checks, and examples of review comments.

## Included Scope

- [x] docs/codex/04-review-checklist.md
- [x] CHANGELOG.md if the change is user-visible

## Excluded Scope

- [x] Do not edit workflow YAML.
- [x] Do not add dependencies.
- [x] Do not change other tool pages.

## Success Criteria

- [x] The guide explains review order, risk checks, test evidence, and final decision options.
- [x] Examples are public-safe.
- [x] Local checks pass or failures are reported.
```
