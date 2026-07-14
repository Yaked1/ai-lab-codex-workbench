# Pull Request

## Outcome

Describe the observable result and the user or maintainer it helps.

## Scope

- Included files or areas:
- Explicitly excluded files or actions:
- Related issue:

## Evidence

- Commands run and exact results:
- Source or claim verification, when applicable:
- Screenshots or rendered output, when applicable:
- Skipped checks and reason:

## Safety and review

- [ ] I read `AGENTS.md` and preserved unrelated work.
- [ ] No secrets, credentials, private paths, or private links were added.
- [ ] No unapproved destructive action, dependency change, workflow change, or publication occurred.
- [ ] Current product claims are dated and sourced.
- [ ] The final diff contains only files mapped to this PR's scope.
- [ ] Changelog and documentation links were updated when reader-visible behavior changed.

## Checks

- [ ] `python scripts/repo_health_check.py`
- [ ] `python scripts/safe_autofix.py --check`
- [ ] `python -m unittest discover -s tests`
- [ ] `git diff --check`

## Reviewer focus

Name the riskiest assumption, file, or behavior the reviewer should inspect.
