# Agent Task Lifecycle

Use this workflow for Codex, Claude Code, Cursor, Antigravity, GitHub Copilot, OpenCode, Kilo Code, Aider, Windsurf, MCP-enabled agents, or any other AI coding assistant.

The workflow is intentionally simple: one task, one branch, one agent prompt, one reviewable diff, local checks, CI, review, merge, changelog.

## Lifecycle Diagram

```mermaid
flowchart LR
    A[issue or task intake] --> B[branch naming]
    B --> C[goal prompt]
    C --> D[agent execution]
    D --> E[local checks]
    E --> F[pull request]
    F --> G[CI checks]
    G --> H[PR review]
    H --> I[squash merge]
    I --> J[changelog update]
    H --> K[rollback plan]
```

## 1. Issue/Task Intake

Start by turning the request into a testable task. A good task has boundaries:

| Field | Good example | Weak example |
| --- | --- | --- |
| Objective | "Expand `docs/tools/codex.md` with setup, risks, and review checklist." | "Improve docs." |
| Included scope | "`docs/tools/codex.md` only." | "Anything that seems related." |
| Excluded scope | "Do not edit workflow YAML or install dependencies." | "Be careful." |
| Success criteria | "Includes prompt template and verification notes; local checks pass." | "Make it better." |
| Verification | "Run the three local checks." | "Looks fine." |

Use [docs/templates/task-spec.md](../templates/task-spec.md) when you need a reusable task format.

## 2. Branch Naming

Use a short branch name that describes one task:

```powershell
git switch -c agent/expand-codex-guide
```

Recommended pattern:

```text
agent/<short-task-name>
```

Good examples:

```text
agent/add-public-safety-checklist
agent/fix-repo-health-docs
agent/update-codex-prompts
```

Avoid branch names that include private project names, account IDs, internal ticket numbers, or sensitive context.

## 3. Goal Prompt Creation

Use a goal-style prompt when work is more than a one-line edit. A strong prompt includes:

- Target tool.
- Objective.
- Context to read first.
- Included scope.
- Excluded scope.
- Safety boundaries.
- Success criteria.
- Verification commands.
- Final report format.

Template:

```text
Objective:
[One clear task.]

Context:
- Read AGENTS.md.
- Inspect [files] before editing.

Included scope:
- [Files or folders allowed.]

Excluded scope:
- Do not edit workflow YAML.
- Do not add dependencies.
- Do not touch secrets or private files.

Success criteria:
- [Behavior or documentation requirement.]
- No unrelated files changed.
- Local checks pass.

Verification:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests

Final report:
- Summary
- Files changed
- Commands run
- Checks run
- Remaining risks
```

## 4. Agent Execution

Before editing, the agent should:

- Read `AGENTS.md`.
- Run or inspect `git status`.
- Read the relevant files.
- Identify a minimal plan.
- Confirm risky assumptions instead of guessing.

During editing, the agent should:

- Keep changes inside the requested scope.
- Avoid unrelated cleanup.
- Preserve local conventions.
- Avoid dependency changes unless explicitly approved.
- Avoid exact external-tool claims unless verified.
- Keep public safety constraints in mind.

For broad tasks, ask the agent to produce a plan first and then implement only the approved part.

## 5. Local Checks

Run from PowerShell in the repository root:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

What each check means:

| Command | Purpose | Common failure |
| --- | --- | --- |
| `python scripts/repo_health_check.py` | Required files, final newlines, simple secret patterns, large-file warnings. | Missing final newline or secret-like text. |
| `python scripts/safe_autofix.py --check` | Reports files that would change under deterministic whitespace cleanup. | Trailing spaces or missing final newline. |
| `python -m unittest discover -s tests` | Runs tests for repository scripts. | Script behavior changed without test updates. |

If `safe_autofix.py --check` fails, you may run:

```powershell
python scripts/safe_autofix.py --write
python scripts/safe_autofix.py --check
```

Review the diff after any write command.

## 6. CI Checks

CI repeats the repository validation on GitHub. Read the workflow logs when CI fails instead of guessing.

Current CI checks:

| Workflow | Trigger | What it checks |
| --- | --- | --- |
| `ci.yml` | Push to `main`, pull request, manual dispatch. | Repo health, safe autofix check, unit tests. |
| `autofix.yml` | Manual dispatch. | Applies deterministic cleanup and opens a PR if files changed. |
| `merge-pr.yml` | Manual dispatch. | Checks a PR and merges only after required checks pass. |

Do not edit workflow YAML unless the task is specifically about automation.

## 7. Pull Request

A good PR body includes:

- What changed.
- Why it changed.
- Files or areas touched.
- Commands run.
- Checks run.
- Known limitations.
- Claims that still need official-doc verification.
- Screenshots only for visual changes.

Example:

```markdown
## Summary
- Expanded Codex guide with setup, safety risks, and prompt template.

## Commands run
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests

## Known limitations
- Current Codex platform details should be verified in official docs before workshop use.
```

## 8. PR Review

Review the diff as if it came from a new contributor:

- Does it solve the stated task?
- Is the diff small enough to understand?
- Did it change unrelated files?
- Did it touch workflow YAML or dependencies without approval?
- Are public safety rules still true?
- Are external tool claims conservative?
- Did local checks and CI pass?
- Do CI logs expose anything private?

Use [docs/codex/04-review-checklist.md](../codex/04-review-checklist.md) for a deeper checklist.

## 9. Squash Merge

Prefer squash merge for small learning branches because it keeps `main` readable:

```powershell
gh pr merge <number> --squash --delete-branch
```

Use the controlled merge workflow when maintainers want GitHub Actions to enforce the required checks before merge.

Do not merge when:

- CI is failing.
- The diff is not reviewed.
- The PR contains secrets or private data.
- The PR changes unrelated files.
- The final report claims checks passed but no evidence is provided.

## 10. Rollback

If a bad commit reaches `main`, prefer `git revert` over rewriting shared history:

```powershell
git log --oneline
git revert <bad_commit_hash>
git push
```

Rollback checklist:

- Identify the bad commit.
- Confirm whether a revert is safe.
- Run local checks after the revert.
- Open a PR if your branch protection expects PR review.
- Add a changelog or incident note if learners need to understand what happened.

## 11. Public Repo Safety

Before merge or public release:

- Check for secrets and token-like strings.
- Check for private links.
- Check for personal data and private paths.
- Check screenshots if any were added.
- Check GitHub Actions logs.
- Keep product claims conservative.

Use [public-repo-safety.md](public-repo-safety.md) for the full safety guide.

## 12. Secret Scanning

This repo includes a simple secret-pattern check, but maintainers should still review manually:

```powershell
python scripts/repo_health_check.py
```

Manual searches can help:

```powershell
rg -n "\.env|token|secret|password|private key|api key" .
```

Do not paste real secrets into issues, prompts, or examples.

## 13. Changelog Updates

Update [CHANGELOG.md](../../CHANGELOG.md) when a change is:

- User-visible.
- Workflow-visible.
- A new guide, template, or safety rule.
- A change to local checks or GitHub Actions behavior.
- A notable limitation or migration note.

Good changelog entries are factual:

```markdown
- Expanded Codex goal workflow with prompt structure, validation, and failure modes.
```

Avoid vague entries:

```markdown
- Improved stuff.
```

## Common Failure Modes

| Failure | Likely cause | Fix |
| --- | --- | --- |
| Agent changed too many files | Prompt scope was vague. | Re-scope and revert only the unrelated changes after review. |
| CI fails but local passed | Environment difference or missed command. | Read logs and rerun the matching local check. |
| Safe autofix check fails | Whitespace or missing final newline. | Run `safe_autofix.py --write`, review diff, rerun check. |
| Tool claims sound too exact | Product docs were not verified. | Reword as "verify in official docs." |
| PR is hard to review | Task was too broad. | Split into smaller PRs. |

## Definition Of Done

A task is complete only when:

- The requested change is done.
- The diff is focused.
- Local checks were run.
- CI passed or failures are honestly reported.
- Public safety rules are preserved.
- Changelog is updated when appropriate.
- Remaining risks are documented.
