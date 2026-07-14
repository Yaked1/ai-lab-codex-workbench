# Gemini 3.5 Live Translate Prompting Guide

Checked: 2026-07-12

Gemini 3.5 Live Translate is a **translation-specialized audio-to-audio
interpreter path**, not a general conversational agent. API ID (public
preview): `gemini-3.5-live-translate-preview`.

| Property | Value |
| --- | --- |
| Job | Continuous speech translation |
| Languages | 70+ (vendor) |
| Tools | **No** tool calling, search grounding, function calling, system instructions, or thinking controls |
| Audio hints | ~16 kHz mono PCM in, ~24 kHz PCM out, ~100 ms chunks (vendor guide) |
| Consumer path | Google Translate app → Live translate |
| Dev path | Google AI Studio Live Translate demo / Gemini Live API with BCP-47 target |

This is **not** interchangeable with [GPT-Live-1](gpt-live-1-prompting.md).

## What You Can "Prompt"

Because system instructions and thinking controls are unsupported, "prompting"
means configuring the **session contract** outside the model:

1. Source language / auto-detect behavior (product-dependent)
2. Target language BCP-47 code
3. Mode: Listening, Conversation, Text only, or custom output (app)
4. Hardware: headphones recommended for conversation mode
5. Domain vocabulary you speak clearly (names, numbers, technical terms)

Do not expect a long system prompt to reshape personality or tool use.

## Session Setup Templates

### Conversation mode (two humans)

```text
Session goal: two-way spoken translation between [lang A] and [lang B].
Mode: Conversation
Hardware: headphones for each speaker if possible
Speaking rules for humans:
- One person at a time when possible
- Pause briefly after numbers and proper nouns
- Spell critical codes once (confirmation codes, emails)
```

### Listening mode (lecture / media)

```text
Session goal: translate ongoing speech into [target language] audio.
Mode: Listening
Speaker tips:
- Prefer clear mic placement
- Avoid talking over the source
- Re-state critical numbers if the first rendering is wrong
```

### Developer API session

```text
model: gemini-3.5-live-translate-preview
target_language: [BCP-47, e.g. ar-EG, en-US]
input_audio: 16 kHz mono PCM chunks ~100ms
output_audio: expect ~24 kHz PCM + optional transcripts
Do not send: system instructions, tool schemas, thinking levels
```

## Domain Vocabulary Technique

Since you cannot inject a rich system glossary, **speak the glossary into the
session** when quality matters:

```text
Human (before the real content):
"Proper nouns: Ahmed, Yaked, Codex. Product name: AI Lab Workbench.
Always keep these names in the original form."
Then continue with the real speech.
```

Re-state after long pauses if quality drops.

## Evaluation Protocol

Test both directions for each language pair:

| Case | Why |
| --- | --- |
| Names and brands | Proper noun survival |
| Numbers and codes | Digit accuracy |
| Technical vocabulary | Domain terms |
| Dialect shifts | Robustness |
| Emotional tone | Tone retention (subjective) |
| Interruptions | Recovery |
| Long pauses | No false end-of-turn collapse |
| Overlap | Stability under two speakers |

Record whether the system does continuous simultaneous translation or waits for
turn boundaries. That is a product behavior observation, not a prompt flag.

## Failure Modes

| Symptom | Repair |
| --- | --- |
| Expecting tools/search | Use GPT-Live or a text agent instead |
| Long system prompt ignored | Configure languages/modes only |
| Proper nouns mangled | Pre-speak glossary; slow enunciation |
| Compared unfairly to GPT-Live | Different product jobs |

## Verification Checklist

- [ ] Correct model ID for API work
- [ ] Target BCP-47 set
- [ ] No reliance on system instructions or tools
- [ ] Headphones for conversation trials
- [ ] Domain names pre-stated when critical
- [ ] Preview quotas/behavior may change

## Related

- [GPT-Live-1](gpt-live-1-prompting.md)
- [Live audio overview](../live-audio-and-translation.md)
- [Surface map](surface-and-effort-map.md)
- [Sources and observations](sources-and-observations.md)
- [Effort evaluation playbook](effort-evaluation-playbook.md)

## Shared execution policy

Run records, verification, escalation, and operational failure handling live
in one place:

- [Shared execution contract](shared-execution-contract.md)

Use that contract for every serious run. Keep only model-specific identity,
surfaces, task fit, examples, limits, and evidence on this page.

## Model-specific operating notes

### Translation evaluation matrix

Test both language directions with names, numbers, terminology, dialects,
interruptions, and overlap. Score meaning, tone, proper nouns, latency, and
turn-taking separately. Do not attribute general Gemini tool controls to this
translation-specific preview surface.
