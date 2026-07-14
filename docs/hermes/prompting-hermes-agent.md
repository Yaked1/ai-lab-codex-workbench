# Prompting Hermes Agent

Use Hermes Agent prompts for public research and documentation only when the
source material is public-safe and the output will be reviewed.

## What Makes A Prompt Too Vague For This Agent

Hermes Agent holds memory and tool access across a session, so a vague
prompt does not just produce a mediocre answer the way it might in a single-
turn chatbot. It produces a session that reaches for whatever context,
memory, or tool access it has, with no boundary telling it to stop.

| Too vague | Well-scoped for Hermes Agent |
| --- | --- |
| "Help me update the docs." | "Read only `data/research/candidates.json` and draft a Markdown outline for one new guide section; no file writes, no shell access." |
| "Look into what's out there and summarize it." | "Summarize these three public URLs I provide, label each source official or community, and flag anything needing official-doc verification." |
| "Keep an eye on this and let me know." | "Draft a private reminder checklist for me to review candidates weekly; do not schedule anything that publishes automatically." |
| "Use whatever you remember about this project." | "Do not use prior memory from other sessions. Treat this as a fresh task with only the sources listed below." |
| "Fix up the repo however you think is best." | Not a Hermes Agent task at all: repository edits go through Codex or Claude Code with a scoped, reviewable diff. |

The pattern in every "too vague" row is the same: no named source boundary,
no named output boundary, and no named stop condition. The well-scoped
column names all three every time, because a persistent agent will fill an
unstated boundary with whatever it has access to, not with what you meant.

## Worked Example: Task Intake To Verification To Report

This walks one task through every stage so the shape is concrete, not just
templated language.

**1. Task intake (what the maintainer wants):** "We keep finding good public
articles about agent skills. I want a first-pass outline for a new guide
section, but I don't want to hand-write it from scratch."

**2. Scoped prompt (what actually gets sent to Hermes Agent):**

```text
Target: Hermes Agent

Goal:
Draft a private outline for a new "agent skills" guide section.

Allowed sources:
- The three public URLs listed below.
- Official Hermes Agent and Codex documentation if directly relevant.

Forbidden sources:
- Any memory from prior sessions.
- Private notes, browser sessions, or local files not listed here.

Deliver:
- A source ledger: title, URL, official/community/unverified status.
- A beginner-friendly outline with headings only, no full prose.
- A list of claims that need official-doc verification.
- A list of anything you were unsure whether to include.

Do not write to any file. Do not use shell tools. Return the outline as
chat output only.
```

**3. Verification (what the maintainer checks before using the output):**

- Does the source ledger label every source, with none left unlabeled?
- Does any heading drift into Hermes language-model, benchmark,
  quantization, or local-serving territory? If so, cut it before reuse.
- Does any claim look asserted as fact without a "verify in official docs"
  flag next to it?
- Did the agent reference anything not in the provided source list, which
  would suggest it pulled from memory instead of the stated sources?

**4. Report (what goes back to the maintainer, and eventually a PR):** "Used
3 public sources, all labeled official or community. Produced a 6-heading
outline. Flagged 2 claims needing official-doc verification before
publishing. No memory or private files were used. Next step: hand this
outline to Claude Code as context for a scoped branch and PR against
`docs/skills/README.md`." That last line is the important one: the outline
is not the deliverable, the reviewed PR is.

## How This Connects To The Agent-Task Templates

This repository already has per-tool task templates at
`prompts/*/agent-task.md` (for example `prompts/cursor/agent-task.md` and
`prompts/aider/agent-task.md`). Those templates are written for Git-first
tools that edit repository files directly and share a common shape: target
tool, purpose, inputs to fill, full prompt, boundaries, success criteria,
verification commands, and a final report format.

Hermes Agent prompts in this file follow the same shape deliberately, with
one structural difference: the "deliver" section never asks for a file
write or a commit. Where an `agent-task.md` template ends with "apply the
diff and open a PR," a Hermes Agent prompt ends with "return the draft as
output," because Hermes Agent is not the tool that owns the repository
working tree here. See
[hermes-agent.md](hermes-agent.md#role-boundaries-in-a-safe-workflow) for
that boundary.

In practice this means: use a `prompts/*/agent-task.md` template for the
actual repository edit, and use the templates on this page only for the
planning/drafting step that feeds into it. If a task only needs one step,
skip Hermes Agent and go straight to the Git-first template.

## Full Prompt Template

```text
Target: Hermes Agent

Purpose: Review public AI skills and prompt-guide candidates for a public
documentation repository.

Read only the public candidate report and source policy. Do not use private
memory, private chats, OAuth files, provider tokens, browser sessions, or local
logs as source material.

Select up to [N] public-safe sources. Prefer official documentation. Label
community, unofficial, leak-derived, inferred, or unverified sources.

Draft a Markdown guide section with:
- what the tool/resource is
- beginner friendliness
- public-safe use cases
- install commands only if verified
- placeholders for unverified commands
- Windows notes
- failure modes
- evaluation checklist
- source links
- license/source status

Do not push to main. Prepare output for branch, PR, checks, review, and merge.
```

## Short Version

```text
Use only public candidate sources, draft a reviewed guide update, exclude
private memory and secrets, and prepare it for PR review.
```

## Why This Works

- It separates public candidate reports from private Hermes state.
- It limits source count.
- It requires source labels.
- It blocks direct publishing.
- It requires failure modes and evaluation.

## Failure Cases

- The agent uses private memory as evidence.
- The agent invents install commands.
- The output copies leaked prompts.
- The automation writes directly to `main`.
- The guide omits source status or license notes.

## Output Constraints

- Markdown only.
- No secrets or private paths.
- No copied prompt dumps.
- No Hermes language-model coverage.
- Source links required.
- Unverified commands must be placeholders.

## Revision Checklist

- [ ] Did the prompt define source boundaries?
- [ ] Did it forbid private memory and logs?
- [ ] Did it require branch and PR review?
- [ ] Did it require official-doc verification?
- [ ] Did it include failure modes?

## Source Ledger Add-On

Add this to Hermes Agent prompts when source material is involved:

```text
For every source, record:
- Source name
- Source URL if public
- Source status: official, community, unofficial, leak-derived, inferred, or unverified
- What claim it supports
- What claim it cannot support
- License or reuse concern
- Whether current behavior must be verified in official docs
```

## Review Prompt

```text
Review the Hermes Agent draft as a public repository maintainer.

Check:
- No private memory, OAuth state, logs, provider keys, or local paths.
- No Hermes language-model, benchmark, quantization, GGUF, Ollama, vLLM, or
  SGLang coverage.
- Commands are official-doc verified or placeholders.
- Source status is labeled.
- The draft requires branch, PR, checks, and human review.

Return:
- Findings ordered by severity.
- Files or sections affected.
- Claims needing official-doc verification.
- Required fixes before publication.
```

## Evaluation Cases

| Case | Expected behavior |
| --- | --- |
| Public official doc source | Summarize conservatively and link source. |
| Community source | Use for pattern only; mark current claims for official verification. |
| Private memory available | Do not use it as public evidence. |
| User asks for model-serving guide | Decline or redirect out of Hermes Agent scope. |
| Automation asks to push to `main` | Refuse; require branch, PR, checks, review. |

## Final Report Fields

- Sources used.
- Sources skipped.
- Public-safety checks.
- Commands verified or left as placeholders.
- Files changed or draft sections produced.
- Claims needing official-doc verification.
- Remaining risks.
