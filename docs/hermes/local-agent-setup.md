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
