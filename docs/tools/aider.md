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

## What Aider Is Good At Vs. Not

Aider is good at:

- Small, explicit-file edits where you already know which files matter.
- Fast terminal loops: describe a change, review the diff, commit, repeat.
- Repositories where Git history should stay clean and legible, since Aider
  is built around a commit-per-change workflow.
- Users who already think in "which files does this touch" terms.

Aider is not good at:

- Open-ended "explore the whole repo and find the bug" tasks. Its repo map
  helps orient the model, but it is not a substitute for you narrowing scope.
- Visual review. There is no diff viewer beyond your terminal and Git tooling,
  so pair it with a terminal that renders `git diff` well or review in an
  editor afterward.
- Users who want an agent to decide file scope for them. Aider's strength
  (explicit files) is also its limitation: if you add too few files, it can't
  see what it needs; if you add too many, review gets hard.

## Beginner Friendliness

Medium. The mental model is clear, but the user should be comfortable with:

- Starting from the repository root.
- Checking `git status`.
- Selecting files.
- Reading diffs.
- Running local checks.

## Using This Repository's Workflow With Aider

- Prompt template: [prompts/aider/agent-task.md](../../prompts/aider/agent-task.md).
  It already encodes the "selected files only" pattern this repo expects.
- Local rules: Aider reads repository-level conventions from a conventions or
  config file (commonly referenced as `.aider.conf.yml` or a plain
  instructions file passed with a read-only flag). Verify the current exact
  filename and loading behavior in official docs; do not assume the name
  without checking. Regardless of the mechanism, put the same content
  `AGENTS.md` already has in this repo (scope, safety boundaries, check
  commands) somewhere Aider reads automatically so you are not retyping it
  every session.
- Point Aider at `AGENTS.md` explicitly in your first message of a session if
  there is no automatic-loading mechanism configured, so it inherits this
  repo's rules before making any edit.

## Task Intake Worksheet

Use this short intake before opening Aider. It keeps the session from turning
into an unbounded terminal chat.

| Question | Beginner-friendly answer to write down |
| --- | --- |
| What result do I want? | One sentence, such as "clarify the Windows setup note in `docs/tools/aider.md`." |
| Which files are allowed? | Exact file paths to add with `/add`; avoid folders unless every file in the folder is in scope. |
| Which files are excluded? | Workflow YAML, secrets, generated files, unrelated docs, and anything the task does not name. |
| What context does Aider need? | `AGENTS.md`, the target file, and any directly related test or template file. |
| What proves the task is done? | A readable diff plus the local checks listed in this repo's AGENTS.md. |
| What could cost money? | Provider API calls, model retries, long sessions, or accidentally choosing a more expensive model. |
| Who reviews the result? | The human running Aider reads `/diff` or `git diff` before committing or pushing. |

If you cannot answer those questions in a few minutes, start with a read-only
question in your normal terminal or another planning tool before letting Aider
edit files.

## Context Selection Rules

Aider works best when the human chooses context deliberately.

- Add `AGENTS.md` or restate its rules at the start of the session so Aider
  sees the repository's safety boundaries.
- Add the smallest complete file set. For a Markdown page, usually add that
  page and, if needed, one linked template or index. For a script fix, add the
  script and its focused test.
- Do not add the repository root, a whole `docs/` tree, generated artifacts,
  archives, logs, screenshots, `.env` files, or browser/profile directories.
- If the agent says it needs another file, ask it to explain the reason first,
  then add the file yourself only if the reason is concrete.
- Use `/drop` to remove files when the task changes. Do not let old context
  from a previous task shape the next edit.
- Prefer command output summaries over pasting long logs into chat. Keep
  private paths, tokens, and account-specific output out of the session.

## Beginner Workflow Guidance

For a first Aider run in this repository, use a single Markdown file and a
single outcome:

1. Open PowerShell at the repository root and run `git status`.
2. Start Aider with auto-commit disabled.
3. Add only the target file and, if useful, `AGENTS.md`.
4. Ask for a short plan before edits.
5. Review `/diff` before accepting anything.
6. Run the repository checks yourself.
7. Commit only after the diff and checks both make sense.

Do not use Aider as a "fix everything" button. Treat it like a fast terminal
pair programmer that needs a narrow file list and a human reviewer.

## Example Workflow: Task Intake To PR

1. **Task intake.** Confirm `git status` is clean and you know exactly which
   file(s) the task touches.
2. **Start Aider from the repo root** and add only the files in scope:

   ```powershell
   git switch -c agent/aider-docs-update
   aider docs/tools/aider.md
   ```

3. **Scoped prompt.** Use the template in
   [prompts/aider/agent-task.md](../../prompts/aider/agent-task.md), filling in
   the selected files and the one-sentence task.
4. **Agent work.** Aider proposes an edit and, depending on your commit
   settings, stages or commits it. Confirm you know whether auto-commit is on
   before you start.
5. **Local checks.**

   ```powershell
   python scripts/repo_health_check.py
   python scripts/safe_autofix.py --check
   python -m unittest discover -s tests
   ```

6. **Diff review.** Run `git diff` (or `git show` if Aider already committed)
   and read every changed line.
7. **PR.** Push the branch and open a PR describing the task, files changed,
   and checks run.

## Troubleshooting

| Symptom | Likely cause | Response |
| --- | --- | --- |
| Aider wants to edit a file you did not add | Repo map or model inferred it needed a related file. | Approve deliberately if it is genuinely required, otherwise decline and narrow the prompt. |
| Repo map feels slow or truncated on a large repo | Repo map size scales with tracked files and can hit internal limits. | Add files explicitly instead of relying on repo-map inference; exclude large generated directories. |
| Unexpected Git author on new commits | Aider uses the local Git identity, which may be unset or wrong (e.g. a shared machine). | Run `git config user.name` / `git config user.email` and fix before committing. |
| Auto-commit creates commits you didn't expect to review | Auto-commit is enabled by default in some configurations. | Check current commit-behavior flags/config and disable auto-commit if you want to review before committing. |
| Diff includes unrelated whitespace or formatting changes | Editor or line-ending mismatch (CRLF vs LF) on Windows. | Check `.gitattributes` / `.editorconfig` and confirm Aider and your editor agree on line endings. |
| Provider call fails or hangs | Missing or misconfigured API credentials for the selected model provider. | Verify credential setup in official docs; never paste keys into chat or commit them. |

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

## Permissions And Defaults

By default, Aider can read and edit only the files you explicitly add to the
session (plus the repo map summary it builds for context). It runs shell
commands only when you ask it to or when a configured test/lint command is
set up to run automatically. Scope it down by:

- Adding only the files the task needs, not the whole directory.
- Leaving auto-commit and auto-test settings off until you understand them.
- Never adding `.env`, credential files, or private paths to a session.
- Running Aider from the intended repository root only, to avoid touching a
  sibling project by mistake.

## Permission, Cost, And Data Guardrails

| Risk | Practical control |
| --- | --- |
| Provider cost | Start with the cheapest suitable configured model, keep file context small, and stop retry loops quickly. |
| Unexpected auto-commit | Launch with auto-commit disabled until you understand the current config. |
| Shell command execution | Read every command before approval; run checks yourself if the command is unclear. |
| Secret exposure | Never add credential files or paste environment variable output into chat. |
| Wrong repository | Confirm `pwd` and `git status` before launch, especially on Windows where similar folders may be open. |
| Long context drift | Start a new Aider session for a new task rather than carrying stale files and chat history forward. |

For public documentation, avoid exact claims about model availability, pricing,
rate limits, or provider behavior unless you have just verified them in the
provider's official docs and can cite the date.

## When To Prefer Aider Over Other Tools In This Guide

Prefer Aider when you already know the exact file(s) to change and want a
fast, terminal-native, Git-committed loop without IDE overhead. Prefer an
IDE-first tool like Cursor or Windsurf instead when you want visible inline
diffs before anything touches Git, or Codex when you want an agent that
inspects the repo and decides file scope itself.

## Safety Risks

- Adding too many files can make output hard to review.
- Automatic commits, if enabled, can hide review steps.
- Provider credentials can be misconfigured.
- Running from the wrong directory can target the wrong repository.

## Review Checklist

- [ ] Was Aider launched from the repository root?
- [ ] Were only needed files added?
- [ ] Is automatic commit behavior understood?
- [ ] Was the task written as one measurable outcome?
- [ ] Did any added context include secrets, private paths, or generated logs?
- [ ] Does `git diff` show only expected changes?
- [ ] Were local checks run?
- [ ] Are provider and cost details verified or avoided?

## Final Report Expectations

A useful Aider final report should be brief but auditable:

- Name the exact files changed.
- Say whether auto-commit was enabled or disabled.
- List commands run and whether each passed.
- Call out any skipped check and why it was skipped.
- Identify any product behavior, pricing, model, or provider claim that still
  needs official-doc verification.
- Mention remaining risks, especially scope expansion, failed checks, or
  context that could not be inspected.

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
