# Current Plan: Visible Mixed Media

## Goal

Make the important benchmark and availability guides visibly mix concise text,
rendered diagrams, and large clickable video thumbnails in GitHub Markdown.

## Phases

- [x] Phase 1: Inspect the live branch, existing media, and GitHub constraints.
- [x] Phase 2: Verify video IDs, thumbnails, titles, and publishers.
- [x] Phase 3: Add visible video cards and rebalance their placement.
- [x] Phase 4: Test media markup, run repository checks, review, and commit.

## Key questions

1. Does each important guide visibly render media instead of only listing links?
2. Does every thumbnail open the intended verified video?
3. Is each vendor, independent, or community source labeled correctly?

## Decisions

- Use clickable YouTube thumbnails because GitHub strips or blocks ordinary
  iframe video embeds.
- Keep the existing local SVG diagrams and place video cards near the related
  explanation instead of collecting all media at the end.
- Do not add video binaries or downloaded screenshots to Git.
- Preserve the unrelated `CLAUDE.md` edit.

## Errors and resolutions

- PowerShell `Invoke-WebRequest` and `curl.exe` could not complete thumbnail
  checks because this session's Windows TLS credential provider failed.
  Python's standard HTTPS client returned HTTP 200 and `image/jpeg` for all
  four thumbnail endpoints; `yt-dlp` independently verified each public video.

## Status

Complete. Five visible video cards are mixed through the three important
guides. All video metadata and thumbnail endpoints were verified, all 87 tests
passed, and the repository health, safe-format, and diff checks passed. The
unrelated `CLAUDE.md` edit remains outside this task.

## Verification

- Four public videos verified with `yt-dlp`.
- Four thumbnail endpoints returned HTTP 200 and `image/jpeg`.
- `python -m unittest tests.test_model_media`: 4 tests passed.
- `python scripts/repo_health_check.py`: passed.
- `python scripts/safe_autofix.py --check`: passed.
- `python -m unittest discover -s tests`: 87 tests passed.
- `git diff --check`: passed.
