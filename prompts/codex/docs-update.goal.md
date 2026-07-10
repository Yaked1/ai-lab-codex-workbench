# Codex Prompt: Documentation Update

## Target Tool

OpenAI Codex CLI or Codex-style coding-agent goal mode.

## Purpose

Use this prompt when a README section, documentation page, workflow guide, tool guide, prompt guide, or public-safety checklist needs a focused public-ready improvement.

## Inputs To Fill

| Input | Description | Example |
| --- | --- | --- |
| `{topic}` | The documentation topic to improve. | `Codex goal workflow` |
| `{audience}` | The reader and prior knowledge. | `Beginner contributors with basic Git knowledge` |
| `{files_to_inspect}` | Files the agent must read before editing. | `README.md`, `docs/codex/00-start-here.md` |
| `{allowed_scope}` | Files or sections that may change. | `README.md and CHANGELOG.md only` |
| `{excluded_scope}` | Files or actions that must not change. | `.github/workflows/`, dependencies, secrets |
| `{claims_to_verify}` | Fast-changing product claims to avoid or mark for manual verification. | `pricing, model availability, connector behavior` |

## Full Prompt

```text
/goal
Objective:
Improve the documentation for {topic} so it is clearer, more public-safe, easier to navigate, and useful to {audience}.

Mandatory first steps:
1. Run git status.
2. Read AGENTS.md fully.
3. Inspect README.md and {files_to_inspect} before editing.
4. Identify any pre-existing working-tree changes and treat them as user work.
5. Read the target section end to end before drafting a rewrite. Do not edit
   against a skim.
6. Note every internal link and code reference inside the target section so
   they can be re-checked after editing.

Included scope:
- {allowed_scope}
- Update CHANGELOG.md if the change is user-visible.

Excluded scope:
- {excluded_scope}
- Do not edit secrets, .env files, credentials, private links, private paths, browser profiles, or private data.
- Do not add dependencies.
- Do not modify workflow YAML unless explicitly requested.
- Do not invent exact pricing, model availability, benchmark numbers, release timing, or unsupported product behavior.
- Do not publish copied prompt dumps or leaked prompt text.
- Do not rewrite sections outside {allowed_scope} even if they look stale;
  flag them in the report instead.

Safety boundaries:
- Keep the diff reviewable and focused.
- Preserve existing user work.
- Use conservative language for fast-changing tools and mark {claims_to_verify} for official-doc verification.
- Prefer Windows PowerShell examples where commands are needed.
- If a claim cannot be verified against a file already in this repository,
  soften the wording instead of asserting it as fact.

Verification steps:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests
- git diff --check
- git diff --stat
- git diff
- Manually click or trace every internal link touched in the diff to confirm
  the target file and anchor still exist.

Success criteria:
- The target docs have a clearer purpose, audience, navigation path, examples/checklists where useful, and explicit failure modes or safety notes.
- Internal links are correct.
- Public-safety rules are preserved.
- The changelog records the visible change if appropriate.
- Required checks pass, or failures are honestly reported with relevant output.

Final report format:
## Summary
## Git state
## Files changed
## Commands run
## Verification results
## Claims needing manual verification
## Remaining risks
```

### Worked Example

```text
/goal
Objective:
Improve the documentation for "Codex goal workflow" so it is clearer, more
public-safe, easier to navigate, and useful to beginner contributors with
basic Git knowledge.

Mandatory first steps:
1. Run git status.
2. Read AGENTS.md fully.
3. Inspect README.md and docs/codex/00-start-here.md before editing.
4. Identify any pre-existing working-tree changes and treat them as user work.
5. Read docs/codex/00-start-here.md end to end before drafting changes.
6. Note every internal link inside that file so they can be re-checked.

Included scope:
- docs/codex/00-start-here.md
- CHANGELOG.md (this change is user-visible)

Excluded scope:
- Do not touch prompts/codex/*.md or README.md in this task.
- Do not edit secrets, .env files, credentials, private links, private paths,
  browser profiles, or private data.
- Do not add dependencies.
- Do not modify workflow YAML.
- Do not invent exact pricing, model availability, benchmark numbers,
  release timing, or unsupported product behavior.
- Do not publish copied prompt dumps or leaked prompt text.

Safety boundaries:
- Keep the diff reviewable and focused on the start-here guide.
- Preserve existing user work.
- Use conservative language for fast-changing tools; mark connector
  permission behavior and model-availability claims for official-doc
  verification.
- Prefer Windows PowerShell examples where commands are needed.

Verification steps:
- python scripts/repo_health_check.py
- python scripts/safe_autofix.py --check
- python -m unittest discover -s tests
- git diff --check
- git diff --stat
- git diff

Success criteria:
- docs/codex/00-start-here.md has a clear "who is this for" line, a numbered
  first-run path, and a link to prompts/codex/ for templates.
- Internal links resolve to real files.
- CHANGELOG.md has one new entry describing the doc improvement.
- Required checks pass, or failures are reported honestly.

Final report format:
## Summary
## Git state
## Files changed
## Commands run
## Verification results
## Claims needing manual verification
## Remaining risks
```

## Short Version

```text
Improve {topic} docs for {audience}. Run git status, read AGENTS.md, inspect README and target files, edit only {allowed_scope}, avoid secrets/dependencies/workflows/unverified product claims, update changelog if user-visible, run the three local checks, inspect git diff, and report files, commands, check results, manual-verification claims, and risks.
```

## Included Scope

- The documentation files named in `{allowed_scope}`.
- Supporting navigation links when needed.
- CHANGELOG.md for user-visible documentation changes.

## Excluded Scope

- Secrets, credentials, private data, `.env` files, browser profiles, and private links.
- Workflow YAML, dependencies, generated binaries, archives, screenshots, or broad refactors unless explicitly requested.
- Unsupported or exact claims about fast-changing products.

## Safety Boundaries

- Treat pre-existing edits and untracked files as user work.
- Do not delete or move files without explicit approval.
- Do not quote leaked prompts or copied prompt dumps.
- Do not claim tests passed unless run in the current session.

## Verification Steps

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
git diff --check
git diff --stat
git diff
```

Run `python -m unittest tests.test_prompting_docs` directly if the edited
file is a guide or prompt template covered by that suite, so the failure
signal is faster than the full discovery run.

## Success Criteria

- The target documentation is clearer, public-safe, and easier to navigate for
  the named audience.
- Scope, safety, and verification requirements are satisfied.
- Internal links and related docs are updated where needed.
- Checks pass or failures are reported with relevant context.

## Final Report Format

```markdown
## Summary
## Git state
## Files changed
## Commands run
## Verification results
## Claims needing manual verification
## Remaining risks
```

## Failure Cases

| Failure | What to do |
| --- | --- |
| Branch has unsafe divergence or unexpected changes | Stop and report the safe commands a human should run. |
| Official tool docs are needed but not checked | Mark the claim for manual verification instead of guessing. |
| Scope grows beyond the requested files | Stop and recommend a separate task. |
| A local check fails | Fix related failures; report unrelated failures clearly. |
| The prompt requests exact product details | Reword conservatively unless freshly verified and dated. |
| The doc rewrite breaks an internal link or anchor | Fix the link before reporting success, or revert the section rename. |
| The topic spans multiple guides with overlapping content | Update the primary guide and add a cross-link instead of duplicating prose. |
| The requested edit would make the file read as marketing copy | Rewrite for accuracy and neutrality instead of persuasive language. |
| A required heading from AGENTS.md's prompt template rules is missing after the edit | Restore the heading before finishing; do not rely on the test suite to catch it later. |
| The audience described in `{audience}` does not match the file's existing reading level | Note the mismatch in the report and ask which audience should win instead of guessing. |

## Anti-Patterns

- Rewriting an entire guide "while I'm in there" instead of the section the
  task named. Bigger diffs are harder to review and more likely to hide an
  unintended meaning change.
- Adding a confident claim about pricing, limits, or model availability
  because it "sounds right." If it is not sourced from a file in this repo
  or freshly verified, mark it for manual verification instead.
- Treating a broken internal link as someone else's problem. If the edit
  touches the file with the broken link, fix it or report it explicitly.
- Skipping the changelog entry because the change "is just docs." Doc
  changes that readers will notice are user-visible and belong in
  CHANGELOG.md.
