# Security Policy

## Main rule

This repository is for safe AI-agent learning and GitHub automation. It must not contain secrets, private documents, credentials, tokens, or dangerous automation.

## Secrets

Never commit:

- `.env` files.
- API keys.
- GitHub tokens.
- Browser cookies.
- SSH private keys.
- School/private account credentials.

## Agent permissions

Codex and other agents should stay inside the repository folder. They should not edit system settings, browser profiles, Downloads, Documents outside the repo, or private files.

## Reporting a problem

Open a GitHub issue using the bug report template. Do not paste secrets into the issue.

## Safe automation policy

Automated workflows may:

- run tests,
- check formatting,
- apply deterministic whitespace cleanup,
- open pull requests for review.

Automated workflows must not:

- merge without CI and review,
- delete repository history,
- change secrets,
- install unknown dependencies,
- modify files outside the repository.
