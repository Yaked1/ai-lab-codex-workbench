# Prompt Audit Checklist

Use this checklist before giving a prompt to an AI coding agent, before publishing a prompt guide, or before teaching a workflow from a public repository.

The audit goal is simple: make the prompt specific enough to execute, narrow enough to review, and safe enough for a public repo.

## Beginner Path

1. Read the prompt out loud once.
2. Underline the objective.
3. Circle the files in scope.
4. Mark the files and actions out of scope.
5. Confirm there are verification steps.
6. Confirm there is a final report format.
7. Remove secrets, private links, private paths, and personal data.

Beginner pass/fail rule:

```text
If the prompt does not say what to edit, what not to edit, and how to verify the result, do not send it yet.
```

## Advanced Path

Use this path for prompts that will be reused, published, or handed to students.

1. Check whether the prompt can accidentally authorize broad filesystem access.
2. Check whether it asks for exact facts about fast-changing tools.
3. Check whether it allows dependency installation or workflow YAML changes.
4. Check whether it gives the agent a recovery path for conflicts and unrelated test failures.
5. Check whether it requires the agent to report commands and verification honestly.
6. Check whether the prompt can be executed on Windows without Docker, WSL, or GPU-heavy assumptions.
7. Test the prompt on a disposable branch before publishing it.

## Quick Audit Table

| Area | Question | Pass condition |
| --- | --- | --- |
| Objective | Is there one primary outcome? | One clear task, not a bundle of unrelated requests. |
| Scope | Are included paths named? | The agent can identify the likely files. |
| Exclusions | Are risky paths excluded? | Secrets, private files, dependencies, and workflow YAML are controlled. |
| Safety | Does it forbid private data? | No secrets, tokens, private links, private paths, or personal data. |
| Verification | Are checks listed? | Commands or manual checks are explicit. |
| Reporting | Is the final format clear? | Summary, files, commands, checks, risks. |
| External claims | Are fast-changing facts controlled? | "Verify in official documentation" appears where needed. |

## Red Flags

Stop and revise the prompt if it says or implies:

- "Fix everything."
- "Clean up the whole repo."
- "Install whatever you need."
- "Use my token below."
- "Search my whole computer."
- "Auto-merge when done."
- "Delete anything unused."
- "State current pricing/model access without checking."
- "Connect to my private account and make changes."

## Required Prompt Sections

For agentic coding tasks, include:

```text
Objective:

Context:

Scope:
- Include:
- Exclude:

Safety:

Verification:

Final report:
```

For review-only tasks, add:

```text
Mode:
Review only. Do not edit files.

Findings format:
- Severity
- File and line
- Issue
- Suggested fix
```

## Prompt Examples

### Documentation Edit

```text
Read AGENTS.md and docs/workflows/public-repo-safety.md.

Objective:
Add a short checklist for reviewing offline HTML documentation.

Scope:
- Include: docs/workflows/public-repo-safety.md, CHANGELOG.md
- Exclude: scripts, tests, dependencies, workflow YAML

Safety:
- No external trackers, analytics, CDNs, remote fonts, secrets, private links, or private paths.
- Mark fast-changing tool behavior as "verify in official documentation."

Verification:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check

Final report:
- Summary
- Files changed
- Commands run
- Checks run
- Remaining risks
```

### Review-Only Prompt

```text
Review the current diff only. Do not edit files.

Prioritize:
- Bugs
- Public-safety risks
- Unverified fast-changing claims
- Missing checks

Format findings first, ordered by severity, with file and line references.
Then list open questions and test gaps.
```

## Safe Command Labels

Use labels in prompt guides so beginners can tell what is safe.

Safe repo-local commands:

```powershell
git status
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

Placeholder external command:

```powershell
# Verify this command in official docs before running.
# Replace placeholders before use.
# Do not paste secrets into commands.
npx TOOL_NAME@latest --help
```

Risky commands that need explicit approval:

```powershell
pip install ...
npm install ...
git clean -fd
Remove-Item -Recurse -Force ...
```

## Public Repo Safety Questions

- [ ] Could this prompt cause the agent to read outside the repository?
- [ ] Could it cause the agent to print environment variables or secrets?
- [ ] Could it cause the agent to modify credentials, browser profiles, or private documents?
- [ ] Could it create private links or private machine paths in docs?
- [ ] Could it create screenshots or logs that reveal personal data?
- [ ] Could it add external scripts, trackers, analytics, CDNs, or remote fonts to static HTML?
- [ ] Could it state exact pricing, plan access, model names, or platform support without verification?
- [ ] Could it auto-merge or force-push without review?

## Common Mistakes

| Mistake | Why it fails | Audit fix |
| --- | --- | --- |
| Missing final report | You cannot tell what actually happened. | Add required report bullets. |
| Missing stop condition | Agent may keep editing around unrelated failures. | Add "report unrelated failures clearly." |
| Too much trust in tool knowledge | Tool behavior changes. | Add official-doc verification notes. |
| No branch instruction | Work may happen on the wrong branch. | Require `git status` and branch awareness. |
| No public-safety scan | Private data can leak. | Add secret, link, and path review. |

## Review Checklist

- [ ] One objective.
- [ ] Clear audience.
- [ ] Relevant files named.
- [ ] Excluded files named.
- [ ] No secrets or private data.
- [ ] No dependency install unless approved.
- [ ] No workflow YAML change unless requested.
- [ ] Safe Windows-friendly commands.
- [ ] Verification commands listed.
- [ ] Fast-changing claims marked for official-doc verification.
- [ ] Final report required.
- [ ] Failure behavior defined.

## Failure Modes

| Failure mode | Prompt audit miss | Prevention |
| --- | --- | --- |
| Agent changes unrelated files | Scope and exclusions missing. | Name include and exclude paths. |
| Agent invents setup commands | Official-doc rule missing. | Require verification for fast-changing tools. |
| Agent exposes private data | Filesystem boundary missing. | Restrict work to repo and forbid private paths. |
| Agent skips checks | Verification optional. | Make checks required or require skipped-check explanation. |
| Agent over-fixes | Failure handling missing. | Say to report unrelated failures instead of broad rewrites. |

## Publishable Prompt Guide Checklist

Before publishing a prompt guide:

- [ ] It works as plain text without private context.
- [ ] It uses placeholders for all user-specific values.
- [ ] It says "Replace placeholders before use" where needed.
- [ ] It says "Do not paste secrets into commands" where needed.
- [ ] It avoids exact pricing, plan, model, and platform claims.
- [ ] It includes public-safe examples only.
- [ ] It has a license or attribution note if copied from another public source.
- [ ] It was tested on a disposable branch or clearly marked as untested.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `docs/guides/prompt-audit-checklist.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `prompt audit checklist` state what decision, workflow, or reusable behavior it supports?
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
