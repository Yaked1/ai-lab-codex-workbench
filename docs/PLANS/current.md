# Current Plan: Media in Every Relevant File

## Goal

Embed visible images and clickable video-preview images directly in every
model benchmark, availability, plan, notes, and provenance file readers may
open.

![Availability map for the model families covered by this plan](../assets/model-guides/availability-map.svg)

[![Play the GPT-5.6 and GPT-Live launch discussion by ThursdAI](https://i.ytimg.com/vi/QjuuTHJKxWI/maxresdefault.jpg)](https://www.youtube.com/watch?v=QjuuTHJKxWI)

*Click the video image to watch. The availability diagram is a local SVG that
renders directly in GitHub.*

## Phases

- [x] Phase 1: Reproduce the text-only experience in the plan and notes files.
- [x] Phase 2: Embed media in every file in the documented model-media set.
- [x] Phase 3: Add a regression test that checks every file, not only guides.
- [x] Phase 4: Verify rendering inputs, run checks, commit, and push.

## Root cause

The first media pass embedded diagrams and video cards in three guides but left
the README, plan, notes, claim ledger, and provenance ledger mostly or entirely
text-only. Tests checked the guides rather than the complete reader-facing set.

## Decisions

- Every relevant file must include both an image and a clickable video preview.
- GitHub Markdown video previews use a rendered thumbnail linked to YouTube.
- Videos remain labeled as official, third-party, or community material.
- The unrelated `CLAUDE.md` edit remains outside the task.

## Status

Complete. All eight reader-facing model files contain at least one rendered
image and one clickable video preview. GitHub's Markdown API rendered the plan
and notes with two image elements and one YouTube link each. All 88 tests and
repository checks passed; the unrelated `CLAUDE.md` edit remains excluded.

## Verification

- Eight files checked for rendered-image and video-preview markup.
- GitHub Markdown API: plan `img_tags=2`, notes `img_tags=2`.
- `python -m unittest tests.test_model_media`: 5 tests passed.
- `python scripts/repo_health_check.py`: passed.
- `python scripts/safe_autofix.py --check`: passed.
- `python -m unittest discover -s tests`: 88 tests passed.
- `git diff --check`: passed.
