# Effort Evaluation Playbook

Checked: 2026-07-12

This playbook helps choose an effort level with evidence. It applies to GPT-5.6
Low/Light through Max, Claude Low through Max, Grok Low through High, and
Gemini Flash API thinking levels. Ultra and Ultracode require a separate
orchestration evaluation because they change the workflow, not only the amount
of single-model reasoning.

## The Decision to Measure

Choose the lowest effort that meets the task's quality threshold at an
acceptable total cost. Total cost includes model or credit use, retries,
elapsed time, tool calls, and human correction.

```text
Decision: choose [model + surface + effort] for [task class]
Quality threshold: [pass rate / rubric score]
Latency ceiling: [seconds or minutes]
Cost ceiling: [per task]
Safety gate: [no secrets / approval / refusal behavior]
Review burden: [maximum human correction time]
```

## Build a Representative Task Set

Use 10 to 30 tasks drawn from real work. A useful set contains:

- easy tasks that should expose over-spending;
- normal tasks that represent most volume;
- hard tasks that test useful headroom;
- known failure cases from prior runs;
- tasks with deterministic checks where possible.

Do not select only impressive demos. Keep the task set frozen while comparing
efforts.

## Freeze the Prompt Contract

Change only the effort control during the first comparison. Keep model,
surface, prompt, context, tools, time limit, and acceptance checks identical.

```text
Goal: [observable result]
Inputs: [frozen files or source packet]
Scope: [include / exclude]
Tools: [exact list]
Verification: [commands or rubric]
Failure: [stop condition]
Output: [schema]
```

If one effort needs a different prompt to succeed, record a second “prompt
tuning” experiment rather than silently changing the baseline.

## Metrics

| Metric | Why it matters | Collection |
| --- | --- | --- |
| Task success | Primary outcome | Deterministic test or blinded rubric |
| First-pass success | Reliability | Pass before any retry |
| Human correction | Hidden operating cost | Minutes and edit count |
| Elapsed time | User experience | Wall-clock start to accepted result |
| Input/output tokens | API cost driver | Provider usage record |
| Tool calls | Agent efficiency | Trace count and failures |
| Retry count | Stability | Number of repair loops |
| Scope violations | Safety/maintainability | Diff or action audit |
| Refusal/fallback | Product behavior | Visible notice and final model identity |

## Single-Model Ladder

Use this procedure for Sol, Terra, Luna, Fable, Opus, Grok, and Gemini Flash:

1. Start at the recommended daily level, not automatically at the minimum.
2. Run the frozen set at least twice if outputs are nondeterministic.
3. Escalate one band only when a failed acceptance check plausibly needs more
   reasoning or tool use.
4. Stop when the quality threshold passes or the failure is missing data,
   permissions, or an unsupported product feature.
5. Prefer the lower effort when the quality confidence intervals overlap and
   correction burden is similar.

Typical starting bands:

| Task | GPT-5.6 | Claude | Grok | Gemini Flash API |
| --- | --- | --- | --- | --- |
| Schema transform | Low/Light | Low | Low | minimal/low |
| Normal feature or report | Medium | High or Medium after eval | Medium | medium |
| Difficult debugging | High | High/xhigh | High | high |
| Ambiguous architecture | Sol Extra High | xhigh | High plus strict evidence | high plus stronger tools |
| Final single-agent review | Max after proof of headroom | Max after proof of headroom | High | high |

## Ultra and Ultracode Experiment

Do not compare Ultra to Max by changing only a menu label. Ultra adds parallel
agents; Ultracode adds `xhigh` plus standing permission for multi-agent
workflows.

Compare two end-to-end workflows:

```text
Baseline A: one agent at High or Max
Workflow B: Ultra / Ultracode with explicit independent streams

Same overall task, repository state, acceptance suite, and time limit.
Measure total tokens across all agents, wall time, duplicate work, merge
conflicts, final pass rate, and human reconciliation time.
```

Parallel evaluation contract:

```text
Overall outcome: [project]
Stream A ownership: [paths]
Stream B ownership: [paths]
Stream C ownership: [paths]
Reviewer: read-only
Shared interface freeze: [file/schema]
Synthesis rule: [tests are truth / primary agent resolves]
Abort condition: streams are sequential or collide on one hot file
```

An orchestration win requires more than a higher-quality answer. It should
improve accepted task success or elapsed time enough to justify higher total
tokens and coordination risk.

## Coding Evaluation

Use a clean checkout or reproducible fixture for each run. Record:

```text
commit_before:
model:
surface:
effort:
prompt_hash:
tools_enabled:
commands_run:
tests_passed:
files_changed:
scope_violations:
elapsed_seconds:
human_fix_minutes:
commit_after_or_patch_hash:
```

Reject a run that reports success without executing the named check. A good
explanation cannot substitute for a passing regression test.

## Research and Document Evaluation

Score each artifact on:

1. claim-to-source traceability;
2. numerical accuracy;
3. conflict handling;
4. decision usefulness;
5. editability;
6. unsupported-claim count;
7. human correction time.

Use a blind reviewer when possible. Keep visual polish separate from analytical
correctness.

## Live Audio Evaluation

Text-model effort does not transfer directly to full-duplex voice. For
GPT-Live and Live Translate, freeze the microphone, network, script, language
pair, and background-noise conditions. Measure interruption, pause handling,
proper nouns, numbers, overlap, tool-delegation time, and transcript match.

## Image and Video Evaluation

Image and video systems generally do not expose the same effort ladder. Hold
prompt, references, aspect ratio, resolution, and revision count constant.
Score prompt adherence, typography, identity consistency, edit precision,
artifacts, audio sync, latency, and safety. Inspect original outputs rather
than compressed social media.

## Failure Modes

| Failure | Repair |
| --- | --- |
| Max wins because prompt changed | Re-run with frozen baseline prompt |
| One lucky output decides routing | Use repeated runs and a task set |
| Ultra appears cheaper because worker tokens omitted | Count all agents |
| Higher effort fixes missing context | Add the missing input; effort was not the cause |
| Benchmark score replaces local eval | Use benchmark only to choose candidates |
| Human correction ignored | Record minutes and edit count |

## Verification Checklist

- [ ] Task set represents real easy, normal, hard, and failure cases
- [ ] Prompt, context, tools, and checks are frozen across effort comparisons
- [ ] Success, latency, total tokens, retries, and human correction recorded
- [ ] Ultra/Ultracode counted as a workflow with all agent costs
- [ ] Fable fallback and harness identity logged
- [ ] Decision rule chooses the lowest effort meeting the threshold
- [ ] Results include date, product surface, client version, and model ID

## Related

- [Surface and effort map](surface-and-effort-map.md)
- [Sources and observations](sources-and-observations.md)
- [Model prompting index](README.md)

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
### Surface-specific confirmation

Recheck live product documentation before relying on a changed model picker,
price, context limit, tool, or preview status. Keep any local observation labeled
as local evidence rather than a universal capability claim.

## Weighted Decision Rubric

Define weights before viewing results. A general coding or research starting
rubric is below; specialist guides replace criteria that do not fit.

| Criterion | Weight | Measurement |
| --- | ---: | --- |
| Acceptance-test success | 35 | Deterministic tests, schema validator, or ground truth |
| Factual or source accuracy | 20 | Verified claims and unsupported-claim count |
| Scope and permission compliance | 15 | Diff, tool trace, and approval audit |
| Completeness of required output | 10 | Contract field coverage |
| First-pass reliability | 10 | Pass before repair or retry |
| Successful-task cost and latency | 10 | Total model/tool cost and wall time for accepted runs |

Score each criterion from 0 to 5, multiply by its weight, and divide by 5 for a
0-to-100 result. Set the pass threshold before running. A useful starting gate
is 85/100 with no auto-fail. Do not average away secret exposure, an unapproved
write, a fabricated citation, a failed mandatory test, or wrong model identity.

## Experiment Design and Confidence

Use paired tasks when comparing efforts. Each task appears at every candidate
setting with the same prompt, inputs, tool schemas, permissions, and validator.
Randomize run order where time, cache warmth, or service load could bias the
result. For nondeterministic tasks, use at least three repetitions per cell;
ten or more is better for routing rules that affect high volume or cost.

Report numerator and denominator, not only a percentage. `18/20 accepted` is
more useful than `90%`. Report median and p90 latency, median successful-task
cost, first-pass success, retry rate, and human-fix minutes. Label small-sample
results as directional.

### Promotion and rollback rule

Promote a higher effort or model only when it improves the predeclared primary
metric, clears every safety gate, exceeds normal run variation, stays inside
cost and latency ceilings, and repeats on a held-out task or later batch.
Rollback when two consecutive validation batches miss the gate, the harness or
model version changes, or a plan or price change breaks the operating envelope.

## Auto-Fail Conditions

- The run used a different model, fallback, effort, surface, or harness than
  recorded.
- A mandatory validator was not executed or its failure was reported as a pass.
- The agent used an unapproved tool, permission, network destination, or write
  scope.
- A citation, score, model ID, price, or architecture fact was invented or
  could not be traced to the evidence packet.
- An orchestration comparison omitted worker tokens, tool costs, merge time, or
  human reconciliation.
- A media run was judged from a compressed preview when original inspection was
  required.
- A live or robotics test bypassed consent, safety, or human-control gates.

## Failure Protocol

1. Save the prompt hash, run identity, trace, outputs, and validator result.
2. Classify the failure as prompt, context, tool, permission, model, effort,
   service, or unsupported-capability failure.
3. Repair the prompt once for an omitted constraint or output contract. Repeat
   once more only when the first repair yields new evidence.
4. Do not raise effort for missing inputs, denied permissions, or an unavailable
   feature.
5. When reasoning depth is the plausible cause, escalate one band and rerun the
   same task cell.
6. If the harness changed, start a new experiment rather than merging results.
7. Record the decision: retain, promote, route by task class, or reject.
