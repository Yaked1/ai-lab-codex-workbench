# Nous Research Hermes Agent

Source status: official-doc anchored. Verify current behavior in the official
Hermes Agent docs before publishing exact setup details.

Source links:

- Official docs: <https://hermes-agent.nousresearch.com/docs/>
- Official repository: <https://github.com/NousResearch/hermes-agent>
- License/source status: official repository, MIT license. Verify the current
  license before adapting examples.

## Source And Verification Status

Use Hermes Agent docs only after separating source types:

| Source type | Public guide status | Example handling |
| --- | --- | --- |
| Official Hermes Agent docs or repository | Preferred source. | Link it, summarize narrowly, and recheck current setup or behavior before publishing exact commands. |
| Provider documentation | Required for provider-specific behavior. | Say "verify in the provider and Hermes Agent docs" instead of treating one provider as universal. |
| Community examples | Context only. | Use for ideas, then verify against official docs before teaching. |
| Local memory, logs, or private notes | Not a publishable source. | Keep private; do not copy into this repository. |
| Hermes language-model material | Out of scope for this page. | Do not include model-card, benchmark, quantization, local-serving, GGUF, Ollama, vLLM, SGLang, or fine-tuning content. |

When a maintainer has not freshly checked the official docs, write with
"official-doc anchored" language. For example: "Hermes Agent supports
provider configuration; verify the current configuration fields in the
official docs before publishing exact examples."

## What Hermes Agent Is

Hermes Agent is an autonomous agent workflow tool from Nous Research. It can run
as a command-line or desktop-oriented agent, use tools, maintain persistent
context, use skills, and run scheduled or event-driven workflows when configured.

Hermes Agent is different from a normal chatbot because it is designed around
ongoing agent work: tool use, sessions, provider configuration, memory, skills,
and automations. A chatbot is usually a single conversation surface; Hermes
Agent can be configured as a longer-running agent workspace that persists
context and state between sessions.

This guide treats Hermes Agent as an agent/workflow tool only. It does not
cover the Hermes language-model family, model cards, performance
measurements, model file formats, or local model-serving stacks. If a claim
would require any of that, this guide marks it "verify in official Hermes
Agent docs" instead of describing it.

## What Hermes Agent Is For

At its core, Hermes Agent gives you a persistent agent workspace that:

- Calls a configured backend provider to generate responses and plan actions.
- Uses tools (file access, shell commands, gateways) subject to whatever
  permissions the current setup grants.
- Keeps memory across sessions so it does not start from zero every time.
- Loads skills: reusable task instructions it can apply without you re-writing
  them each time.
- Can run scheduled or event-driven jobs (cron-style automations) once you
  configure them.

That combination — memory, skills, and scheduling, on top of tool use — is
what separates an "agent workflow tool" from a single-turn assistant. It is
also exactly why it carries more setup responsibility: persistent state and
unattended jobs are places where private information or runaway cost can
accumulate quietly if you do not review them.

## What Hermes Agent Is Not For In This Repository

This repository is public and beginner-focused, so Hermes Agent has a
conservative role here. Do not use this page to:

- Teach or compare Hermes language models.
- Recommend local model-serving stacks or quantization formats.
- Publish provider credentials, memory files, logs, or browser/OAuth state.
- Present scheduled generation as a replacement for review.
- Describe exact current pricing, model availability, or provider limits
  unless the official docs were checked during the same change and the
  verification date is recorded.

If a reader asks for any of those, redirect them to official product docs or a
separate private experiment. Do not fold the material into this public guide.

## Hermes Agent's Role In This Repo's Own Workflow

This repository already documents two other agent/workflow surfaces: Codex and
Claude Code (see [docs/tools/comparison-matrix.md](../tools/comparison-matrix.md)
for the full comparison). Hermes Agent is documented here as a third option,
not as a replacement for either.

Concretely, in this repository's own workflow:

- Codex and Claude Code are the tools that actually edit repository files,
  run local checks, and prepare pull requests. They are Git-first: branch,
  edit, check, PR, review, merge.
- Hermes Agent is documented as a personal/local agent workspace. It is useful
  for organizing public research candidates, drafting outlines, and running
  your own scheduled reminders — but it is not wired into this repository's
  automation as a publisher. See
  [Public Repository Workflow](#public-repository-workflow) below.
- None of the three tools may push directly to `main` or publish generated
  guide content without a human reviewing the diff first.

## Role Boundaries In A Safe Workflow

| Task | Hermes Agent role | Human or Git-first agent role |
| --- | --- | --- |
| Public source triage | Summarize public candidate links and label source quality. | Decide whether the source belongs in the repo. |
| Documentation planning | Draft an outline, checklist, or risk list. | Turn the plan into a scoped branch and reviewable diff. |
| Skill/memory design | Suggest a private local procedure and safety gates. | Keep private memory out of Git and decide what becomes public docs. |
| Scheduled reminders | Remind the maintainer to review public candidates. | Approve, edit, test, and merge any resulting docs. |
| Repository editing | Not the default tool for this repo. | Codex or Claude Code edits files, runs checks, and prepares PR notes. |

This boundary prevents persistent state from quietly becoming public source
material. Hermes Agent can help prepare work; it should not be the final
authority for public repository changes.

## When To Reach For Hermes Agent Vs Codex Or Claude Code

Use Hermes Agent when:

- You want an ongoing personal agent workspace with memory that persists
  across many small tasks, not just one editing session.
- You want to experiment with skills or scheduled automations for your own
  workflow (research triage, reminders, drafting) outside of a Git repo.
- You are comfortable keeping the resulting local state (memory, provider
  config, logs) private and separate from anything you commit.

Use Codex or Claude Code instead when:

- The task is "edit files in this repository and prepare a reviewable diff."
  Both are Git-first and this repository's checks, branch rules, and PR
  workflow are built around that shape.
- You need a tool whose output is expected to be committed. Hermes Agent's
  strength (persistent private state) is the opposite of what a public-repo
  edit needs (a clean, reviewable, stateless diff).
- You want the narrowest blast radius for a single documentation edit. A
  short-lived Codex or Claude Code session with no memory carried into the
  next task is easier to review than a long-running agent workspace.

If you are not sure which to use for a given task, default to Codex or Claude
Code for anything that touches this repository, and reserve Hermes Agent for
personal, non-repository workflows until you have read
[public-repo-safety.md](public-repo-safety.md) end to end.

## Beginner Workflow: From First Use To A Reviewed Doc Idea

Start with the least risky version of the workflow and only add permissions
after each stage is understood.

1. **Read-only public task:** Ask Hermes Agent to summarize one public page
   you already selected. Check whether it cites the page, avoids private
   assumptions, and marks unknowns.
2. **Source ledger:** Ask it to list source title, URL, publisher/source
   status, license/status if visible, and claims needing official-doc
   verification. Do not ask it to write repository docs yet.
3. **Outline draft:** Ask for a beginner outline with safety warnings,
   failure modes, and verification steps. Treat the result as a private
   draft.
4. **Human filter:** Remove anything based on memory, private context,
   unsupported product claims, or out-of-scope Hermes model content.
5. **Git-first edit:** Use Codex or Claude Code to make the actual repository
   change in a branch, with AGENTS.md rules, checks, and PR review.

This path gives beginners a visible trail from public source to reviewed
documentation without trusting hidden memory or unattended automation.

## Task Decomposition Template

Use this mini-template when asking Hermes Agent for help with public-safe
planning:

```text
Goal:
Draft a private plan for [public documentation topic].

Allowed sources:
- Public URLs I provide.
- Official docs linked in the task.

Forbidden sources:
- Private memory.
- Browser sessions.
- Credentials, logs, private chats, private file paths.
- Hermes language-model, quantization, benchmark, or local-serving material.

Deliver:
- Source ledger with status labels.
- Beginner workflow outline.
- Safety boundaries.
- Failure modes.
- Claims needing official-doc verification.
- Suggested verification evidence for a later PR.

Do not edit repository files or publish anything.
```

The output should be a planning artifact. A separate Git-first agent or human
maintainer performs the edit and verification.

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

## Review Rubric

Before accepting Hermes Agent output as input to a docs change, review it with
this rubric.

| Area | Question | Reject or revise when |
| --- | --- | --- |
| Scope | Is every section about Hermes Agent as a workflow tool? | It discusses Hermes models, serving stacks, model files, quantization, benchmarks, or fine-tuning. |
| Source ledger | Are public sources labeled official/community/local/unknown? | Claims appear without source status. |
| Current behavior | Are setup, provider, platform, pricing, and availability claims marked for official-doc verification? | The draft asserts exact current behavior without a fresh source. |
| Privacy | Does the output avoid secrets, private paths, memory, logs, and account data? | It asks to copy local config, logs, or private memory into docs. |
| Automation | Does scheduled work remain local/private and manually reviewed? | It suggests auto-publishing, auto-committing, or auto-merging generated content. |
| Evidence | Can a reviewer see what was checked and what was not? | The draft has no commands, sources, or unresolved-risk list. |

## Verification Evidence For A Hermes-Informed Docs PR

When a docs PR was informed by Hermes Agent planning, the final report should
still come from the Git-first editing tool or the maintainer. Include:

- The public sources used.
- Which sources were official docs and which were not.
- Any claims left as "verify in official Hermes Agent docs."
- Files changed.
- Commands and checks run in the repository.
- Confirmation that no private memory, provider config, logs, screenshots, or
  account-specific data were copied into the docs.
- Confirmation that the change excludes Hermes language-model and local-serving
  coverage.

## First Task Recommendation

If this is your first time touching Hermes Agent, do not start with a
repository-editing task at all. Start with something disposable and read-only:
ask it to summarize a single public URL you already trust, or draft an outline
from a file you paste in, and inspect the output before you decide whether to
give it broader tool access. That gives you a feel for its behavior without
any risk to this repository. Once you have done that, move to
[local-agent-setup.md](local-agent-setup.md) for the fuller setup flow.

## Evaluation Checklist

- [ ] Is the source official, community, unofficial, or unverified?
- [ ] Are install commands verified or clearly placeholders?
- [ ] Are provider secrets excluded?
- [ ] Is memory kept private?
- [ ] Are automations manually reviewed before publishing?
- [ ] Does the guide avoid Hermes language-model coverage?
- [ ] Are exact provider, pricing, platform, or model-availability claims
      marked for official-doc verification?
- [ ] Does the output separate planning from repository editing?
- [ ] Does the final report list evidence, checks, and unresolved risks?

## Failure Modes And Responses

| Failure | Likely cause | Response |
| --- | --- | --- |
| Output includes model-card or benchmark language | The task drifted from Hermes Agent workflow into Hermes model coverage. | Remove the material and restate the scope boundary. |
| Output relies on private memory | Persistent memory was treated as source material. | Replace it with public sources or omit the claim. |
| Setup instructions look exact but were not checked | The guide copied a command or path from memory or an old source. | Mark as placeholder or verify in official docs before publishing. |
| Automation would write docs unattended | The scheduled task was not bounded to local/private output. | Require manual review, branch, checks, and PR before any publishable content. |
| Provider-specific behavior is generalized | One backend's behavior was treated as universal. | Move details behind a provider-specific verification note. |
| Troubleshooting asks for raw logs or config | Debug process may expose credentials or private paths. | Ask for redacted symptoms and configuration shape only. |
