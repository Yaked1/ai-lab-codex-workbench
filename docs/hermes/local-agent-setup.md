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

## Failure Modes

| Symptom | Likely cause | Response |
| --- | --- | --- |
| `hermes` command not found | PATH not refreshed or install failed. | Open a new terminal and check official install logs. |
| Setup asks for provider credentials | A provider has not been configured. | Use environment variables or official secret setup; do not paste keys into docs. |
| Gateway/tool features fail | Missing dependencies or incomplete setup. | Run official diagnostics or setup commands before adding automations. |

## Weak Laptop Realism

Hermes Agent can still be useful on weak laptops for documentation and public
research workflows, but avoid using the laptop as a heavy local model or GPU
serving host. Keep heavy compute in browser/API/cloud workflows.
