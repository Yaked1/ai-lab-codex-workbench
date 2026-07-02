# Contributing

This repository uses a small, reviewable workflow. The goal is to teach reliable AI-assisted repository work, not to reward large unreviewed diffs.

## Contribution Principles

- One task per branch.
- Clear task intake before agent work starts.
- Small diffs that a human can review.
- Local checks before a pull request.
- CI checks before merge.
- Conservative claims about third-party AI tools.
- No secrets, private links, personal data, or private machine details.

## Standard Workflow

1. Create or choose a small issue.
2. Write the objective, included scope, excluded scope, success criteria, and checks.
3. Create a branch named `agent/<task-name>`.
4. Ask the agent to read [AGENTS.md](AGENTS.md) and inspect files before editing.
5. Make the smallest useful change.
6. Run local checks.
7. Review `git diff`.
8. Commit with a short factual message.
9. Open a pull request.
10. Wait for CI.
11. Review the full diff and CI logs.
12. Squash merge only after the change is understood.
13. Update [CHANGELOG.md](CHANGELOG.md) when the change is user-visible.

## Branch Names

Use:

```text
agent/<short-task-name>
```

Examples:

```text
agent/expand-codex-guide
agent/add-public-safety-checklist
agent/fix-local-check-docs
```

Avoid branch names that include private project names, account IDs, internal tickets, or sensitive context.

## Local Checks

Run from PowerShell in the repository root:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

To apply deterministic whitespace cleanup:

```powershell
python scripts/safe_autofix.py --write
```

Then rerun:

```powershell
python scripts/safe_autofix.py --check
```

## Pull Request Expectations

Every PR should include:

- What changed.
- Why it changed.
- Files or areas touched.
- Commands run.
- Checks run.
- Known limitations.
- Claims that still need official-doc verification.
- Screenshots only if the change affects visuals.

## Research-Grade PR Evidence

For broad documentation, prompt, skill, or policy changes, include a short
evidence block in the PR body:

```markdown
## Research-grade evidence

- Surfaces covered:
- New or expanded deep guide:
- Navigation updated:
- Tests or health checks updated:
- Public-safety review:
- Commands run:
- Staged paths:
```

Reviewers should be able to map every changed file to one of those rows. If a
file cannot be mapped, it is probably out of scope or needs a clearer reason.

Use this standard for "comprehensive" claims:

| Claim | Required evidence |
| --- | --- |
| New workflow is core documentation | README link, required-file health check, and test coverage. |
| Prompt/template surface improved | Required sections, success criteria, safety boundaries, and final report format. |
| Safety posture improved | Specific forbidden behavior, review gate, incident response step, or scan result. |
| Automation guidance improved | Dry-run/apply distinction, side effects, failure handling, and rollback path. |
| Package/release guidance improved | Manifest, file count, byte count, hash, or package inspection command. |

## Documentation Contributions

Good documentation changes in this repo are:

- Beginner-friendly.
- Structured with headings, tables, checklists, and examples.
- Practical for Windows PowerShell users.
- Honest about limitations and failure modes.
- Conservative about fast-changing AI tools.
- Linked to deeper docs where useful.

For broad documentation passes, use
[docs/workflows/research-grade-repository-expansion.md](docs/workflows/research-grade-repository-expansion.md)
before editing. A research-grade contribution should make each touched file
materially easier to use or review. Prefer:

- a clear audience and use case;
- included and excluded scope;
- command examples or review evidence;
- failure modes and recovery paths;
- public-safety boundaries;
- links to related guides, prompts, tests, or scripts;
- changelog entries for user-visible changes.

Avoid broad rewrites where the only visible outcome is more prose. Reviewers
should be able to point at the new section and say what decision, command,
check, or safety review it improves.

Do not add:

- Exact pricing unless verified immediately from official docs and clearly dated.
- Unsupported model or feature claims.
- Private links.
- Fake secrets that match real secret patterns.
- Long vendor marketing copy.

## Prompt Template Contributions

Prompt templates should include:

- Target tool.
- Purpose.
- Full prompt.
- Short version.
- Inputs to fill.
- Success criteria.
- Safety boundaries.
- Verification steps.
- Final report format.
- Failure cases.

Use existing files in [prompts/](prompts/) as the pattern.

## Commit Style

Use short factual commit messages:

```text
Add Codex task template
Fix README setup commands
Update safe autofix policy
Expand tool comparison matrix
```

Do not claim broad outcomes in commit messages unless the diff proves them.

## Do Not Contribute

- Secrets or API keys.
- `.env` files.
- Private personal documents.
- Private repository links.
- Browser cookies or profiles.
- Huge generated files.
- Large model weights.
- Docker stacks unless the project deliberately grows into that later.
- Unsafe automation that merges without review.
- Tool claims copied from old docs without verification.

## Maintainer Review Checklist

- [ ] Scope matches the issue.
- [ ] Diff is understandable.
- [ ] Local checks are reported.
- [ ] CI passed or failure is explained.
- [ ] No secrets or private data are present.
- [ ] External claims are conservative.
- [ ] Broad documentation changes follow the research-grade expansion workflow.
- [ ] Every touched file is materially more useful, not only longer.
- [ ] Changelog was updated when needed.
- [ ] PR can be squash merged cleanly.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **top-level repository policy document** surface. During broad
maintenance, reviewers should treat `CONTRIBUTING.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `CONTRIBUTING` state what decision, workflow, or reusable behavior it supports?
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
