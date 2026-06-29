# Hermes Agent Troubleshooting

Use this guide for public documentation workflows. For current product behavior,
verify official Hermes Agent docs and local `hermes --help` output.

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
