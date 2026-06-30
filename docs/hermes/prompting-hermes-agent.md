# Prompting Hermes Agent

Use Hermes Agent prompts for public research and documentation only when the
source material is public-safe and the output will be reviewed.

## Full Prompt Template

```text
Target: Hermes Agent

Purpose: Review public AI skills and prompt-guide candidates for a public
documentation repository.

Read only the public candidate report and source policy. Do not use private
memory, private chats, OAuth files, provider tokens, browser sessions, or local
logs as source material.

Select up to [N] public-safe sources. Prefer official documentation. Label
community, unofficial, leak-derived, inferred, or unverified sources.

Draft a Markdown guide section with:
- what the tool/resource is
- beginner friendliness
- public-safe use cases
- install commands only if verified
- placeholders for unverified commands
- Windows notes
- failure modes
- evaluation checklist
- source links
- license/source status

Do not push to main. Prepare output for branch, PR, checks, review, and merge.
```

## Short Version

```text
Use only public candidate sources, draft a reviewed guide update, exclude
private memory and secrets, and prepare it for PR review.
```

## Why This Works

- It separates public candidate reports from private Hermes state.
- It limits source count.
- It requires source labels.
- It blocks direct publishing.
- It requires failure modes and evaluation.

## Failure Cases

- The agent uses private memory as evidence.
- The agent invents install commands.
- The output copies leaked prompts.
- The automation writes directly to `main`.
- The guide omits source status or license notes.

## Output Constraints

- Markdown only.
- No secrets or private paths.
- No copied prompt dumps.
- No Hermes language-model coverage.
- Source links required.
- Unverified commands must be placeholders.

## Revision Checklist

- [ ] Did the prompt define source boundaries?
- [ ] Did it forbid private memory and logs?
- [ ] Did it require branch and PR review?
- [ ] Did it require official-doc verification?
- [ ] Did it include failure modes?

## Source Ledger Add-On

Add this to Hermes Agent prompts when source material is involved:

```text
For every source, record:
- Source name
- Source URL if public
- Source status: official, community, unofficial, leak-derived, inferred, or unverified
- What claim it supports
- What claim it cannot support
- License or reuse concern
- Whether current behavior must be verified in official docs
```

## Review Prompt

```text
Review the Hermes Agent draft as a public repository maintainer.

Check:
- No private memory, OAuth state, logs, provider keys, or local paths.
- No Hermes language-model, benchmark, quantization, GGUF, Ollama, vLLM, or
  SGLang coverage.
- Commands are official-doc verified or placeholders.
- Source status is labeled.
- The draft requires branch, PR, checks, and human review.

Return:
- Findings ordered by severity.
- Files or sections affected.
- Claims needing official-doc verification.
- Required fixes before publication.
```

## Evaluation Cases

| Case | Expected behavior |
| --- | --- |
| Public official doc source | Summarize conservatively and link source. |
| Community source | Use for pattern only; mark current claims for official verification. |
| Private memory available | Do not use it as public evidence. |
| User asks for model-serving guide | Decline or redirect out of Hermes Agent scope. |
| Automation asks to push to `main` | Refuse; require branch, PR, checks, review. |

## Final Report Fields

- Sources used.
- Sources skipped.
- Public-safety checks.
- Commands verified or left as placeholders.
- Files changed or draft sections produced.
- Claims needing official-doc verification.
- Remaining risks.
