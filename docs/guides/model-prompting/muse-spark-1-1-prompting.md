# Meta Muse Spark 1.1 Prompting Guide

Checked: 2026-07-12

Muse Spark 1.1 is Meta's **multimodal reasoning model** for agentic work,
computer use, coding, and multimodal understanding. It appears in Thinking mode
in Meta AI and through the Meta Model API public preview. The model name alone
does **not** grant a repository editor, browser, or computer-control harness;
the client supplies tools.

| Property | Value |
| --- | --- |
| Role | Lower-cost fast multimodal reasoning |
| Independent snapshot | ~51 Intelligence Index at xhigh; ~116 tok/s; 1M context; ~$1.25/$4.25 per 1M |
| Surfaces | Meta AI Thinking mode; Meta Model API public preview |
| Equal-score warning | Rounded Intelligence near Luna Max does not imply equal Codex coding reliability |

## When to Choose Muse Spark 1.1

Choose Muse when:

- you need multimodal understanding plus reasoning at lower cost;
- throughput matters;
- your own client provides tools (browser, computer use, code runner).

Prefer Luna/Terra/Grok/Sol when:

- you need a measured Codex coding-agent configuration;
- you need GPT-5.6 product integration (Work/Codex);
- GUI computer-use quality is unproven for your app.

## Prompting Principles

1. **Name the tools** the client actually exposes.
2. **Separate modalities** in the prompt (image facts vs text instructions).
3. **Keep one goal** per turn for agent loops.
4. **Require evidence** (screenshots, DOM snippets, file paths, command output).
5. **Do not assume** hidden computer control.

## Effort / Thinking Modes

Exact API enum names can change; independent testing has used an **xhigh-like**
deep setting. Treat Thinking vs non-Thinking (Meta AI) and API reasoning levels
as compute dials, not different model families.

| Mode band | Use | Prompt emphasis |
| --- | --- | --- |
| Fast / low thinking | Extraction, captioning, simple Q&A on clear inputs | Schema, short answers |
| Default thinking | Multistep tool use, coding with clear tests | Goal, tools, checks |
| Deep / xhigh | Ambiguous multimodal problems, multi-app computer tasks | Hypotheses, checkpoints, stop rules |

### Fast template

```text
Model: Muse Spark 1.1 | Mode: fast/low thinking

From the attached image/document, extract:
[fields]

Return JSON only matching:
[schema]

If a field is unreadable, use null and add "issues": ["..."].
```

### Agentic coding template

```text
Model: Muse Spark 1.1 | Mode: default/deep thinking

Available tools: [list exactly]
Workspace: [path or none]

Goal:
[outcome]

Constraints:
- Only use listed tools
- No invented file contents
- After each tool call, summarize observation before next action

Done when:
[tests or acceptance]

Final report:
actions taken, artifacts, verification, residual uncertainty
```

### Computer-use template

```text
Model: Muse Spark 1.1 | Computer-use client

Task:
Complete [UI workflow] in [app].

Start state:
[URL or screen description]

Rules:
- Prefer accessibility labels over brittle coordinates when available
- Confirm destructive clicks
- After each step: observe screenshot -> decide -> act
- Stop if login, CAPTCHA, or payment is required

Success screenshot criteria:
[what must be visible]
```

### Multimodal analysis template

```text
You will receive [images/pdfs/audio transcript].

Questions:
1. ...
2. ...

Answer format:
- Observation (what is visible/said)
- Inference (what you conclude)
- Confidence
- Missing evidence

Do not invent text that is not legible.
```

## Failure Modes

| Symptom | Repair |
| --- | --- |
| Invents UI state | Require screenshot observation before action |
| Treats model as full IDE | Attach or name real tools |
| Overlong chain | Cap steps; checkpoint every N actions |
| Compared unfairly to Luna Max coding | Run same harness, same tests |

## Verification Checklist

- [ ] Tools actually available to the client
- [ ] Thinking depth matched to ambiguity
- [ ] Multimodal answers separate observation vs inference
- [ ] Computer-use stop conditions for login/payment
- [ ] Local eval if used for production coding

## Related

- [Luna](gpt-5-6-luna-prompting.md) for cheaper GPT coding volume
- [Gemini 3.5 Flash](gemini-3-5-flash-prompting.md) for Google tool stack
- [Surface map](surface-and-effort-map.md)
- [Sources and observations](sources-and-observations.md)
- [Effort evaluation playbook](effort-evaluation-playbook.md)
