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
