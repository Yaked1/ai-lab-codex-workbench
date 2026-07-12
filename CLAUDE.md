# Project brief
This repository is an AI prompting and agent-workflow knowledge base.
Preserve useful content, remove junk, keep changes reviewable.

# Common commands
- Run tests: `python -m unittest discover -s tests`
- Health check: `python scripts/repo_health_check.py`
- Autofix check: `python scripts/safe_autofix.py --check`
- Diff check: `git diff --check`

# Rules
- Prefer scripts for deterministic repo-wide edits.
- Do not rewrite prose unless explicitly asked.
- Do not delete skills, prompts, docs, or workflows unless explicitly instructed.
- Every completion claim must cite a command result, diff, or file check.
