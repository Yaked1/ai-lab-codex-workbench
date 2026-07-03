# Safe Automerge Policy

Safe generated-file automerge exists only for mechanical research artifacts.
It does not merge curated guide content, code changes, workflow changes, or
policy changes. If you remember one rule from this page: automerge is for
metadata the scout produced, never for prose a human or an agent wrote for
readers.

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

## Required Checks

Before enabling squash merge, the workflow runs:

```powershell
python scripts/check_safe_generated_diff.py --base <BASE> --head <HEAD>
python scripts/repo_health_check.py --ci
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

The merge command uses squash merge and does not use admin bypass. Repository
branch protection still applies.

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
| PR includes README, docs, scripts, tests, workflow, policy, or changelog changes | Refuse automerge. |
| PR includes only generated candidate/inbox/curator-prompt files and checks pass | Eligible for squash merge without admin bypass. |

## Required Evidence

The automerge workflow should leave enough evidence for a maintainer to
audit:

- Base and head refs checked.
- Changed-file list.
- Result of `check_safe_generated_diff.py`.
- Repository health check result.
- Safe autofix check result.
- Unit test result.
- Merge method used, if merged.

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
| Workflow lacks permissions | Fix workflow permissions in a separate reviewed PR. |
| Branch name is wrong | Rename or recreate from `autopilot/` only if files are generated-only. |
| Generated prompt contains unsafe source text | Keep it as a curator prompt only; do not publish as guide content. |
| PR mixes allowed and forbidden files | Split the PR; never widen the allowlist to force a merge. |
| Path uses backslashes or `../` traversal | The checker normalizes paths before matching; a suspicious result should be treated as refused, not bypassed. |
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `docs/automation/safe-automerge-policy.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `safe automerge policy` state what decision, workflow, or reusable behavior it supports?
- Are included scope, excluded scope, and unsafe actions clear enough for an
  agent or contributor to follow?
- Are examples public-safe, repository-relative, and free of private data?
- Are fast-changing product or platform claims phrased conservatively or marked
  for official-doc verification?
- Does the file point to the next artifact a reader should inspect: a command,
  template, test, manifest, package, or deeper guide?
- Could a reviewer cite this file in a PR review and know what evidence proves
  the work is complete?

Keep future edits focused on stronger evidence, clearer failure modes, better
navigation, and safer automation boundaries. Do not add length unless the new
material makes the repository easier to operate, teach, audit, or recover.
<!-- RESEARCH-GRADE-EXPANSION:END -->
