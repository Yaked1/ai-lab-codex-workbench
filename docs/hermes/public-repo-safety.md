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
