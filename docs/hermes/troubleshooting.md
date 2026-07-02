# Hermes Agent Troubleshooting

Use this guide for public documentation workflows. For current product behavior,
verify official Hermes Agent docs and local `hermes --help` output.

Source status: official-doc anchored. License/source status: official
documentation plus official MIT-licensed repository; verify current commands
before publishing exact remediation steps.

This page assumes the reader already knows Hermes Agent's role in this
repository: a local, personal agent workspace for research and planning, not
the tool that edits and commits repository files. See
[hermes-agent.md](hermes-agent.md) for that boundary. Several symptom rows
below exist specifically because that boundary was ignored, not because
Hermes Agent misbehaved on its own.

Read "Likely cause" before applying a fix; if a symptom involved anything
touching this Git repository, also read
[public-repo-safety.md](public-repo-safety.md) before continuing.

## Install Problems

| Symptom | Likely cause | Response |
| --- | --- | --- |
| `hermes` is not recognized | PATH not refreshed after install. | Open a new terminal and check official install notes. |
| Installer fails on Windows | Missing dependency, network failure, or blocked script execution. | Review official Windows-native guide and rerun only after understanding the failure. |
| Setup completes but chat fails | Provider not configured. | Run official provider setup; do not paste keys into repo files. |

## Provider Problems

| Symptom | Likely cause | Response |
| --- | --- | --- |
| Authentication fails | Missing, expired, or wrong provider credential. | Re-run setup and keep secrets private. |
| Unexpected cost | Provider or tool usage is not bounded. | Set usage limits and avoid always-on jobs until reviewed. |
| Config mismatch | Manual edits conflict with setup commands. | Use `hermes config check` and `hermes config migrate` when official docs recommend them. |

## Memory Problems

| Symptom | Likely cause | Response |
| --- | --- | --- |
| Private facts appear in draft docs | Public task used private memory. | Stop, remove the draft, and separate public workflows from private memory. |
| Memory provider does not work | Provider setup incomplete. | Use `hermes memory status` and official provider docs. |
| Memory files appear in Git | Repo ignore rules or manual copy failed. | Remove from Git and rotate exposed secrets if needed. |

## Automation Problems

| Symptom | Likely cause | Response |
| --- | --- | --- |
| Job runs without review | Automation is too autonomous. | Disable it and require dry-run plus PR review. |
| Output goes to wrong place | Destination or gateway config is wrong. | Test with private dry-run output first. |
| Duplicate scheduled runs | Scheduler or gateway overlap. | Check official cron docs and lock behavior. |
| Job skips after model changes | Unattended job is not pinned to the new provider/model. | Review current official cron docs, then explicitly update the job only if the cost and provider choice are intended. |
| Job ignores repo instructions | Scheduled job did not run in the intended project directory. | Use a reviewed absolute work directory and confirm the output before publishing. |

## Unexpected File Edits

| Symptom | Likely cause | Response |
| --- | --- | --- |
| Hermes Agent output shows edits to repository files, not a draft | The session had write access to this repository and was treated as a Git-first editor, a role reserved for Codex or Claude Code. | Discard the edit. Re-run as a planning/drafting request, then feed the outline to Codex or Claude Code for the reviewable diff. See [hermes-agent.md](hermes-agent.md#role-boundaries-in-a-safe-workflow). |
| A file changed that was never named in the task | Scope was not stated, or a broad tool permission let the agent touch more than intended. | Revert the unrequested change with `git checkout -- <path>` (only after confirming no wanted work lives in it), then restate scope explicitly next run. |
| Draft content looks like it was written directly into a tracked file instead of returned as output | The working directory pointed at this repository instead of a scratch/private location. | Point the session at a private scratch directory for drafting; only a Git-first agent should write inside this repository. |
| Output references or duplicates unrelated files it was never shown | Broad file-read permissions let it pull in context beyond the task. | Narrow file access to the specific inputs for the task and re-run. |

## Stuck Or Hanging Sessions

| Symptom | Likely cause | Response |
| --- | --- | --- |
| Session stops producing output and never returns | A long-running tool call, network request, or provider call is blocked or the provider is rate-limited. | Cancel the session. Check provider status and quota before retrying. Do not leave an unattended job retrying indefinitely. |
| Agent repeats the same step or tool call in a loop | The task lacks a clear success condition, or the agent is retrying a failing tool call without a cap. | Stop the session. Restate the task with an explicit, checkable success criterion and a hard step or time limit. |
| Session appears to finish but the terminal or window never regains control | A background process (scheduled watcher, provider stream, shell subprocess) is still attached. | Close the session cleanly through its own exit command rather than killing the terminal; verify no orphaned process keeps calling the provider. |
| Memory or skill loading takes far longer than expected | Local memory store or skill index has grown very large or is corrupted. | Check `hermes memory status`, prune or archive old memory per official docs, and verify before resuming automation. |

## Branch And PR Conflicts

| Symptom | Likely cause | Response |
| --- | --- | --- |
| Hermes Agent output cannot be applied as a clean diff | Hermes Agent output is a draft artifact, not a Git diff; it was never meant to be applied directly. | Hand the draft to Codex or Claude Code as input context. Let that tool create the branch and commit inside its own working copy. |
| Two branches conflict because a Hermes-informed draft and a separate Git-first edit both touched the same doc | Planning output and repository editing ran in parallel without coordination. | Finish one branch, merge or close it, then re-run the other Git-first task against the updated `main` before opening a second PR. |
| PR review flags content that looks AI-generated without attribution | The draft was copied into a PR description or file without noting it came from Hermes Agent planning. | Label Hermes-informed sections clearly in the PR description per [public-repo-safety.md](public-repo-safety.md#publishing-rules). |
| Branch name or commit message contains private task context | A local task description leaked into `git commit` or `git branch` verbatim. | Rename the branch and amend the message to a factual, public-safe description before pushing. |

## Missing Or Skipped Local Checks

| Symptom | Likely cause | Response |
| --- | --- | --- |
| PR is opened without repository checks having been run | The task went straight from Hermes Agent draft to PR without routing through the Git-first workflow's check step. | Do not merge. Run the three repository checks locally and attach the results to the PR before requesting review. |
| `python scripts/repo_health_check.py` fails after a Hermes-informed doc edit | The draft included a secret-shaped string, a missing final newline, or an oversized file. | Fix the smallest cause the failure names, then rerun the single check rather than rewriting the whole file. |
| `python scripts/safe_autofix.py --check` reports formatting issues | Draft text used CRLF line endings, trailing whitespace, or was pasted without a trailing newline. | Run `python scripts/safe_autofix.py --write`, review the diff, then rerun `--check`. |
| `python -m unittest discover -s tests` was never run before merge | The final report claimed checks passed without evidence. | Never assert a check passed without running it in this session; run it now and report the real result. |

## Windows-Specific Path And Shell Issues

| Symptom | Likely cause | Response |
| --- | --- | --- |
| A command copied from a guide fails with "not recognized" in PowerShell | The example used a Unix-style command (`cat`, `export`) instead of a PowerShell equivalent. | Prefer PowerShell-native commands from this repository's docs; verify Hermes Agent's own CLI flags in official docs. |
| A path with spaces breaks a command | The path was not quoted. | Wrap the path in double quotes, for example `"C:\Users\<name>\Documents\project"`. |
| A file appears twice with different line endings after editing on Windows then Linux/WSL | Mixed CRLF/LF line endings from cross-platform editing. | Run `python scripts/safe_autofix.py --write`, which normalizes line endings to `\n` and re-adds a trailing newline. |
| PowerShell blocks a script from running | Execution policy restricts script execution. | Follow official Windows-native setup guidance for the current execution policy; do not disable execution policy protections repository-wide to force a script through. |
| A private local path leaks into a draft or command example | An absolute machine path was copied into output without redaction. | Remove the private path, use a placeholder or relative path, and check the draft against [public-repo-safety.md](public-repo-safety.md) before any PR. |

## Rate-Limit And Quota Errors

| Symptom | Likely cause | Response |
| --- | --- | --- |
| Provider call fails with a rate-limit or quota-exceeded error | Too many requests in a short window, or a plan/usage limit was reached. | Wait for the provider's cooldown window, verify current limits in the provider's docs, and avoid immediately retrying in a tight loop. |
| Scheduled job silently stops producing output | The job hit a quota ceiling and the schedule kept firing without alerting anyone. | Add a bounded retry with backoff per official docs, and check the job's own logs (kept private, not committed) for the failure reason. |
| Cost climbs faster than expected with no output change | An automation retries on every rate-limit error without a cap, multiplying provider calls. | Set explicit usage limits, disable the automation until reviewed, and confirm the fix in a private dry run before re-enabling. |
| Error message differs across providers for the same underlying limit | Providers report rate limits and quotas differently. | Do not assume one provider's error format generalizes; verify in the specific provider's docs and Hermes Agent's provider configuration docs. |

## Public Repository Recovery

1. Stop the automation.
2. Remove private files from the working tree.
3. Rotate any exposed secrets.
4. Review Git history if secrets were committed.
5. Add `.env`, local memory, logs, sessions, and OAuth files to ignore rules if
   they are not already excluded.
6. Re-run repository checks.

## Verification Commands

Use only after installation is complete:

```powershell
hermes --help
hermes config check
hermes memory status
```

Do not include command output in public docs if it contains private paths,
tokens, provider account details, or memory contents.

## When To Stop And Ask A Human

Stop the session and get maintainer input when a secret or credential-shaped
string appears in draft output or a proposed commit, the agent proposes
pushing directly to `main` or skipping review, a failure keeps recurring
after the documented fix, or task scope was unclear enough that you cannot
tell whether an edit was in-scope.

## Related Reading

- [hermes-agent.md](hermes-agent.md) for the role boundary that explains why
  several symptoms above route back to Codex or Claude Code.
- [public-repo-safety.md](public-repo-safety.md) for the checklist and
  incident-response steps once private state or a secret is involved.
- [prompting-hermes-agent.md](prompting-hermes-agent.md) for scoping a task
  well enough up front to avoid the stuck-session and unexpected-edit
  symptoms above.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **Hermes Agent guide** surface. During broad
maintenance, reviewers should treat `docs/hermes/troubleshooting.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `troubleshooting` state what decision, workflow, or reusable behavior it supports?
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
