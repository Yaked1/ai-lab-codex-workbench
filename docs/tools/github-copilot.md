# GitHub Copilot and Copilot Coding Agent

## What It Is

GitHub Copilot is GitHub's AI assistance family for code suggestions, chat, IDE help, and agentic issue-to-PR work depending on the user's plan, IDE, organization policy, and current GitHub product surface. In this repository, Copilot is useful for small IDE edits, GitHub issue work, PR drafts, and review practice.

Avoid exact pricing, plan, model, and feature claims unless they are verified in current GitHub documentation.

## Best Use Cases

| Use case | Fit | Notes |
| --- | --- | --- |
| Inline code suggestions | Strong | Review suggestions before accepting. |
| Explaining code in an IDE | Strong | Good for beginners. |
| Small docs PR from an issue | Strong | Keep issue acceptance criteria clear. |
| PR review assistance | Medium | Human review still decides. |
| CI-aware GitHub workflow | Medium | Always read Actions logs. |
| Large autonomous implementation | Medium to weak | Scope the issue tightly. |

## What Copilot Is Good At Vs. Not

Good at:

- Inline completions and small in-editor suggestions where you stay in
  control of every accepted line.
- Explaining unfamiliar code while you read through a file.
- Turning a well-scoped GitHub issue into a draft PR, when the repo already
  has GitHub Actions CI to catch regressions.
- Fitting naturally into a GitHub-native workflow: issues, PRs, Actions,
  review, all in one platform.

Not good at:

- Vague or open-ended issues. The coding agent needs concrete acceptance
  criteria; without them it will guess, and the guess becomes a PR you still
  have to fully review.
- Local, non-GitHub workflows. If your task isn't going through issues/PRs,
  the coding-agent half of Copilot has less to offer than a CLI-first tool.
- Large architectural changes without a maintainer-authored design; scope
  agent-driven PRs tightly.

## Beginner Friendliness

High for IDE suggestions and explanations. Medium for autonomous coding-agent work because a generated PR can look complete even when the diff or CI has problems.

## Using This Repository's Workflow With Copilot

- Prompt/issue template: [prompts/github-copilot/agent-task.md](../../prompts/github-copilot/agent-task.md).
- Local rules: GitHub Copilot supports repository-level custom instructions,
  commonly placed in a dedicated instructions file under `.github/` (for
  example a Copilot-specific instructions file). Verify the exact current
  filename and scope rules (repo-wide vs. path-specific) in official GitHub
  docs, since Copilot has iterated on this mechanism. Mirror the same scope
  and safety boundaries this repo's `AGENTS.md` already states.
- For coding-agent (issue-to-PR) work, put the acceptance criteria directly
  in the GitHub issue body — that is the primary channel that shapes agent
  behavior, more than chat instructions.

## Task Intake Worksheet

Copilot works best when the issue or chat prompt is already reviewable.

| Intake item | What to write before assigning the task |
| --- | --- |
| Issue goal | A short title plus one paragraph describing the user-visible outcome. |
| Expected files | Exact files the coding agent may change. |
| Acceptance criteria | Checkable bullets that say what must be true in the PR. |
| Out of scope | Dependencies, workflow YAML, unrelated docs, secrets, or broad refactors. |
| Verification | Required local commands and GitHub Actions checks. |
| Reviewer | The human who reads the diff, Actions logs, and final PR body. |
| Plan/cost risk | Current Copilot plan, organization policy, premium request behavior, and agent availability to verify in official docs. |

If the issue cannot name expected files and acceptance criteria, it is not
ready for a coding-agent assignment. Ask Copilot Chat for a draft issue first
or do a local planning pass.

## Context Selection Rules

For Copilot, context often comes from the IDE workspace, GitHub issue, PR
thread, repository instructions, and organization policy. Keep the important
context close to the task:

- Put exact file paths and acceptance criteria in the issue body, not only in a
  comment or chat message.
- Keep repository custom instructions short, durable, and aligned with
  `AGENTS.md`.
- Attach or reference directly related files in Copilot Chat for IDE work; do
  not rely on vague "look around the repo" wording for small tasks.
- Do not paste secrets, private logs, private links, `.env` contents, or
  account-specific settings into an issue, PR, or chat.
- If a generated PR edits files outside the expected list, treat that as a
  review finding and require either a revert or a maintainer-approved scope
  expansion.
- For public docs, ask the agent to mark product behavior, pricing, model, and
  plan claims as official-doc verification items unless they are freshly cited.

## Beginner Workflow Guidance

A safe first Copilot coding-agent task should look like this:

1. Open a tiny documentation issue with one target file.
2. Include acceptance criteria and out-of-scope items.
3. Let the agent create a draft branch or PR where available.
4. Read the diff and Actions logs yourself.
5. Pull the branch locally and run this repository's checks when practical.
6. Request changes instead of merging if the PR is broader than the issue.

Inline suggestions are even simpler: accept only the lines you understand,
then run the relevant file or tests.

## Example Workflow: Task Intake To PR

1. **Task intake.** Write a GitHub issue with an exact file, a one-sentence
   task, and acceptance criteria (borrow structure from
   [prompts/github-copilot/agent-task.md](../../prompts/github-copilot/agent-task.md)).
2. **Scoped prompt.** Assign the issue to the Copilot coding agent (or use
   in-editor chat for a smaller inline task) with the scope and boundaries
   spelled out in the issue.
3. **Agent work.** The agent drafts a branch and opens a PR (for coding-agent
   flow) or proposes inline edits (for IDE flow).
4. **Local checks.** Pull the branch locally or rely on GitHub Actions CI, but
   verify at least once locally before trusting CI alone:

   ```powershell
   git fetch origin
   git switch <agent-branch>
   python scripts/repo_health_check.py
   python scripts/safe_autofix.py --check
   python -m unittest discover -s tests
   ```

5. **Diff review.** Review every changed line in the PR like any other
   contributor's PR — do not skip review because it was agent-authored.
6. **PR.** Merge only after CI is green and the diff matches the issue's
   acceptance criteria.

## Troubleshooting

| Symptom | Likely cause | Response |
| --- | --- | --- |
| Generated PR touches files outside the issue's scope | Issue lacked explicit file/scope boundaries. | Close or request changes; rewrite the issue with a named file list. |
| CI passes but the diff doesn't match intent | CI checks syntax/tests, not intent. | Always read the diff yourself; CI green is necessary, not sufficient. |
| Custom instructions seem ignored | Wrong file location, or instructions conflict with org-level policy. | Verify current instructions-file path and check organization Copilot policy settings. |
| Coding agent stalls or produces an empty PR | Issue was too vague or acceptance criteria were unmeasurable. | Rewrite with concrete, checkable acceptance criteria. |
| Inline suggestion looks right but doesn't compile/run | Model suggestions are drafts based on local context, not verified output. | Always run the file/tests before trusting a suggestion. |
| Actions logs show a failure the PR description doesn't mention | PR summaries can be generated without cross-checking CI. | Always open the Actions tab and read the actual log before merging. |

## Setup Style

| Style | When to use it | Beginner note |
| --- | --- | --- |
| IDE | Suggestions, chat, small edits. | Best entry point. |
| GitHub cloud | Issue-to-branch-to-PR agent work where available. | Review PR and CI before merge. |
| Browser | Reviewing PRs and Actions logs. | Keep human approval in the loop. |
| Hybrid | IDE work plus GitHub PR review. | Common and practical. |

## Windows Suitability

Good through supported IDEs and GitHub.com. Verify current support for the exact editor and account type before teaching setup.

## Hardware, API, Docker, and WSL Requirements

| Requirement | Practical guidance |
| --- | --- |
| Hardware | Lightweight for IDE suggestions and GitHub-hosted agent tasks. |
| API/account | Verify plan, organization policy, and feature availability. |
| Docker | Not needed for this repo. |
| WSL | Not needed for docs and script tasks. |
| GPU | Not needed. |

## Best First Task

Create a tiny documentation issue and ask the Copilot coding agent to draft a PR. Review every changed line and CI result before merging.

## Prompt/Issue Template

```text
Title:
Improve beginner clarity in [file]

Task:
Update [section] so a first-time Windows user can follow it.

Scope:
- Edit only [file].
- Do not modify workflow YAML.
- Do not add dependencies.
- Do not include pricing or current feature claims unless verified.

Acceptance criteria:
- Text is beginner-friendly.
- No private data or secrets are added.
- CI checks pass.
- PR summary lists commands or checks run.
```

## Safety Risks

- IDE suggestions can be accepted without understanding.
- A generated PR is not the same as a reviewed PR.
- Organization policies and plan differences can change behavior.
- GitHub Actions logs may reveal issues that the PR description misses.

## Permission, Cost, And Data Guardrails

| Risk | Practical control |
| --- | --- |
| Organization policy differences | Verify whether Copilot features, coding agent access, and repository permissions are enabled for the account/org. |
| Paid or limited usage | Check current plan, premium request, model, and usage-limit docs before assigning large tasks. |
| Repository write access | Treat agent branches and PRs as contributor work; require review before merge. |
| CI trust gap | Read Actions logs directly and rerun local checks for important changes. |
| Issue data exposure | Do not include secrets, private logs, private URLs, or account-specific screenshots in issues or PRs. |
| Instruction conflicts | Check repo, org, and IDE instructions when the agent appears to ignore scope. |

Do not use public docs to promise availability, pricing, model routing, or
platform behavior. Those details should be verified in current GitHub docs for
the account type being used.

## Review Checklist

- [ ] Does the issue define exact scope?
- [ ] Is the generated branch focused?
- [ ] Do acceptance criteria match the final diff?
- [ ] Did CI pass?
- [ ] Were Actions logs reviewed?
- [ ] Are there any private links, tokens, or personal data?
- [ ] Does the PR body list limitations and checks?

## Final Report Expectations

For Copilot coding-agent work, the PR body or final chat summary should state:

- Issue goal and exact files changed.
- Acceptance criteria satisfied and any criteria not completed.
- Checks run locally and in GitHub Actions, with failures called out.
- Whether any files outside the expected scope were touched.
- Product behavior, plan, pricing, or model claims that need official-doc
  verification.
- Remaining reviewer risks, especially CI gaps, broad diffs, or unverifiable
  claims.

## When To Avoid It

Avoid Copilot agent workflows for:

- Tasks with vague acceptance criteria.
- Repositories with secrets in files the agent may inspect.
- Broad dependency upgrades without a maintainer plan.
- Public docs that make unverified claims about plans, pricing, or models.

## Alternatives

| Alternative | Use when |
| --- | --- |
| Codex | You want local branch work and local command execution. |
| Cursor | You want editor-first planning and visible diffs. |
| Claude Code | You want a read-only second opinion. |
| Aider | You want terminal edits with explicit files. |

## Verification Notes

Verify current Copilot coding-agent availability, plan requirements, organization policy behavior, supported IDEs, model options, and pricing in GitHub docs.

## Claims To Verify In Official Docs

- Current Copilot plan and feature availability.
- Supported IDEs and operating systems.
- Coding agent behavior and permissions.
- Issue assignment and PR workflow.
- CI integration and review requirements.
- Pricing, limits, and model details.

Official docs:

- <https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent>
