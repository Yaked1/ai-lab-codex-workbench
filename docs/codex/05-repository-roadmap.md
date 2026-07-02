# Repository Roadmap

This roadmap keeps the repository useful as a public guide while avoiding premature complexity. The sequence matters: safety, documentation, prompt quality, checks, then optional advanced automation.

## Roadmap Principles

- Keep the repo lightweight.
- Prefer Markdown, PowerShell, and standard-library Python.
- Avoid heavy dependencies unless they solve a real teaching need.
- Add automation only when the manual workflow is already understood.
- Keep public safety and human review ahead of agent autonomy.
- Verify fast-changing product claims in official docs before workshops or releases.

## Current Baseline

The repository already contains:

- Public README and project positioning.
- `AGENTS.md` operating rules.
- Tool guide pages.
- Workflow docs.
- Prompt templates.
- Local health and safe autofix scripts.
- Release package builder and release/package guide.
- Unit tests for local scripts.
- CI, safe autofix PR, release package, and controlled merge workflows.

## Next 10 Tasks

| Number | Task | Difficulty | Why it matters | Suggested branch name |
| ---: | --- | --- | --- | --- |
| 1 | Add a Codex task checklist for first-time contributors. | Easy | Gives beginners a repeatable inspect, edit, test, report loop. | `agent/codex-task-checklist` |
| 2 | Add one simple prompt evaluation example with input, expected qualities, and score notes. | Easy | Turns prompt evaluation into a concrete practice exercise. | `agent/prompt-eval-example` |
| 3 | Add a guide for reading failing GitHub Actions logs. | Medium | Helps students diagnose CI instead of guessing. | `agent/actions-log-guide` |
| 4 | Add repo health troubleshooting for common local check failures. | Easy | Makes broken checks easier to fix. | `agent/repo-health-troubleshooting` |
| 5 | Add a safe automation dry-run example for docs cleanup. | Medium | Reinforces preview-first automation. | `agent/docs-dry-run-example` |
| 6 | Add beginner issue templates for small agent tasks. | Easy | Guides users toward focused issues and reviewable PRs. | `agent/beginner-issue-template` |
| 7 | Add prompt before/after examples. | Easy | Shows how to make prompts clearer and testable. | `agent/prompt-before-after` |
| 8 | Add a docs freshness checklist. | Easy | Keeps setup and roadmap docs aligned with the repo. | `agent/docs-freshness-checklist` |
| 9 | Add a lightweight link checker or link-check guidance. | Medium | Helps public docs stay usable without heavy tooling. | `agent/link-check-guidance` |
| 10 | Add a release package inspection exercise. | Easy | Teaches users how to inspect release artifacts before publishing. | `agent/release-package-inspection` |

## Phase 1: Safe Foundation

Goal: make the repo safe to use in public and easy to validate locally.

Includes:

- README.
- `AGENTS.md`.
- `CONTRIBUTING.md`.
- `SECURITY.md`.
- Local checks.
- Unit tests.
- CI.
- Basic prompt templates.
- Public safety guide.

Completion criteria:

- A new learner can run checks.
- A maintainer can review an agent-generated PR.
- No secrets or private data are required.
- The repo works without Docker, WSL, or local models.

## Phase 2: Prompt And Agent Notebook

Goal: teach reusable prompt design.

Add:

- Prompt audit rubric.
- Before/after prompt examples.
- Small prompt evaluation examples.
- Failure-case examples.
- Tool-specific prompt variants.
- Final report templates.

Completion criteria:

- Prompt templates have consistent structure.
- Learners can compare a weak prompt and a strong prompt.
- Prompt outputs can be reviewed against success criteria.

## Phase 3: GitHub Automation

Goal: teach safe GitHub automation without removing human review.

Add or improve:

- Issue templates.
- PR templates.
- CI troubleshooting guide.
- Safe autofix examples.
- Controlled merge documentation.
- Release package review examples.
- Changelog review checklist.

Completion criteria:

- CI failures are understandable.
- Automation opens PRs instead of pushing directly to `main`.
- Merge remains a human decision.

## Phase 4: Small AI Project Track

Goal: add optional learning projects that work in low-setup Windows environments without making hardware limits the public identity of the repository.

Candidate projects:

| Project | Why it fits |
| --- | --- |
| Prompt audit notebook | Teaches evaluation without heavy infrastructure. |
| Markdown RAG reading exercise | Can use small local files and public docs. |
| Image prompt comparison notes | Can be documentation-only without local generation. |
| GitHub reading tracker | Teaches API boundaries and public data handling. |
| AI tool setup checklist | Teaches claim verification and public-safe docs. |

Each project should:

- Avoid secrets.
- Use public data.
- Avoid heavy dependencies.
- Include local checks.
- Include a rollback or cleanup note.

## Phase 5: Advanced Automation

Only after the basics are stable:

- Optional prompt evaluation tooling.
- Changelog validation.
- Link checking.
- Docs generation checks.
- Release note validation.
- Read-only MCP examples.
- Agent skills or subagents examples.
- Lightweight dashboard or status report.

Advanced automation requirements:

- Clear owner.
- Clear rollback.
- Tests or dry-run mode.
- No secrets in logs.
- Human review before merge.

## Do Not Add Yet

| Item | Why not yet |
| --- | --- |
| Heavy Docker stack | Not aligned with the low-setup beginner path. |
| Local model hosting | Too hardware-heavy for the baseline. |
| Auto-merge AI workflow | Removes review from the teaching path. |
| Broad dependency framework | Adds maintenance burden before need is proven. |
| Write-capable MCP services | Too much permission risk for early learners. |

## Roadmap Review Checklist

Before adding a roadmap item:

- [ ] Does it serve the public guide purpose?
- [ ] Is it safe for beginner learners?
- [ ] Does it work in a low-setup Windows environment or clearly label heavier requirements?
- [ ] Can it be validated locally?
- [ ] Does it avoid secrets and private data?
- [ ] Does it keep human review in the loop?
- [ ] Are external claims marked for official-doc verification?

## Suggested Release Milestones

| Milestone | Theme | Exit criteria |
| --- | --- | --- |
| `0.2.0` | Professional guide baseline | Expanded docs, release package workflow, prompts, workflows, checks passing. |
| `0.3.0` | Prompt evaluation practice | Rubric, examples, and before/after prompts. |
| `0.4.0` | GitHub workflow teaching kit | Issue/PR templates and CI troubleshooting. |
| `0.5.0` | Optional advanced integrations | Read-only MCP and automation examples with safeguards. |
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `docs/codex/05-repository-roadmap.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `05 repository roadmap` state what decision, workflow, or reusable behavior it supports?
- Are included scope, excluded scope, and unsafe actions clear enough for an
  agent or contributor to follow?
- Are examples public-safe, repository-relative, and free of private data?
- Are fast-changing product or platform claims phrased conservatively or marked
  for official-doc verification?
- Does the file point to the next artifact a reader should inspect: a command,
  template, test, manifest, package, or deeper guide?
- Could a reviewer cite this file in a PR review and know what evidence proves
  the work is complete?

Keep future edits focused on stronger evidence, clearer failure modes, better
navigation, and safer automation boundaries. Do not add length unless the new
material makes the repository easier to operate, teach, audit, or recover.
<!-- RESEARCH-GRADE-EXPANSION:END -->
