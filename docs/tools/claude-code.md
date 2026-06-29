# Claude Code

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

## Beginner Friendliness

Medium. Claude Code can explain reasoning clearly, which helps learners understand a codebase. The risk is that beginners may accept broad suggested rewrites because the explanation sounds confident. Start with review-only prompts.

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
