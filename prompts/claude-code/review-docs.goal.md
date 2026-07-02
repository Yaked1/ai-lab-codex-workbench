# Claude Code Goal: Review Documentation

## Target Tool

Claude Code, used here in a read-only reviewer role (not as an editor).
Works whether invoked from the CLI, an IDE integration, or a `/goal`-style
custom slash command defined in `.claude/commands/`.

## Purpose

Use this prompt for read-only documentation review. Claude Code should
identify clarity, safety, consistency, and verification issues before a
maintainer edits or merges docs, without making any edits itself. This is
the review gate you run before a docs PR is opened, or as a second pass on
an existing PR before merge.

## Inputs To Fill

| Input | Description | Example |
| --- | --- | --- |
| `{docs_to_review}` | Exact files or globs to review. | `README.md`, `docs/tools/*.md` |
| `{audience}` | Reader and prior knowledge level. | `Beginner Windows users with basic Git knowledge` |
| `{main_risks}` | Specific risks to prioritize in this pass. | `Unverified AI tool pricing/availability claims` |
| `{allowed_edits}` | Whether any edits are allowed after review. | `None - findings only` |
| `{base_context}` | Files that establish house style/rules. | `AGENTS.md`, `README.md`, `CONTRIBUTING.md`, `SECURITY.md` |

## Full Prompt

```text
Target tool:
Claude Code

Objective:
Review this repository's documentation for beginner clarity, public
repository safety, and consistency with AGENTS.md. This is a read-only
review: do not edit any file during this pass.

Files to read first:
- AGENTS.md
- README.md
- CONTRIBUTING.md
- SECURITY.md
- {docs_to_review}

Audience:
{audience}

Priority risks for this pass:
{main_risks}

Allowed edits:
{allowed_edits}

Boundaries:
- Do not edit files unless {allowed_edits} explicitly says edits are
  permitted, and even then, wait until after the review is delivered.
- Do not add dependencies.
- Do not inspect, fetch, or reference files outside this repository.
- Do not include secrets, private links, personal account details, private
  machine paths, or credentials in the findings.
- Do not state exact pricing, model availability, benchmark numbers, or
  platform support for any AI tool; flag those claims instead of repeating
  them as fact.

Review tasks:
1. Identify unclear or ambiguous instructions for {audience}.
2. Identify claims about external AI tools that should be verified against
   official docs before publishing.
3. Identify missing safety warnings (secrets, destructive commands, private
   data) relative to AGENTS.md's Safe Edit Boundaries.
4. Identify workflow steps that could encourage unsafe automation (auto-merge,
   auto-commit, unattended destructive commands).
5. Identify outdated, vague, or unsupported guidance, including broken or
   stale internal links.
6. Identify inconsistencies in heading structure, terminology, or formatting
   across the reviewed files.
7. Recommend the smallest useful documentation changes that would fix each
   finding, without proposing a full rewrite.

Final response:
- Verdict (approve as-is / needs changes / needs maintainer decision)
- Findings ordered by severity, each with the specific file and, where
  possible, the specific heading or line
- Suggested edits for each finding
- Files reviewed
- Checks not run (if command execution was not part of this review)
- Tool claims that should be manually verified before public release
```

## Short Version

```text
Review {docs_to_review} for {audience} clarity, public-repo safety, and
AGENTS.md consistency. Read-only, no edits. Prioritize {main_risks}. Return
a verdict, severity-ordered findings with file references, suggested edits,
files reviewed, checks not run, and claims needing manual verification.
```

## Included Scope

- Documentation files explicitly named in `{docs_to_review}`.
- The baseline context files in `{base_context}` needed to judge
  consistency and house style.
- Adjacent repository instructions (AGENTS.md rules, CONTRIBUTING.md,
  SECURITY.md) needed to evaluate whether the docs follow them.
- Read-only local checks, only if `{allowed_edits}` or a separate
  instruction explicitly permits command execution during the review.

## Excluded Scope

- Any file edit, rename, or deletion during the review pass.
- Dependency installation or configuration changes.
- Private folders, secrets, `.env` files, browser profiles, credentials, and
  any file outside this repository.
- Exact current pricing, model access tiers, or platform support claims for
  any AI tool, unless official docs were checked in this session and the
  date is noted.

## Success Criteria

- Every finding names a specific file (and heading or line where possible)
  rather than a vague generalization.
- The review stays read-only unless `{allowed_edits}` explicitly changes
  that.
- Public-safety issues (secrets, destructive command guidance, unsafe
  automation) are surfaced first, ahead of style nits.
- Every external AI-tool claim that could go stale is flagged for
  verification rather than repeated as fact.
- The verdict is unambiguous: approve as-is, needs changes, or needs a
  maintainer decision.

## Safety Boundaries

- No edits during the review pass, regardless of how confident the findings
  are, unless `{allowed_edits}` explicitly permits them.
- No dependency installation or environment changes.
- No access to private folders, secrets, `.env` files, or anything outside
  this repository's tracked files.
- No secret values quoted in the output, even partially; if a secret-looking
  string is found, name the file and describe the issue without reproducing
  the value.
- No unsupported product claims presented as current fact; use "verify in
  official docs" language for anything time-sensitive.

## Verification

This is usually a review-only task with no command execution. If command
execution is explicitly allowed for this pass, optional checks are:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
```

If these were not run, say so plainly in "Checks not run" rather than
implying they passed.

## Final Report Format

```markdown
## Verdict
## Findings
## Suggested edits
## Files reviewed
## Checks not run
## Claims needing manual verification
```

## Failure Cases

| Failure | What to do |
| --- | --- |
| The review starts editing files instead of only reporting | Stop immediately, discard any partial edit, and return findings only. |
| A claim needs current, dated information (pricing, model availability, platform support) | Do not state it as fact; mark it in "Claims needing manual verification" instead. |
| The file scope in `{docs_to_review}` is ambiguous or too broad | Ask which specific docs to review rather than scanning the entire repository. |
| A secret-looking string (API key, token pattern) appears in the reviewed content | Do not quote it in the report; name the file and flag it as a safety issue for immediate rotation and removal. |
