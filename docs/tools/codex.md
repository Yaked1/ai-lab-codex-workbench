# OpenAI Codex

OpenAI Codex is a coding agent workflow for reading a repository, editing files, running commands, and helping prepare changes for review. In this repo, Codex is treated as the reference workflow because the project began as a Codex workbench.

## Best For

- Small documentation edits.
- Bug fixes with tests.
- Repository cleanup inside a branch.
- Pull request preparation.
- Repeated workflows expressed as `/goal` prompts.

## Beginner Fit

Codex is beginner-friendly after the user understands Git branches, diffs, and local checks. It is not a replacement for review. Treat it as a fast collaborator that still needs a clear task and a constrained work area.

## Windows Fit

Good for this repo's PowerShell-first workflow. Keep tasks inside the repository folder, run the Python checks locally, and review diffs before committing.

## Surface

Codex may be used through CLI, IDE, web, or hybrid surfaces depending on the current product and account setup. Verify the official documentation before teaching installation or plan details.

## Main Risks

- Allowing edits outside the requested scope.
- Running commands without understanding their effect.
- Trusting generated summaries without checking the diff.
- Assuming current product behavior from older docs.

## Best First Task

Ask Codex to improve one paragraph in `README.md`, then run:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

## Official Docs

- <https://developers.openai.com/codex/cli>
