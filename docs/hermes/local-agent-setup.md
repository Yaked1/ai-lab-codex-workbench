# Hermes Agent Local Setup

Source status: official-doc anchored. The commands below are from official
Hermes Agent installation documentation as of 2026-06-29. Verify the official
installation guide before teaching or publishing them:
<https://hermes-agent.nousresearch.com/docs/getting-started/installation>

License/source status: official documentation plus official MIT-licensed
repository. Link to the source instead of copying installer scripts.

## Recommended First Choice

For beginners on macOS or Windows, the official docs recommend the Hermes
Desktop installer for the command-line and desktop applications. Use the
official download page rather than copying installer binaries into this
repository.

## Command-Line Install

Linux, macOS, WSL2, or Android Termux:

```powershell
# Run in the appropriate shell, not necessarily PowerShell.
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

Native Windows PowerShell:

```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

After installing, official docs point users to setup:

```powershell
hermes setup --portal
```

For users who do not want the portal path, official docs also expose the general
setup and model/tool configuration commands:

```powershell
hermes setup
hermes model
hermes tools
hermes gateway setup
```

If the official docs change, replace these commands rather than preserving stale
copies.

## Verification Steps

```powershell
hermes --help
hermes setup --portal
```

If `hermes setup --portal` is not appropriate for the user, follow the current
official setup flow for the provider they intend to use.

## Setup Decision Flow

Use the smallest setup that matches the learner's goal:

| Goal | Recommended path |
| --- | --- |
| Read the guide only | No Hermes install required. |
| Try the CLI locally | Official installer, then `hermes --help`. |
| Configure a provider | Official setup flow plus private secret storage. |
| Use tools or gateway features | Review enabled tools before write-capable work. |
| Build public docs | Keep Hermes local state outside this repository. |

Do not ask beginners to install heavy local model stacks, GPU runtimes, or
containerized serving layers just to follow this repository. Those topics are
outside the Hermes Agent guide scope here.

## Windows Notes

- Open a new PowerShell after installation so PATH changes are visible.
- Do not commit `%LOCALAPPDATA%` paths or local Hermes data.
- Do not commit `.env`, `auth.json`, logs, memory files, sessions, or OAuth
  files.
- If a guide references Windows-native behavior, verify it in the official
  Windows guide first.

## Linux/macOS Notes

- Prefer per-user installs for personal machines.
- Avoid running installer commands with `sudo` unless the official docs and the
  user's environment require it.
- Keep `~/.hermes/` private.

## Public Documentation Rules

When documenting a Hermes setup in this repository:

- Link to the official installer instead of copying installer scripts.
- Avoid screenshots that expose local paths, account names, or provider state.
- Use placeholders for provider credentials.
- Mark exact command behavior as official-doc anchored and refresh it before
  release.
- Separate setup instructions from automation instructions.
- Keep memory, sessions, logs, cron jobs, and gateway state out of Git.

## Failure Modes

| Symptom | Likely cause | Response |
| --- | --- | --- |
| `hermes` command not found | PATH not refreshed or install failed. | Open a new terminal and check official install logs. |
| Setup asks for provider credentials | A provider has not been configured. | Use environment variables or official secret setup; do not paste keys into docs. |
| Gateway/tool features fail | Missing dependencies or incomplete setup. | Run official diagnostics or setup commands before adding automations. |
| Public guide includes local state | Troubleshooting output was copied too broadly. | Remove private material, rotate exposed secrets if needed, and update the guide with placeholders. |

## Entry-Level Hardware Realism

Hermes Agent can still be useful on entry-level hardware for documentation and
public research workflows, but avoid using such a machine as a heavy local model
or GPU serving host. Keep heavy compute in browser/API/cloud workflows.

## Completion Checklist

- [ ] Official installation docs were checked before publishing exact commands.
- [ ] `hermes --help` or the current official equivalent was tested locally if
  setup claims are being made.
- [ ] Provider secrets and local Hermes state stayed outside the repository.
- [ ] Any failed setup step is described as a troubleshooting note, not hidden.
- [ ] The guide still treats Hermes Agent as an agent/workflow tool, not as
  Hermes language-model coverage.

## Prerequisites

Confirm these before starting the install, so a failure later is easier to
diagnose:

| Prerequisite | Why it matters | How to check in PowerShell |
| --- | --- | --- |
| Windows PowerShell available | The official Windows install command runs in PowerShell. | `$PSVersionTable.PSVersion` should print a version, not an error. |
| Network access to the official install host | The installer downloads from the official Hermes Agent domain. | Confirm you can reach the official docs site in a browser first. |
| A place to keep provider secrets outside this repo | You will need to store a provider key locally, never inside this repository. | Decide now: environment variable or a config file outside the repo folder (see [provider-configuration.md](provider-configuration.md)). |
| No expectation of GPU or Docker | This repo's guidance avoids GPU-heavy and Docker-heavy setups as beginner defaults. | Not applicable; just confirm you are not trying to combine this with a heavy local model stack. |
| A disposable public task in mind | The first real run should be read-only and low-stakes. | Pick one public URL or file you are comfortable summarizing as a test. |

## Windows PowerShell-First Walkthrough

This walkthrough assumes native Windows PowerShell, not WSL, and assumes you
have not installed Hermes Agent before.

1. **Open a fresh PowerShell window.** Do this even if you already had one
   open, so any prior PATH state does not mask install problems later.

2. **Run the official Windows install command** (verify current syntax
   against the official install page before running):

   ```powershell
   iex (irm https://hermes-agent.nousresearch.com/install.ps1)
   ```

3. **Close and reopen PowerShell.** This refreshes PATH so the new `hermes`
   command is visible in the current session.

4. **Verify the binary is on PATH:**

   ```powershell
   hermes --help
   ```

   If this fails with "command not found," the install did not complete or
   PATH was not refreshed. Reopen PowerShell once more before assuming the
   install itself failed.

5. **Run the official setup flow:**

   ```powershell
   hermes setup --portal
   ```

   Follow the interactive prompts. If the portal path is not right for your
   provider choice, use the general setup and model commands instead:

   ```powershell
   hermes setup
   hermes model
   ```

6. **Verify the provider connection before doing anything real.** See
   [provider-configuration.md](provider-configuration.md) for the specific
   verification steps (status/check command, one disposable prompt, confirm
   no secret is echoed back).

7. **Review enabled tools before running a write-capable task.** Use the
   current official tools command (for example `hermes tools`) to see what
   the agent can access, and disable anything you do not need yet.

## First Safe Test Task

Do not point Hermes Agent at this repository, or any repository, for the
first task. Instead:

1. Pick one public URL or paste one public block of text you already trust.
2. Ask Hermes Agent, in a fresh session, to summarize it and list any claims
   that would need a source check.
3. Do not grant write or shell tool access for this first task; keep it to
   read/summarize only if the current setup lets you scope tools that way.
4. Confirm the output stays on-topic, cites the source you gave it, and does
   not invent private context it could not have had.

This is deliberately boring. The goal is to see the agent's default behavior
before it has memory, skills, or automations layered on top.

## How To Confirm It Worked

Work through these checks in order; each one rules out a different class of
"looks like it worked but did not" problem:

| Check | What "it worked" looks like | What a failure looks like |
| --- | --- | --- |
| Binary check | `hermes --help` prints usage text. | "Command not found" or a shell error. |
| Setup check | `hermes setup --portal` (or the current equivalent) completes without an unhandled error. | The flow crashes, hangs, or loops back to the same prompt. |
| Provider check | The official status/check command reports a connected provider. | It reports missing credentials or an auth error (see the troubleshooting table in [provider-configuration.md](provider-configuration.md)). |
| First-task check | The disposable summarization task returns a relevant, source-grounded answer. | The output is generic, ignores the source you gave it, or references content you never provided. |
| Privacy check | No secrets, tokens, account IDs, or local file paths appear in the output or in anything you are about to paste elsewhere. | Any of those appear in a response, a log, or a screenshot you were about to share. |

Only once every row in that table is green should you consider a second,
slightly less trivial task, and only after reading
[public-repo-safety.md](public-repo-safety.md) should any output influence
this repository.

## First Run Checklist

Use this as a final gate before calling the first run "done":

- [ ] `hermes --help` (or the current official equivalent) ran successfully
      in a fresh PowerShell window.
- [ ] Setup completed and a provider is configured.
- [ ] The provider connection was verified with a real check, not assumed.
- [ ] Enabled tools were reviewed; nothing unnecessary was left switched on.
- [ ] The first task was read-only, disposable, and used a public source.
- [ ] The output was inspected for source grounding and private-data leakage.
- [ ] No provider secret, config file, log, or local path was pasted into any
      shared or public location during this process.
- [ ] You know where local Hermes state lives and have confirmed it is
      outside this repository's working tree.
