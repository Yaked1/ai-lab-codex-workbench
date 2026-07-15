# Current Plan

## Goal

Apply the repository-audit remediation plan on branch
`codex/apply-repository-audit-fixes` while preserving public safety,
Windows-first behavior, source-backed claims, and test-first evidence.

The detailed implementation contract is the
[16-task repository-audit remediation plan](../superpowers/plans/2026-07-13-repository-audit-remediation.md).

## Success Criteria

- All 16 tasks satisfy their stated contracts and focused tests.
- Current documentation uses verified first-party sources for changing facts.
- Repository-wide validation passes before the branch is offered for review.
- No unrelated working-tree changes are overwritten or included in task work.

## Constraints

- Work only on `codex/apply-repository-audit-fixes`.
- Use red-green-refactor for behavior changes.
- Preserve unrelated work and never bypass hooks.
- Do not push, publish, delete refs, or change GitHub settings without explicit
  owner authorization.
- Keep current operational status here and detailed implementation steps in the
  linked plan.

## Decisions

- Anthropic's [current Fable promotion terms](https://support.claude.com/en/articles/15424964-claude-fable-5-promotional-access),
  checked 2026-07-13, extend included promotional access through July 19, 2026
  at 11:59:59 PM PT. The separate 50% Claude Code weekly-limit increase ends
  at the same deadline. Afterward Fable leaves subscription weekly limits but
  remains available using usage credits. July 7 and July 12 are superseded
  historical observations.
- Release artifacts must come from committed Git-tree blobs, record the exact
  source commit, reject output collisions, and match their documentation.
- Generic review policy stays separate from executable prompts.

## Work Breakdown

- [x] Task 1: Decouple the active plan and reconcile Fable claims.
- [x] Task 2: Make the local PowerShell gate fail closed.
- [x] Task 3: Validate the exact staged index in the maintainer.
- [x] Task 4: Move generated-file validation to trusted base code.
- [x] Task 5: Harden workflow inputs and generated-content publication.
- [x] Task 6: Make release packages commit-exact, bounded, and collision-safe.
- [x] Task 7: Make bootstrap review candidates before staging.
- [x] Task 8: Add Windows runtime CI and immutable action references.
- [x] Task 9: Remove mechanical expansion safely.
- [x] Task 10: Replace volume gates with behavior and source contracts.
- [ ] Task 11: Reduce model-guide duplication and split the frontier reference.
- [ ] Task 12: Create a real first-success path and simplify Prompting OS.
- [ ] Task 13: Align governance and contributor surfaces.
- [ ] Task 14: Improve the static discovery surface and starter distribution.
- [ ] Task 15: Record owner-only GitHub actions and release readiness.
- [ ] Task 16: Full review, verification, and branch finish.

## Validation

- Run each task's focused red-green tests.
- Run `python scripts/repo_health_check.py`.
- Run `python scripts/safe_autofix.py --check`.
- Run `python -m unittest discover -s tests`.
- Run `git diff --check`.
- Test-build and test-extract package artifacts before release readiness.

## Progress Notes

- 2026-07-13: Tasks 1 through 10 completed focused implementation,
  verification, and independent review. Task 11 is active.
- 2026-07-13: Task 10 passed its exact six-module suite with 147 tests,
  all repository gates, and a final Luna xhigh verdict of `SPEC: PASS` and
  `CODE QUALITY: APPROVED`.

## Checkpoints

- Branch: `codex/apply-repository-audit-fixes`.
- Completed: Tasks 1 through 10.
- Active: Task 11.
- Detailed task definitions remain in the linked 16-task plan.

## Risks and Open Questions

- Changing vendor access terms must be rechecked after July 19, 2026 or when
  the official Help Center article changes.
- Windows-only process and hook behavior needs real PowerShell coverage.
- GitHub settings and ref state require separately recorded owner-side proof.

## Final Handoff

Not ready. Complete Tasks 11 through 16, run the full validation set,
review the final owned diff, and then present the permitted branch disposition
options without pushing unless explicitly authorized.
