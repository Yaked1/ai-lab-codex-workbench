# Completion Evidence Manual

Completion is not intent. Completion is current-state evidence that every
explicit requirement has been satisfied or honestly reported as not satisfied.
This manual defines how to prove completion for prompt work, documentation
expansion, coding-agent tasks, package builds, and public-safety reviews.

Use this manual whenever a task has multiple requirements, a referenced
instruction file, a package artifact, or a final report that could overclaim.

## Evidence Rule

For each requirement, identify:

1. The exact requirement.
2. The artifact that would prove it.
3. The command, file, manifest, rendered page, or test result that provides
   evidence.
4. Whether the evidence proves completion, contradicts completion, is weak, or
   is missing.
5. The next action if evidence is weak or missing.

Do not mark a broad task complete because "the tests passed" unless the tests
cover the broad requirement.

## Evidence Matrix

| Requirement | Strong evidence | Weak evidence |
| --- | --- | --- |
| README routes readers | Named sections, links, and executable commands. | Visual impression that it is long. |
| Prompting OS preserves core behavior | Named artifacts, example, failure, and verification assertions. | File or byte totals. |
| Package contents are exact | Source commit, hashes, and source/manifest/archive path parity. | ZIP file size alone. |
| Package was built | Command output, ZIP path, manifest path, hash. | Package script exists. |
| Manifest was inspected | Manifest excerpt and derived metrics. | Package command printed success. |
| Public safety preserved | Secret scan, private-path search, source-policy review. | No secrets noticed manually. |
| Prompt templates complete | Tests or checklist across all prompt files. | One template looks complete. |
| Archive used safely | Source map, skipped-source list, no private paths. | Goal file mentioned an archive. |
| Changes staged | `git status --short --branch` after staging. | Intention to stage. |

## Requirement Extraction

When given an instruction file or broad goal, turn it into a checklist before
closing.

Example:

```text
Requirement:
- Prompting OS package preserves its named artifacts and commit-exact paths.

Evidence:
- Worked example, failure case, and verification command.
- Row-level source identity.
- `source_commit` and source/manifest/archive path parity.

Requirement:
- Build package and report SHA-256.

Evidence:
- Package builder output.
- Manifest archive hash.
- Get-FileHash or script output.
```

## Completion States

Use precise states.

| State | Meaning |
| --- | --- |
| Proven | Evidence directly satisfies the requirement. |
| Contradicted | Evidence shows the requirement is not met. |
| Incomplete | Work exists but does not satisfy the requirement. |
| Weak | Evidence is indirect or too narrow. |
| Missing | No evidence gathered. |
| Not applicable | Requirement does not apply, with reason. |
| Blocked | Cannot proceed after repeated blocker and no meaningful progress remains. |

Final reports should use these states implicitly by saying what passed, what
failed, what was skipped, and what remains unverified.

## Package Completion Evidence

A package change is complete only after package evidence is gathered.

Required fields:

```text
Package path:
Manifest path:
ZIP file count:
ZIP size:
ZIP SHA-256:
Markdown file count:
Markdown byte count:
Shortest packaged Markdown:
Required modules present:
Excluded files checked:
Manifest path safety:
```

PowerShell examples:

```powershell
python scripts/create_prompting_os_package.py --version v1 --output-dir .\.tmp\prompting-os-package-check
Get-Content .\.tmp\prompting-os-package-check\prompting-os-v1-manifest.json -TotalCount 120
Get-FileHash .\.tmp\prompting-os-package-check\prompting-os-v1.zip -Algorithm SHA256
```

## Documentation Completion Evidence

For docs:

- Heading list proves navigation shape.
- Link tests or grep prove key links exist.
- Content tests prove required sections.
- Public-safety search proves no obvious private path or secret pattern.
- Changelog proves user-visible change is recorded.

Do not use line or byte counts to prove quality. Test named sections, examples,
failure behavior, source identity, and verification instead.

## Prompt Template Completion Evidence

Required sections:

- Target tool.
- Purpose.
- Full prompt.
- Short version.
- Inputs to fill.
- Included scope.
- Excluded scope.
- Safety boundaries.
- Verification steps.
- Success criteria.
- Final report format.
- Failure cases.

Evidence:

- Automated test across `prompts/**`.
- Manual sample review for one template per tool family.
- No private paths or secrets.

## Source Completion Evidence

For source-grounded work:

- Sources inspected are named.
- Source status is recorded.
- Official-doc needs are marked.
- Skipped sources are listed with reason.
- Structural-only sources are not copied.
- Direct quotes are short and compliant.
- Local paths are removed.

## Red-Team Completion Evidence

For high-risk tasks, include adversarial evidence:

- Prompt injection case checked.
- Missing-information behavior checked.
- Unsafe request behavior checked.
- Stale product claim behavior checked.
- Secret/private-path handling checked.
- Package exclusion behavior checked.

## Final Report Checklist

Use this final report shape:

```text
Summary:
- Main outcome.

Changed files:
- Grouped by area.

Requirements evidence:
- README bytes:
- Prompting OS Markdown files:
- Prompting OS Markdown bytes:
- Shortest packaged Markdown:
- ZIP file count:
- ZIP SHA-256:
- Required tests:
- Public-safety scan:
- Archive sources skipped:

Commands run:
- Command: result.

Remaining risks:
- Unverified external claims.
- Skipped sources.
- Checks not run.
```

## Common Overclaims

| Overclaim | Why it is wrong | Correct report |
| --- | --- | --- |
| "Everything is done" | No requirement-by-requirement evidence. | "The requested checks pass; package metrics are..." |
| "No secrets exist" | Only edited files were skimmed. | "Health check and targeted private-path search found no matches." |
| "Package is verified" | ZIP built but manifest not inspected. | "Package built; manifest count and hashes inspected." |
| "Current model support is documented" | No official docs checked. | "Model support is marked for official-doc verification." |
| "All files are comprehensive" | Some files were not audited. | "Major docs and package files were expanded; remaining small files are scripts/tests/static config." |

## Completion Checklist

- [ ] Requirements were extracted from the task and referenced files.
- [ ] Each requirement has direct evidence.
- [ ] Tests are treated as evidence only for what they cover.
- [ ] Package manifest is inspected when package changed.
- [ ] Public-safety scan is run or skipped with reason.
- [ ] Skipped sources are named.
- [ ] Remaining limitations are stated.
- [ ] Final status does not overclaim beyond evidence.
