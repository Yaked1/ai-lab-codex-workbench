# Repository Roadmap

## Next 10 Tasks

| Number | Task | Difficulty | Why it matters | Suggested branch name |
| --- | --- | --- | --- | --- |
| 1 | Add a Codex task checklist for first-time contributors. | Easy | Gives beginners a repeatable way to inspect, edit, test, and summarize work safely. | `agent/codex-task-checklist` |
| 2 | Add one simple prompt evaluation example with an input, expected qualities, and score notes. | Easy | Turns prompt evaluation from an abstract idea into a concrete practice exercise. | `agent/prompt-eval-example` |
| 3 | Document what each GitHub Actions workflow checks. | Easy | Helps students understand CI results before changing automation. | `agent/document-actions-checks` |
| 4 | Add a repo health troubleshooting page for common local check failures. | Easy | Makes broken checks easier to diagnose without guessing. | `agent/repo-health-troubleshooting` |
| 5 | Add a safe automation dry-run example for a docs cleanup task. | Medium | Reinforces preview-first automation before any write step. | `agent/docs-dry-run-example` |
| 6 | Add a beginner issue template for small Codex tasks. | Easy | Guides users toward focused issues that are easier to solve and review. | `agent/beginner-issue-template` |
| 7 | Add a prompt improvement before-and-after sample. | Easy | Shows how to make prompts clearer, more testable, and easier for agents to follow. | `agent/prompt-before-after` |
| 8 | Add a short guide for reading failing GitHub Actions logs. | Medium | Builds confidence with CI failures and keeps fixes targeted. | `agent/actions-log-guide` |
| 9 | Add a documentation freshness checklist for roadmap and setup pages. | Easy | Keeps docs aligned with the current repository structure and scripts. | `agent/docs-freshness-checklist` |
| 10 | Add a small repo health badge or status section to the README. | Medium | Makes the repository's validation status visible from the starting page. | `agent/readme-health-status` |

## Phase 1: Safe foundation

- Add README, AGENTS.md, templates, scripts, and CI.
- Learn branch and PR workflow.
- Use Codex only on tiny tasks.

## Phase 2: Prompt and agent notebook

- Add prompt examples.
- Add prompt audit rubric.
- Add before/after prompt improvements.
- Add small evaluations.

## Phase 3: GitHub automation

- Use issue templates.
- Use autofix PR workflow.
- Use controlled merge workflow.
- Add labels and milestones manually.

## Phase 4: Small AI project

Choose one:

- Prompt audit notebook.
- Small Markdown RAG assistant.
- Image prompt comparison notebook.
- GitHub reading tracker for AI repositories.

## Phase 5: More advanced automation

Only after the basics work:

- Add promptfoo.
- Add docs generation checks.
- Add release notes generation.
- Add changelog validation.
- Add a lightweight dashboard.

Do not jump to Phase 5 on day one unless your hobby is debugging automation that automates your debugging.
