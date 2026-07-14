# Safe Automerge Policy

Safe generated-file automerge exists only for mechanical research artifacts,
including explicitly allowlisted generated documentation. It does not merge
curated guide content, code changes, workflow changes, or policy changes. If
you remember one rule from this page: automerge is for source-queue artifacts,
never for prose a human or an agent wrote for readers.

## Branch Requirement

Only pull requests from branches starting with this prefix are considered:

```text
autopilot/
```

Pull requests from other branches must use normal human review and merge.

## Allow/Deny Path Table

The changed files in the PR must be limited to this exact allowlist. This
mirrors the Research Automation Rules in `AGENTS.md` and the logic in
`scripts/check_safe_generated_diff.py`.

| Path | Allowed for automerge | Reason |
| --- | --- | --- |
| `data/research/candidates.json` | Yes | Exact-path match; deterministic scout output. |
| `docs/research/inbox/*.md` | Yes | Any `.md` file directly inside `docs/research/inbox/`. |
| `docs/research/curated/curator-prompt-*.md` | Yes | Must start with `curator-prompt-` and end in `.md`, directly inside `docs/research/curated/`. |
| `docs/research/inbox/subdir/*.md` | No | Nested subdirectories are not part of the allowlist (the checker requires an exact 4-part path). |
| `docs/research/curated/notes.md` | No | Does not start with `curator-prompt-`. |
| `README.md` | No | Public-facing content; human review required. |
| `AGENTS.md` | No | Agent policy file; human review required. |
| `CHANGELOG.md` | No | Release-facing content; human review required. |
| `scripts/*` | No | Code; human review required. |
| `tests/*` | No | Code; human review required. |
| `.github/workflows/*` | No | CI/automation policy; human review required. |
| `docs/hermes/*` | No | Curated guide content; human review required. |
| `docs/image-generation/*` | No | Curated guide content; human review required. |
| `docs/skills/*` | No | Curated guide content; human review required. |
| `docs/publication-policy.md` | No | Policy content; human review required. |
| `docs/research/source-policy.md` | No | Policy content; human review required. |
| Any other file not listed above | No | Default deny -- the checker is an allowlist, not a blocklist. |

The checker is deterministic and implemented in
`scripts/check_safe_generated_diff.py`. It normalizes paths (backslashes,
`./` prefixes, `..` traversal) before matching, so a PR cannot dodge the rule
with path tricks.

## Forbidden Files

Automerge must refuse any PR that touches other files, including:

```text
README.md
AGENTS.md
CHANGELOG.md
scripts/
tests/
.github/workflows/
docs/hermes/
docs/image-generation/
docs/skills/
docs/publication-policy.md
docs/research/source-policy.md
```

This includes AI-written docs, guide updates, policy changes, scripts, tests,
and workflow YAML.

## Worked Example: A PR That Must Be Rejected

Suppose a branch `autopilot/generated-research-updates` contains this diff:

```text
 data/research/candidates.json          | 12 +++++++
 docs/research/inbox/2026-07-01.md      | 40 +++++++++++++++++++
 docs/skills/prompt-guides.md           |  6 +++---
```

Two of the three files are on the allowlist. The third,
`docs/skills/prompt-guides.md`, is a curated guide doc, not a generated
research artifact.

Running the checker locally shows the rejection:

```powershell
python scripts/check_safe_generated_diff.py --base main --head autopilot/generated-research-updates
```

Expected output:

```text
Safe generated-file diff check
Allowed changed files:
  OK  data/research/candidates.json
  OK  docs/research/inbox/2026-07-01.md
Refused changed files:
  NO  docs/skills/prompt-guides.md
Result: refused
```

Exit code is non-zero, so `automerge-safe-generated.yml` refuses to squash
merge. The correct fix is **not** to widen the allowlist. It is to split the
PR: keep `data/research/candidates.json` and the inbox report on the
autopilot branch, and move the `docs/skills/prompt-guides.md` change to its
own branch that goes through normal human review, PR checks, and manual
merge.

## Workflow Trust Boundary

The workflow separates a read-only validation job from the write-capable merge
job. `pull_request_target` runs the base-owned workflow definition for a pull
request, rather than the PR merge-branch definition that `pull_request` uses.
Validation records the PR number, base SHA, and head SHA before checking out
any PR code.

```text
base-owned pull_request_target event or default-branch workflow_dispatch
  -> validate on ubuntu-latest (contents/pull-requests/checks: read)
  -> check out the recorded PR head
     with persist-credentials: false
  -> git show <recorded base commit>:scripts/check_safe_generated_diff.py
     into RUNNER_TEMP outside the PR checkout
  -> run the trusted checker, health, autofix, and unit-test gates
  -> expose only PR number and recorded SHAs
  -> merge (contents/pull-requests: write)
  -> gh pr merge --match-head-commit <recorded head SHA>
```

Validation runs on `ubuntu-latest` in Bash. Its shell steps use
`set -euo pipefail`, so a nonzero command stops validation and the merge job
does not run. Validation has read-only permissions, maps no secrets, and never
passes write credentials to checked-out PR code: the exact-head checkout uses
`persist-credentials: false`. The checker that makes the allowlist decision is
always loaded from the recorded base commit into `RUNNER_TEMP`, not from the PR
checkout. The merge job performs no checkout and runs no Python, Git, or
PR-controlled script.

`workflow_dispatch` remains available only when the checked-in validation job
runs from `refs/heads/<default_branch>`, so it rejects an honest non-default
dispatch. Manual dispatch can select another ref, whose modified workflow
could remove that condition. Owner-side workflow execution protection controls
actor and event rules, not ref selection. The owner must use it to limit
`workflow_dispatch` to trusted maintainers, and those maintainers must select
the default branch. The checked-in condition is defense in depth, not an
enforcement boundary against a malicious selected ref. See GitHub's
[Workflow execution protections documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/actions-policies/workflow-execution-protections).

## Required Checks

Before enabling squash merge, validation runs on `ubuntu-latest` in Bash:

```bash
set -euo pipefail
python "$RUNNER_TEMP/safe-generated-checker/check_safe_generated_diff.py" --base <BASE_SHA> --head <HEAD_SHA>
python scripts/repo_health_check.py --ci
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

The merge command uses squash merge, `--match-head-commit`, and no admin
bypass. If the PR head changes after validation, GitHub CLI refuses the guarded
merge. Repository branch protection still applies.

## Why Content Docs Require Human Review

Generated research files can be reviewed as source queues and local prompt
drafts. Finished guide content is different: it can contain stale tool
behavior, unsafe instructions, copied source text, weak citations, or
accidental private data.

For content docs, keep the manual path:

```text
local Codex -> branch -> PR -> checks -> human review -> merge
```

## Automerge Decision Table

| Condition | Decision |
| --- | --- |
| Branch does not start with `autopilot/` | Refuse automerge. |
| Any changed file is outside the generated allowlist | Refuse automerge. |
| Required checks fail | Refuse automerge. |
| PR includes README, curated or non-allowlisted documentation, scripts, tests, workflow, policy, or changelog changes | Refuse automerge. |
| PR includes only generated candidate/inbox/curator-prompt files and checks pass | Eligible for squash merge without admin bypass. |

## Required Evidence

The automerge workflow should leave enough evidence for a maintainer to audit:

| Evidence | Source |
| --- | --- |
| PR number, recorded base SHA, and recorded head SHA | Read-only validation outputs. |
| Branch owner, `autopilot/` prefix, and non-draft decision | PR metadata query in validation. |
| Base-owned trigger, default-branch dispatch gate, and credential-free checkout | Workflow definition; owner-side protection limits `workflow_dispatch` to trusted maintainers but does not restrict ref selection. |
| Changed-file allowlist result | Base-owned checker copied to `RUNNER_TEMP`. |
| Repository health, safe autofix, and unit-test results | Read-only validation job logs. |
| Guarded merge method | Merge job log showing `--squash`, `--auto`, and `--match-head-commit`. |

## Why The Allowlist Is Narrow

Generated research files are source queues, not final guidance. They may
include public source titles, URLs, scores, and local curator prompts. They
do not directly tell users what to do. Finished docs have a different risk
profile: they can publish stale product behavior, unsafe setup instructions,
weak source claims, or copied text.

The narrow allowlist prevents the automation from turning "source discovery"
into "unreviewed guide publication."

## Human Review Path For Rejected PRs

If automerge refuses a PR:

1. Inspect the changed-file list.
2. If the files are intentionally outside the generated allowlist, treat the
   PR as a normal content/code PR.
3. Run local checks.
4. Review public-safety risk.
5. Merge only after human approval.

Do not widen the allowlist just to make one PR merge automatically.

## Failure Modes

| Failure | Response |
| --- | --- |
| Generated PR touches a guide | Stop automerge; require human review. |
| Allowlist script fails | Do not merge; inspect script output. |
| PR changes after validation | `--match-head-commit` refuses the merge; validate the new head again. |
| Base checker cannot be loaded | Do not merge; repair the trusted-base workflow in a separately reviewed PR. |
| Workflow lacks permissions | Fix workflow permissions in a separate reviewed PR. |
| Branch name is wrong | Rename or recreate from `autopilot/` only if files are generated-only. |
| Generated prompt contains unsafe source text | Keep it as a curator prompt only; do not publish as guide content. |
| PR mixes allowed and forbidden files | Split the PR; never widen the allowlist to force a merge. |
| Path uses backslashes or `../` traversal | The checker normalizes paths before matching; a suspicious result should be treated as refused, not bypassed. |
