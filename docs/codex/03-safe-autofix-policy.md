# Safe Autofix Policy

The safe autofix script is intentionally narrow. It exists to make deterministic text cleanup easy without turning formatting into a broad rewrite.

The implementation lives at [scripts/safe_autofix.py](../../scripts/safe_autofix.py). This page describes exactly what that script does. If this page and the script ever disagree, trust the script and file a docs fix.

## What Safe Autofix May Do

Reading the script directly, `safe_autofix.py` performs three transformations inside `normalize_text()`:

- Convert `\r\n` and `\r` line endings to `\n` (normalize line endings to LF).
- Strip trailing whitespace from every line (`line.rstrip()` per line).
- Collapse any trailing blank lines and ensure the file ends with exactly one final newline (`text.rstrip("\n") + "\n"`).

It also has file-selection logic that decides which files it is even allowed to touch:

- Skips anything inside `SKIP_DIRS`: `.git`, `.venv`, `venv`, `node_modules`, `__pycache__`, `.pytest_cache`, `.mypy_cache`, `.cache`, `dist`, `build`, `logs`, `outputs`, `.tmp`, `.idea`, `.vscode`, `.omc`.
- Skips files larger than `MAX_TEXT_BYTES` (1,000,000 bytes).
- Skips files it cannot decode as UTF-8 (a `UnicodeDecodeError` on read means the file is left untouched).
- Only considers a file a "text candidate" if it is named `LICENSE`, `AGENTS.md`, `README.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md`, `.gitignore`, `.editorconfig`, or has one of these extensions: `.md`, `.txt`, `.py`, `.ps1`, `.yml`, `.yaml`, `.json`, `.toml`, `.gitignore`, `.editorconfig`.

## What Safe Autofix Must Not Do

- Rewrite meaning.
- Reformat code using unknown style rules.
- Delete files.
- Install dependencies.
- Touch secrets.
- Modify archives, images, model files, or binaries.
- Change workflow logic.
- Apply subjective prose edits.

Confirmed by reading the script: it does **not** reformat code style (no indentation rules, no bracket placement, no line-length wrapping), does **not** reorder or sort imports, and does **not** run a linter or any language-specific formatter. The only logic in `process_file()` is read, normalize whitespace/newlines, compare, and optionally write back. There is no parsing of Python, Markdown, YAML, or JSON structure at all -- it treats every candidate file as plain text lines.

## Why The Scope Is Small

Small deterministic cleanup is easy to review. Broad automated formatting can create huge diffs, hide real changes, and make beginner PRs harder to understand.

The rule is:

> If a human cannot predict exactly what the autofix will do, it does not belong in safe autofix.

## `--check` Versus `--write`

The script's `argparse` group makes `--check` and `--write` mutually exclusive and requires exactly one of them. They share the same detection logic (`iter_files` and `normalize_text`) and differ only in what happens after a difference is found:

| Flag | What it does | Does it modify files on disk | Exit code when changes are needed | Typical use |
| --- | --- | --- | --- | --- |
| `--check` | Computes the normalized version of each candidate file and compares it to the original, but never calls `path.write_text(...)`. | No | `1` | Local pre-commit check, CI gate, PR validation. |
| `--write` | Computes the normalized version and, if it differs, writes it back to disk with `path.write_text(fixed, encoding="utf-8", newline="\n")`. | Yes | `0` (even when files were changed, because the fixes were just applied) | Local cleanup pass before committing, run manually or by the `Safe Autofix PR` workflow. |

In both modes, if no candidate file needs a change, the script prints `No safe formatting changes needed.` and exits `0`. In `--check` mode with changes pending, it prints one `Needs fix: <path>` line per file and exits `1`. In `--write` mode with changes applied, it prints one `Fixed: <path>` line per file and exits `0`.

Practical rule: never trust `--write` blindly. Always re-run `--check` and read `git diff` afterward, because `--write` succeeding just means the deterministic rules were applied, not that the resulting diff is what you wanted.

## Worked Before/After Example

Suppose `docs/example.md` contains this content, saved with CRLF line endings, trailing spaces on line 2, and two blank lines at the end of the file:

```text
# Example Heading\r\n
Some text with trailing spaces.   \r\n
\r\n
- one\r\n
- two\r\n
\r\n
\r\n
```

Running the check:

```powershell
python scripts/safe_autofix.py --check
```

Output:

```text
Needs fix: docs\example.md
```

Exit code is `1`. Now apply the fix:

```powershell
python scripts/safe_autofix.py --write
```

Output:

```text
Fixed: docs\example.md
```

The file on disk becomes:

```text
# Example Heading\n
Some text with trailing spaces.\n
\n
- one\n
- two\n
```

The `git diff` for this change shows only whitespace markers, no content rewriting:

```diff
--- a/docs/example.md
+++ b/docs/example.md
@@ -1,7 +1,5 @@
-# Example Heading
-Some text with trailing spaces.
-
-- one
-- two
-
-
+# Example Heading
+Some text with trailing spaces.
+
+- one
+- two
```

(The diff above renders as full-line changes because the line-ending style changed for every line; a diff tool configured to ignore line-ending noise would show only the trailing-whitespace line and the removed trailing blank lines.)

Re-run `--check` to confirm the fix is stable:

```powershell
python scripts/safe_autofix.py --check
```

Output:

```text
No safe formatting changes needed.
```

## Expected Diff Shape

A normal safe-autofix diff should be boring. It may show removed trailing
spaces, normalized final newlines, or line-ending cleanup. It should not show
rewritten headings, changed examples, reordered lists, new sections, deleted
paragraphs, or code logic changes.

When reviewing a safe-autofix PR, use this quick triage:

| Diff sign | Expected? | Response |
| --- | --- | --- |
| Only whitespace markers changed | Yes | Continue review. |
| File content changed meaningfully | No | Ask for a separate normal PR. |
| Binary file appears | No | Stop and inspect script candidate rules. |
| Workflow file logic changed | No | Reject as out of scope. |
| Generated output appears | Usually no | Confirm whether it was explicitly requested. |

## Local Usage

Check only:

```powershell
python scripts/safe_autofix.py --check
```

Apply fixes:

```powershell
python scripts/safe_autofix.py --write
```

Then verify:

```powershell
python scripts/safe_autofix.py --check
git diff
```

Run against a different root (rarely needed outside this repository):

```powershell
python scripts/safe_autofix.py --check --root .
```

## GitHub Automation

Use the `Safe Autofix PR` workflow for repository cleanup. It opens a PR instead of pushing directly to `main`.

Expected behavior:

1. Workflow runs manually.
2. Script applies deterministic cleanup.
3. Validation runs.
4. Workflow opens a PR only if files changed.
5. A human reviews and merges the PR.

## How This Connects To Safe Automerge

This repository also has a separate, unrelated automation policy for a completely different kind of file: `.github/workflows/automerge-safe-generated.yml`, described in full in [docs/automation/safe-automerge-policy.md](../automation/safe-automerge-policy.md). It is easy to conflate the two, so keep the distinction clear:

| | Safe autofix | Safe automerge |
| --- | --- | --- |
| What it touches | Whitespace, line endings, final newlines in any text candidate file. | Only `data/research/candidates.json`, `docs/research/inbox/*.md`, and `docs/research/curated/curator-prompt-*.md` on `autopilot/*` branches. |
| What it decides | Whether formatting is clean. | Whether a PR is eligible to squash-merge without human review. |
| Where it runs | `Safe Autofix PR` workflow, plus local `--check`/`--write`. | `automerge-safe-generated.yml`, triggered on PR events or manual dispatch. |
| Required checks | `repo_health_check.py`, `safe_autofix.py --check`, unit tests. | `check_safe_generated_diff.py`, `repo_health_check.py --ci`, `safe_autofix.py --check`, unit tests. |

The connection: `automerge-safe-generated.yml` runs `python scripts/safe_autofix.py --check` as one of its required steps (see "Run required local checks" in that workflow) before it will enable squash merge. This means a generated-file PR from the research scout cannot automerge if it left behind bad line endings, trailing whitespace, or a missing final newline -- the same rule that applies to every other PR in this repository.

Safe autofix and safe automerge are independent policies that happen to share one gate: both require `safe_autofix.py --check` to pass. Safe autofix never decides *what* is allowed to merge, and safe automerge never decides *how* text is formatted. Do not widen either script to cover the other's job.

## Review Checklist

- [ ] Did safe autofix only change whitespace or final newlines?
- [ ] Are changed files text files?
- [ ] Were generated, binary, and large files avoided?
- [ ] Did validation run after cleanup?
- [ ] Is the PR limited to deterministic formatting?

## When Not To Use Safe Autofix

Do not use safe autofix for:

- Code formatting with a language-specific style.
- Markdown rewriting.
- Sorting sections.
- Moving files.
- Removing unused content.
- Updating links.
- Dependency lockfile changes.

Those tasks need normal review and explicit instructions.

## Maintainer Rules

Treat `safe_autofix.py` as infrastructure with a deliberately small contract.
If you want to add a new transformation, first document the transformation in
plain language, then add a focused test that proves the script changes only the
intended text. Do not add behavior because it is convenient for one cleanup PR.

Good candidates:

- More accurate text/binary classification.
- Better ignored-directory handling.
- Clearer reporting in `--check` mode.

Bad candidates:

- Markdown reflow.
- Import sorting.
- Code formatting.
- Link rewriting.
- Heading renumbering.
- Generated documentation updates.

## Failure Modes And Troubleshooting

| Failure | Cause | Fix |
| --- | --- | --- |
| `--check` reports changed files | Whitespace or final newline issue. | Run `--write`, review diff, rerun `--check`. |
| `--check` fails but `git diff` shows nothing changed | You ran `--check` before saving an editor buffer, or a file was modified outside Git's view. | Save all open files, run `git status` to confirm the working tree state, then rerun `--check`. |
| `--check` fails on a file you never touched | An existing file already had bad whitespace or line endings before your task started, and the check is repo-wide, not diff-scoped. | Confirm with `git log -- <path>` whether the issue predates your branch. If unrelated to your task, report it instead of silently fixing unrelated files, or fix it as its own small commit. |
| `--check` fails only in CI, not locally | Git's `autocrlf` setting on your machine may already normalize line endings on checkout, masking the issue locally. | Run `git config --get core.autocrlf` and compare with CI's checkout behavior; run the exact CI command (`python scripts/safe_autofix.py --check`) right after a fresh `git clone` to reproduce. |
| Unexpected file changed | File was considered a text candidate. | Review script inclusion rules (`TEXT_EXTENSIONS`, the named-file allowlist) before committing. |
| Binary file touched | Bug or incorrect file classification. | Stop and investigate before committing; a binary file should have failed the UTF-8 decode and been skipped. |
| PR includes prose changes alongside autofix | Someone mixed manual edits with autofix. | Split into separate PRs. |
| `--write` reports `Fixed` but `--check` still fails afterward | A file changed on disk between the two runs, or the file is at the 1,000,000 byte boundary and behaves inconsistently. | Rerun both commands back to back with no other edits in between; if it persists, treat it as a bug and report the exact file and byte size. |

## Policy For Future Changes

Any expansion of `safe_autofix.py` should meet these requirements:

- Deterministic.
- Easy to explain.
- Easy to test.
- Low risk.
- No dependency installation.
- No destructive behavior.
- Covered by unit tests.
- Documented in this file.

## Final Report Language

When safe autofix is part of a task report, use precise wording:

- Say `safe autofix check passed` only when `--check` ran and returned success.
- Say `safe autofix applied whitespace/final-newline cleanup` only after
  reviewing the diff from `--write`.
- Say `not run` when the command was skipped.
- Do not imply that safe autofix validates prose, links, secrets, or code
  behavior. It only validates the deterministic cleanup rules above.

## Related Guides

- [Codex Goal Workflow](01-codex-goal-workflow.md)
- [Git Branch, Pull Request, and Merge Workflow](02-git-branch-pr-merge-workflow.md)
- [Review Checklist](04-review-checklist.md)
- [Safe Automerge Policy](../automation/safe-automerge-policy.md)
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **repository support file** surface. During broad
maintenance, reviewers should treat `docs/codex/03-safe-autofix-policy.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `03 safe autofix policy` state what decision, workflow, or reusable behavior it supports?
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
