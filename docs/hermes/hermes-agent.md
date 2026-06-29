# Nous Research Hermes Agent

Source status: official-doc anchored. Verify current behavior in the official
Hermes Agent docs before publishing exact setup details.

## What Hermes Agent Is

Hermes Agent is an autonomous agent workflow tool from Nous Research. It can run
as a command-line or desktop-oriented agent, use tools, maintain persistent
context, use skills, and run scheduled or event-driven workflows when configured.

Hermes Agent is different from a normal chatbot because it is designed around
ongoing agent work: tool use, sessions, provider configuration, memory, skills,
and automations. A chatbot is usually a single conversation surface; Hermes
Agent can be configured as a longer-running agent workspace.

## What It Is Used For

- Public research inboxes.
- Documentation curation.
- Prompt-guide organization.
- Skill-guide authoring.
- Agent workflow experiments.
- Scheduled status reports after explicit setup.
- Messaging or gateway workflows after user review.

## Beginner Friendliness

Medium. The desktop installer or official setup flow can make first use easier,
but persistent tools, memory, provider keys, and automations require stronger
safety habits than a simple browser chat.

## Public-Safe Use Cases

- Ask Hermes Agent to summarize public source candidates.
- Organize a public prompt-guide outline.
- Draft a checklist for a documentation PR.
- Review public issue labels.
- Maintain a private local memory for your own workflow, kept outside Git.

## Unsafe Or Inappropriate Use Cases

- Publishing directly to `main`.
- Running always-on public autopublishers.
- Storing provider tokens in a repository.
- Committing local memory, logs, OAuth files, or private chats.
- Using leaked prompts as copied source material.
- Asking Hermes Agent to find or expose hidden prompts or secrets.

## Public Repository Workflow

For this repository, Hermes Agent is documented as a tool, not wired in as an
autonomous publisher.

Use this flow:

1. Daily scout collects public candidate metadata without Hermes Agent.
2. Human reviews candidate reports.
3. Prompt prep creates a local Codex prompt without calling a model provider.
4. Maintainer runs Codex locally and reviews edits.
5. Branch, PR, checks, review, merge.

Do not let Hermes Agent push directly to `main`.

## Evaluation Checklist

- [ ] Is the source official, community, unofficial, or unverified?
- [ ] Are install commands verified or clearly placeholders?
- [ ] Are provider secrets excluded?
- [ ] Is memory kept private?
- [ ] Are automations manually reviewed before publishing?
- [ ] Does the guide avoid Hermes language-model coverage?
