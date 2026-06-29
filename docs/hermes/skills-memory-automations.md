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

## Failure Modes

| Area | Failure | Response |
| --- | --- | --- |
| Skills | Skill trigger is too broad. | Narrow description and allowed actions. |
| Memory | Private facts leak into output. | Keep public tasks separate from private memory. |
| Automations | Scheduled work runs without review. | Require dry-run, branch, PR, checks, review, merge. |
| Provider config | Token appears in logs. | Stop the job, rotate credentials, redact logs. |
| Cron workdir | Scheduled job runs in the wrong project. | Use an explicit reviewed working directory and test with dry-run output. |
| Model routing | Unattended job would use the wrong provider or model. | Pin provider/model only after checking current official docs and cost exposure. |

## Evaluation Checklist

- [ ] Skill source and license are labeled.
- [ ] Memory is private and excluded from Git.
- [ ] Automations are manually reviewed before publishing.
- [ ] No direct push to `main`.
- [ ] No private chats, logs, OAuth files, or tokens are published.
