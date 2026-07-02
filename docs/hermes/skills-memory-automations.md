# Hermes Agent Skills, Memory, And Automations

Source status: official-doc anchored. Verify current behavior in official
Hermes Agent docs before publishing exact commands.

Source links:

- Skills: <https://hermes-agent.nousresearch.com/docs/user-guide/features/skills>
- Memory: <https://hermes-agent.nousresearch.com/docs/user-guide/features/memory>
- Cron: <https://hermes-agent.nousresearch.com/docs/user-guide/features/cron>
- Official repository: <https://github.com/NousResearch/hermes-agent>
- License/source status: official docs and official MIT-licensed repository.

## Skills

Hermes Agent skills are reusable task instructions. Official skill pages show
bundled and optional skills with metadata, file paths, versions, platforms, tags,
and source references.

Official docs describe skills as local knowledge documents stored under Hermes
home and loaded on demand. Treat local skills as private unless you deliberately
author a public-safe example for this repository.

Public guide requirements:

- Explain what the skill does.
- Say whether it is bundled, optional, local, or repo-shipped.
- Include install commands only when verified.
- Include test steps.
- Include safe and unsafe use cases.
- Include public repository safety notes.

Example optional skill install command from an official skill page, only for
that specific verified skill:

```powershell
hermes skills install official/creative/hyperframes
```

Do not generalize one skill's install command to every skill.

### Using this repository's skill catalog with Hermes

This repository's [skills/](../../skills/) folder already uses the Hermes
tap-compatible shape: each skill is a directory containing `SKILL.md`.
There are three practical install routes:

```powershell
# Direct local user install through this repository's installer.
python scripts/install_skill.py --skill use-codex-safely --harness hermes --scope user

# PowerShell equivalent.
.\scripts\install_skill.ps1 -Skill use-codex-safely -Harness hermes -Scope user

# After the branch is public, Hermes can install one skill directly from GitHub.
hermes skills install Yaked1/ai-lab-codex-workbench/skills/use-codex-safely
```

For a project-local dry run or reviewed staging pass, omit `-Scope user` /
`--scope user`. The installer writes `.agent-skills/hermes/<slug>/SKILL.md`.
To let Hermes read that staged directory, add it to `skills.external_dirs` in
`~/.hermes/config.yaml` after review:

```yaml
skills:
  external_dirs:
    - C:/path/to/ai-lab-codex-workbench/.agent-skills/hermes
```

The staged files are complete `SKILL.md` bundles, not placeholders. They still
inherit the same public-repo safety rules as the rest of this repository: no
private paths, no secrets, no direct push to `main`, and no Hermes language
model, quantization, GGUF, Ollama, vLLM, or SGLang coverage in Hermes Agent
skills.

## Memory

Hermes Agent memory is persistent context. Official memory docs list:

```powershell
hermes memory setup
hermes memory status
```

Official memory-provider docs also document:

```powershell
hermes memory off
```

Official memory docs also describe write-approval controls for memory and skill
writes. For public documentation workflows, prefer approval or manual review
before allowing persistent memory or skill changes to influence published text.

Public safety:

- Keep memory private.
- Do not commit memory files.
- Do not publish private user facts.
- Do not use private memory as source material for public docs.
- Keep memory provider credentials out of Git.

## Automations

Hermes Agent automations can use scheduled tasks. Official cron docs describe
the built-in scheduler and lock behavior. Automation blueprints are useful for
learning, but public repo publishing must still be manually reviewed.

Official cron docs also describe fresh sessions for scheduled jobs, optional
skill attachment, delivery targets, project `workdir` behavior, and provider or
model pinning for unattended runs. Public guides should present those as
advanced review items, not beginner defaults.

Safe automation pattern:

1. Draft the automation as a private local experiment.
2. Use dry-run or read-only mode first.
3. Review the output manually.
4. Create a branch and PR for public docs.
5. Run checks.
6. Merge only after review.

Unsafe automation pattern:

- Always-on job that writes polished public docs daily.
- Direct push to `main`.
- Job that reads private memory and publishes it.
- Job that uses provider keys from a public repo.

## Scoping Skills, Memory, And Automations Safely For A Public Repo

Hermes Agent's persistent features (skills, memory, cron) are designed for an
ongoing personal workspace, not for a public Git repository. Before turning any
of them on, decide what "safe scope" means for that specific feature in this
project.

### Skills: scope by allowed action, not by topic

A skill description alone ("summarize research candidates") is not a safety
boundary. Scope a skill by:

- **Allowed inputs.** Public URLs the user supplies, or files explicitly
  pasted into the session. Not "browse the web" or "read my downloads folder."
- **Allowed outputs.** A private local draft file, a chat response, or a
  memory note. Not a direct write into this repository's tracked files.
- **Allowed tools.** If the skill only needs to read and summarize, it does
  not need shell access, file write access, or network write access.

Concrete example: a "research candidate triage" skill for this repo should be
scoped as "read a list of public URLs the user pastes in, return a source
ledger with title/URL/status labels." It should not be scoped as "crawl the
web for AI agent news and file a PR," because that turns a summarization skill
into an unreviewed publishing pipeline.

### Memory: scope by what it is allowed to remember and recall

Memory is useful for continuity across sessions, but a public-repo-adjacent
workflow should treat memory as strictly local and private:

- Do not let memory persist repository secrets, API keys, or internal file
  paths, even temporarily.
- Do not let a later session recall private memory and paste it into a public
  doc or PR description as if it were a verified public source.
- If memory stores task history ("last time we drafted the Hermes comparison
  page"), that is fine as private workflow context. It stops being safe the
  moment it becomes the cited source for a public claim.
- Periodically review `hermes memory status` (or the current official
  equivalent) and clear entries that reference private paths, credentials, or
  one-off debugging sessions that should not accumulate indefinitely.

### Automations: scope by blast radius, not by convenience

A scheduled job's safety scope is defined by what it can touch while no one is
watching:

- **Read-only jobs** (checking a public page for updates, drafting a private
  summary) are the safest default for unattended scheduling.
- **Write-capable jobs** (editing files, opening PRs, calling a provider with
  billed usage) should never run unattended against this repository. Require a
  human to trigger the actual repository edit through Codex or Claude Code
  after reviewing the automation's draft output.
- Pin the working directory, provider, and model explicitly for any scheduled
  job. Do not let a cron job inherit "whatever the last interactive session
  used," because that setting can drift after an unrelated local change.

## Checklist: Review An Automation Before Letting It Run Unattended

Walk through this list every time before enabling a new scheduled job, and
again after any change to an existing one:

- [ ] The job's working directory is explicit and reviewed, not inherited.
- [ ] The job is read-only, or its write target is a private/local file, not a
      tracked repository file.
- [ ] The job cannot push, commit, or open a PR by itself.
- [ ] Provider and model are pinned, not left to default resolution.
- [ ] The job has been run once manually (dry-run or supervised) before being
      scheduled.
- [ ] The job's trigger condition (time, file change, event) is specific
      enough that it cannot fire on an unintended branch, file, or directory.
- [ ] Output goes somewhere a human reviews before anything public happens
      with it (a private draft, a notification, a queue file).
- [ ] Memory or skill state the job depends on has been checked for stale or
      private content.
- [ ] There is a way to stop or disable the job quickly if it misbehaves.
- [ ] The job does not require secrets to be embedded in its own config file
      inside a repository working tree.

## Failure Modes

| Area | Failure | Response |
| --- | --- | --- |
| Skills | Skill trigger is too broad. | Narrow description and allowed actions. |
| Memory | Private facts leak into output. | Keep public tasks separate from private memory. |
| Automations | Scheduled work runs without review. | Require dry-run, branch, PR, checks, review, merge. |
| Provider config | Token appears in logs. | Stop the job, rotate credentials, redact logs. |
| Cron workdir | Scheduled job runs in the wrong project. | Use an explicit reviewed working directory and test with dry-run output. |
| Model routing | Unattended job would use the wrong provider or model. | Pin provider/model only after checking current official docs and cost exposure. |
| Automation runs on the wrong branch | Scheduled job's working directory was left pointed at a stale checkout, or the branch was switched interactively between runs. | Pin an explicit working directory and branch check inside the job; verify the branch before any write step, abort if it does not match. |
| Memory leaks a secret into a later session | A credential, token, or private path was pasted into a session and got picked up as a memory candidate, then surfaced again in an unrelated later task. | Treat memory as untrusted input the same way you treat file input; scan recalled memory for secret-shaped strings before using it, and clear the offending entry. Rotate any credential that was actually exposed. |
| Automation triggers on an unintended file change | A file-watch or broad-glob trigger fired on a generated file, a temp file, or an unrelated docs edit instead of the intended target. | Narrow the trigger to specific paths, add a debounce or confirmation step, and test the trigger condition against a few known-good and known-bad file changes before trusting it unattended. |

## Evaluation Checklist

- [ ] Skill source and license are labeled.
- [ ] Memory is private and excluded from Git.
- [ ] Automations are manually reviewed before publishing.
- [ ] No direct push to `main`.
- [ ] No private chats, logs, OAuth files, or tokens are published.
- [ ] Every scheduled job passed the "review an automation" checklist above
      before being enabled.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **Hermes Agent guide** surface. During broad
maintenance, reviewers should treat `docs/hermes/skills-memory-automations.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `skills memory automations` state what decision, workflow, or reusable behavior it supports?
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
