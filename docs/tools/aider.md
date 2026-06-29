# Aider

## What It Is

Aider is an AI pair-programming tool for the terminal. Its strength is explicit file selection: you choose the files in scope, describe the task, review the diff, and keep Git in the loop.

Verify current installation, model provider, authentication, and pricing exposure in official docs before teaching setup.

## Best Use Cases

| Use case | Fit | Notes |
| --- | --- | --- |
| Explicit-file Markdown edit | Strong | Excellent first task. |
| Small bug fix | Strong | Add only relevant files and tests. |
| Test update | Strong | Keep scope tight. |
| Terminal pair programming | Strong | Good for Git users. |
| Whole-repo exploration | Medium | Use read-only commands first. |
| Huge refactor | Weak | Too many files can overload review. |

## Beginner Friendliness

Medium. The mental model is clear, but the user should be comfortable with:

- Starting from the repository root.
- Checking `git status`.
- Selecting files.
- Reading diffs.
- Running local checks.

## Setup Style

| Style | When to use it | Beginner note |
| --- | --- | --- |
| CLI | Primary Aider workflow. | Good after terminal basics. |
| Local/hybrid | Depends on selected model provider. | Keep provider credentials out of Git. |
| Git-based | Natural fit for branch workflows. | Review commits before pushing. |

## Windows Suitability

Good when Python and Git are installed. Verify current install guidance and provider setup before a workshop.

## Hardware, API, Docker, and WSL Requirements

| Requirement | Practical guidance |
| --- | --- |
| Hardware | Lightweight for docs and small code edits. |
| API/account | Provider-dependent; verify current requirements. |
| Docker | Not needed for this repo. |
| WSL | Not needed for this repo. |
| GPU | Not needed for API-backed use. |

## Best First Task

Run Aider with one Markdown file selected and ask for a small wording improvement. Review the diff before committing.

## Prompt Template

```text
Target tool: Aider

Selected file:
[path/to/file.md]

Task:
Improve this section for beginner clarity without changing the meaning.

Boundaries:
- Edit only the selected file.
- Do not add dependencies.
- Do not edit secrets or workflow YAML.
- Keep claims about external tools conservative.

Verification:
- Run python scripts/repo_health_check.py
- Run python scripts/safe_autofix.py --check
- Run python -m unittest discover -s tests

Final report:
- Summary
- Diff notes
- Checks run
- Risks
```

## Safety Risks

- Adding too many files can make output hard to review.
- Automatic commits, if enabled, can hide review steps.
- Provider credentials can be misconfigured.
- Running from the wrong directory can target the wrong repository.

## Review Checklist

- [ ] Was Aider launched from the repository root?
- [ ] Were only needed files added?
- [ ] Is automatic commit behavior understood?
- [ ] Does `git diff` show only expected changes?
- [ ] Were local checks run?
- [ ] Are provider and cost details verified or avoided?

## When To Avoid It

Avoid Aider for:

- Users who cannot yet read terminal output.
- Very large multi-file rewrites.
- Repositories where provider credentials are not configured safely.
- Tasks that require visual IDE context.

## Alternatives

| Alternative | Use when |
| --- | --- |
| Codex | You want an agent to inspect, edit, run checks, and report. |
| Cursor | You want visible editor diffs. |
| Claude Code | You want explanation or review before editing. |
| OpenCode | You want another open-source terminal agent comparison. |

## Verification Notes

Verify install commands, provider configuration, model support, auto-commit behavior, Windows shell guidance, and pricing exposure.

## Claims To Verify In Official Docs

- Current installation method.
- Supported Python and Git versions.
- Provider and model setup.
- Auto-commit settings.
- Windows behavior.
- Pricing and usage limits through selected providers.

Official docs:

- <https://aider.chat/docs/>
