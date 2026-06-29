# Hermes Agent Provider Configuration

Source status: official-doc anchored. Verify current configuration behavior in
the official Hermes Agent configuration docs:
<https://hermes-agent.nousresearch.com/docs/user-guide/configuration>

License/source status: official documentation plus official MIT-licensed
repository. Provider names, plan behavior, and pricing can change; verify them
in current provider and Hermes docs.

## What Providers Mean

In Hermes Agent, a provider is the configured service or endpoint that supplies
the agent's AI responses or tool gateway access. Provider setup is separate from
the public repository and must be treated as private user configuration.

## Configuration Files

Official docs describe Hermes settings under the user's Hermes home directory,
including files such as configuration, `.env`, auth data, memories, skills,
cron jobs, sessions, and logs. Treat those files as private local state.

Never commit:

- `.env`
- provider tokens
- OAuth files
- auth files
- local memory
- sessions
- logs
- private conversations

## Safe Placeholder Pattern

Use environment variable placeholders in public docs:

```powershell
$env:PROVIDER_API_KEY = "replace-with-your-key"
```

Do not include real keys, realistic token examples, or private provider account
IDs.

## Verified Configuration Commands

Official docs list these configuration commands:

```powershell
hermes config
hermes config edit
hermes config set KEY VAL
hermes config check
hermes config migrate
```

Use specific provider examples only when verified from current official docs.
For public beginner guides, prefer:

```powershell
hermes setup --portal
hermes model
```

## Tool And Terminal Safety

Official configuration docs describe local and container-backed terminal modes.
For a public beginner guide, assume the agent may have access to the user's
files and commands unless the current setup explicitly constrains tools. Tell
learners to review enabled tools with official commands and disable anything
they do not need before running write-capable tasks.

## Public-Safe Provider Checklist

- [ ] Does the doc explain where secrets live?
- [ ] Are all keys placeholders?
- [ ] Are provider names and availability verified?
- [ ] Are subscription or pricing claims avoided or linked to official docs?
- [ ] Does the workflow avoid direct pushes to `main`?
- [ ] Are local/private Hermes files excluded from Git?

## Failure Modes

| Failure | Cause | Response |
| --- | --- | --- |
| Provider auth fails | Missing or invalid key/OAuth state. | Re-run official setup and keep secrets out of docs. |
| Config value goes to wrong file | Manual edits bypassed expected config behavior. | Use official config commands or review `config.yaml` and `.env` privately. |
| Private config appears in a PR | Local state was copied into repo docs. | Remove it, rotate exposed secrets if needed, and review history. |
