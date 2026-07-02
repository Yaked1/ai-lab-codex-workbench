# OpenCode

## What It Is

OpenCode is an open-source AI coding-agent project with terminal, desktop, IDE, or hybrid surfaces depending on the current release. It can be useful for learners who want to understand provider-flexible agent workflows, local command permissions, and open-source alternatives to hosted coding agents.

Verify current install commands, provider setup, platform support, and pricing exposure in official docs.

## Best Use Cases

| Use case | Fit | Notes |
| --- | --- | --- |
| Read-only repository overview | Strong | Safe first task. |
| Terminal-first coding session | Medium | User should understand Git and shell commands. |
| Provider comparison | Medium | Track cost and credentials carefully. |
| Open-source agent experimentation | Strong | Good for learning architecture and permissions. |
| Beginner implementation | Medium | Start with docs and tests. |
| Sensitive private repo | Weak | Understand provider and local permissions first. |

## What OpenCode Is Good At Vs. Not

Good at:

- Read-only repository exploration as a genuinely safe first task, since a
  terminal/TUI agent can summarize a repo's structure without needing edit
  permissions at all.
- Learning how an open-source, provider-flexible agent handles command
  permissions, which is useful context before trusting any hosted agent's
  default permission model.
- Comparing provider/model behavior for the same prompt, since OpenCode is
  built to work with more than one backend.
- Terminal users who are already comfortable reading `git diff` and running
  local checks by hand.

Not good at:

- First-time users who are not yet comfortable reading terminal output; the
  TUI/CLI surface assumes basic shell and Git literacy.
- Sensitive repositories before the local command-permission model and
  provider credential storage are understood, since a misconfigured session
  can run more than intended.
- Guaranteed-support workflows. As an open-source project, feature
  availability, install steps, and platform support can change faster and
  with less notice than a commercial product's documentation.

## Beginner Friendliness

Medium. OpenCode is approachable for terminal users, but beginners need clear setup boundaries: where provider credentials live, which commands can run, and how to review diffs.

## Using This Repository's Workflow With OpenCode

- Prompt template: [prompts/opencode/agent-task.md](../../prompts/opencode/agent-task.md).
  It already encodes the "read-only first, plan, wait for approval" pattern
  this repo expects.
- Local rules: paste or reference `AGENTS.md` explicitly at the start of a
  session. Verify whether the current OpenCode release supports an
  automatic repo-instructions file before assuming it loads `AGENTS.md`
  without being told.
- Because OpenCode is provider-flexible, always confirm which provider/model
  is actually configured before trusting a capability claim the agent makes
  about itself; behavior is not guaranteed to be identical across providers.

## Task Intake Worksheet

| Question | Beginner-friendly answer to write down |
| --- | --- |
| What result do I want? | One sentence, such as "summarize `docs/` and suggest one improvement." |
| Which files are allowed? | Exact files or directories in scope for this session. |
| Which files are excluded? | Workflow YAML, secrets, generated files, unrelated docs. |
| What context does the agent need? | `AGENTS.md`, the target file, and any directly related test or template. |
| What proves the task is done? | A read-only summary or a reviewed diff, plus the local checks in `AGENTS.md`. |
| What could cost money? | Provider API calls, model choice, retries, or a long-running session. |
| Who reviews the result? | The human running OpenCode reads `git diff` before committing or pushing. |

If any answer is unclear, start with the read-only prompt below before
allowing any file edit.

## Example Workflow: Task Intake To PR

1. **Task intake.** Confirm `git status` is clean and write the one-sentence
   outcome plus the exact files in scope.
2. **Start OpenCode read-only** from the repository root:

   ```powershell
   git switch -c agent/opencode-docs-update
   opencode
   ```

3. **Scoped prompt.** Use
   [prompts/opencode/agent-task.md](../../prompts/opencode/agent-task.md),
   filling in the task, files, and provider notes.
4. **Agent work.** Require a read-only summary and a numbered plan before any
   edit; approve explicitly before letting it write to disk.
5. **Local checks.**

   ```powershell
   python scripts/repo_health_check.py
   python scripts/safe_autofix.py --check
   python -m unittest discover -s tests
   ```

6. **Diff review.** Run `git diff` and read every changed line.
7. **PR.** Push the branch and open a PR describing the task, provider used,
   files changed, and checks run.

## Troubleshooting

| Symptom | Likely cause | Response |
| --- | --- | --- |
| Agent edits files outside the requested scope | Session started in an edit-capable mode without an explicit file list. | Reject the diff, restart read-only, and narrow the prompt to exact files. |
| Provider authentication fails or hangs | Missing or misconfigured credentials for the selected provider. | Verify credential setup in official docs; never paste keys or tokens into chat. |
| CLI/TUI doesn't start or exits immediately | Install path incomplete, or a config file is missing/misnamed for the current release. | Re-check the current install guide; confirm the binary/version matches official docs. |
| Repository context looks stale after a `git pull` | Local index or cache not refreshed. | Restart the session; re-run any explicit index/refresh step the current docs describe. |
| Same prompt behaves differently after switching providers | Providers are not guaranteed to produce identical behavior. | Note which provider/model produced the result; re-verify capability claims per provider. |
| Unexpected shell command runs without a clear approval step | Command-permission settings were broader than assumed. | Review the current permission/config settings; narrow allowed commands before continuing. |

## Setup Style

| Style | When to use it | Beginner note |
| --- | --- | --- |
| CLI | Terminal-first work. | Good after Git basics. |
| Desktop/IDE | If current release supports it. | Verify before teaching. |
| Hybrid | Provider plus local repository workflow. | Keep credentials out of the repo. |

## Windows Suitability

Verify current Windows installation and shell support before writing a setup lesson. For this repo, first tasks should be read-only until the environment is understood.

## Hardware, API, Docker, and WSL Requirements

| Requirement | Practical guidance |
| --- | --- |
| Hardware | Lightweight for docs and small script tasks. |
| API/account | Provider-dependent; verify current setup and cost exposure. |
| Docker | Do not assume it is required. |
| WSL | Do not assume it is required. |
| GPU | Not needed for normal API-backed coding-agent work. |

## Best First Task

Ask OpenCode to summarize the repository structure without editing files:

```text
Read the repository and explain its main docs, scripts, workflows, and tests.
Do not modify files.
Do not run write commands.
```

## Prompt Template

```text
Target tool: OpenCode

Mode:
Start read-only.

Task:
Explain this repository and propose one small documentation improvement.

Boundaries:
- Read AGENTS.md first.
- Do not edit files.
- Do not install dependencies.
- Do not access files outside the repository.
- Do not print environment variables.

Final report:
- Repo summary
- Suggested files to change
- Proposed checks
- Risks and assumptions
```

## Permissions And Defaults

By default, OpenCode can run shell commands and edit files according to its
current permission configuration, which varies by release and provider.
Scope it down by:

- Starting every new task read-only, and only granting edit/execute
  permission after a plan is reviewed.
- Naming exact files or directories in scope instead of the whole repo.
- Never printing or logging environment variables or provider credentials,
  even for debugging.
- Confirming the current permission model in official docs rather than
  assuming an older tutorial's defaults still apply.

## Permission, Cost, And Data Guardrails

| Risk | Practical control |
| --- | --- |
| Provider credentials can be misconfigured or accidentally exposed | Never paste keys into chat; verify storage location in official docs. |
| Terminal agents may run commands the user did not expect | Read every proposed command before approval; keep permission scope narrow. |
| Cost exposure can change when switching providers | Confirm the active provider/model before a long session; watch for retry loops. |
| Windows support may differ by install method | Verify the current install path and shell support before teaching. |
| Wrong repository or branch targeted | Confirm `pwd`/`git status` before starting a session. |

## When To Prefer This Over The Others

Prefer OpenCode when you specifically want an open-source, provider-flexible
terminal agent and value being able to inspect or swap the underlying model.
Prefer Codex when you want this repo's Git-first reference workflow with
local checks already wired in. Prefer Aider when you know the exact files to
change and want the simplest explicit-file terminal loop. Prefer Cursor or
Claude Code when you want IDE-first review or read-only second-opinion review
instead of a terminal-only surface.

## Safety Risks

- Provider credentials can be misconfigured or accidentally exposed.
- Terminal agents may run commands the user did not expect.
- Cost exposure can change when switching providers.
- Windows support may differ by install method.

## Review Checklist

- [ ] Were credentials kept outside the repo?
- [ ] Did the first task start read-only?
- [ ] Was command execution limited?
- [ ] Were proposed edits scoped to specific files?
- [ ] Were local checks run after any write task?
- [ ] Are provider and pricing details marked for verification?

## When To Avoid It

Avoid OpenCode for:

- First-time users uncomfortable with terminal output.
- Repositories containing secrets before permissions are reviewed.
- Tasks requiring guaranteed vendor support.
- Public setup docs that have not been verified against current release notes.

## Alternatives

| Alternative | Use when |
| --- | --- |
| Codex | You want the repo's reference workflow. |
| Aider | You want explicit-file terminal editing. |
| Cursor | You want IDE-first review. |
| Claude Code | You want review and explanation. |

## Verification Notes

Verify current install commands, supported surfaces, provider configuration, permission controls, Windows behavior, pricing exposure, and model/provider options.

## Claims To Verify In Official Docs

- Current installation method.
- Supported operating systems.
- CLI, desktop, and IDE support.
- Provider setup and credential storage.
- Permission model.
- Pricing exposure through providers.

Official docs:

- <https://opencode.ai/docs/>
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **tool guide** surface. During broad
maintenance, reviewers should treat `docs/tools/opencode.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `opencode` state what decision, workflow, or reusable behavior it supports?
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
