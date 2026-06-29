# Hermes Agent Public Repository Safety

Hermes Agent can hold private memory, provider credentials, OAuth state,
sessions, logs, skills, and scheduled automations. Treat that local state as
private unless you have deliberately created a public-safe example.

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
