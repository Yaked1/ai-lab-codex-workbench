# Hermes Agent Public Repository Safety

Hermes Agent can hold private memory, provider credentials, OAuth state,
sessions, logs, skills, and scheduled automations. Treat that local state as
private unless you have deliberately created a public-safe example.

This page adds Hermes-specific items on top of the repository-wide baseline
in [docs/workflows/public-repo-safety.md](../workflows/public-repo-safety.md).
Read that page for general secret scanning, link hygiene, and the PR safety
checklist that applies to every tool in this repository, not just Hermes
Agent. Do not duplicate that checklist here; this page covers what is unique
to running a persistent, memory-holding agent against a real public repo.

## Scoping Permissions Before A Real Task

Before pointing Hermes Agent at anything connected to this repository,
decide the permission boundary in advance, not while the session is running.

- **Working directory:** point the session at a private scratch directory
  for drafting, not this repository's working tree. If a task must read
  repository files for context, grant read-only access to the specific
  files needed, not the whole repository root.
- **Tool access:** disable shell/file-write tools for research and planning
  tasks. Hermes Agent does not need write access to produce a source ledger,
  an outline, or a risk list.
- **Provider scope:** use the least-capable provider/model tier that
  finishes the task; verify current provider and model options in official
  docs rather than defaulting to the broadest available access.
- **Session lifetime:** prefer a single-task session over a long-running one
  when the task touches anything meant for this repository. A short session
  with no memory carried into the next task is easier to audit.
- **Automation scope:** if a scheduled job is involved, confirm it can only
  write to a private, local destination. See
  [skills-memory-automations.md](skills-memory-automations.md) for the
  safety model around persistent automations.

## Never Commit

- Hermes Agent memory.
- Provider tokens or API keys.
- `.env`.
- OAuth files.
- Browser session data.
- Private conversations.
- Private automations.
- Logs that contain secrets.
- Local sessions.
- Private paths or account IDs.

## Publishing Rules

- Never allow Hermes Agent to push directly to `main`.
- Prefer branch, pull request, checks, review, and merge.
- Use dry runs before publishing.
- Label AI-generated docs clearly when appropriate.
- Verify commands against official docs before publishing.
- Review all source links and license/source labels.
- Do not publish leaked prompts, prompt dumps, or private memory-derived content.

## Avoiding Secret Leakage In Logs And PRs

Hermes Agent sessions generate their own logs, memory writes, and tool-call
traces. None of that is written with a public reader in mind, so review it
before any of it can reach a PR.

- Never paste raw Hermes Agent logs, memory dumps, or tool-call traces into a
  PR description, issue, or commit message. Summarize the outcome instead.
- If a draft references a command's output, re-run the command yourself and
  copy only the redacted, public-safe portion; do not trust the agent's own
  transcript to have redacted it already.
- Treat every provider name, account identifier, endpoint URL, and file path
  that appears in a session as private until proven otherwise. When in
  doubt, replace it with a placeholder such as `YOUR_API_KEY_HERE`.
- Check screenshots or terminal captures for visible tabs, account menus, or
  file paths before attaching them anywhere public.

## Review-Before-Merge Discipline

Hermes Agent output is planning input, never a merge-ready artifact.

1. Treat every draft as unreviewed until a human has read it end to end.
2. Confirm the draft's claims are marked "verify in official Hermes Agent
   docs" wherever they depend on current pricing, platform support, or
   provider behavior.
3. Confirm the draft does not cite private memory, browser sessions, or
   OAuth state as evidence for a public claim.
4. Only after that review does a Git-first agent (Codex or Claude Code) or a
   maintainer turn the draft into an actual branch and diff.
5. Follow this repository's normal branch, PR, checks, and merge flow; do
   not shortcut it because the underlying idea came from Hermes Agent.

## Handling A Runaway Or Looping Agent

A persistent agent with memory and tool access can loop or run longer than
intended. Do not let that keep running unattended against anything
connected to this repository.

1. Stop the session immediately; do not wait for it to "finish on its own."
2. Check whether any tool call it made had write access to files, Git, or an
   external service, and inspect what actually happened before assuming
   nothing changed.
3. Revert any unintended file change with `git checkout -- <path>` after
   confirming no wanted work lives in it.
4. If the loop involved repeated provider calls, check for unexpected cost
   or rate-limit exhaustion before re-running anything.
5. Restate the task with a narrower scope, an explicit success condition,
   and reduced tool access before trying again.
6. See [troubleshooting.md](troubleshooting.md#stuck-or-hanging-sessions)
   for the matching symptom table.

## If It Touches Files Outside Scope

If a Hermes Agent session was ever given write access and it modified,
created, or deleted anything outside the task's stated scope:

1. Stop the session before it does anything else.
2. Run `git status` and `git diff --stat` to see the full extent of the
   change, not just the file you noticed first.
3. Revert everything outside the approved scope; keep only the intended
   change, and only after confirming it is actually wanted.
4. Do not open a PR from a working tree that still has unreviewed
   out-of-scope changes in it.
5. Record what happened as a lesson: tighten the permission boundary for
   next time (working directory, tool access, or session lifetime) rather
   than trusting the same broad grant again.

## Worked Example: Safe Task Boundary Vs Unsafe Task Boundary

**Safe:** "Using only the public candidate report at
`data/research/candidates.json` and the official Hermes Agent docs, draft a
Markdown outline for a new guide section. Read-only access to that one file.
No shell access, no write access, no memory carried in from other tasks.
Return the outline as chat output; do not write it to any file." This stays
inside a bounded read set, produces a draft artifact instead of a commit, and
leaves the actual file write to a Git-first agent after human review.

**Unsafe:** "Look through the repository, figure out what documentation
needs updating, and commit whatever you think is best." This grants
unbounded read scope, unbounded write scope, no success criterion, and no
review gate. It is exactly the shape of task that produces unexpected file
edits, scope creep, and unreviewable diffs. Even if the resulting docs look
reasonable, this pattern must be rejected regardless of output quality: the
process, not just the result, has to be reviewable.

## Public-Safe Automation Pattern

| Stage | Rule |
| --- | --- |
| Discovery | Cheap metadata scout only; no Hermes Agent required. |
| Drafting | Manual workflow only. |
| Review | Human reads diff and source labels. |
| Merge | Checks pass; maintainer approves. |

## Red Flags

- An automation can commit without a PR.
- A guide includes real provider keys or OAuth files.
- A generated doc cites private memory.
- A scheduled task publishes daily without human review.
- A source is leak-derived but copied verbatim.

## Pre-Publish Checklist

- [ ] `git status` shows only expected public files.
- [ ] No local Hermes state is tracked.
- [ ] No provider keys or OAuth files appear.
- [ ] Commands are verified or placeholders.
- [ ] Source status and license notes are present.
- [ ] Dry-run output was reviewed before PR creation.
- [ ] Repository checks passed.

## Private State Inventory

Treat these as private by default:

| State | Why it is risky |
| --- | --- |
| Memory | May contain private conversations, preferences, source summaries, or personal context. |
| Provider config | May include credentials, endpoints, accounts, or billing-related setup. |
| OAuth files | Can grant account access. |
| Logs | May include prompts, paths, tool calls, and errors with private details. |
| Scheduled tasks | Can publish or run repeatedly without fresh review. |
| Local skills | May contain private procedures or machine-specific paths. |

## Public-Safe Review Procedure

1. Run `git status --short --branch`.
2. Confirm changed files are expected public docs, prompts, or tests.
3. Search for provider keys, OAuth terms, private paths, and token-looking
   strings.
4. Confirm Hermes Agent output was treated as draft material.
5. Confirm source links are public and source status is labeled.
6. Run repository checks.
7. Open a PR for human review.

## Incident Response

If private Hermes Agent state is committed:

1. Stop publishing or merging.
2. Remove the file in a new fix commit or follow the repository's secret
   removal process if a real secret was exposed.
3. Rotate any exposed provider token or OAuth credential.
4. Review logs and generated files for additional exposure.
5. Add a test or checklist item if the incident reveals a missing guard.

## Automation Boundary

Hermes Agent can be useful for local personal workflows. In this public
repository, automation must remain reviewable:

- No direct push to `main`.
- No automatic release publication.
- No unattended guide writing from private memory.
- No scheduled workflow that requires provider secrets in GitHub Actions.
- No generated guide content merged without human review.
