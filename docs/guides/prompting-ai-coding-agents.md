# Prompting AI Coding Agents

A practical, tool-agnostic guide to getting reliable work out of AI coding
agents such as Codex, Claude Code, Cursor, GitHub Copilot, Aider, and Windsurf.

This guide is about the **craft** of prompting: how to think, structure, and
verify. For the repository-specific safe work-order skeleton, use the
[Prompt engineering playbook](prompt-engineering-playbook.md). For agent-by-agent
tricks, use the [Coding agent power tips](coding-agent-power-tips.md). For the
public resources this guide draws on, see the
[Prompting references](prompting-references.md).

All product feature names below are pointers, not promises. Tool behavior,
flags, and defaults change. Confirm anything specific in the official docs linked
from [prompting-references.md](prompting-references.md).

## Why Coding-Agent Prompting Is Different

A chat prompt asks for text. A coding-agent prompt authorizes **actions**:
reading files, editing code, running commands, opening pull requests. That
changes the goal. You are not trying to get one good answer; you are trying to
get a reviewable change with a clear stopping point.

| Chatbot prompting | Coding-agent prompting |
| --- | --- |
| One response is the deliverable. | A diff plus a report is the deliverable. |
| Wrong answers waste your time. | Wrong actions can break a branch or leak data. |
| Context is what you paste. | Context is the repo, the tools, and the memory files. |
| "Good enough" is subjective. | "Done" is checks passing and a human review. |

The single most useful mental model: **a prompt is a work order, not a wish.**
A work order names the outcome, the boundaries, the evidence of completion, and
what to do when something goes wrong.

## The Anatomy Of A Strong Agent Prompt

Most reliable coding prompts contain the same parts. You do not need all of them
every time, but you should know which one you are skipping and why.

| Part | Question it answers | Example phrase |
| --- | --- | --- |
| Role / framing | Who is the agent acting as? | "You are reviewing a public docs repo before merge." |
| Context | What does the agent need to know first? | "Read AGENTS.md and the target files before editing." |
| Objective | What is the one outcome? | "Add a troubleshooting section to X." |
| Scope fence | What is in and out of bounds? | "Include these paths; do not touch workflow YAML." |
| Constraints | What rules and safety limits apply? | "No new dependencies. No secrets. Keep the diff small." |
| Examples | What does good look like? | "Match the table style already used in this file." |
| Plan gate | Should it think or plan first? | "Propose a plan and wait before editing." |
| Verification | How is done proven? | "Run these checks and report exact results." |
| Report format | What should come back? | "Return changed files, commands run, risks." |
| Recovery rule | What if it gets stuck? | "If unrelated tests fail, report them, do not fix them." |

A compact, copy-ready version of this anatomy lives in the
[prompt engineering playbook](prompt-engineering-playbook.md#advanced-path).

## Core Techniques That Transfer Across Every Agent

These techniques work regardless of which tool or model you use. They are the
load-bearing skills; the tool-specific features in
[coding-agent-power-tips.md](coding-agent-power-tips.md) only amplify them.

### 1. Be specific about the outcome, not just the topic

Vague: "improve the error handling." Specific: "wrap the file read in
`load_config` so a missing file raises a clear `FileNotFoundError` with the path,
and add one test that proves it." Specific outcomes are testable; topics are not.

### 2. Give context before instructions

Tell the agent what to read and what the project is before you tell it what to
do. An agent that has read the conventions writes code that matches them. An
agent that edits first invents its own style.

### 3. Decompose large tasks

A task that touches many files or several concerns is several prompts, not one.
Split into inspect, plan, implement, verify. Large single prompts produce large
unreviewable diffs and quiet mistakes. If you cannot describe the change in one
sentence, it is too big for one prompt.

### 4. Ask for a plan before edits on anything non-trivial

"Propose a plan and wait for my approval before changing files" turns a risky
edit into a cheap conversation. You catch a wrong approach in the plan, where
fixing it costs one message, instead of in a 400-line diff.

### 5. Make the agent verify its own work

The most common failure is an agent that says "done" without proof. Always name
the checks and require exact results: "Run the test suite and paste the output.
If anything fails, stop and report it." Treat a passing self-report with no
command output as unverified.

### 6. Use examples and output shapes

Show the format you want. If you want a table, show a row. If you want a commit
message style, show one. Few-shot examples constrain output far more reliably
than adjectives like "clean" or "professional."

### 7. State negative constraints explicitly

Agents fill ambiguity with action. "Do not add dependencies, do not edit
workflow files, do not refactor unrelated code, do not invent pricing or model
claims" prevents the most common scope blowups. Excluded scope is as important
as included scope.

### 8. Budget the context window

The context window is your only control surface. Load the spec, the contract,
and the relevant files; leave the noise out. When a session drifts, the first
question is "what is in the window," not "is the model dumb." Start a fresh
session for a new task rather than dragging a long, polluted history forward.

### 9. Separate latent work from deterministic work

If the same question asked twice has the same correct answer by definition
(date math, formatting, file lookups, JSON transforms), ask the agent to write a
script for it, not to do it by hand each time. Reserve the model's judgment for
genuinely ambiguous work. The script then constrains every future run.

### 10. Control claims about fast-changing tools

Tell the agent to mark pricing, plan access, model availability, and install
commands as "verify in official documentation" instead of asserting them.
Confident, stale claims are worse than an honest "confirm this."

## Prompting Patterns Library

| Pattern | When to use it | Instruction to include |
| --- | --- | --- |
| Inspect-then-edit | Agent may not know conventions. | "Read these files before changing anything." |
| Plan-first | Change is non-trivial or risky. | "Propose a plan and wait for approval." |
| Test-first (TDD) | Behavior change with a clear spec. | "Write a failing test first, then make it pass." |
| Smallest-correct-change | Reviewability matters. | "Keep the diff minimal; no unrelated refactors." |
| Scope fence | Risk of broad edits. | "Include X; exclude Y, Z, and workflow YAML." |
| Verification contract | You need trustworthy completion. | "Run these checks and paste exact output." |
| Self-critique | Quality and edge cases matter. | "List how this could fail, then fix the top risks." |
| Role framing | Task needs a clear stance. | "Act as a skeptical reviewer, not an implementer." |
| Stop-on-ambiguity | High-stakes or unclear input. | "If requirements are ambiguous, ask before acting." |
| Decomposition | Task spans files or concerns. | "Break this into phases and do phase one only." |
| Claim control | External products are mentioned. | "Mark fast-changing facts as verify-in-docs." |
| Recovery rule | Conflicts or failures are likely. | "Report unrelated failures; do not fix them." |

## Reasoning And Planning Controls

Many agents expose a way to spend more reasoning effort on hard problems, and a
way to plan before acting. Use them deliberately.

- **Plan before acting.** Ask for a plan, review it, then approve. This is the
  cheapest place to correct course.
- **Escalate effort on hard problems.** Several tools let you request deeper
  reasoning for complex tasks. Use more effort for architecture, tricky bugs,
  and ambiguous trade-offs; use less for mechanical edits. Spending maximum
  effort on a one-line change is waste; spending minimum effort on a subtle race
  condition is a bug.
- **Right-size the task.** Reasoning effort does not rescue a vague prompt. A
  clear small prompt beats a deep model pointed at mush.

The exact keywords, flags, and modes differ per tool; see
[coding-agent-power-tips.md](coding-agent-power-tips.md) and confirm in official
docs.

## Memory And Rules Files: Prompt Once, Apply Always

The highest-leverage prompting often is not a prompt at all. It is a persistent
instructions file the agent reads every session:

| Tool | File | What it is for |
| --- | --- | --- |
| Codex | `AGENTS.md` | Durable repo + global instructions, layered. |
| Claude Code | `CLAUDE.md` | Durable project memory and conventions. |
| Cursor | Project rules | Repo conventions and guardrails. |
| Most agents | A conventions file | Style, commands, do-not-touch lists. |

Rules for good memory files:

- Keep them short. Long files get half-ignored; important rules drown in noise.
- Put commands, conventions, and hard "never do" lines first.
- If the agent already behaves correctly without a rule, delete the rule.
- Treat the file as code: review changes to it, do not let it sprawl.

This repository ships an [AGENTS.md](../../AGENTS.md) as a worked example.

## Anti-Patterns To Avoid

| Anti-pattern | Why it fails | Do instead |
| --- | --- | --- |
| "Fix everything" | Huge unreviewable diff. | One objective, explicit scope. |
| No verification | False "done." | Name checks; require exact output. |
| No excluded scope | Agent edits workflows or generated files. | Add a "do not touch" list. |
| Prompting from a polluted session | Stale context misleads the agent. | Start fresh per task. |
| Trusting the summary | Summaries hide what changed. | Read the diff yourself. |
| Asserting tool facts | Docs go stale or wrong. | "Verify in official docs." |
| Doing arithmetic in chat | Silent, unrepeatable errors. | Have the agent write a script. |
| One giant prompt | Mixed concerns, mixed results. | Decompose into phases. |
| Pasting secrets for "context" | Public-repo and security risk. | Use placeholders; never paste secrets. |

## A Worked Before-And-After

**Weak prompt**

```text
Refactor the config loading and make it better, add tests.
```

No scope, no definition of "better", no verification, no report.

**Strong prompt**

```text
Read scripts/config.py and tests/test_config.py first.

Objective:
Make config.py raise a clear FileNotFoundError (including the path) when the
config file is missing, instead of crashing with a generic error.

Scope:
- Include: scripts/config.py, tests/test_config.py
- Exclude: other scripts, workflow YAML, dependencies

Approach:
1. Add a failing test that asserts FileNotFoundError with the path in the message.
2. Make the smallest change to config.py to pass it.
3. Do not refactor unrelated code.

Verification:
- Run: python -m unittest discover -s tests
- Paste the exact output.

Final report:
- Summary, files changed, commands run, checks run, remaining risks.
```

## Verification And Evaluation

Prompting does not end at "send." Treat verification as part of the prompt and,
for prompts you reuse, measure them:

- **Per task:** require commands, read the diff, confirm the report matches reality.
- **For reusable prompts and agent rules:** keep a few known inputs and expected
  behaviors, and re-check them when you change the prompt. Tools such as
  [promptfoo](https://www.promptfoo.dev/docs/intro/) exist for exactly this. A
  prompt you reuse is software; give it a regression check.

See the [prompt audit checklist](prompt-audit-checklist.md) for a fast review
pass before you send, publish, or teach a prompt.

## Quick Checklist

- [ ] One clear objective stated as an outcome, not a topic.
- [ ] The agent is told what to read first.
- [ ] Included and excluded scope are explicit.
- [ ] Safety constraints (secrets, dependencies, workflow files) are stated.
- [ ] An example or output shape is given when format matters.
- [ ] A plan gate is used for non-trivial changes.
- [ ] Verification commands are named and exact results required.
- [ ] A final report format is required.
- [ ] A recovery rule covers unrelated failures and ambiguity.
- [ ] Fast-changing tool claims are marked for official-doc verification.

## Where To Go Next

- [Coding agent power tips](coding-agent-power-tips.md) — per-agent tricks.
- [Prompting references](prompting-references.md) — the public resources to learn from.
- [Prompt engineering playbook](prompt-engineering-playbook.md) — this repo's safe work-order skeleton.
- [Prompt audit checklist](prompt-audit-checklist.md) — review a prompt before sending it.
