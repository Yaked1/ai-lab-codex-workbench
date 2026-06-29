# AGENTS.md

This file gives Codex and other AI coding agents the local rules for this repository. Read it before editing anything.

## Project Purpose

This is a public, student-friendly AI coding-agent and prompting guide. It teaches safe repository work with Codex and comparable tools: task intake, branch creation, prompt design, local checks, pull requests, review, controlled merge, rollback, changelog updates, and public-repository hygiene.

## Repository Profile

- Lightweight documentation, prompts, scripts, and templates.
- Windows and PowerShell friendly by default.
- Python standard library preferred.
- GitHub Actions used for validation and conservative automation.
- No heavy runtime dependencies.
- Avoid Docker, WSL, local model hosting, GPU-heavy tasks, and large dependency trees unless the user explicitly asks.

## Required Operating Rules

1. Run `git status` before making changes.
2. Inspect relevant files before editing.
3. Keep diffs small, focused, and tied to the requested task.
4. Do not edit unrelated files.
5. Do not delete files unless the user explicitly requests deletion.
6. Do not edit `.env`, `.env.*`, credentials, browser profiles, private documents, or secrets.
7. Do not add dependencies without explicit approval.
8. Do not run destructive commands.
9. Prefer Windows PowerShell commands in docs and final instructions.
10. Use conservative language for fast-changing external tools.
11. Mark product behavior, pricing, platform support, and model availability as items to verify in official docs.
12. Report anything you did not verify.

## Documentation Quality Rules

- Write for beginners first, but include enough detail for advanced users to audit the workflow.
- Prefer practical tables, checklists, command examples, prompt examples, and failure modes.
- Do not invent exact pricing, private model details, release claims, or unsupported features.
- Do not include secrets, personal data, private links, private repository URLs, or machine-specific private paths.
- For Codex references, keep guidance aligned with official concepts such as `AGENTS.md`, configuration, skills, subagents, local/IDE/web/cloud workflows, permissions, and reviewable goal-style work.
- For non-Codex tools, keep claims conservative and direct readers to official documentation.
- Link to deeper docs instead of making this file bloated.

## Safe Edit Boundaries

Safe by default:

- Markdown docs.
- Prompt templates.
- Standard-library Python scripts already present in the repo.
- Tests for existing scripts.
- GitHub Actions only when the task explicitly involves automation.

Avoid unless explicitly requested:

- Workflow YAML changes.
- Dependency installation.
- Package manager lock files.
- Broad rewrites across unrelated docs.
- Large generated artifacts.
- Binary files, images, archives, and model files.

## Local Checks

Run these after relevant changes:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

If a check fails:

- Fix the smallest likely cause when it is related to your change.
- Rerun the focused failing check.
- If the failure is unrelated to the requested task, report it clearly instead of rewriting the project.

## Approved Safe Commands

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

Never run commands that format disks, delete broad directories, expose secrets, force-push shared history, or modify system-wide settings.

## Branch, Commit, and PR Rules

- Use branches named `agent/<short-task-name>`.
- Keep one branch focused on one task.
- Commit messages should be concise and factual.
- Never claim tests passed unless they were actually run.
- Every PR should include what changed, why it changed, commands run, checks run, screenshots only for visual changes, and known limitations.

## Prompt Template Rules

Prompt templates in [prompts/](prompts/) should include:

- Target tool.
- Purpose.
- Full prompt.
- Short version.
- Inputs to fill.
- Success criteria.
- Safety boundaries.
- Verification steps.
- Final report format.
- Failure cases.

## Public Repository Hygiene

Before finalizing public-facing docs:

- Confirm no secrets or token-like examples are present.
- Confirm no private links, private account IDs, or private file paths are present.
- Keep external tool claims evergreen where possible.
- Add "verify in official docs" notes for fast-changing tool behavior.
- Update [CHANGELOG.md](CHANGELOG.md) for user-visible documentation or workflow changes.

## Deeper References

- Project overview: [README.md](README.md)
- Contribution workflow: [CONTRIBUTING.md](CONTRIBUTING.md)
- Security policy: [SECURITY.md](SECURITY.md)
- Agent lifecycle: [docs/workflows/agent-task-lifecycle.md](docs/workflows/agent-task-lifecycle.md)
- Public repo safety: [docs/workflows/public-repo-safety.md](docs/workflows/public-repo-safety.md)
- Tool comparison: [docs/tools/comparison-matrix.md](docs/tools/comparison-matrix.md)
- Codex start guide: [docs/codex/00-start-here.md](docs/codex/00-start-here.md)

## Definition of Done

A task is done only when:

- The requested change is complete.
- The diff is minimal and reviewable.
- Relevant checks were run.
- Failing checks are fixed or honestly reported.
- Public-safety constraints are preserved.
- The final response includes changed files, commands run, checks run, and remaining risks.
