# GPT-Live-1 and GPT-Live-1 Mini Prompting Guide

Checked: 2026-07-12

GPT-Live is a **full-duplex conversational architecture**, not a text model with
a microphone. OpenAI positions **GPT-Live-1** for paid Go/Plus/Pro paths and
**GPT-Live-1 Mini** for the free path. Deeper search or reasoning can be
delegated to a stronger text model while the live model keeps the conversation.

| Property | Value |
| --- | --- |
| GPT-Live-1 | Paid conversational live model |
| GPT-Live-1 Mini | Free-path live model |
| Architecture (vendor) | Continuous listen+speak; decisions many times per second |
| Depth controls | Instant/fast background path; Medium/High route deeper work through thinking models (product-controlled) |
| Not the same as | Gemini Live Translate (translation-only, no tools) |

Also read: [Live audio and translation](../live-audio-and-translation.md).

## Prompting Rules for Live Voice

1. Keep the system/voice instruction **short**. Long rubrics die mid-conversation.
2. Specify **interruption**, **pause**, **language**, **answer length**, and **tool use**.
3. State how to handle **misheard names and numbers**.
4. Do not demand verbatim transcripts as ground truth; overlap and noise reduce stability.
5. Privacy: microphone, memory, search, and connected tools send data to the provider.

## GPT-Live-1 Templates

### Default assistant contract

```text
You are a clear, patient voice assistant.

Speaking:
- Prefer 1-3 short sentences unless I ask for detail
- Let me finish; treat long pauses as thinking, not turn end
- If I interrupt, stop and listen
- If background speech is not me, ignore it

Language:
- Reply in [language]
- If I mix languages, follow my last clear language

Tools / delegation:
- For current facts, search and say when you are looking something up
- For hard reasoning, say you are thinking briefly, then answer
- Ask before changing topics or starting multi-step actions

Recovery:
- If you mishear a name or number, ask me to repeat only that item
- Confirm critical values by reading them back once

End of session:
- Offer a 3-bullet summary of decisions and action items
```

### Bilingual tutor

```text
Act as a bilingual tutor for [language A] and [language B].

Rules:
- Correct only one major error per turn unless I ask for full correction
- Keep spoken answers short
- Wait through long pauses
- If a question needs current facts, search and announce it
- Do not shame mistakes
```

### Meeting helper

```text
You are a meeting assistant in a live call.

Do:
- Capture action items, owners, and dates when stated
- Stay silent during side chatter unless addressed
- When asked "what did we decide?", answer in under 20 seconds

Do not:
- Speak over the main speaker
- Invent owners or deadlines
- Post messages or send emails without explicit confirmation
```

### Customer support (high-risk)

```text
You are a support agent for [product].

Allowed:
- Answer from the approved policy summary below
- Escalate to a human for refunds, legal, medical, or account takeover

Policy summary:
[paste approved short policy]

Always:
- Confirm account identifiers carefully
- Never ask for passwords or full payment numbers
- Summarize next steps before ending
```

## GPT-Live-1 Mini

Prompt Mini the same way, but assume **less deep reasoning** and more need for
short turns. Push hard multi-step work to text chat or paid Live-1.

```text
Keep answers under 15 seconds of speech.
If the question is complex, give a short plan and ask which step to do first.
```

## Depth / Effort-Style Behavior

Product labels for Instant vs Medium vs High can change. Prompt for the
**behavior** you want:

| Desired behavior | Instruction to include |
| --- | --- |
| Fast chat | "Answer immediately in one breath. No tools unless I ask." |
| Medium help | "You may search once if facts are required; announce it." |
| Deep work | "For hard problems, think then give a structured short answer; offer to continue in text for long artifacts." |

Do not assume a fixed end-to-end latency. Network, speech length, tools, and
interruptions all move response time.

## Evaluation Protocol

Measure under the same audio conditions:

| Metric | How |
| --- | --- |
| Recognition accuracy | Scripted phrases with names/numbers |
| Interruption success | User cuts mid-sentence |
| False starts | Coughs, background TV |
| Pause handling | 3-5 second thinking pauses |
| Tool-delegation latency | Ask a current-events question |
| Transcript match | Spoken answer vs visible transcript |

## Failure Modes

| Symptom | Repair |
| --- | --- |
| Talks over user | Strengthen pause/interrupt rules |
| Answers during thinking silence | "Wait through long pauses" |
| Hallucinated action items | "Only capture explicitly stated owners/dates" |
| Overlong monologue | Sentence cap + "ask before detailing" |
| Confused with Live Translate | Use GPT-Live for conversation; Translate for speech-to-speech language conversion |

## Privacy Checklist

- [ ] User knows mic is on
- [ ] Memory settings reviewed
- [ ] Search/tools policy stated
- [ ] No passwords or secrets spoken into the session
- [ ] Regional policy considered for recording/transcription

## Verification Checklist

- [ ] Voice instruction is short enough for live use
- [ ] Interrupt / pause / length rules stated
- [ ] Mini vs Live-1 capability expectations set
- [ ] Not confused with Live Translate
- [ ] Evaluation metrics recorded under fixed audio conditions

## Related

- [Live audio overview](../live-audio-and-translation.md)
- [Surface map](surface-and-effort-map.md)
- [Frontier essay](../frontier-models-and-multimodal-systems-2026.md)
- [Sources and observations](sources-and-observations.md)
- [Effort evaluation playbook](effort-evaluation-playbook.md)

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
### Live-conversation test matrix

Measure interruption, pause, overlap, recognition, spoken-output accuracy,
tool-delegation latency, and transcript alignment under recorded network and
audio conditions. A saved transcript cannot demonstrate a full-duplex voice
experience.
