# Security Policy

## Main Rule

This repository is for safe AI-agent learning and public GitHub automation. It must not contain secrets, credentials, private documents, private links, personal account data, or dangerous automation.

## Supported Security Scope

This project provides:

- Documentation safety rules.
- Simple secret-pattern checks in `scripts/repo_health_check.py`.
- Deterministic whitespace cleanup in `scripts/safe_autofix.py`.
- Conservative GitHub Actions workflows.
- Public-repository review checklists.

This project does not provide:

- A complete enterprise security scanner.
- Secret rotation.
- Dependency vulnerability management beyond the current lightweight scope.
- Production deployment hardening.
- Automated approval of AI-generated code.

## Secrets and Private Data

Never commit:

- `.env` or `.env.*` files.
- API keys.
- GitHub tokens.
- Browser cookies.
- SSH private keys.
- Passwords.
- Private account credentials.
- Private repository URLs.
- Personal emails, account IDs, or private machine paths.
- Screenshots that reveal user names, tabs, file paths, or accounts.

Do not include fake secrets that look real enough to trigger scanners. Use placeholders such as:

```text
YOUR_API_KEY_HERE
YOUR_GITHUB_TOKEN_HERE
```

## Agent Permission Policy

Codex and other agents should:

- Work inside this repository.
- Inspect files before editing.
- Keep changes scoped to the task.
- Ask before installing dependencies.
- Ask before changing workflow YAML.
- Report commands they ran.

Agents should not:

- Edit system settings.
- Read browser profiles.
- Read private folders outside the repository.
- Print environment variables.
- Modify secrets.
- Run destructive commands.
- Auto-merge generated code without review.

## GitHub Actions Policy

Automated workflows may:

- Run repository health checks.
- Check formatting.
- Run unit tests.
- Apply deterministic whitespace cleanup.
- Open pull requests for review.
- Merge a reviewed PR only through an explicit manual workflow and required checks.

Automated workflows must not:

- Print secrets or environment variables.
- Delete repository history.
- Force-push shared branches.
- Install unknown dependencies.
- Modify files outside the repository.
- Merge AI-generated work without review.

## Public Release Checklist

Before public release or external teaching:

- [ ] Run `python scripts/repo_health_check.py`.
- [ ] Run `python scripts/safe_autofix.py --check`.
- [ ] Run `python -m unittest discover -s tests`.
- [ ] Review `git diff`.
- [ ] Review GitHub Actions logs.
- [ ] Search docs for private links and account details.
- [ ] Verify external tool claims in official docs.
- [ ] Confirm `CHANGELOG.md` records user-visible changes.

See [docs/workflows/public-repo-safety.md](docs/workflows/public-repo-safety.md) for the full guide.

## Broad Expansion Security Review

Large documentation and prompt-expansion passes deserve a security review even
when they do not change runtime code. They often add examples, command blocks,
source references, agent permissions, workflow descriptions, and staging
instructions, which are common places for unsafe details to slip in.

Before staging a broad expansion, review:

| Area | Security question | Safer outcome |
| --- | --- | --- |
| Examples | Do any examples look like real keys, tokens, account IDs, emails, or private URLs? | Use placeholders such as `YOUR_TOKEN_HERE` and generic repository-relative paths. |
| Commands | Do commands print environment variables, read browser profiles, or operate outside the repo? | Keep commands scoped to the repository and validation tools. |
| Agent permissions | Does the text encourage agents to read private folders, change system settings, or run destructive commands? | State ask-first or forbidden boundaries. |
| External claims | Are fast-changing setup, pricing, model, or platform details stated as permanent? | Mark them for official-doc verification. |
| Source usage | Is local archive, leaked prompt, or license-unclear material copied into public docs? | Use structural lessons only and write original guidance. |
| Staging | Could unrelated dirty work be staged with the expansion? | Inspect `git status` before and after staging. |

For research-grade documentation work, security evidence should appear in the
final report or PR body. A useful statement is:

```text
Security review:
- Repository health check passed.
- No generated artifacts were added.
- Commands stay inside the repository.
- External product claims are conservative or marked for verification.
- Staged paths match the requested scope.
```

## Reporting a Problem

Open a GitHub issue if you find a public-safety problem, unsafe automation behavior, or documentation that encourages risky agent use.

Do not paste secrets into an issue. If a secret was committed, rotate it outside this repository first, then report the cleanup need without revealing the secret value.
