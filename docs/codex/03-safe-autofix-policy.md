# Safe Autofix Policy

The safe autofix script is intentionally boring.

It may:

- Trim trailing whitespace.
- Normalize line endings to LF for text files.
- Ensure exactly one final newline.
- Skip binary files and large files.
- Skip ignored/generated folders.

It must not:

- Rewrite meaning.
- Reformat code using unknown style rules.
- Delete files.
- Install dependencies.
- Touch secrets.
- Modify archives, images, model files, or binaries.

## Local usage

Check only:

```powershell
python scripts/safe_autofix.py --check
```

Apply fixes:

```powershell
python scripts/safe_autofix.py --write
```

## GitHub automation

Use the `Safe Autofix PR` workflow. It opens a PR instead of pushing directly to `main`.
