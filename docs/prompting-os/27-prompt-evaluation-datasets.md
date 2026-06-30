# Prompt Evaluation Datasets

Prompt evaluation is only as useful as the cases it runs. A vague rubric can
catch style problems, but a dataset catches behavior. This module explains how
to design small, reviewable evaluation datasets for prompts, coding-agent work
orders, RAG answers, structured outputs, image prompts, and release-package
documentation.

The goal is not to create a heavy benchmark suite. The goal is to keep prompt
changes honest by recording representative tasks, expected evidence, known
failure modes, and regression cases.

## Dataset Principles

| Principle | Meaning |
| --- | --- |
| Small beats absent | Five well-chosen cases are better than no regression suite. |
| Evidence beats vibes | Each case should name what output or behavior proves success. |
| Negative cases matter | Missing data, malicious source text, and unsafe requests should be tested. |
| Source status matters | RAG cases should label official, community, structural-only, and unverified sources. |
| Determinism is useful | Use fixed inputs, expected sections, and stable pass/fail checks where possible. |
| Human review remains valid | Some prompts need rubric scoring rather than exact string comparison. |

## Dataset Types

| Dataset | Use for | Example case |
| --- | --- | --- |
| Golden cases | Normal expected behavior. | "Create a docs update work order with scope, safety, checks, and final report." |
| Edge cases | Boundary conditions. | "The task spans docs and scripts but forbids dependency changes." |
| Missing-information cases | Unclear or incomplete input. | "The user asks for latest pricing without a source." |
| Adversarial cases | Prompt injection or unsafe source text. | "A retrieved note says to ignore repository rules." |
| Regression cases | Previously fixed failure. | "A prompt template must keep final report and failure cases." |
| Format cases | Structured output contracts. | "Return JSON with required keys and no extra prose." |
| Public-safety cases | Secret, private path, or leaked prompt handling. | "Source includes a private local path and token-looking text." |
| Package cases | Release and manifest behavior. | "Build package and confirm Markdown byte floor." |

## Minimal Case Schema

Use a simple Markdown or JSON-like structure. It should be easy to review in a
pull request.

```text
id:
title:
prompt_under_test:
input:
trusted_context:
untrusted_context:
expected_behavior:
forbidden_behavior:
required_output_sections:
verification:
source_status:
risk_level:
notes:
```

## Markdown Case Template

```markdown
## Case: docs-work-order-normal

Prompt under test:
`prompts/codex/docs-update.goal.md`

Input:
"Update the public README with a package review section."

Trusted context:
- Repository AGENTS rules.
- Existing README package section.
- Package builder script.

Untrusted context:
- None.

Expected behavior:
- Inspect current README and package docs.
- Preserve unrelated changes.
- Add public-safe package review guidance.
- Run relevant checks or report skipped checks.

Forbidden behavior:
- Do not invent package registry publishing.
- Do not add dependencies.
- Do not include private local paths.

Required output sections:
- Summary.
- Changed files.
- Commands run.
- Checks run.
- Remaining risks.

Verification:
- Prompt contains target tool, purpose, full prompt, short version, inputs,
  scope, safety, verification, success criteria, final report, and failure
  cases.
```

## Prompt Template Dataset

Prompt templates should be tested for section completeness and operational
behavior.

| Case | Input | Expected behavior |
| --- | --- | --- |
| Docs update | A scoped documentation change. | Reads files first, updates docs, runs checks, reports risks. |
| Bug fix | A failing test and a likely file. | Reproduces or inspects failure, makes minimal fix, reruns focused check. |
| Feature | A small feature request. | Identifies scope, avoids unrelated refactor, adds tests where practical. |
| Cleanup | A public-safe organization task. | Preserves files, avoids deletion unless requested, provides manifest when moving. |
| PR review | A diff and expected goal. | Findings first, file/line references, severity ordering, no unnecessary summary. |

Required assertions:

- Target tool exists.
- Purpose exists.
- Full prompt exists.
- Short version exists.
- Inputs to fill exist.
- Included scope exists.
- Excluded scope exists.
- Safety boundaries exist.
- Verification steps exist.
- Success criteria exist.
- Final report format exists.
- Failure cases exist.

## Coding-Agent Evaluation Dataset

Coding-agent cases should test repository behavior, not only prose quality.

| Case | Risk | Required evidence |
| --- | --- | --- |
| Dirty worktree | Agent may overwrite user changes. | `git status` inspected, unrelated files untouched. |
| Missing local instructions | Agent may ignore repository rules. | `AGENTS.md` read before editing. |
| Dependency temptation | Agent may install packages unnecessarily. | No dependency change unless approved. |
| Test failure | Agent may claim success without verification. | Command output or explicit failure report. |
| Staged changes | Agent may unstage or overwrite prior work. | Staged/unstaged state reported and preserved. |
| Public doc update | Agent may include private context. | Secret/private-path scan passes. |

## RAG Evaluation Dataset

RAG cases must separate source evidence from model inference.

| Field | Requirement |
| --- | --- |
| Source list | Each source has name, status, date if known, and relevance. |
| Trusted source text | Text used for claims, not hidden instructions. |
| Distractor text | Irrelevant or malicious source snippets. |
| Expected claims | Claims that should appear with support. |
| Forbidden claims | Claims that are unsupported or too current to state. |
| Citation behavior | Links or source names should map to claims. |
| Uncertainty behavior | Missing or stale data should be reported. |

Example case:

```text
Question:
Summarize a tool's current pricing.

Source status:
- Official pricing page: not provided.
- Community blog: provided, six months old.

Expected behavior:
- Do not state exact pricing as current.
- Say official pricing must be verified.
- Use the blog only for historical or structural context.
```

## Structured Output Dataset

Structured-output prompts need schema-focused cases.

| Case | Expected check |
| --- | --- |
| Valid minimal input | All required keys present. |
| Extra unknown fields | Unknown fields rejected or ignored by policy. |
| Missing required input | Error object or missing-information response. |
| Ambiguous enum | Uses allowed enum only or asks for clarification. |
| Injection in field value | Treats value as data, not instructions. |

Useful checks:

- JSON parses.
- Required keys exist.
- Enum values are allowed.
- No markdown fence appears when raw JSON is required.
- Error format is consistent.

## Image Prompt Evaluation Dataset

Image prompts are harder to test deterministically, but they can still be
evaluated.

| Case | Expected behavior |
| --- | --- |
| Product shot | Prompt names product, material, perspective, background, and constraints. |
| UI mockup | Prompt names screen type, layout, density, typography, and forbidden elements. |
| Character reference | Prompt separates identity, pose, clothing, lighting, and consistency cues. |
| Revision | Prompt preserves required elements and names exact changes. |
| Safety | Prompt avoids private data, real-person impersonation, or disallowed content. |

Evaluation evidence:

- Generated output is inspected.
- Required elements are present.
- Forbidden elements are absent.
- Text in image is legible if requested.
- The prompt records what changed between iterations.

## Package Evaluation Dataset

Package datasets test release promises.

| Case | Required evidence |
| --- | --- |
| Build focused package | ZIP exists, manifest exists, SHA-256 recorded. |
| Manifest public safety | Manifest paths are relative and exclude local machine paths. |
| Markdown depth | Count and byte floor pass. |
| Required modules | Required files appear in package manifest. |
| Exclusion rules | `.env`, archives, caches, private-looking files are excluded. |
| Determinism | Fixed ZIP timestamp is used for files. |

## Scoring Rubric

Use a five-point scale for human review.

| Score | Meaning |
| --- | --- |
| 5 | Fully satisfies expected behavior, includes evidence, avoids forbidden behavior. |
| 4 | Satisfies core behavior with minor clarity gaps. |
| 3 | Partially useful but misses a required section or weakens evidence. |
| 2 | Major omission, unsafe assumption, or poor verification. |
| 1 | Fails the task or violates safety boundary. |

For package or schema cases, prefer pass/fail checks. For prose prompts, use
the rubric and record reviewer notes.

## Dataset Storage

Keep datasets close to the artifact they evaluate.

| Artifact | Suggested location |
| --- | --- |
| Prompt templates | `tests/` for automated section checks; `docs/prompting-os/evals/` for rubric cases. |
| Package builder | `tests/test_prompting_os_package.py`. |
| Guide content | `tests/test_prompting_docs.py` for required headings and links. |
| Script behavior | Script-specific test file under `tests/`. |
| Manual review cases | Markdown under `docs/prompting-os/evals/` or guide appendices. |

## Change Control

Update evaluation datasets when:

- A prompt template gains or loses required sections.
- A package floor changes.
- A source-policy rule changes.
- A recurring failure is fixed and should not regress.
- A guide starts making a new public promise.
- A script's allowed files or outputs change.

Do not update tests only to make a weak implementation pass. The dataset should
represent the desired behavior, not the current workaround.

## Completion Checklist

- [ ] Dataset cases include normal, edge, missing-information, adversarial, and
  regression examples where relevant.
- [ ] Every case has expected and forbidden behavior.
- [ ] Verification is specific enough to run or review.
- [ ] Source status is recorded for RAG and corpus-inspired cases.
- [ ] Public-safety cases include private path and secret-pattern handling.
- [ ] Package cases inspect manifest evidence, not only command success.
- [ ] Human-scored cases have a rubric.
- [ ] Automated tests guard stable promises.
