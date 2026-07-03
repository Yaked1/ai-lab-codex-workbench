# Hermes Agent Guides

These guides cover Nous Research Hermes Agent as an agent and workflow tool for
public research, documentation, skills, memory, provider configuration, and
automations.

Scope: Hermes Agent only. This folder does not cover the Hermes language-model
family itself: model files, model cards, performance measurements, model file
formats, or local model-serving stacks. If a topic sits close to that line,
these guides say "verify in official Hermes Agent docs" instead of guessing.

Official source anchors:

- Hermes Agent docs: <https://hermes-agent.nousresearch.com/docs/>
- Hermes Agent repository: <https://github.com/NousResearch/hermes-agent>
- Repository license: MIT, as listed by the official repository and docs.
- Installation: <https://hermes-agent.nousresearch.com/docs/getting-started/installation>
- Configuration: <https://hermes-agent.nousresearch.com/docs/user-guide/configuration>
- Skills: <https://hermes-agent.nousresearch.com/docs/user-guide/features/skills>
- Memory: <https://hermes-agent.nousresearch.com/docs/user-guide/features/memory>
- Cron: <https://hermes-agent.nousresearch.com/docs/user-guide/features/cron>

Source status: official documentation and official repository. Link to these
sources and summarize conservatively rather than copying long examples. Verify
current commands, platform support, provider behavior, and pricing in the
official docs before teaching setup.

## Source And Status Labels

Use the same label style across every Hermes Agent guide so readers can tell
what has been checked and what still needs a maintainer review.

| Label | Meaning | How to write about it |
| --- | --- | --- |
| Official-doc verified | Checked against the official Hermes Agent docs or repository during the current change. | State the behavior narrowly, include the source link, and avoid copying long examples. |
| Official-doc anchored | Based on official docs or repository links, but not freshly rechecked in this change. | Use conservative wording and add "verify in official Hermes Agent docs" for commands, platform support, provider behavior, or pricing. |
| Community or third-party | From a blog, issue, forum, video, or community guide. | Treat it as context only; do not present it as product behavior. |
| Local observation | Seen in one local setup. | Mark it as environment-specific and avoid making it a general guarantee. |
| Out of scope | About Hermes language models, model files, benchmarks, quantization, local serving, or training. | Move it out of this folder or reject it unless the project scope changes explicitly. |

Public docs should prefer "official-doc anchored" over exact claims when a
maintainer has not checked the current docs during the same PR. That keeps the
guide useful without pretending that fast-changing setup details are permanent.

## Why This Folder Exists

Hermes Agent is one of three agent/workflow surfaces this repository discusses
(the other two are Codex and Claude Code). This folder exists so a reader can
evaluate Hermes Agent, wire it up safely, and know exactly where the public
repository draws the line between "useful local tool" and "thing that must
never touch this Git history." Every guide below assumes the reader already
has, or is about to get, a working Hermes Agent install and wants to use it
without leaking private state into a public repository.

## Role Boundaries

Hermes Agent can be useful in a local workflow, but this repository assigns it
a narrow public role.

| Role | Hermes Agent may do | Hermes Agent must not do |
| --- | --- | --- |
| Research assistant | Organize public source candidates, summarize public pages, draft private notes for maintainer review. | Treat private memory, private chats, browser state, or hidden prompts as publishable sources. |
| Planning assistant | Break a public documentation task into reviewable steps and risks. | Push edits directly to `main`, approve its own output, or bypass pull request review. |
| Automation assistant | Run private/local reminders or scheduled drafts after explicit setup. | Auto-publish guide content, run paid or provider-heavy jobs unattended, or require `OPENAI_API_KEY` in GitHub Actions. |
| Documentation subject | Be documented as an agent/workflow tool with skills, memory, providers, and scheduling. | Be used as an entry point for Hermes language-model, quantization, GGUF, Ollama, vLLM, SGLang, benchmark, or model-card coverage. |

If a proposed guide cannot fit one of the "may do" columns, it probably
belongs outside this folder.

## Beginner Workflow

For a first Hermes Agent learning path, keep the work read-only until the
reader has proved the setup, provider configuration, and safety boundaries.

1. Read this README and [Hermes Agent](hermes-agent.md) to confirm the topic
   is Hermes Agent workflow, not Hermes model coverage.
2. Read [Local agent setup](local-agent-setup.md) and verify current commands
   in the official docs before running them.
3. Configure the provider outside this repository, using placeholders in docs
   and environment-specific secret storage locally.
4. Run one disposable read-only task against public material, then inspect the
   output for source handling, overconfident claims, and private-state leakage.
5. Only after the read-only task is clean, try a bounded local planning task:
   outline a docs PR, list risks, or draft a checklist.
6. Use Codex or Claude Code for actual repository edits, then run checks and
   open a reviewed pull request.

This sequence is intentionally slower than "install and automate everything."
It teaches the failure modes before any persistent memory or scheduling can
affect a public repository.

## Task Decomposition Pattern

When writing or reviewing Hermes Agent guidance, decompose work into visible
stages instead of one broad "use the agent" instruction.

| Stage | Output | Review question |
| --- | --- | --- |
| Intake | Goal, reader, allowed files, forbidden files, source status. | Is the task public-safe and inside Hermes Agent scope? |
| Source check | Official links, community links, local observations, unknowns. | Are fast-changing claims marked for official-doc verification? |
| Plan | Small steps, tool permissions, memory/scheduling decisions. | Can a beginner see what happens before any write or automation? |
| Draft | Private outline, checklist, or proposed wording. | Does the draft avoid secrets, private paths, and model-serving scope? |
| Review | Rubric results, evidence, unresolved claims. | Can a maintainer audit the output without trusting hidden state? |
| Publish path | Branch, PR, checks, human review. | Is Hermes Agent output treated as input to review, not final authority? |

## Guide Map

| Guide | One-line description |
| --- | --- |
| [Hermes Agent](hermes-agent.md) | What Hermes Agent is for, how it differs from a chatbot, and when to reach for it instead of Codex or Claude Code. |
| [Local agent setup](local-agent-setup.md) | Step-by-step conceptual install-to-first-task flow with a "what could go wrong" callout per step. |
| [Provider configuration](provider-configuration.md) | What a provider is, why credentials must never enter this repo, and how to verify one is wired correctly. |
| [Skills, memory, automations](skills-memory-automations.md) | Safety model for persistent memory and scheduled jobs: what to automate, what needs review every run. |
| [Prompting Hermes Agent](prompting-hermes-agent.md) | Work-order-style example prompts (goal, scope, verification, failure behavior) for public-safe tasks. |
| [Hermes Agent vs Codex vs Claude Code](hermes-agent-vs-codex-vs-claude-code.md) | Comparison table: strengths, typical use case, safety posture, and repo fit for each tool. |
| [Public repo safety](public-repo-safety.md) | Hermes-specific pre-publish checklist for memory and automation output; general safety lives elsewhere. |
| [Troubleshooting](troubleshooting.md) | Symptom, likely cause, and response tables for install, provider, memory, and automation failures. |

## Suggested Reading Order

Pick the path that matches what you are trying to do. Each path is short by
design; read only what you need.

### (a) First-time setup

1. [Hermes Agent](hermes-agent.md) — confirm this is the right tool before installing anything.
2. [Local agent setup](local-agent-setup.md) — install, configure, verify, run a first task.
3. [Provider configuration](provider-configuration.md) — wire up the backend the agent actually calls.
4. [Public repo safety](public-repo-safety.md) — know the boundaries before your first real task touches this repo.

### (b) Automation and scheduling use

1. [Skills, memory, automations](skills-memory-automations.md) — the safety model for anything unattended.
2. [Provider configuration](provider-configuration.md) — pin provider/model choices before a job runs without you watching.
3. [Public repo safety](public-repo-safety.md) — the pre-publish checklist for automation output specifically.
4. [Troubleshooting](troubleshooting.md) — automation failure table, read before your first scheduled job, not after.

### (c) Troubleshooting

1. [Troubleshooting](troubleshooting.md) — start here; it is organized by symptom.
2. [Provider configuration](provider-configuration.md) — most "it stopped working" reports trace back to provider config.
3. [Local agent setup](local-agent-setup.md) — re-check the setup steps if the failure looks install-related.
4. [Public repo safety](public-repo-safety.md) — if the failure involved something being committed, follow the incident response steps here.

## Research Loop Role

The daily research scout may discover Hermes Agent updates, but it must not run
Hermes Agent automatically. Curator prompt prep may prepare a local Codex prompt,
but Hermes Agent documentation updates still happen through local/manual editing
and a reviewed pull request.

## Reader Paths

| Reader | Path |
| --- | --- |
| Beginner evaluating Hermes Agent | Read this README, then `hermes-agent.md`, then `public-repo-safety.md`. |
| Maintainer writing setup docs | Read `local-agent-setup.md`, `provider-configuration.md`, and verify official docs. |
| Prompt author | Read `prompting-hermes-agent.md` and adapt the public-safe prompt template. |
| Automation reviewer | Read `skills-memory-automations.md`, `public-repo-safety.md`, and `troubleshooting.md`. |
| Tool comparison reader | Read `hermes-agent-vs-codex-vs-claude-code.md` and avoid model comparisons. |

## Hard Scope Boundary

This folder covers Hermes Agent as a workflow tool:

- public research organization
- provider configuration safety
- skills
- memory
- scheduled work
- public repository documentation workflows

This folder does not cover:

- the Hermes language-model family itself
- model cards
- performance or capability measurements
- model file formats or conversion pipelines
- third-party local model-serving stacks
- training or fine-tuning

If a future contribution adds model-serving material here, move it out or
reject it unless the project scope changes explicitly. When in doubt, leave the
claim out and mark it "verify in official Hermes Agent docs."

## Verification Standard

Before updating Hermes Agent docs:

- Check official docs for installation, configuration, skills, memory, and cron
  behavior.
- Use placeholders for commands not verified in the current change.
- Keep provider credentials out of examples.
- Run repository checks.
- Update changelog when the public guide changes.
- Mark pricing, provider behavior, and platform support as official-doc
  verification items.

## Review Rubric For Hermes Agent Docs

Use this rubric before merging changes in this folder.

| Area | Accept | Needs work |
| --- | --- | --- |
| Scope | The guide clearly covers Hermes Agent workflow only. | It drifts into Hermes language models, benchmarks, quantization, local serving, or training. |
| Source status | Official links and verification status are visible. | Product behavior is asserted without a source or verification note. |
| Beginner path | Read-only first steps and safety gates are explained. | The guide jumps straight to automation or repository writes. |
| Secrets | Credentials, provider config, memory, logs, and private files stay outside Git. | Examples include real-looking tokens, private paths, account identifiers, or browser/OAuth state. |
| Automation | Scheduled work is opt-in, bounded, and manually reviewed before publishing. | The guide suggests auto-publishing, auto-merging, or running provider-heavy jobs unattended. |
| Evidence | The final report asks for files changed, commands run, checks, sources, and unresolved verification items. | The reader cannot tell what was verified or what remains uncertain. |

## Evidence To Capture

For any Hermes Agent documentation update, the PR or final report should
include:

- Files changed in this folder.
- Official docs or repository pages checked, with the date of review when the
  change depends on current behavior.
- Claims deliberately marked "verify in official Hermes Agent docs."
- Commands run, or a plain statement that no command verification was run.
- Checks run for this repository.
- Any source that was rejected because it was community-only, private,
  copied, leaked, or out of scope.

## Public-Safe Example Boundary

Safe examples:

- Public candidate report review.
- Public source ledger creation.
- Drafting a guide outline for PR review.
- Read-only explanation of a public repository folder.

Unsafe examples:

- Using private memory as source material.
- Publishing a scheduled daily guide update automatically.
- Committing provider config.
- Copying prompt dumps.
- Reading browser sessions or OAuth state.

## Common Failure Modes

| Failure mode | Why it matters | Safe response |
| --- | --- | --- |
| Hermes Agent guide starts discussing Hermes models | It confuses workflow tooling with model coverage and violates this folder's scope. | Remove the material or move it to a separate task only if the project scope changes. |
| Install command is stale | Tool setup changes quickly. | Replace exact command text with official-doc verification language until rechecked. |
| Memory output is treated as source material | Persistent memory may include private or outdated context. | Require public sources and mark memory as private local context only. |
| Scheduled job writes publishable docs | Unattended generation can leak data or publish unchecked claims. | Keep scheduled work local/private and require human PR review. |
| Provider behavior is asserted as universal | Provider features, pricing, and limits change. | State that behavior must be verified in the provider and Hermes Agent docs. |
| Troubleshooting steps request secrets | Debug logs can expose tokens, keys, account IDs, or private paths. | Ask for redacted symptoms and configuration shape, never raw credentials. |

## How This Folder Relates To The Rest Of The Repo

- General public-repository hygiene lives in
  [docs/workflows/public-repo-safety.md](../workflows/public-repo-safety.md).
  `public-repo-safety.md` in this folder adds Hermes-specific items on top of
  that baseline instead of repeating it.
- The overall tool comparison lives in
  [docs/tools/comparison-matrix.md](../tools/comparison-matrix.md);
  `hermes-agent-vs-codex-vs-claude-code.md` here goes deeper on the same three
  tools from a workflow-fit angle.
- Agent task lifecycle guidance (branch, PR, checks, review, merge) lives in
  [docs/workflows/agent-task-lifecycle.md](../workflows/agent-task-lifecycle.md)
  and applies to Hermes Agent output exactly as it applies to Codex or Claude
  Code output.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **Hermes Agent guide** surface. During broad
maintenance, reviewers should treat `docs/hermes/README.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `README` state what decision, workflow, or reusable behavior it supports?
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
