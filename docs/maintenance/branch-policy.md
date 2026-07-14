# Branch Namespace and Retirement Policy

## Active namespaces

| Namespace | Intended owner and use | Publication rule |
| --- | --- | --- |
| `agent/<topic>` | General coding-agent task branches | Pull request and review |
| `codex/<topic>` | Codex-authored repository work | Pull request and review |
| `cleanup/<topic>` | Deterministic, explicitly bounded cleanup | Pull request and review |
| `autopilot/<run-id>` | One generated-content automation run | Per-run branch and pull request; never a permanent accumulating branch |

A branch name does not grant permission to change protected files, publish a
release, bypass tests, or merge itself.

## Retirement

After a pull request is merged or abandoned, record the disposition before
removing the branch. Remote deletion is an owner action and must not be inferred
from local files. Do not delete a branch that contains unmerged work, an open
pull request, release evidence, or an unresolved incident record.

Stale historical namespaces should be documented as `keep`, `merge`, `archive`,
or `delete after verification`. Repository automation must not silently reuse a
per-run `autopilot/` branch.

## Required checks

Branch protection should require the repository health check, safe-autofix
check, unit tests, Windows runtime gate, and any focused package or site checks
introduced by the change. Whether those settings are active must be verified in
GitHub, not claimed from this document.
