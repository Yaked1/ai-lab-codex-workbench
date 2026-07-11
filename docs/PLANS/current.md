# Current Plan: Embedded Video Playback

## Goal

Let readers watch the selected model videos on this repository's GitHub Pages
site instead of navigating to YouTube, without copying video binaries into Git.

![Availability map for the models covered by the embedded players](../assets/model-guides/availability-map.svg)

[![Open the embedded GPT-5.6 and GPT-Live launch discussion](https://i.ytimg.com/vi/QjuuTHJKxWI/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#launch-discussion)

*The thumbnail now opens an embedded player on this repository's GitHub Pages
site rather than a YouTube watch page.*

## Phases

- [x] Phase 1: Verify GitHub Markdown and GitHub Pages capabilities.
- [x] Phase 2: Build an in-repository embedded-video page.
- [x] Phase 3: Point every video card to its matching embedded player.
- [x] Phase 4: Validate player surfaces, run checks, commit, and push.

## Platform finding

GitHub's official documentation says embedded YouTube video HTML cannot render
inside repository Markdown. GitHub Flavored Markdown also filters `<iframe>`.
The repository already publishes `docs/` through GitHub Pages, where normal
HTML iframe players are supported.

## Implementation

- `docs/site/model-media.html` contains four privacy-enhanced YouTube embeds.
- Each Markdown thumbnail links to an anchor on that GitHub Pages player page.
- The browser stays on `yaked1.github.io`; playback still streams from YouTube.
- Players do not autoplay and video files are not stored in the repository.

## Sources

- [GitHub Docs: working with non-code files](https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files)
- [GitHub Flavored Markdown: disallowed raw HTML](https://github.github.com/gfm/#disallowed-raw-html-extension-)
- [GitHub Pages quickstart](https://docs.github.com/en/pages/quickstart)

## Status

Complete. Four privacy-enhanced iframe players, their accessible titles,
fullscreen flags, source IDs, Markdown destinations, and player anchors pass
deterministic tests. All 89 repository tests and standard checks pass. Live
browser automation could not launch because Playwright is not installed and
the bundled browser-tool call was rejected after the account reached its Codex
usage limit; no dependency was added or restriction bypassed.

## Verification

- Four `youtube-nocookie.com` iframe sources present.
- Four accessible iframe titles and fullscreen controls present.
- Ten visible video cards point to GitHub Pages, with zero direct YouTube card
  destinations.
- `python scripts/repo_health_check.py`: passed.
- `python scripts/safe_autofix.py --check`: passed.
- `python -m unittest discover -s tests`: 89 tests passed.
- `git diff --check`: passed.
