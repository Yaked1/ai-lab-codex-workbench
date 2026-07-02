# Kilo Code

## What It Is

Kilo Code is an open-source AI coding agent positioned across IDE, CLI, and cloud-oriented workflows depending on current configuration. In this repository it is a comparison tool for agent modes, provider choices, planning, and small documentation or bug-fix tasks.

Verify current docs for installation, provider support, model access, cloud behavior, and pricing exposure.

## Best Use Cases

| Use case | Fit | Notes |
| --- | --- | --- |
| IDE-based planning | Strong | Good first mode for beginners. |
| Small docs task | Strong | Keep edits reviewable. |
| CLI experiment | Medium | Requires shell comfort. |
| Provider comparison | Medium | Track cost and credentials. |
| Codebase refactor | Medium | Require a plan and tests. |
| Sensitive repo work | Weak at first | Review permissions first. |

## What Kilo Code Is Good At Vs. Not

Good at:

- Mode-based workflows where a distinct "plan" or "architect" mode can
  propose a change before any file is touched, which fits this repo's
  plan-before-edit habit well.
- Comparing provider and model behavior side by side, since Kilo Code is
  built to be provider-flexible rather than locked to one vendor.
- Small, well-scoped documentation or bug-fix tasks where the mode boundary
  (plan vs. act) keeps the session honest about what stage it is in.
- Learners who want to see an explicit mode switch as a forcing function for
  review, instead of relying on habit alone.

Not good at:

- Tasks where the current mode's permission set is unclear. Because modes
  carry different edit/execute permissions, a task started in the wrong mode
  can either fail silently or apply changes wider than intended.
- Sensitive repositories before you have verified exactly what each mode is
  allowed to touch. Mode names and their permission scopes have changed
  between releases; do not assume an older tutorial's mode boundaries still
  apply.
- Long, unattended sessions. Provider/model switching plus mode switching in
  the same session multiplies the number of assumptions a beginner has to
  track at once.

## Beginner Friendliness

Medium. IDE mode is usually easier than CLI mode. Start with planning or documentation tasks before allowing broad code edits.

## Using This Repository's Workflow With Kilo Code

- No dedicated `prompts/kilo-code/` template exists yet in this repository.
  Use the [Prompt Template](#prompt-template) below directly, or adapt the
  structure from [prompts/cursor/agent-task.md](../../prompts/cursor/agent-task.md)
  or [prompts/windsurf/agent-task.md](../../prompts/windsurf/agent-task.md),
  since both already encode the "explain or plan first, edit after approval"
  pattern this repo expects.
- Local rules: point the current planning/architect mode at `AGENTS.md`
  explicitly at the start of the session. Verify whether the installed Kilo
  Code version supports an automatic repo-instructions file before assuming
  it reads `AGENTS.md` on its own.
- Always name the mode you are using in your task intake notes and in the
  final report. Mode name and scope are the single most important piece of
  session metadata for this tool.

## Task Intake Worksheet

| Question | Beginner-friendly answer to write down |
| --- | --- |
| What result do I want? | One sentence, such as "fix the broken link in `docs/tools/kilo-code.md`." |
| Which mode am I starting in? | Name the exact mode (e.g. plan/architect vs. act/code) and confirm what it can and cannot do. |
| Which files are allowed? | Exact file paths in scope for this session. |
| Which files are excluded? | Workflow YAML, secrets, generated files, unrelated docs. |
| What context does the mode need? | `AGENTS.md`, the target file, and any directly related test or template. |
| What proves the task is done? | A reviewed plan, a readable diff, and the local checks in this repo's `AGENTS.md`. |
| What could cost money? | Provider API calls, model choice, retries, or an unexpectedly long session. |
| Who reviews the result? | The human running Kilo Code reads the diff before committing or pushing. |

If you cannot name the current mode and its permission scope, stop and check
the mode selector before typing a task.

## Example Workflow: Task Intake To PR

1. **Task intake.** Confirm `git status` is clean and write down the one
   sentence outcome plus the mode you intend to start in.
2. **Start in a planning/architect mode** so the first output is a plan, not
   a diff:

   ```powershell
   git switch -c agent/kilo-docs-update
   ```

3. **Scoped prompt.** Use the [Prompt Template](#prompt-template) below,
   filling in the exact file and the one-sentence task.
4. **Agent work.** Let the agent produce a plan first. Read it fully before
   switching to an editing/act mode.
5. **Local checks.**

   ```powershell
   python scripts/repo_health_check.py
   python scripts/safe_autofix.py --check
   python -m unittest discover -s tests
   ```

6. **Diff review.** Run `git diff` and read every changed line, paying
   attention to whether the edit stayed inside the approved plan.
7. **PR.** Push the branch and open a PR describing the task, the mode used,
   files changed, and checks run.

## Troubleshooting

| Symptom | Likely cause | Response |
| --- | --- | --- |
| Agent edits a file it never asked to plan for | Mode switched to an editing mode with a broader default scope than expected. | Reject the change, switch back to a planning mode, and re-scope the task explicitly. |
| Confusion about what the current mode can do | Mode names and permission boundaries differ across releases and configurations. | Check the current mode selector/docs before typing a task; do not assume an older tutorial's mode map still applies. |
| Session applies edits without a visible plan step | Started directly in an act/code mode instead of a plan/architect mode. | Stop, discard unreviewed changes if needed, and restart the task in a planning mode first. |
| Provider or model switch mid-session changes behavior unexpectedly | Kilo Code is provider-flexible, and different providers can behave differently for the same prompt. | Note which provider/model produced the result; do not assume behavior is transferable across providers without checking. |
| Credentials appear misconfigured or missing | Provider setup was incomplete or the wrong provider was selected for the current mode. | Verify current provider/credential setup in official docs; never paste keys into chat. |
| Diff is much larger than the task described | Mode's permission scope was broader than intended, or the plan was not followed exactly. | Reject the diff, narrow the prompt, and re-run in a planning mode to get a smaller, matching plan. |

## Setup Style

| Style | When to use it | Beginner note |
| --- | --- | --- |
| IDE | Planning and visible edits. | Best first path if supported. |
| CLI | Terminal-first workflows. | Use after Git and shell basics. |
| Cloud/hybrid | If current docs support it. | Confirm repo access and permissions. |
| Provider-flexible | When comparing models or APIs. | Keep credentials out of the repo. |

## Windows Suitability

Good if the selected IDE extension or CLI path supports the current Windows setup. Verify current install guidance before teaching.

## Hardware, API, Docker, and WSL Requirements

| Requirement | Practical guidance |
| --- | --- |
| Hardware | Lightweight for docs and small scripts. |
| API/account | Provider-dependent; verify current requirements. |
| Docker | Not needed for this repo unless current docs require it for a selected mode. |
| WSL | Not needed for basic work unless selected setup requires it. |
| GPU | Not needed for API-backed tasks. |

## Best First Task

Use planning mode for one small docs issue, then manually decide whether to apply the proposed change.

## Prompt Template

```text
Target tool: Kilo Code

Task:
Plan a small update to [file].

Instructions:
- Read AGENTS.md.
- Start in planning mode.
- List the exact files to change.
- Do not edit until the plan is approved.
- Keep provider and pricing claims out of the docs unless verified.

Validation after edits:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests

Final report:
- Plan or summary
- Mode used
- Files changed
- Checks run
- Remaining risks
```

## Permissions And Defaults

Kilo Code's permission model is mode-based: what the agent can read, edit, or
execute depends on which mode is active, and default mode names and scopes
have changed between releases. Scope it down by:

- Confirming the current mode's permissions before typing a task, not after.
- Starting sessions in a planning/architect-style mode rather than a direct
  edit/execute mode.
- Adding only the files the task needs into context.
- Never assuming a mode is read-only just because it sounds like one; verify
  in current official docs.

## Permission, Cost, And Data Guardrails

| Risk | Practical control |
| --- | --- |
| Wrong mode selected | Name the mode explicitly in your task intake and confirm its scope before proceeding. |
| Provider cost | Start with the cheapest suitable configured model; keep sessions short. |
| Credential misconfiguration | Verify provider setup in official docs; never paste keys into chat or commit them. |
| Unreviewed broad diff | Require a plan step before any edit-mode session; review `git diff` before committing. |
| Wrong repository or branch | Confirm `git status` and the current branch before starting a session. |

## When To Prefer This Over The Others

Prefer Kilo Code when you specifically want to compare agent modes or
provider/model behavior side by side, or when its plan/act mode split gives
you a clearer forcing function for review than a single-mode tool. Prefer
Cursor when you want the most common, well-documented IDE-agent starting
point. Prefer Codex when you want this repo's reference Git-first workflow
with local checks built in. Prefer OpenCode when the comparison you want is
specifically open-source terminal agents rather than mode-based IDE agents.

## Safety Risks

- Provider setup can be confusing.
- Credentials may be stored incorrectly.
- Cost or rate-limit behavior depends on provider and plan.
- Agent modes may have different permission levels.
- Large diffs can be accepted too quickly.

## Review Checklist

- [ ] Was the selected mode documented?
- [ ] Were provider credentials kept out of Git?
- [ ] Was a plan reviewed before edits?
- [ ] Did edits stay inside the task scope?
- [ ] Were checks run?
- [ ] Were product claims kept conservative?

## When To Avoid It

Avoid Kilo Code for:

- First tasks where setup is not verified.
- Secret-heavy projects.
- Broad refactors without tests.
- Public docs that need exact product claims but have not been checked.

## Alternatives

| Alternative | Use when |
| --- | --- |
| Cursor | You want a more common IDE-agent starting point. |
| Codex | You want local Git-first execution and checks. |
| OpenCode | You want another open-source agent comparison. |
| Aider | You want explicit-file terminal editing. |

## Verification Notes

Verify current product name, install paths, supported modes, provider setup, permission controls, Windows support, limits, and pricing exposure.

## Claims To Verify In Official Docs

- Current installation instructions.
- IDE, CLI, cloud, and hybrid support.
- Provider and model setup.
- Permission controls, including exact mode names and their scopes.
- Windows support.
- Pricing, limits, and rate behavior.

Official docs:

- <https://kilo.ai/docs>
