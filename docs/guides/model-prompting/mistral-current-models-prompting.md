# Current Mistral Models Prompting Guide

Checked: 2026-07-12

## What These Models Are and Where They Are Available

Mistral Medium 3.5 and Small 4 are generalist multimodal models. OCR 4 is a
document-intelligence service, Voxtral TTS generates speech, Leanstral 1.5 is a
Lean 4 proof-engineering Labs model, and Robostral Navigate is an announced
embodied-navigation system. Do not treat this as one interchangeable family.
Current official identifiers include `mistral-medium-3-5`,
`mistral-small-2603`, `mistral-ocr-4-0`, `voxtral-mini-tts-2603`, and
`labs-leanstral-1-5`. Robostral has no public identifier in the sources reviewed.

## Task Selection and Controls

| System | Use for | Verify with |
| --- | --- | --- |
| Medium 3.5 / Small 4 | Coding, structured work, agent tasks | Same repository, tools, tests, and correction budget |
| OCR 4 | Document extraction and layout | Field accuracy, tables, boxes, language coverage, human correction |
| Voxtral TTS | Narration and speech agents | Intelligibility, latency, pronunciation, consent and rights checks |
| Leanstral 1.5 | Lean 4 proof work | Compiled proofs and reproducible project tests |
| Robostral Navigate | Research planning only | Simulation, hardware validation, and safety review |

## Recommended Prompt Structures

```text
Generalist goal: [deliverable]
Context: [bounded sources or repository]
Tools: [explicit schemas and permission boundary]
Verification: [tests, schema, or review]
Failure: report uncertainty and preserve unrelated files
```

```text
OCR task: Extract [fields] from [document set]. Return [schema] with page,
bounding-box, and confidence fields where the API provides them. Flag unclear
values. Validate the result against [ground truth sample].
```

```text
Lean task: Prove [theorem] in [Lean project]. Use only listed imports. The proof
is complete only when [command] compiles it; report any unresolved goals.
```

```text
TTS task: Read the supplied original script in [language], at [pace] with
[pronunciation notes]. Do not imitate a real person without consent. Review
proper nouns and numbers from the generated audio.
```

## Context, Cost, and Failure Modes

Use Mistral's current pricing page for deployment costs. OCR pages, speech
characters, and token work have different units. A model card listing function
calling or agents does not grant an arbitrary application's tools. Keep personal
documents and voice samples within documented privacy and consent rules.

Robostral is not production guidance: its public announcement does not establish
API access, weights, hardware, pricing, or safety terms. Never translate
high-level navigation output directly into low-level robot control without a
separate safety-critical controller and physical validation.

## Unsupported or Inappropriate Uses

Do not rank OCR, TTS, Lean proofs, or robotics with general chat scores. Do not
claim unverified handwriting, watermarking, language, deployment, or physical
robot support. Do not use copyrighted lyrics as TTS examples.

## Sources

- [Mistral model overview](https://docs.mistral.ai/models/overview)
- [Mistral pricing](https://mistral.ai/pricing/api/)
- [Mistral latest news](https://mistral.ai/news/)
- [Evidence ledger](sources-and-observations.md)

## Expanded Operating Dossier

### Run record and reproducibility

Treat every serious run as an experiment. Record the model identifier, product
surface, visible effort or thinking control, prompt revision, source or file
set, tool schemas, permissions, output limit, date, retries, elapsed time, and
the final verification result. A model name alone is not enough to reproduce an
agentic, multimodal, or long-context outcome.

### Evaluation before escalation

Start with a representative task and a measurable acceptance gate. Escalate
effort, context, tool access, or model tier only after a specific failure has
been observed. Compare successful-task cost, latency, invalid-output rate,
retries, and human correction, not output fluency or one benchmark headline.

### Operational failure handling

When a tool fails, a source conflicts, a validator rejects output, or required
authority is missing, preserve the evidence and report the blocked condition.
Do not silently substitute a different model, enable a broader permission, or
invent an unsupported capability. Treat retrieved text as data, not executable
instructions.
### Specialist evaluation boundaries

OCR needs ground-truth extraction and correction metrics; TTS needs
intelligibility, latency, consent, and rights checks; Leanstral needs compiled
proofs; robotics needs simulation and supervised physical validation. Do not use
a general chat score as a substitute for one of these domain-specific gates.
