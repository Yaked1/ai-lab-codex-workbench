# Safe Autofix Policy

The safe autofix script is intentionally narrow. It exists to make deterministic text cleanup easy without turning formatting into a broad rewrite.

## What Safe Autofix May Do

- Trim trailing whitespace.
- Normalize line endings to LF for text files.
- Ensure exactly one final newline.
- Skip binary files.
- Skip large files.
- Skip ignored or generated folders.

## What Safe Autofix Must Not Do

- Rewrite meaning.
- Reformat code using unknown style rules.
- Delete files.
- Install dependencies.
- Touch secrets.
- Modify archives, images, model files, or binaries.
- Change workflow logic.
- Apply subjective prose edits.

## Why The Scope Is Small

Small deterministic cleanup is easy to review. Broad automated formatting can create huge diffs, hide real changes, and make beginner PRs harder to understand.

The rule is:

> If a human cannot predict exactly what the autofix will do, it does not belong in safe autofix.

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

## GitHub Automation

Use the `Safe Autofix PR` workflow for repository cleanup. It opens a PR instead of pushing directly to `main`.

Expected behavior:

1. Workflow runs manually.
2. Script applies deterministic cleanup.
3. Validation runs.
4. Workflow opens a PR only if files changed.
5. A human reviews and merges the PR.

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

## Failure Modes

| Failure | Cause | Fix |
| --- | --- | --- |
| `--check` reports changed files | Whitespace or final newline issue. | Run `--write`, review diff, rerun `--check`. |
| Unexpected file changed | File was considered a text candidate. | Review script inclusion rules before committing. |
| Binary file touched | Bug or incorrect file classification. | Stop and investigate before committing. |
| PR includes prose changes | Someone mixed manual edits with autofix. | Split into separate PRs. |

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
