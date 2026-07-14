# Aider Agent Task Template

## Target Tool

Aider, the terminal-based AI pair-programming tool. Works with any supported
model provider (Anthropic, OpenAI, local models via Ollama, etc.) that you
configure separately. This template assumes you invoke `aider` from a
PowerShell prompt at the repository root and drive it through its chat
interface and in-chat commands (`/add`, `/drop`, `/diff`, `/undo`).

## Purpose

Use this template for terminal pair programming where the human explicitly
chooses the exact files Aider may see and edit, then reviews every diff
before it lands. Aider's core behavior is different from IDE agents: it
edits files directly on disk and, by default, creates a Git commit after
each accepted edit. This template exists to make that behavior safe and
predictable for a small, well-scoped documentation or script change in this
repository.

## Inputs To Fill

| Input | Description | Example |
| --- | --- | --- |
| `{selected_files}` | Exact files added to the Aider session with `/add`. | `README.md`, `docs/tools/aider.md` |
| `{task}` | One-sentence description of the change. | `Add a Windows install section` |
| `{out_of_scope}` | Files or actions explicitly excluded. | `No workflow YAML, no dependencies, no other docs pages` |
| `{commit_mode}` | Whether Aider may auto-commit each edit. | `Disabled - I will review and commit manually` |
| `{checks}` | Local checks to run after edits. | `repo health, safe autofix, unit tests` |

## Task Intake Checklist

Fill this in before launching Aider:

- Desired outcome: one sentence that can be checked in the final diff.
- Selected files: exact paths to add with `/add`; no wildcards unless the
  task genuinely owns every matching file.
- Excluded files: workflow YAML, generated artifacts, secrets, unrelated docs,
  and any file the task does not mention.
- Current repo state: `git status` output reviewed, including any pre-existing
  changes that are not yours.
- Review owner: the human who will read `/diff` or `git diff` before commit.
- Cost boundary: provider/model choice understood, no long retry loop, and no
  paid usage surprises for a workshop or shared account.
- Verification proof: commands or manual checks that must appear in the final
  report.

If any line is unclear, ask Aider a read-only planning question first instead
of starting with an edit.

## Context Selection Rules

- Add only files that the task needs to understand and edit.
- Include `AGENTS.md` either as a selected/read-only file or by pasting a short
  instruction to read it before edits.
- For docs work, add the target page plus one linked template or index only if
  consistency requires it.
- For script work, add the script and its focused test. Do not add the full
  `scripts/` directory by default.
- Do not add `.env`, credentials, browser profiles, private notes, private
  paths, logs with account data, archives, binaries, screenshots, or generated
  package outputs.
- If another file seems necessary, stop and ask for approval before `/add`.
- Use `/drop` after a task changes so stale context does not influence the next
  edit.

## Before Starting

- Start from the repository root in PowerShell: `cd path\to\repo`.
- Run `git status` and confirm the working tree is clean or that any
  existing changes are intentional and yours.
- Launch Aider with auto-commit disabled so you control when commits happen:
  `aider --no-auto-commits`.
- Add only the files needed for the task with `/add {selected_files}`. Do
  not use `/add .` or wildcard-add a whole directory unless the task
  genuinely requires every file in it.
- Confirm provider credentials (API keys) are set as environment variables
  or in a gitignored `.env` file, never typed into the chat or committed.
- If Aider proposes adding a file you did not list, stop and confirm before
  accepting with `/add`.

## Full Prompt

```text
Target tool:
Aider

Selected files (already added with /add):
{selected_files}

Task:
{task}

Out of scope:
{out_of_scope}

Commit mode:
{commit_mode}

Instructions:
- Read and follow AGENTS.md before proposing any edit.
- Edit only the files listed in "Selected files". If another file needs a
  change, stop and tell me which file and why instead of adding it yourself.
- Keep the diff small, focused, and reviewable in one pass.
- Preserve existing meaning, structure, and headings unless the task says
  otherwise.
- Match the existing Markdown style and heading casing in each file.
- Do not add dependencies or new packages.
- Do not edit .env, .env.*, credentials, browser profiles, private links,
  private paths, or any folder outside the selected files.
- Do not modify GitHub Actions workflow YAML.
- Do not run destructive commands (no git reset --hard, no git push --force,
  no recursive deletes).
- Do not invent exact pricing, model availability, benchmark numbers, or
  platform support claims for any AI tool; use conservative language and
  flag anything that needs official-doc verification.
- If auto-commit is disabled, stop after proposing edits and let me review
  with /diff before I commit manually.

Success criteria:
- The requested change is complete and matches "{task}".
- No file outside {selected_files} is changed.
- The diff is small enough to read in under two minutes.
- Local checks pass, or failures are reported honestly with their output.

Validation (run in PowerShell after Aider proposes edits):
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests
- git diff --check

Final response:
- Summary of what changed and why
- Files changed (exact paths)
- Commands run
- Checks run and their pass/fail result
- Anything Aider could not verify (mark for manual follow-up)
- Remaining risks
```

## Short Version

```text
In Aider, with only {selected_files} added and auto-commit off: {task}.
Follow AGENTS.md, touch no other files, no secrets/dependencies/workflow
edits, no invented tool claims, run the repo health/autofix/unittest checks,
then report files changed, commands run, check results, and risks before I
commit.
```

## Included Scope

- Exactly the files passed to `/add` for this session (for example
  `README.md`, `docs/tools/aider.md`, a single script under `scripts/`).
- Documentation prose, Markdown tables, and code comments inside those
  files.
- Small, additive edits to existing tests for a script already in scope.
- Local verification commands run from PowerShell after Aider proposes
  edits.

## Excluded Scope

- Any file not explicitly added with `/add`, including files Aider
  discovers via search or suggests adding mid-session.
- Secrets, `.env` / `.env.*` files, credentials, API keys, browser profiles,
  private links, and machine-specific private paths.
- Dependency installation (`pip install`, `npm install`), lock file changes,
  GitHub Actions workflow YAML, and generated archives or binaries.
- Automatic Git commits unless `{commit_mode}` explicitly enables them.
- Repository-wide reformatting or rewrites outside the named task.

## Safety Boundaries

- Aider writes directly to disk and can auto-commit per edit by default.
  Always start with `aider --no-auto-commits` for anything beyond a trivial,
  already-trusted change, so you can inspect `/diff` before committing.
- Only files added via `/add` are writable in a given session; never let the
  model talk you into a blanket `/add .`.
- Treat any file Aider wants to touch outside `{selected_files}` as a scope
  violation: stop and confirm first.
- Never paste API keys, tokens, or `.env` contents into the Aider chat; keep
  provider credentials in environment variables outside the repository.
- Do not accept a proposed edit you have not read. Use `/diff` before
  committing and `/undo` if a commit turns out to be wrong.
- Do not run shell commands Aider suggests without reading them first;
  Aider can execute commands you approve, and destructive ones (`git clean
  -fd`, `Remove-Item -Recurse -Force`) require explicit human confirmation
  per this repo's AGENTS.md.

## Permission And Cost Notes

- Aider can modify files directly and may auto-commit depending on current
  configuration. Treat write access as active once the session starts.
- Provider usage may be metered. Keep context small, avoid unnecessary retries,
  and verify current model/provider pricing in official docs before teaching
  setup.
- Do not ask Aider to display environment variables, API keys, tokens, or
  provider configuration files. Debug authentication outside chat.
- If a command would push, force-push, delete files, rewrite history, install
  packages, or publish artifacts, stop and get explicit human approval.
- Public docs should use conservative language for tool behavior and mark
  pricing, platform support, model availability, and defaults as
  official-doc verification items.

## Verification

```powershell
git status
git diff
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
git diff --check
```

Run these after Aider proposes edits and before you commit. If auto-commit
is enabled and a check fails, use `/undo` to revert the last Aider commit
rather than leaving a broken commit in history.

## Verification Checklist

- [ ] `git status` reviewed before and after the Aider run.
- [ ] `/diff` or `git diff` contains only the selected files.
- [ ] No secret-looking values, private links, or private paths were added.
- [ ] Markdown links and command examples still make sense for Windows users.
- [ ] Required checks were run, or skipped checks are named with a reason.
- [ ] Any claim about external tool behavior is either cited/dated or marked
      for official-doc verification.

## Success Criteria

- Only the files listed in `{selected_files}` changed.
- The task described in `{task}` is fully addressed, not partially stubbed.
- The diff reads cleanly in `git diff` with no unrelated hunks.
- All local checks pass, or any failure is reported with the exact command
  and output rather than glossed over.
- No secrets, credentials, or private paths appear anywhere in the diff.

## Final Report Format

```markdown
## Summary
## Files changed
## Commands run
## Checks/tests
## Claims needing manual verification
## Remaining risks
```

## Final Report Expectations

The report should be concrete enough for a maintainer to audit without opening
the full chat transcript:

- Exact paths changed.
- Whether auto-commit was enabled.
- Which commands ran and their pass/fail result.
- Any command Aider suggested but the human declined.
- Scope exceptions requested and whether they were approved.
- Remaining risks, including skipped checks, unverified official-doc claims,
  or any file Aider wanted but did not receive.

## Failure Cases

| Failure | What to do |
| --- | --- |
| Aider says it needs another file not in `{selected_files}` | Stop, ask Aider which file and why, then explicitly `/add` it yourself before continuing. |
| Aider touches a file outside the selected set (visible in `/diff` or `git diff`) | Use `/undo` if already committed, or discard the unstaged change; re-add only the files needed and restate the boundary. |
| A verification command fails after the edit | Read the failure output, fix the smallest related cause, and rerun the single failing check before rerunning the full suite. |
| Aider makes an exact claim about a tool's pricing, model support, or platform availability | Reject the wording, ask for conservative phrasing, and add a note that it needs official-doc verification. |
| Auto-commit was left on and produced an unwanted commit | Run `/undo` immediately (or `git reset --soft HEAD~1` if outside the Aider session) before making further edits. |
| Provider authentication fails mid-session | Report the failure without pasting the key or token; check environment variables outside the chat. |
| Aider suggests a long retry loop or a larger model to "fix" a vague task | Stop, narrow the prompt and file list, and verify cost exposure before continuing. |
| The final summary says checks passed but does not name commands | Treat the result as unverified and run the commands yourself before commit. |
