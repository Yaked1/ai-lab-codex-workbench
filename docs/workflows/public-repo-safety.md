# Public Repository Safety

Use this checklist before making the repository public, before accepting an AI-generated pull request, and before teaching from a fork.

## Identity and Git Checks

- Confirm commits use a GitHub noreply email or another public-safe email.
- Confirm no private account names, school account IDs, or personal machine details appear in docs.
- Confirm branch names and commit messages do not include sensitive project names.

## Secret Checks

- Confirm no `.env` or `.env.*` files are tracked.
- Search for API keys, tokens, private keys, cookies, and passwords.
- Check prompt templates for fake-looking examples that might be mistaken for real secrets.
- Review GitHub Actions logs for accidental environment output.

## Link and Data Checks

- Confirm all links are public.
- Remove private repository links, private dashboards, school portals, personal cloud links, and internal documents.
- Do not include screenshots that reveal user names, emails, file paths, private tabs, or account details.

## Automation Checks

- Confirm CI only reads repository content and runs safe checks.
- Confirm autofix only performs deterministic formatting cleanup.
- Confirm merge workflows require human intent and passing checks.
- Confirm no workflow auto-merges AI-generated code without review.
- Confirm workflows do not print secrets or account tokens.

## Agent Checks

- Confirm the agent task was scoped to the repository.
- Confirm the agent did not edit unrelated files.
- Review every generated diff.
- Run the strongest realistic local checks.
- Keep a written summary of commands run and known limitations.

## Release Gate

Before public release, run:

```powershell
git status
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

If any check fails, fix the smallest relevant cause or clearly document the failure before release.
