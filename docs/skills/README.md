# AI Skills And Prompt Guides

This folder collects public-safe guide patterns for agent skills, prompt
guides, and tool-use workflows. It is for general readers, so every guide
should be clear about prerequisites, safety boundaries, failure modes,
verification, and source status.

## Guide Map

| Guide | Use it for |
| --- | --- |
| [Claude Code skills](claude-code.md) | Understanding Claude Code skill structure, the `.claude/commands/` custom-command model, and safety checks. |
| [Codex skills](codex.md) | Creating public-safe Codex skills, understanding `AGENTS.md`'s role, and skill-like repo workflows. |
| [MCP tool-use systems](mcp.md) | Connecting tools through MCP without overexposing private data, with a pre-connection audit checklist. |
| [Prompt guides](prompt-guides.md) | Writing reusable prompts as a skill-equivalent asset, with evaluation and revision criteria. |

## What Counts As A "Skill" In Each Tool

The word "skill" means different things depending on the tool. Getting this
straight up front avoids describing behavior a tool does not actually have.

| Tool | Native skill concept | Reuse mechanism this repo relies on | Where it lives |
| --- | --- | --- | --- |
| Claude Code | Skills (instruction bundles with `SKILL.md`, optional scripts/references) that Claude loads when relevant. | Skills, plus user-defined custom slash commands under `.claude/commands/` (custom commands are **not** a built-in feature -- you author them). | `SKILL.md` bundles; `.claude/commands/*.md` for custom commands. |
| Codex | Skills (task-specific instruction/resource bundles) plus `AGENTS.md` for always-on repo rules. | Skills for repeatable procedures; `AGENTS.md` for standing constraints every session should read. | `.agents/skills/<slug>/SKILL.md`; `AGENTS.md` at repo root; `.github/codex/prompts/` in this repo for reusable prompt files. |
| Hermes Agent | Skills (`SKILL.md` bundles), external skill directories, bundles, and hub/tap installs. | Local skills, GitHub/tap/direct-URL installs, or an external directory such as `.agent-skills/hermes` configured in `skills.external_dirs`. | `~/.hermes/skills/<slug>/SKILL.md` for local user skills; `skills/<slug>/SKILL.md` in a GitHub tap; `.agent-skills/hermes/<slug>/SKILL.md` for this repo's project staging path. |
| MCP clients (any tool) | No "skill" concept -- MCP is a protocol for exposing tools, resources, and prompts to a client. | A connected MCP server's tools/resources act like an extension, but reuse and packaging depend on the client, not MCP itself. | Client-specific MCP config; server-specific docs. |
| Tools without a native skill system | None. | This repo's own prompt guides and prompt templates, used as a manually-pasted skill-equivalent. | [prompt-guides.md](prompt-guides.md), `prompts/` at repo root. |

The common thread: a skill is a reusable, documented procedure with a clear
trigger, clear boundaries, and a way to verify it worked. Whether the tool
has a native mechanism for that (Claude Code, Codex, Hermes Agent) or not
(most other tools, and MCP itself) changes only how you package it, not the
underlying discipline in the "Quality Bar" section below.

## Source And Status Handling

Every public skill guide should identify where its claims come from. Use
these labels in the guide body or final report:

| Status | Use when | Required wording |
| --- | --- | --- |
| Official-doc verified | The behavior, command, path, or packaging rule was checked in official docs during the current change. | Link the source and keep the claim narrow. |
| Official-doc anchored | The guide links to official docs, but the current command or product behavior was not rechecked in this change. | Say "verify in official docs before publishing exact setup details." |
| Repo-local convention | The behavior is a pattern this repository uses, not a product feature. | Say it is repo-local or user-authored, especially for custom commands like `/goal`. |
| Community example | The source is a blog, forum, video, issue, or sample repo. | Treat it as inspiration, not authority. |
| Private/local-only | The source is a user's private skill folder, memory, config, or chat. | Do not publish it; replace with a public-safe placeholder or omit it. |

This distinction matters because "skill" is an overloaded word. A custom
Markdown shortcut, a native skill bundle, an MCP server, and a reusable prompt
can all improve an agent workflow, but they have different security and
packaging rules.

## Role Boundaries

| Asset | Good role | Bad role |
| --- | --- | --- |
| Native skill | Encodes a repeated, bounded procedure with references and optional helper scripts. | Becomes a catch-all instruction set that silently edits broad parts of the repo. |
| Custom slash command | Saves a reusable prompt for a human-invoked task. | Pretends to be a built-in product feature or silently commits/pushes. |
| Prompt guide | Teaches a human how to fill and run a prompt manually. | Makes undocumented claims about tool internals or encourages copy-paste of secrets. |
| MCP tool connection | Exposes a specific tool/resource through a client after a permission audit. | Grants broad access to private files, accounts, or destructive actions by default. |
| Repository automation | Runs cheap, scoped checks or metadata preparation. | Runs paid LLM generation, publishes guide content, or modifies protected docs without review. |

Keep these boundaries visible in every guide so a beginner can tell whether
they are reading about a product feature, a local convention, or a reusable
workflow pattern.

## Quality Bar

Every generated guide should include:

- What the tool, skill, or resource is.
- Beginner friendliness.
- Public-safe use cases.
- Installation commands only when verified.
- Placeholder commands when not verified.
- Windows-friendly notes.
- Linux/macOS notes when useful.
- API key or subscription requirements.
- Hardware requirements where relevant.
- Whether it is realistic for entry-level hardware.
- Safer lightweight alternatives.
- Failure modes.
- Evaluation checklist.
- Links/source references.
- License/source status.
- Clear role boundaries: what the skill may do, what the human must do, and
  what is forbidden.
- Evidence requirements: files changed, commands run, checks run, and claims
  left for manual verification.
- A rollback or disable path for anything persistent.

## Beginner Workflow

Beginners should learn skills in increasing order of risk:

1. **Read a prompt guide.** Understand the task, inputs, boundaries, and final
   report before adding any tool integration.
2. **Run a read-only prompt.** Ask the agent to review or explain public docs
   without editing.
3. **Create a tiny custom command or prompt shortcut.** Keep it one Markdown
   file, no scripts, no secrets, no commits.
4. **Draft a native skill.** Add `SKILL.md` only; describe trigger, scope,
   forbidden actions, and verification.
5. **Add references or scripts only when needed.** Prefer public-safe
   references and standard-library helper scripts that are easy to audit.
6. **Test on a fixture or scratch branch.** Confirm the agent reads the right
   files, stays in scope, and reports evidence.
7. **Review before reuse.** Treat a skill as living documentation; update or
   disable it when product behavior changes.

Do not start with a broad write-capable skill. If a beginner cannot explain
what the skill is allowed to touch, the skill is not ready to run.

## Task Decomposition For Skill Design

Break skill work into small reviewable pieces:

| Step | Output | Review question |
| --- | --- | --- |
| Task intake | One-sentence goal and target audience. | Is this recurring enough to deserve a skill? |
| Trigger design | Clear trigger and non-trigger cases. | Will the agent load it only when relevant? |
| Scope | Allowed files, forbidden files, allowed commands, forbidden commands. | Can it avoid secrets and unrelated edits? |
| Procedure | Ordered steps with read-before-edit gates. | Does it inspect context before acting? |
| Evidence | Required final report fields and checks. | Can a reviewer verify what happened? |
| Failure handling | Stop conditions and escalation rules. | Will it stop instead of guessing or overreaching? |
| Maintenance | Official-doc review points and disable path. | Can maintainers keep it current safely? |

## Public-Safe Defaults

- Start with read-only examples.
- Keep secrets out of the repository.
- Do not copy private skill folders or private prompt packs.
- Use branch, PR, checks, review, and merge for generated updates.
- Mark fast-changing product behavior as an official-doc verification item.

## Skill Lifecycle

| Phase | Output | Review gate |
| --- | --- | --- |
| Idea | Short description of the repeated task. | Is this frequent enough to deserve a skill or guide? |
| Scope | Allowed files, forbidden files, tools, and commands. | Does the skill avoid secrets, private paths, and destructive actions? |
| Draft | `SKILL.md`, prompt guide, or tool-use instructions. | Does it include trigger, purpose, steps, failure cases, and verification? |
| Read-only test | Agent explains or reviews without editing. | Does it trigger at the right time and stay bounded? |
| Write-capable test | Agent edits a small fixture or docs page. | Are diffs scoped and checks run? |
| Package/release | Guide is linked and included where appropriate. | Are source status and changelog updated? |
| Maintenance | Periodic review against official docs and local checks. | Are stale commands removed or marked for verification? |

## Skill Anatomy Checklist

For a native skill bundle, the `SKILL.md` should answer:

- **Trigger:** When should the agent use this skill, and when should it not?
- **Purpose:** What task does it make safer or more repeatable?
- **Inputs:** What must the user provide before the skill can act?
- **Scope:** Which files, tools, commands, accounts, or external sources are
  allowed?
- **Forbidden actions:** What must never be read, changed, published, or
  automated?
- **Procedure:** What steps happen before editing, during editing, and after
  editing?
- **Verification:** What checks or manual evidence prove the result?
- **Failure cases:** When should the agent stop and ask instead of continuing?
- **Final report:** What must be reported so a human can review the work?
- **Disable path:** How does a maintainer turn the skill off or remove it?

For a prompt guide, use the same questions, but package the answers as a
copyable prompt instead of a skill bundle.

## Skill Or Prompt Guide Decision

Use a skill when:

- The same task recurs often.
- The agent needs a consistent procedure.
- References or helper scripts are useful.
- The workflow has non-obvious safety boundaries.

Use a prompt guide when:

- The task is occasional.
- The user should read and adapt the prompt manually.
- A single Markdown template is enough.
- Current product behavior is changing too quickly for a bundled skill.

Use normal documentation when:

- The material is mostly explanation.
- There is no agent action to repeat.
- The safest output is a checklist or review guide.

## Public Example Rules

Public examples should use:

- Placeholder paths such as `docs/example.md`.
- Placeholder tokens such as `<API_TOKEN>` only in explanatory text.
- Public-safe repository tasks.
- Read-only first runs.
- Checks that exist in this repository.
- Conservative product claims with official-doc verification notes.

Public examples should not use:

- Real private paths.
- Private memories.
- Hidden prompts.
- Browser profile data.
- Screenshots with account details.
- Commands that publish, delete, or spend money.

## Review Checklist

- [ ] The guide says when to use the skill and when not to use it.
- [ ] Source status is clear.
- [ ] Install/setup commands are official-doc verified or marked as
      placeholders.
- [ ] Safety boundaries are concrete.
- [ ] Failure modes are listed.
- [ ] Verification commands are present.
- [ ] The final report format is reviewable.
- [ ] The guide links back to prompt templates, Prompting OS, or workflow
      docs.
- [ ] Native product behavior is distinguished from repository-local
      conventions.
- [ ] The guide explains who approves edits, who runs checks, and who may
      publish.
- [ ] It includes stop conditions for ambiguous scope, private data, missing
      official docs, dependency changes, or destructive actions.
- [ ] It records enough evidence for another maintainer to reproduce or audit
      the result.

## Review Rubric

| Area | Strong guide | Needs revision |
| --- | --- | --- |
| Trigger | Narrow, example-driven, with non-trigger cases. | Vague "use for all docs/code/research" wording. |
| Scope | Names allowed and forbidden files/actions. | Leaves the agent to infer what it may edit. |
| Source status | Labels official, community, repo-local, and private sources. | Treats product behavior or private examples as universal fact. |
| Beginner clarity | Uses short workflows, tables, and concrete examples. | Assumes the reader already knows agent packaging, permissions, or Git review. |
| Safety | Starts read-only where practical and forbids secrets/destructive actions. | Encourages broad tool access, auto-merge, or silent publishing. |
| Verification | Requires commands, evidence, and claims needing manual verification. | Ends with a vague "done" report. |
| Maintenance | Has a disable path and stale-claim handling. | Gives no way to retire or refresh the skill. |

## Evidence Package For Skill Changes

When a PR changes skill docs or prompt templates, the final report should
include:

- Which files were changed.
- Whether the change describes a native feature, repo-local convention, or
  manual prompt pattern.
- Official docs checked, or claims deliberately marked for official-doc
  verification.
- Checks run in this repository.
- Any command examples that are placeholders rather than verified commands.
- Any rejected source or example because it was private, unsafe, or out of
  scope.

## Common Failure Modes

| Failure | Why it happens | Safer response |
| --- | --- | --- |
| Skill triggers on too many tasks | The description is broad or aspirational. | Add concrete trigger and non-trigger examples. |
| Skill edits unrelated files | Scope and allowed paths are missing. | Add allowed/forbidden files and a stop condition for unclear scope. |
| Private example leaks into docs | A local skill, memory, or command was copied directly. | Replace with placeholders and public-safe examples. |
| Custom command is described as built-in | Repo-local convention was confused with product behavior. | Label it user-authored and link to official docs only for the mechanism. |
| MCP access is overbroad | Tool permissions were treated as implementation detail. | Add a pre-connection audit and least-privilege boundaries. |
| Verification is skipped | The guide lacks evidence requirements. | Require files changed, commands run, checks run, and unresolved claims. |

## How This Maps To Repository Automation

The skill docs in this folder are read by humans deciding how to work with an
agent. They are not consumed by CI. Repository Autopilot and the safe
automerge workflow never generate or edit files in `docs/skills/`; any change
here goes through the normal local-agent, branch, PR, checks, and human
review path described in
[repository-autopilot.md](../automation/repository-autopilot.md) and
[safe-automerge-policy.md](../automation/safe-automerge-policy.md).
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `docs/skills/README.md` as a contract-bearing artifact
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
