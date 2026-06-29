# AGENTS.md

## Project purpose

This repository is a student-friendly AI agent and GitHub automation workbench. It teaches safe usage of Codex for repository creation, documentation, bug fixes, small features, commits, pull requests, CI checks, and controlled merges.

## User environment

- OS: Windows 11 Pro.
- Preferred shell: PowerShell.
- Laptop: Dell Latitude 5490.
- CPU: Intel Core i7-8650U.
- RAM: 8 GB.
- GPU: NVIDIA GeForce MX130 with about 2 GB VRAM.
- Practical rule: avoid Docker-heavy workflows, local large language models, heavy local image generation, and GPU-heavy tasks unless explicitly requested.

## Repository type

- Lightweight docs/scripts/template repository.
- No heavy runtime dependencies.
- Python standard library preferred.
- GitHub Actions used for validation and controlled automation.

## Codex operating rules

1. Read this file before editing anything.
2. Run `git status` before making changes.
3. Inspect the relevant files before editing.
4. Make small, focused diffs.
5. Do not edit unrelated files.
6. Do not delete files unless the user explicitly requests deletion.
7. Do not edit `.env`, `.env.*`, credentials, browser profiles, private documents, or secrets.
8. Do not install dependencies without explicit approval.
9. Do not run destructive commands.
10. Prefer Windows PowerShell commands when giving user-facing instructions.
11. Run local checks after changes:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

12. If a check fails, fix the smallest likely cause and rerun the focused check.
13. If a failure is outside the requested task, report it instead of rewriting the project.

## Approved safe commands

Generally safe inside this repository:

```powershell
git status
git diff
git branch
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python scripts/safe_autofix.py --write
python -m unittest discover -s tests
```

Use caution and ask before:

```powershell
pip install ...
npm install ...
gh repo delete ...
git clean -fd
Remove-Item -Recurse -Force ...
```

Never run commands that format disks, delete broad directories, expose secrets, or modify system-wide settings.

## Branch and commit rules

- Use branches named `agent/<short-task-name>`.
- Commit messages should be concise and factual.
- Never claim tests passed unless they were actually run.
- Keep each PR focused on one task.

## Pull request expectations

Every PR should include:

- What changed.
- Why it changed.
- Commands run.
- Tests/checks run.
- Screenshots only if the change affects visuals.
- Known limitations.

## Definition of done

A task is done only when:

- The requested change is complete.
- Relevant checks were run.
- Failing checks are fixed or honestly reported.
- The diff is minimal.
- The final response includes changed files, commands run, and remaining risks.
