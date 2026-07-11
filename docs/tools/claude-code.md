# Claude Code

> For the dated Fable 5 effort, Cowork, Claude Code desktop, pricing, and
> Ultracode map, see
> [Current models, interfaces, and effort controls](../guides/current-models-and-interfaces.md).

## What It Is

Claude Code is an agentic coding tool for understanding codebases, editing files, running commands, and reviewing development work across supported surfaces. In this repository it is best treated as a documentation reviewer, codebase explainer, and second-opinion reviewer before merge.

Claude Code changes over time. Verify installation, account, platform, model, and feature claims in Anthropic's official docs before publishing setup instructions.

## Best Use Cases

| Use case | Fit | Notes |
| --- | --- | --- |
| Documentation review | Strong | Ask for findings before edits. |
| Codebase explanation | Strong | Useful before handing a task to another agent. |
| PR review | Strong | Keep it read-only unless follow-up edits are requested. |
| Multi-file planning | Strong | Ask for a plan artifact before implementation. |
| Small implementation task | Medium | Scope files and require checks. |
| Unbounded repo rewrite | Weak | Split into review, plan, and small PRs. |

## What Claude Code Is Good At Vs. Not

Good at:

- Explaining an unfamiliar codebase clearly before any edit happens, which
  makes it a strong first pass for a beginner trying to understand a repo.
- Read-only review: finding unclear instructions, unsupported claims, and
  missing safety warnings across multiple files at once.
- Multi-file planning, where asking for a written plan before implementation
  gives you something concrete to review before any diff exists.
- Acting as a second opinion on a PR produced by a different tool or agent,
  since it can be pointed at a diff without being the tool that wrote it.

Not good at:

- Unbounded repo rewrites in one pass. Confident, well-written explanations
  can make a large generated change look more trustworthy than it is; split
  big changes into review, plan, and small PRs instead.
- Guaranteeing that "review" and "edit" stay separate unless you say so
  explicitly. A permissioned session can move from explaining to editing
  faster than a beginner expects if the prompt does not draw the line.
- Long, unattended sessions. Cost, model, and permission behavior are
  account/plan-dependent and can change; do not assume an old tutorial's
  defaults still apply.

## Beginner Friendliness

Medium. Claude Code can explain reasoning clearly, which helps learners understand a codebase. The risk is that beginners may accept broad suggested rewrites because the explanation sounds confident. Start with review-only prompts.

## Using This Repository's Workflow With Claude Code

- Prompt template: [prompts/claude-code/review-docs.goal.md](../../prompts/claude-code/review-docs.goal.md).
  It is written as a read-only reviewer role: Claude Code identifies clarity,
  safety, and verification issues without editing files itself.
- Local rules: point Claude Code at `AGENTS.md`, `README.md`,
  `CONTRIBUTING.md`, and `SECURITY.md` explicitly at the start of a session,
  the same way the prompt template does, so it inherits this repo's rules
  before reviewing or editing anything.
- For implementation tasks (not just review), restate the same boundaries
  and add the exact files in scope, mirroring the pattern the research
  curation workflow below already uses for `/goal`-style custom commands.

## Task Intake Worksheet

| Question | Beginner-friendly answer to write down |
| --- | --- |
| What result do I want? | One sentence: a review verdict, a plan, or a specific small edit. |
| Read-only or editable? | Decide before starting; state it explicitly in the prompt. |
| Which files are in scope? | Exact files or globs for review or editing. |
| Which files are excluded? | Workflow YAML, secrets, generated files, unrelated docs. |
| What context does it need? | `AGENTS.md`, `README.md`, `CONTRIBUTING.md`, `SECURITY.md`, and the target file(s). |
| What proves the task is done? | A severity-ordered findings list, or a reviewed diff plus local checks. |
| What could cost money? | Model choice, session length, and retries under the current plan. |
| Who reviews the result? | The human reads the findings or `git diff` before any edit is committed. |

If the task could be read either as "review this" or "fix this," pick one
explicitly in the prompt; do not let the agent decide.

## Example Workflow: Task Intake To PR

1. **Task intake.** Decide whether this session is read-only review or an
   editable task, and name the exact files involved.
2. **Start Claude Code from the repo root** on a dedicated branch if edits
   are in scope:

   ```powershell
   git switch -c agent/claude-code-docs-review
   claude
   ```

3. **Scoped prompt.** Use
   [prompts/claude-code/review-docs.goal.md](../../prompts/claude-code/review-docs.goal.md)
   for review, or restate the same boundaries with edit permission explicitly
   granted for implementation.
4. **Agent work.** For review, expect a verdict and severity-ordered
   findings, not a diff. For implementation, expect a plan before any edit.
5. **Local checks.**

   ```powershell
   python scripts/repo_health_check.py
   python scripts/safe_autofix.py --check
   python -m unittest discover -s tests
   ```

6. **Diff review.** If edits were made, run `git diff` and read every changed
   line; if this was review-only, confirm no files changed at all.
7. **PR.** Push the branch and open a PR that states whether the session was
   review-only, plan-only, or implementation, plus checks run.

## Troubleshooting

| Symptom | Likely cause | Response |
| --- | --- | --- |
| A review session starts editing files | The prompt did not draw a hard line between review and implementation. | Stop, discard any partial edit, and restate the task as explicitly read-only. |
| Agent edits files unrelated to the review scope | Broad repo context or an ambiguous file list let the session drift. | Narrow the file list in the prompt; require it to name a file before touching it. |
| Session seems to lose earlier instructions mid-task | Context window filled with long output or many files read in one session. | Start a fresh session for a new task instead of extending one indefinitely. |
| CLI, IDE, or desktop integration doesn't activate | Install/update needs a restart, or the surface-specific feature is gated behind a setting. | Restart the surface and check current docs for the feature flag or setup step. |
| Findings reference stale file content after a `git pull` | Session read files before the pull, or local indexing/context is stale. | Start a new session after pulling so file reads reflect the current tree. |
| Custom `/command` doesn't run as expected | Wrong directory or filename for the current custom-command convention. | Verify the current custom-command directory and syntax in official docs before relying on it. |

## Setup Style

| Style | When to use it | Beginner note |
| --- | --- | --- |
| CLI | Terminal-driven codebase review and edits. | Verify current Windows shell guidance. |
| IDE | When editor diffs and selected files help review. | Good for visual review discipline. |
| Web/desktop | When the product surface supports code review or repo context. | Confirm current file access and privacy behavior. |
| Hybrid | Combine review in one surface with implementation in another. | Keep one branch and one source of truth. |

## Windows Suitability

Good when the current supported install path works on the user's Windows setup. For this repo, avoid workflows that require WSL, Docker, or large local dependencies.

## Hardware, API, Docker, and WSL Requirements

| Requirement | Practical guidance |
| --- | --- |
| Hardware | Lightweight for docs and review tasks. |
| API/account | Verify current account, plan, model, and usage requirements. |
| Docker | Not needed for this repo. |
| WSL | Not needed for this repo unless official setup requires it for a specific path. |
| GPU | Not needed. |

## Best First Task

Use Claude Code for a read-only documentation review:

```text
Review README.md for beginner clarity, public repository safety, and conservative claims.
Do not edit files.
Return findings ordered by severity, suggested edits, and claims that need official-doc verification.
```

## Prompt Template

```text
Target tool: Claude Code

Purpose:
Review documentation before an AI-generated PR is merged.

Instructions:
- Read AGENTS.md, README.md, CONTRIBUTING.md, and SECURITY.md.
- Do not edit files.
- Identify confusing beginner instructions.
- Identify unsupported or fast-changing tool claims.
- Identify missing safety warnings.
- Recommend the smallest useful edits.

Final report:
- Findings ordered by severity
- Suggested edits
- Files reviewed
- Checks not run
- Claims to verify in official docs
```

## Local Research Curation Workflow

Claude Code is a first-class alternative to Codex for the repository's local
research curation loop. The flow is the same: the cheap GitHub workflows prepare
a curator prompt, and a local agent does the actual guide edits on a branch.
No GitHub Actions workflow calls a model provider or needs an API key.

The helper script can set up the branch, fast-forward `main`, and copy the
latest curator prompt for you:

```powershell
.\scripts\local_autopilot.ps1 -Mode prompt -Scope hermes-agent -DryRun $true -MaxSources 5
.\scripts\local_autopilot.ps1 -Mode local-claude
```

`-Mode local-claude` defaults to the `claude/curate-research-guides` branch; pass
`-Branch <name>` to override it. To do the same steps by hand:

```powershell
git switch main
git pull --ff-only origin main
git switch -c claude/curate-research-guides
claude
```

Then set the task from the generated prompt at
`docs/research/curated/curator-prompt-YYYY-MM-DD.md`. You can paste the prompt
directly, or save a reusable custom slash command. Claude Code loads Markdown
files from `.claude/commands/` as `/command`, so a `.claude/commands/goal.md`
file containing the instructions lets you run `/goal` each session:

```text
Follow docs/research/curated/curator-prompt-YYYY-MM-DD.md exactly. Only edit the listed guide files, keep claims conservative, run the three local checks, and report files changed plus checks run.
```

`/goal` here is a custom command you define, not a built-in. Verify the current
custom-command directory and syntax in the official docs.

After Claude Code edits, review the diff and run the local checks before opening
a pull request for human review:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

The script never commits, never merges pull requests, never force-pushes, and
never deletes branches. Human review and merge stay manual.

## Permissions And Defaults

Claude Code's permission model governs which files it can read/edit and
which commands it can run, and the exact defaults depend on the surface
(CLI, IDE integration, desktop, or web) and current settings. Scope it down
by:

- Stating explicitly whether a session is read-only or editable before it
  starts, rather than relying on the tool to infer intent.
- Granting file-edit and command-execution permission only for the task at
  hand, not for the whole session by default.
- Reviewing any requested permission escalation (broader file access, shell
  execution) before approving it.
- Confirming current permission-model details in official docs rather than
  assuming an older tutorial's defaults still apply.

## Permission, Cost, And Data Guardrails

| Risk | Practical control |
| --- | --- |
| Review drifts into implementation | State "read-only, no edits" explicitly; treat any edit attempt as a stop condition. |
| Broad file or command permissions | Grant the narrowest scope the task needs; review escalation requests before approving. |
| Account/plan/model cost exposure | Verify current plan, model, and usage limits before a long session. |
| Secret exposure in findings or diffs | Never quote secret-looking values in output; name the file and flag it instead. |
| Stale product assumptions | Re-verify installation, surface behavior, and permission model against current official docs. |

## When To Prefer This Over The Others

Prefer Claude Code when you want a read-only review pass, a codebase
explanation, or a second opinion on a PR before merge, especially as a gate
ahead of implementation by another tool. Prefer Codex when you want an agent
that inspects the repo, edits files, runs checks, and reports in one
Git-first loop. Prefer Cursor or Windsurf when you want IDE-first visible
diffs during the editing step itself. Prefer Aider when you already know the
exact files to change and want a fast, explicit-file terminal loop.

## Safety Risks

- A review can drift into an implementation if the prompt is unclear.
- Permissioned tools may run commands or edit files unexpectedly.
- Tool, model, and plan details can become stale.
- Long explanations can hide missing verification.

## Review Checklist

- [ ] Was the task read-only or explicitly editable?
- [ ] Were the reviewed files listed?
- [ ] Were findings grounded in file references?
- [ ] Did the tool avoid private files and secrets?
- [ ] Were external claims marked for verification?
- [ ] Did the reviewer separate required fixes from optional improvements?

## When To Avoid It

Avoid Claude Code for:

- Tasks where no file access should be granted.
- Secret-heavy repositories unless the security model is explicitly approved.
- Broad rewrites without a reviewed plan.
- Cost-sensitive long sessions without usage awareness.

## Alternatives

| Alternative | Use when |
| --- | --- |
| Codex | You want implementation plus local checks in this repo. |
| Cursor | You want IDE-first planning and diffs. |
| GitHub Copilot | You want in-editor suggestions or GitHub issue-to-PR flow. |
| Aider | You want explicit-file terminal editing. |

## Verification Notes

Treat current installation commands, platform support, model access, plan limits, permissions, and tool integrations as official-doc verification items.

## Claims To Verify In Official Docs

- Current Claude Code installation path.
- Supported operating systems and shells.
- CLI, IDE, desktop, and web behavior.
- Permission model for file edits and command execution.
- Current model availability, limits, and pricing.
- Recommended security practices.

Official docs:

- <https://docs.anthropic.com/en/docs/claude-code/overview>
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **tool guide** surface. During broad
maintenance, reviewers should treat `docs/tools/claude-code.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `claude code` state what decision, workflow, or reusable behavior it supports?
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
