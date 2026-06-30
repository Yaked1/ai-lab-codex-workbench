# Safe Automerge Policy

Safe generated-file automerge exists only for mechanical research artifacts. It does not merge curated guide content, code changes, workflow changes, or policy changes.

## Branch Requirement

Only pull requests from branches starting with this prefix are considered:

```text
autopilot/
```

Pull requests from other branches must use normal human review and merge.

## Allowed Files

The changed files must be limited to:

```text
data/research/candidates.json
docs/research/inbox/*.md
docs/research/curated/curator-prompt-*.md
```

The checker is deterministic and implemented in `scripts/check_safe_generated_diff.py`.

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

This includes AI-written docs, guide updates, policy changes, scripts, tests, and workflow YAML.

## Required Checks

Before enabling squash merge, the workflow runs:

```powershell
python scripts/check_safe_generated_diff.py --base <BASE> --head <HEAD>
python scripts/repo_health_check.py --ci
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

The merge command uses squash merge and does not use admin bypass. Repository branch protection still applies.

## Why Content Docs Require Human Review

Generated research files can be reviewed as source queues and local prompt drafts. Finished guide content is different: it can contain stale tool behavior, unsafe instructions, copied source text, weak citations, or accidental private data.

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
| PR includes README, docs, scripts, tests, workflow, policy, or changelog changes | Refuse automerge. |
| PR includes only generated candidate/inbox/curator-prompt files and checks pass | Eligible for squash merge without admin bypass. |

## Required Evidence

The automerge workflow should leave enough evidence for a maintainer to audit:

- Base and head refs checked.
- Changed-file list.
- Result of `check_safe_generated_diff.py`.
- Repository health check result.
- Safe autofix check result.
- Unit test result.
- Merge method used, if merged.

## Why The Allowlist Is Narrow

Generated research files are source queues, not final guidance. They may
include public source titles, URLs, scores, and local curator prompts. They do
not directly tell users what to do. Finished docs have a different risk
profile: they can publish stale product behavior, unsafe setup instructions,
weak source claims, or copied text.

The narrow allowlist prevents the automation from turning "source discovery"
into "unreviewed guide publication."

## Human Review Path For Rejected PRs

If automerge refuses a PR:

1. Inspect the changed-file list.
2. If the files are intentionally outside the generated allowlist, treat the PR
   as a normal content/code PR.
3. Run local checks.
4. Review public-safety risk.
5. Merge only after human approval.

Do not widen the allowlist just to make one PR merge automatically.

## Failure Modes

| Failure | Response |
| --- | --- |
| Generated PR touches a guide | Stop automerge; require human review. |
| Allowlist script fails | Do not merge; inspect script output. |
| Workflow lacks permissions | Fix workflow permissions in a separate reviewed PR. |
| Branch name is wrong | Rename or recreate from `autopilot/` only if files are generated-only. |
| Generated prompt contains unsafe source text | Keep it as a curator prompt only; do not publish as guide content. |
