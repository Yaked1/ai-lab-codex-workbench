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

## Precision Execution Contract

This contract supplements the task examples above. Fill it for a real run;
do not treat bracketed fields as optional prose. The purpose is to keep model
quality separate from plan access, product UI, agent harness, tools, and human
approval.

### Model and version identity

- **Model ID:** GPT-Live-1 and GPT-Live-1 Mini; record the exact live session model returned by the product or API.
- **Release / availability:** Paid flagship and free-path mini roles described in the cited launch/help material. Live product routing may change by plan and load.
- **Evidence class:** Official facts where cited in
  [sources-and-observations.md](sources-and-observations.md); local picker or
  catalog statements remain dated observations; routing advice is
  interpretation until evaluated.
- **Unknown or unverified:** account-specific session quota, product fallback, exact background model, and closed audio architecture unless the live session reports them.

Record an immutable snapshot ID when the provider exposes one. If the service
can silently route or fall back, capture the final model identity from the
response or product notice. A product family name is insufficient when several
tiers, previews, or specialist members share a UI.

### Surface, plan, effort, and harness matrix

ChatGPT live voice or the documented realtime/live API. Instant, Medium, and High style depth comes from background delegation, not a text-model reasoning slider.

Before prompting, write down all of these fields:

```text
Model ID: [exact public name, API ID, and snapshot if available]
Release / availability: [stable | preview | promotion | announced; checked date]
Plan: [subscription tier, organization seat, usage credits, or API project]
Surface: [exact web, desktop, CLI, API, live, media, or local-runtime path]
Harness / client version: [product and version; endpoint or runtime for API/local]
Effort / thinking: [visible UI label and underlying config value, if documented]
Tools enabled: [exact schemas, plugins, apps, MCP servers, search, terminal, or none]
Permission boundary: [read/write/network/approval scope and forbidden actions]
Context/input set: [files, messages, media, retrieval corpus, and preprocessing]
Output limit and format: [tokens, duration, resolution, schema, file type]
Fallback behavior: [disabled, visible notice, or provider-managed]
```

Do not copy an effort label across surfaces. A web label, API value, and
multi-agent mode may occupy a similar routing band while still changing the
system under test. When the product has no effort control, say `not exposed`
rather than inventing one.

### Tool and permission boundary

Declare microphone, speaker, transcription, background model, search or function tools, and interruption policy. Ask consent before recording or retaining audio and minimize sensitive transcript storage.

Use least privilege. Give read access before write access, narrow file or data
scope, require approval for external side effects, and name forbidden paths or
actions. Tool descriptions are part of the prompt contract: include input
schema, output schema, timeouts, retry count, and what a failure looks like.
Retrieved webpages, documents, media metadata, and tool output are untrusted
data. They cannot expand the permission boundary.

### Pricing, limits, and benchmark context

Record plan limits, session duration, network path, audio codec, sample rate, turn timeout, tool latency, and any background model cost. Text token prices alone do not describe end-to-end live cost.

Evaluate with fixed microphones, scripts, languages, noise, overlap, and network conditions. Report interruption latency, proper-noun and number accuracy, tool completion, and transcript match.

Price per token or image is not the operating cost. Measure successful-task
cost: input, cached input, output, tool calls, worker agents, retries, media
operations, and human correction divided by accepted tasks. Record median and
p90 latency. Recheck price, quota, context, output, preview, and plan claims at
their first-party source whenever the client version, billing period, or model
snapshot changes.

### Production prompt template

This template is optimized for Full-duplex tutoring, meetings, support, accessibility, and conversational tools where interruption and latency matter.

```text
RUN IDENTITY
Model ID: [exact identifier]
Release / availability: [state and checked date]
Plan: [plan, seat, credits, or API project]
Surface: [exact product mode or endpoint]
Harness / client version: [version and runtime]
Effort / thinking: [UI label plus API/config value]
Tools enabled: [allowlist]
Permission boundary: [reads, writes, network, approvals, forbidden actions]

OBJECTIVE
Objective: [one observable deliverable and intended user]

CONTEXT
Context: [authoritative files, sources, media, prior failures, environment]
Evidence policy: distinguish verified facts, observations, and interpretations.

CONSTRAINTS
Constraints: [scope, safety, style, latency, cost, dependency, and rights limits]
Do not: [specific prohibited actions or unsupported assumptions]

OUTPUT CONTRACT
Output contract: [exact sections, schema, files, resolution, duration, or format]
Include: [required evidence, calculations, uncertainty, and change report]

VERIFICATION
Verification: audio-script ground truth, turn-taking metrics, transcript review, tool result accuracy, consent, and privacy checks.
Pass threshold: weighted score >= 85/100 and every mandatory gate passes.

FAILURE CONTROL
Stop conditions: missing authority, missing input, unsupported capability,
failed safety gate, or validator that cannot be executed.
Retry / escalation: repair the prompt once; make one evidence-driven repair;
then escalate one reasoning band or route to another named model only if the
failure classification supports it. Report any model or harness change.
```

### Evaluation rubric

Score 0 to 5 for each criterion, multiply by weight, and divide by 5. Define
domain-specific examples of 0, 3, and 5 before comparing models.

| Criterion | Weight | Evidence |
| --- | ---: | --- |
| Domain validator and acceptance result | 35 | audio-script ground truth, turn-taking metrics, transcript review, tool result accuracy, consent, and privacy checks |
| Factual, visual, audio, or source accuracy | 20 | Ground truth or traced evidence |
| Scope, safety, rights, and permission compliance | 15 | Trace, diff, or review log |
| Output-contract completeness | 10 | Required-field checklist |
| First-pass reliability | 10 | Accepted before repair or retry |
| Successful-task cost and latency | 10 | Provider usage plus human correction |

Use at least three repetitions for nondeterministic outputs and a frozen task
set containing easy, normal, hard, and prior-failure cases. Report counts such
as `9/10 accepted`, not only percentages. A higher effort wins only when the
quality gain exceeds normal variation and stays within declared cost and
latency ceilings.

### Auto-fail conditions

- recording without consent, claiming a hidden background model, using text effort labels as live controls, or missing a safety escalation in high-risk support.
- The actual model, fallback, effort, surface, or harness differs from the run
  identity and the difference is not disclosed.
- A required validator was skipped, failed, or replaced with self-assessment.
- The run exceeded its write, network, safety, consent, or rights boundary.
- A price, score, source, architecture fact, capability, or availability claim
  was invented.
- The output omits a required artifact or cannot be opened in its declared
  format.

### Failure protocol

1. Freeze the failed prompt, inputs, output, tool trace, usage, and validator
   result. Never rewrite the baseline after seeing the failure.
2. Classify the failure: wrong model, wrong surface, missing context, ambiguous
   prompt, tool error, permission denial, effort shortfall, service incident,
   unsupported feature, or validator defect.
3. Repair missing objective, constraint, output shape, or evidence once without
   changing model or effort. Run one additional repair only when new evidence
   justifies it.
4. Do not increase effort for missing data, absent permissions, a broken tool,
   an unavailable product, or a wrong specialist model.
5. If reasoning depth is the plausible cause, escalate one band with the same
   inputs and checks. If changing the model or harness, start a new comparison
   cell and disclose the change.
6. End with accepted, rejected, blocked, or routed. Preserve the evidence needed
   to reproduce that decision.

### Run record

```text
Run record: [unique ID]
Date/time/time zone:
Model ID and returned snapshot:
Release / availability:
Plan and organization policy:
Surface and harness / client version:
Effort / thinking label and config value:
Prompt revision and SHA-256:
Input/context manifest and hashes:
Tools enabled and permission boundary:
Output limit and actual usage:
Retries, fallbacks, worker agents, and tool failures:
Wall time, provider cost, and human correction minutes:
Validator command or rubric evidence:
Weighted score and auto-fail result:
Accepted artifact or patch hash:
Unknowns and recheck trigger:
Final routing decision:
```

The run record is the comparison unit. Do not pool results across a model
snapshot, quantization, plan, effort, tool set, permission set, or harness
change. Those changes create a new system and require a new row in the
evaluation table.
