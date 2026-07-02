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

## Choosing A Provider Path

For this repository, provider documentation should stay generic unless the
current official Hermes Agent docs and the provider docs have both been checked.
Beginner-facing examples should focus on the decision process rather than
claiming that one provider, plan, or model is always available.

Use this table when writing or reviewing provider guidance:

| Question | Public-safe guidance |
| --- | --- |
| Does the reader already have an account? | Tell them to follow that provider's official setup flow. |
| Is pricing mentioned? | Link to official pricing instead of copying numbers. |
| Is a model name mentioned? | Mark availability as something to verify. |
| Is a token required? | Use an environment-variable placeholder only. |
| Is local state created? | Explain that it stays outside the public repository. |

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

## Private State Inventory

Provider setup can create useful local state that must stay private. Before
copying commands, screenshots, logs, or troubleshooting output into a public
guide, scan for:

- Provider keys and bearer tokens.
- OAuth refresh tokens or browser session references.
- Account IDs, tenant IDs, workspace IDs, or project IDs.
- Local absolute paths to Hermes home folders.
- Model-provider billing or quota details.
- Private tool gateway URLs.
- Chat transcripts, memories, or scheduled job payloads.

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

## Documentation Pattern

When adding provider-specific material, prefer this shape:

1. Name the provider and link to official docs.
2. State that pricing, region support, model names, and account requirements
   may change.
3. Show placeholder environment-variable examples only.
4. Explain how to verify the configuration locally.
5. Explain which generated files must stay out of Git.

This keeps the guide useful without turning it into a stale setup mirror.

## API Key Handling: The Core Rule

Whatever the provider, the same rule applies: a credential that can reach a
paid API or a private account must never exist as plain text inside this
repository's working tree, in a commit, in a PR description, or in a code
block that gets pasted into an issue or chat log. Practically, that means:

- Treat every provider key as equivalent to a password. Do not paste it into
  a terminal command that gets logged, a shared document, or a screenshot.
- If a key was ever pasted somewhere it should not have been (a public
  gist, a shared chat, a committed file), treat it as compromised and rotate
  it immediately rather than hoping no one saw it.
- Prefer a key with the narrowest scope the provider offers (project-scoped
  over account-wide, read-only over read-write) when the provider supports
  scoped keys.

## Environment Variable Vs Config-File Storage

Hermes Agent, like most provider-backed agent tools, generally supports both
an environment-variable path and a config-file path for credentials. Both are
valid for local use; they carry different risks for a public-repo-adjacent
workflow.

| Storage method | Where it lives | Public-repo safety notes |
| --- | --- | --- |
| Environment variable (session-scoped) | Set in the current PowerShell session only. | Safest for one-off testing; disappears when the terminal closes, so nothing persists to accidentally commit. |
| Environment variable (user/machine profile) | Persisted via `setx` or Windows user environment settings. | Convenient for repeated local use; still never touches the repo, but remember it persists across reboots and other tools on the same machine can read it. |
| Config file under Hermes home | A file such as `config.yaml` or `.env` under the Hermes home directory, outside this repository. | Safe as long as that directory is genuinely outside the Git working tree and is never copied into the repo for "documentation" purposes. |
| Config file inside a repository working tree | Same shape as above, but placed inside a cloned project folder. | Unsafe by default. If a tool ever defaults to writing config inside the current working directory, move it out or add it to `.gitignore` immediately and verify it was never staged. |

For this repository specifically: never let a provider config file, `.env`,
or credential-bearing file land inside `ai-lab-codex-workbench-main`. If a
setup flow suggests a project-local config, redirect it to the user's Hermes
home directory or an environment variable instead.

## Verifying A Provider Connection Before Running A Real Task

Before trusting a provider configuration with a real (possibly billed) task,
verify the connection with the smallest possible check:

1. Run the current official "check" or "status" command (for example
   `hermes config check` or the current equivalent) and confirm it reports a
   healthy provider connection rather than a missing-credential error.
2. Send one trivial, disposable prompt (for example, "reply with the word
   ok") and confirm a response comes back from the expected provider/model,
   not an error or a silent fallback.
3. Confirm the response did not echo back a raw key, token, or internal
   config path — if it did, treat that as a leak and rotate the credential.
4. Only after steps 1 to 3 pass, move on to a real read-only task, and only
   after that succeeds, consider any write-capable or scheduled task.

Skipping straight to a real task without this check risks discovering a
misconfiguration (wrong provider, expired token, wrong project) only after an
unattended job has already run with the wrong settings.

## Troubleshooting Table: Auth Failures

| Symptom | Likely cause | Response |
| --- | --- | --- |
| "Unauthorized" or 401-style error | Key is missing, expired, revoked, or was never set in the active session. | Re-run the official setup/config command; confirm the environment variable or config file actually contains a current key. |
| "Forbidden" or 403-style error | Key is valid but lacks permission for the requested model, project, or endpoint. | Check the provider's dashboard for key scope and project/model access; use a key with the correct scope rather than widening permissions blindly. |
| Command hangs waiting for input | An interactive OAuth or portal flow expected a browser step that did not complete. | Re-run the setup command in a normal terminal with browser access; avoid running first-time auth flows inside restricted or headless sessions. |
| Config check passes but real requests fail | Config file and environment variable disagree, or a stale cached token is being reused. | Run the official config-check/diagnostic command; clear cached auth state per official docs, then re-authenticate. |
| Works locally, fails in a scheduled job | Scheduled job runs under a different user/session context that does not see the same environment variables. | Pin credentials explicitly for the scheduled job per official docs, or confirm the job inherits the correct environment before enabling it unattended. |
| Key appears to work but responses look wrong or truncated | Provider/model mismatch, or a quota/rate limit is silently degrading output. | Verify the configured model name and current quota status in the provider's own dashboard; do not assume Hermes Agent's default model matches what you intended. |
| Secret visible in terminal output or logs | A command echoed the key, or verbose/debug logging captured it. | Stop the job, rotate the credential immediately, and redact or delete the log before it is shared or committed. |
