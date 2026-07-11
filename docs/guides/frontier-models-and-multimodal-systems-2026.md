# Frontier Models and Multimodal Systems in 2026

Checked: 2026-07-11

This guide explains the GPT-5.6 family, Claude Fable 5 and Opus 4.8, Grok
4.5, Muse Spark 1.1, Gemini 3.5 Flash, current live-audio systems, and current
image and video model families. It is a dated research snapshot, not a promise
that every model picker will look the same on every account.

Facts are labeled by evidence type:

- **Official** means a vendor launch post, help article, API page, or live
  product catalog.
- **Independent** means a benchmark maintainer tested the model and published
  the method or configuration.
- **Local evidence** means a deterministic query of the Codex catalog installed
  in this checkout on the checked date.
- **Unconfirmed** means the checked public sources did not establish the claim.

Two additional labels matter throughout this guide. **Vendor claim** identifies
a result or qualitative statement published by the model maker but not
independently reproduced here. **Interpretation** identifies a recommendation
derived from the cited facts rather than a property guaranteed by a vendor.
Third-party videos are workflow evidence only. They do not establish prices,
plan eligibility, model IDs, architecture, or benchmark scores. The
[video research pack](../research/video-research-pack-2026-07-11.md) records
verified videos and discovery searches separately.

## The Short Answer

GPT-5.6 is not one model with cosmetic speed buttons. Sol, Terra, and Luna are
three capability and price tiers, while effort controls how much work a tier
does before answering. Product surfaces then add another layer. Standard
ChatGPT exposes Sol reasoning choices. Work and Codex expose the family more
broadly. The API exposes model IDs and single-model reasoning levels. `ultra`
is different again because it coordinates agents rather than merely increasing
one model's reasoning setting.

Claude Fable 5 sits near Sol Max on broad independent intelligence testing and
below Sol Max in the current coding-agent composite, but its product safeguards
can route some requests to Opus 4.8. Grok 4.5 is a strong lower-cost coding
option in Grok Build. Gemini 3.5 Flash combines high throughput with agentic
performance. Muse Spark 1.1 is a fast, lower-cost Meta reasoning model. None of
those summaries means one model wins every math, engineering, coding, visual,
audio, or safety task.

![GPT-5.6 effort controls by product surface](../assets/model-guides/gpt-5-6-effort-surfaces.svg)

## GPT-5.6 Is a Family, Not a Ladder of Nicknames

OpenAI defines three durable tiers:

| Tier | Official role | Base API price per 1M input/output tokens | Practical starting point |
| --- | --- | ---: | --- |
| GPT-5.6 Sol | Flagship for the hardest professional work | $5 / $30 | Complex coding, research, science, design, and high-stakes synthesis |
| GPT-5.6 Terra | Balanced intelligence and cost | $2.50 / $15 | Daily repository work, documents, analysis, and tool-heavy tasks |
| GPT-5.6 Luna | Fastest and least expensive tier | $1 / $6 | High-volume extraction, bounded edits, classification, and subagents |

The tier and the effort answer different questions. The tier determines the
model family and its price-performance envelope. Effort tells that model how
aggressively to reason and use tools. A well-specified Luna task can beat a
poorly specified Sol task, but raising Luna's effort does not turn it into Sol.

### Standard ChatGPT Chat

OpenAI's current Help Center table says:

| Plan | GPT-5.6 Sol choices in ordinary Chat | What the plan label changes |
| --- | --- | --- |
| Plus | Medium and High | Included access and Plus usage allowance |
| Pro $100, often called Pro 5x | Medium, High, Extra High, and Sol Pro | Same model capabilities as Pro 20x, lower usage allowance |
| Pro $200, often called Pro 20x | Medium, High, Extra High, and Sol Pro | Same model capabilities as Pro 5x, higher usage allowance |
| Business and Enterprise | Medium, High, Extra High, and Sol Pro | Admin controls and workspace limits can apply |
| Free and Go | No GPT-5.6 Sol in ordinary Chat | GPT-5.5 Instant remains the ordinary fast path |

Medium, High, and Extra High use GPT-5.6 Sol. Pro uses GPT-5.6 Sol Pro, which
OpenAI presents as a separate highest-quality option for difficult, longer
workflows. Terra and Luna are not selectable in ordinary Chat. “Pro 5x” and
“Pro 20x” describe usage allowances, not different Sol effort menus.

### Work and Codex

The official launch post confirms Sol, Terra, and Luna for Plus, Pro, Business,
and Enterprise in Work and Codex. Free and Go receive Terra in Codex. It also
confirms per-model effort, `max` for users with GPT-5.6 access, Work `ultra`
for Pro and Enterprise, and Codex `ultra` for Plus and higher.

The exact lower menu labels are less cleanly documented. OpenAI's public Help
Center does not enumerate every Work menu on every client. The installed Codex
0.144.0 catalog does provide direct local evidence. The desktop interface uses
display labels while internal configuration can use lowercase values:

| Codex model | Visible local menu | Default in local catalog |
| --- | --- | --- |
| GPT-5.6 Sol | Low, Medium, High, Extra High, Max, Ultra | `low` |
| GPT-5.6 Terra | Low, Medium, High, Extra High, Max, Ultra | `medium` |
| GPT-5.6 Luna | Low, Medium, High, Extra High, Max | `medium` |

The current product label is **Low**, not "Light." User interfaces can display
**Extra High** while configuration files and model catalogs use `xhigh`.

The surfaces have related model controls but different jobs:

| Surface | Primary operating context | Access and artifact boundary |
| --- | --- | --- |
| Desktop Codex | Repository operation, shell commands, tests, patches, and Git | Works against an approved local workspace and produces repository changes |
| Desktop Work | Document and artifact production across approved local files and apps | Desktop integration can use local sources that the user exposes |
| Web Work | Cloud-hosted project work and artifacts | Does not directly open arbitrary local files; uploads and connected sources define scope |
| Standard Chat | Conversational answers and attached-file analysis | No repository or desktop control unless a separate product feature supplies it |

OpenAI documents the GPT-5.6 family and effort structure for Work and Codex,
but account pickers can still depend on plan, client version, workspace policy,
region, and staged rollout. On the checked web Work account, Sol, Terra, and
Luna each showed Low, Medium, High, Extra High, and Max. That exact menu is a
dated interface observation, not a universal Help Center guarantee. Desktop
Work follows the documented family and per-model effort structure, but this
guide does not infer an exact picker where official documentation and local
evidence do not enumerate it. OpenAI also says web Work and desktop Work
threads are separate at launch.

### API

The API model IDs are `gpt-5.6-sol`, `gpt-5.6-terra`, and `gpt-5.6-luna`.
Their published reasoning values are `none`, `low`, `medium`, `high`, `xhigh`,
and `max`. The API does not list `ultra` as a reasoning value. Multi-agent beta
in the Responses API is a separate orchestration capability. Model tier,
reasoning effort, and orchestration must therefore be configured and measured
as three different variables.

| API control | What it changes | What it does not imply |
| --- | --- | --- |
| Model ID | Sol, Terra, or Luna capability and token price | A particular reasoning effort |
| Reasoning value | Single-model time and compute allocation | Ultra or automatic parallel agents |
| Multi-agent beta | Concurrent subagents plus synthesis in one response | A new model tier |
| Programmatic Tool Calling | In-memory programs that coordinate tools and filter intermediate data | Unlimited tool permissions |
| Prompt caching | Reuse economics for stable prompt prefixes and explicit breakpoints | A larger context window |
| Context and output limits | 1.05M input context and 128K maximum output | Guaranteed useful recall across every token |

That distinction prevents a common benchmark error. Artificial Analysis tested
GPT-5.6 Sol Max in Codex. It did not test “Sol Ultra” as if Ultra were a larger
single-model effort. An Ultra run may do better or worse on a real project, but
the Max score cannot be relabeled.

## What Each GPT-5.6 Effort Is For

Effort should be chosen against a measurable outcome, not task anxiety.

| Effort | Best fit | Prompt shape | Main failure risk |
| --- | --- | --- | --- |
| `low` | Small edits, lookups, formatting, focused extraction | Exact input, one output, one check | Missing hidden dependencies |
| `medium` | Normal coding, research, and document tasks | Goal, files, constraints, acceptance tests | Under-scoping a genuinely hard task |
| `high` | Multi-file work, difficult debugging, source synthesis | Add failure cases, stronger checks, and decision criteria | More latency and tool use |
| `xhigh` | Hard architecture, long investigations, uncertain root causes | Give checkpoints, stop conditions, and evidence rules | Over-analysis on routine work |
| `max` | Frontier single-agent reasoning where errors are expensive | State the decision, alternatives, test matrix, and review gate | Large token and time cost |
| `ultra` | Parallelizable projects with separable workstreams | Define subtask boundaries and synthesis criteria | Coordination overhead and duplicated work |

### Sol at Low, Medium, High, Extra High, Max, and Ultra

Sol Low is useful when the task is easy to verify but still benefits from the
flagship model's judgment. Good examples are a narrow code review, a one-file
repair, or a sourced answer with a fixed schema. Give it a short scope and a
deterministic check.

Sol Medium is the default practical choice for ordinary professional work. It
has enough room for tool calls and correction without turning every task into
a long investigation. In standard Chat this is also the first GPT-5.6 Sol
reasoning level available to eligible users.

Sol High fits multi-step reasoning, difficult implementation, and work where
the first plausible answer needs testing. Ask it to inspect before editing,
name the acceptance tests, and require evidence for completion.

Sol Extra High or `xhigh` fits problems with real uncertainty: a cross-service
failure, an unfamiliar repository, a hard proof, or research where sources
conflict. Give it a decision log and explicit boundaries so the extra effort is
spent resolving uncertainty rather than expanding scope.

Sol Max is the deepest documented single-model effort. Use it for a final
architecture decision, difficult math or science work, a high-risk migration,
or a review where a missed defect is expensive. The prompt should state what
would falsify the answer and what evidence the reviewer must inspect.

Sol Ultra is an orchestration mode. OpenAI says the documented product mode
coordinates four agents in parallel by default, then has a primary agent
synthesize the work. Use it when the problem divides cleanly into independent
workstreams such as implementation, tests, documentation, source verification,
and adversarial review. It can reduce elapsed time when those streams can run
at once, but total token use can rise. Weak task boundaries can also create
duplicated investigation, conflicting edits, and expensive reconciliation. A
single tiny bug, a tightly sequential migration, or a task with one shared
mutable file is usually better at High or Max. OpenAI's API lets developers
build ultra-like workflows with multi-agent beta, but `ultra` itself is not an
API reasoning value.

### Terra at Low, Medium, High, Extra High, Max, and Ultra

Terra Low is a cost-aware executor for scoped tasks with clear inputs. It is a
good fit for deterministic repository edits, structured data cleanup, and
drafting from a supplied outline.

Terra Medium is the strongest default for routine work when cost matters. Use
it for daily coding, test updates, document synthesis, and tool use where the
acceptance criteria are already clear.

Terra High gives more room for debugging and multi-file reasoning. It is often
the right escalation when a Medium attempt found the relevant area but did not
close the issue.

Terra Extra High or `xhigh` suits broad but bounded engineering tasks. It can
inspect more callers, test more hypotheses, and verify more surfaces. Require
progress checkpoints so it does not drift into unrelated cleanup.

Terra Max is useful when Sol's price is hard to justify but the task still
needs the deepest Terra attempt. Artificial Analysis measured Terra Max at 55
on the Intelligence Index and 77 in the Codex coding-agent harness.

Terra Ultra is available in the local Codex catalog and should be treated as
parallel orchestration, not “Terra beyond Max.” It is attractive for bounded
multi-area work where several Terra agents can operate against stable
contracts and a final reviewer can reconcile their outputs. Terra's lower
token price can make this pattern practical, but parallel duplication can erase
the saving. High or Max is normally better when every step depends on the
previous one.

### Luna at Low, Medium, High, Extra High, and Max

Luna Low is for speed-sensitive, high-volume work with a simple correctness
test. Classification, metadata extraction, repeated small transformations, and
bounded subagent tasks are good examples.

Luna Medium is a fast daily driver for clear work orders. It can implement a
small feature, summarize a source packet, or update tests when the repository
pattern is already known.

Luna High is useful when speed still matters but the task has several steps or
requires tool use. Keep the output contract tight and give it examples of edge
cases.

Luna Extra High or `xhigh` is the deepest exploratory tier before Max. It makes
sense when a lower-cost model needs more search or verification but the task
does not justify Sol.

Luna Max is Luna's highest local Codex effort. Artificial Analysis measured it
at 51 on the Intelligence Index and 75 in the Codex coding-agent harness. The
local catalog does not expose Luna Ultra.

Across the family, a higher tier usually buys stronger judgment and coding
reliability, while a higher effort gives the selected tier more opportunity to
inspect context, call tools, test hypotheses, and revise. Neither guarantees a
better result. Long-context work can fail through poor retrieval or weak task
decomposition even inside a 1.05M-token window. Parallel delegation works best
when subtasks have independent inputs, explicit ownership, and a deterministic
synthesis gate. For bounded transformations, Luna or Terra with a clear test
often beats an expensive open-ended Sol run on cost and latency. For ambiguous
architecture, mathematics, engineering analysis, or high-risk synthesis, Sol
High through Max offers more useful headroom.

### Prompt Patterns by Interface

In Chat, ask for the reasoning product you want: a decision, proof, draft,
analysis, or critique. The model does not have a repository unless you supply
files or use a compatible product feature.

In Work, describe the finished artifact, its audience, its source files, and
the review gate. For example: “Produce a two-page decision memo from these
three documents. Keep every numeric claim traceable. Flag conflicts and end
with a recommendation.”

In Codex, describe observable repository state: exact scope, files that must
remain untouched, commands to run, and what a passing diff looks like. For
Ultra, add subtask boundaries and a synthesis rule.

In the API, select effort through configuration and measure it. Compare task
success, latency, output tokens, tool calls, and human correction time on your
own evaluation set. Do not assume a higher effort always improves a structured
or latency-sensitive task.

### Price, Context, and Caching

All three GPT-5.6 API tiers publish a 1.05M-token context window and 128K maximum
output. Requests above 272K input tokens are billed at 2x input and 1.5x output
for the full request. Cache writes cost 1.25x uncached input. Cache reads retain
the 90% cached-input discount. OpenAI also documents explicit cache breakpoints
and a minimum 30-minute cache life for GPT-5.6 and later.

Those headline rates do not predict project cost by themselves. Higher effort
can generate more reasoning tokens, more tool calls, and longer agent traces.
The right comparison is cost per successful task, including retries and human
correction.

### Safeguards and Reliability

OpenAI describes GPT-5.6 as combining model protections with real-time checks,
monitoring, and access controls. Higher capability does not remove refusals or
temporary restrictions. Biology, cyber, and other high-risk work can receive
additional checks. A reliable workflow should log what model ran, what effort
was selected, what tools were allowed, and whether a fallback occurred.

### Watch: GPT-5.6 Family Testing

[![Watch a hands-on test of GPT-5.6 Sol, Terra, and Luna](https://i.ytimg.com/vi/xDXX2M5DrO0/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#gpt-5-6-family-test)

*Third-party test by AICodeKing. Use it for workflow context, not as the source
for access, pricing, or benchmark claims.*

## Claude Fable 5 and Claude Opus 4.8

Anthropic describes Fable 5 as a Mythos-class model made available with an
additional safeguard layer. Its API effort values are `low`, `medium`, `high`,
`xhigh`, and `max`; `high` is the default. Claude Code's Ultracode is not a
sixth API effort. Anthropic documents it as `xhigh` plus standing permission
for multi-agent workflows.

### The July 12 Subscription Cutoff

The official promotion ends July 12, 2026 at 11:59:59 PM Pacific Time. During
the promotion, eligible Pro, Max, Team, and premium Enterprise seats can use up
to 50% of weekly subscription limits on Fable 5. After the cutoff, Fable 5 is
no longer included in weekly subscription limits and remains usable through
separately billed usage credits. API usage is never part of that promotion.

The promotion covers Claude web, mobile, Desktop, Cowork, Claude Code, Design,
Microsoft 365, Teams, and Tag where the account and organization are eligible.
Claude Code requires version 2.1.170 or later, and Cowork requires the latest
Claude Desktop version. Cowork on the web or desktop still requires the
eligible account and product access documented by Anthropic; the promotional
allowance does not convert API use into subscription use.

The cutoff removes Fable from ordinary included weekly subscription usage. It
does not remove the model from every Anthropic surface. After July 12, users
who meet the terms can continue through separately billed usage credits, and
developers can continue through the API at API rates. This distinction matters
for both availability writing and cost comparisons.

### Price, Context, and Fallback

Fable 5 costs $10 per million input tokens and $50 per million output tokens.
Opus 4.8 costs $5/$25. Anthropic currently keeps standard pricing across the
full 1M context window for both. Prompt-cache writes and data-residency choices
can add their own multipliers.

Fable's production safeguards matter to evaluation. Anthropic says flagged
cyber, biology, chemistry, or distillation requests can be handled by Opus 4.8
instead, with the user informed. Artificial Analysis therefore labels its
Fable configuration “with fallback.” That is a product result, not a pure
underlying-model score.

Fable's `low`, `medium`, `high`, `xhigh`, and `max` controls are single-model
effort values. Claude Code's Ultracode combines `xhigh` with standing permission
to use multi-agent workflows; it is not a sixth API effort. Low and Medium fit
bounded edits and inexpensive drafting. High is Anthropic's default. Extra
High fits harder coding and agentic work. Max is the expensive final attempt
when an evaluation shows that more computation improves the result. Because
fallback can change which model actually handles a sensitive prompt, serious
tests should record the visible fallback notice and avoid claiming a pure
Fable result when routing occurred.

### Claude Opus 4.8 as Model and Claude Code Configuration

Opus 4.8 remains a strong model in its own right and the documented fallback
for specified Fable safeguards. Anthropic recommends `xhigh` as the coding and
agentic starting point, `high` for most other demanding work, and `max` only
when evaluation shows useful headroom. For document analysis, long financial
work, and finished professional artifacts, model choice should be judged on
citation accuracy, spreadsheet or document operations, analytical quality,
and correction cost rather than prose fluency alone.

The official API price is $5 per million input tokens and $25 per million
output tokens, with the same published 1M context pricing rule cited above.
Fable costs twice as much per input token and twice as much per output token,
but pricing alone does not decide task cost because effort, retries, tool calls,
and fallback can dominate.

Artificial Analysis reports Opus 4.8 Max at 55.7 on Intelligence Index v4.1
and 73 in the Coding Agent Index **in Claude Code**. That coding number includes
Claude Code's system prompt, tools, permission model, terminal loop, and file
editing behavior. It is not a bare API-model score. Fable Max with fallback
scores higher in the dated intelligence and coding snapshots, while Opus offers
a cleaner comparison when the evaluator needs to avoid Fable's model-routing
layer.

## Grok 4.5 in Grok Build

Grok 4.5 is the default Grok Build model. SpaceXAI documents low, medium, and
high reasoning, with high as the default. Base API pricing is $2 per million
input tokens and $6 per million output tokens. Artificial Analysis reports
that long inputs above 200K double those costs. That threshold is independent
benchmark reporting rather than a value reproduced in this guide from the
current xAI price table, so production users should check the live xAI pricing
page before deployment.

Grok Build is the agent harness around the model. Its documented workflow can
search a repository, edit multiple files, run terminal commands and tests,
inspect Git state, recover after a failed command, and delegate work to
subagents. xAI also documents live web and X-search tools. Those capabilities
change the product result: a capable model can still fail if the harness loses
command output, applies an unsafe patch, or never runs the right test. A good
Grok Build prompt therefore names the repository root, files in scope, commands
to run, failure-recovery rule, and final evidence required.

In Artificial Analysis, Grok 4.5 High scores 54 on Intelligence Index v4.1 and
76 in the Grok Build coding-agent harness. Its coding result trails Sol Max by
four points, Terra Max and Fable Max with fallback by one, leads Luna Max by
one, and leads Opus 4.8 Max in Claude Code by three in this dated composite.
Its published task cost is much lower than Sol, Fable, or Opus. Those gaps do
not make Grok universally better or worse: repository languages, terminal
recovery, live-search needs, safety policy, latency, and harness behavior can
reverse the practical ranking. The xAI launch post also publishes strong coding
results, but those charts remain vendor evidence rather than independent
confirmation.

[![Watch a 27-minute Grok 4.5 coding test](https://i.ytimg.com/vi/5J6HCDEkg64/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#grok-4-5-test)

*Third-party test by ForrestKnight. The cited xAI and Artificial Analysis
pages remain the authority for availability and measured scores.*

## Artificial Analysis: What the Scores Do and Do Not Mean

![Artificial Analysis Intelligence and Coding Agent Index snapshot](../assets/model-guides/aa-frontier-benchmark-2026-07-11.svg)

### Intelligence Index v4.1

The current composite covers GDPval-AA v2, tau3-Banking, Terminal-Bench v2.1,
SciCode, Humanity's Last Exam, GPQA Diamond, CritPt, AA-Omniscience, and
AA-LCR. It blends professional work, tool use, coding, science, knowledge,
physics, hallucination resistance, and long-context reasoning.

The components answer different questions. GDPval-AA tests valuable
professional work. GPQA Diamond, CritPt, and SciCode emphasize graduate-level
science, physics, and scientific coding. Humanity's Last Exam targets difficult
broad knowledge and reasoning. AA-Omniscience measures both correct answers and
appropriate uncertainty rather than rewarding confident guessing. AA-LCR probes
long-context retrieval and reasoning. A composite can rise because of strength
in one cluster while hiding weakness in another, so the subtests should be
matched to the intended workload.

The July launch snapshot puts Fable 5 Max with fallback at 59.9, Sol Max at
58.9, Opus 4.8 Max at 55.7, Terra Max at 55, Grok 4.5 High at 54, Luna Max at
51.2, Muse Spark 1.1 xhigh at 51, and Gemini 3.5 Flash High at 50.2. A one-point
gap in a composite should not be treated as a universal practical difference.

### Coding Agent Index

The coding composite pairs models with an agent harness and averages DeepSWE,
Terminal-Bench v2, and SWE-Atlas-QnA. The current comparison shows:

| Model and harness | Index | Cost/task | Time/task | Important qualifier |
| --- | ---: | ---: | ---: | --- |
| GPT-5.6 Sol Max in Codex | 80 | $7.08 | 10.2 min | Max, not Ultra |
| GPT-5.6 Terra Max in Codex | 77 | $2.76 | 8.4 min | Same composite, cheaper tier |
| Fable 5 Max in Claude Code | 77 | $11.75 | 23.5 min | Includes production fallback |
| Grok 4.5 High in Grok Build | 76 | about $2.49 | See live comparison | Different harness |
| GPT-5.6 Luna Max in Codex | 75 | $1.57 | 8.0 min | Lowest-cost GPT-5.6 result shown |
| Opus 4.8 Max in Claude Code | 73 | $7.70 | 23.1 min | No Fable fallback layer |

Harness choice affects tools, permissions, caching, prompt scaffolding, turns,
and orchestration. The Coding Agent Index is closer to a product workflow test
than a bare model exam. The repository keeps the harness name beside every
score for that reason.

The three coding components also reward different behavior. DeepSWE measures
software-engineering issue resolution, Terminal-Bench v2 exercises interactive
terminal operation, and SWE-Atlas-QnA tests repository understanding through
questions and answers. Artificial Analysis reports Sol at 69, 88, and 84 on
those three components; Terra at 67, 84, and 81; and Luna at 63, 80, and 81 in
the cited GPT-5.6 article. Those figures belong to the tested Codex
configurations. They should not be copied onto API calls or other agent
harnesses.

Cost per task, tokens used, and time per task are part of the engineering
decision. A higher index with twice the cost may still be right for a rare
high-stakes repair, while a slightly lower model can be better for thousands of
bounded tasks. Time is also harness-sensitive: parallel tool calls, command
latency, caching, retry policy, and fallback can all move it. No independent
Sol Ultra Coding Agent Index result is cited here, so the Sol Max result must
not be presented as an Ultra score.

### AA-Briefcase and Other Useful Views

AA-Briefcase tests long-horizon knowledge work and finished artifacts. Fable 5
Max leads the cited comparison with a 56% rubric score and 1764 Analytical
Quality Elo. Sol Max records a 42% rubric score and 1592 Analytical Quality Elo,
but leads Presentation Elo. That split is useful: factual and analytical task
completion is not the same measure as visual polish.

Artificial Analysis also publishes GDPval-AA v2, AA-Omniscience, AA-LCR,
agentic, legal, finance, automation, enterprise-operations, image, video, and
speech evaluations. Choose the view that matches the work. A coding index is a
poor way to select a translation model, and an image preference Elo is a poor
way to choose a repository agent.

AA-Briefcase separates rubric completion from Analytical Quality Elo and
Presentation Elo. The first asks whether required work was done, the second
compares reasoning and analysis, and the third compares the finished artifact's
presentation. That separation explains how one model can lead analytical work
while another produces a more polished-looking deliverable. None of those
measures alone captures reliability, safeguards, or user happiness. Those need
repeated task success, correction burden, refusal quality, and user studies.

## Meta Muse Spark 1.1

Meta describes Muse Spark 1.1 as a multimodal reasoning model for agentic work,
computer use, coding, and multimodal understanding. It is available in
Thinking mode in Meta AI and through the Meta Model API public preview. The
official product claim covers multimodal reasoning and action-oriented work;
it does not mean that every API client supplies a repository editor, browser,
or computer-control harness automatically.

Artificial Analysis reports Muse Spark 1.1 xhigh at 51 on Intelligence Index
v4.1, 116.3 output tokens per second, a 1M context window, and Meta API pricing
of $1.25/$4.25 per million input/output tokens. Its 51-point composite matches
the rounded Luna Max score but does not establish equal behavior in Codex,
computer use, or any specific repository task.

At those reported rates and throughput, Muse is positioned as a lower-cost,
fast reasoning option. Luna has a nearby rounded Intelligence score and a
measured Codex coding-agent result, Terra scores higher in both the dated
Intelligence and Codex snapshots, Grok adds a different live-search and CLI
harness, and Gemini 3.5 Flash exposes a broader documented developer-tool set.
Those comparisons are directional only. Equal rounded Intelligence values do
not establish equal coding reliability, GUI control, safety behavior, latency,
or repository completion.

[![Watch a 33-minute Muse Spark 1.1 test](https://i.ytimg.com/vi/XCYYDhG9zKw/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#muse-spark-test)

*Third-party test by Bijan Bowen. Meta and Artificial Analysis provide the
factual product and benchmark record.*

## Gemini 3.5 Flash

Gemini 3.5 Flash is Google's stable Flash model for agentic and coding work at
scale. The API uses `minimal`, `low`, `medium`, and `high`, with `medium` as the
default. Google recommends low for lower-latency work, medium for most complex
code and agents, and high for hard reasoning, math, and difficult coding.

Google's developer documentation lists Google Search, Maps, File Search, code
execution, URL Context, function calling, and computer use among the supported
tool paths. Tool availability still depends on the API and client being used;
the model name alone does not grant a browser or computer. The published model
surface supports long context, while useful long-context performance still
depends on retrieval, prompt structure, and tool results. Google described the
release as roughly four times faster than its preceding comparable path at
I/O 2026. That throughput statement is a vendor claim until reproduced under a
matching workload and service tier.

Gemini Apps uses a simpler consumer vocabulary where available:

| Gemini Apps label | Meaning |
| --- | --- |
| Standard thinking | Faster default for most questions |
| Extended thinking | More reasoning for complex problem solving |
| Deep Think | Separate Pro-model parallel reasoning for eligible AI Ultra use, not a Flash effort label |

Google's API and consumer labels should not be mixed. Standard and Extended
are interface choices. Minimal through High are developer controls. Deep Think
is not “Gemini 3.5 Flash Max.”

Artificial Analysis scores Gemini 3.5 Flash High at 50.2 on Intelligence Index
v4.1. Google's launch material reports 76.2% on Terminal-Bench 2.1, 1656 Elo on
GDPval-AA, and 83.6% on MCP Atlas, but those launch figures remain vendor
evidence unless independently reproduced under the same conditions.

Against GPT-5.6 Luna and Terra, Flash is not simply a midpoint on one ladder.
Luna and Terra have lower-level integration in Codex and measured Coding Agent
Index configurations; Gemini has its own API tools, consumer labels, pricing,
throughput, and Google product integrations. Choose by running the same coding
or agent task with equivalent tools, prompts, time limits, and correction
rules. Do not compare Google's vendor Terminal-Bench number directly with an
Artificial Analysis harness score as if the procedures were identical.

[![Watch a long Gemini 3.5 Flash coding test](https://i.ytimg.com/vi/TdN-YdFLWvY/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#gemini-3-5-flash-test)

*Third-party test by Bijan Bowen. The official Google developer pages define
the model controls and supported tools.*

## GPT-Live-1 and Gemini 3.5 Live Translate

These systems both process streaming audio, but they solve different jobs.

### GPT-Live-1 and GPT-Live-1 Mini

GPT-Live is a conversational architecture. OpenAI says it continuously
processes input while generating output, can listen and speak at the same
time, and makes interaction decisions many times per second about speaking,
listening, pausing, interrupting, and using tools. That full-duplex loop is
designed to reduce the rigid turn-taking of older voice pipelines. Deeper
search or reasoning can be delegated to a stronger text model while the live
model maintains the conversation. These are official architectural
descriptions, not an independent reverse-engineering result, and a user-
interface animation does not disclose internal implementation.

OpenAI positions GPT-Live-1 for paid Go, Plus, and Pro users and GPT-Live-1
Mini for the free path. At launch, GPT-Live-1 Instant and Mini can use a fast
background model, while Medium and High route deeper work through the current
thinking model described by OpenAI. That delegation is distinct from the live
speech loop itself. The launch does not establish one fixed end-to-end latency:
network quality, speech length, tool calls, background reasoning, and
interruptions all affect response time.

Full duplex creates new failure modes. The system must distinguish a real
interruption from a cough or background speaker, respect a request to wait,
avoid answering during a thoughtful pause, and recover when two people speak
at once. OpenAI notes that transcripts may not be verbatim and that overlap,
background noise, and fast conversation can reduce stability. Independent
tests should therefore measure recognition accuracy, interruption success,
false starts, pause handling, translation continuity, tool-delegation latency,
and whether the spoken answer matches the visible transcript.

Safety and privacy are part of the product, not afterthoughts. OpenAI describes
voice-native safety training, real-time steering, predefined voices, and limits
on impersonation. Users should also account for microphone capture, transcript
and memory settings, web search, connected tools, regional policy, and the fact
that playing remote media or using live services sends data to the provider.

### Gemini 3.5 Flash Live Translate

Gemini 3.5 Flash Live Translate is a translation-specialized interpreter path.
The public-preview model ID is `gemini-3.5-live-translate-preview`. It accepts
audio input, emits translated audio plus optional transcripts, supports more
than 70 languages, and does not support tool calling, search grounding,
function calling, system instructions, or reasoning/thinking controls. Google
recommends 16 kHz mono PCM input, 24 kHz PCM output, and approximately 100 ms
input chunks.

For a consumer trial, Google says to open the Google Translate app on Android
or iOS, connect headphones, and choose Live translate. For a developer trial,
use the Google AI Studio Live Translate demo or connect through the Gemini Live
API with a target BCP-47 language code. The preview label matters: supported
behavior, quotas, and quality can change before a stable release.

An Arabic-English evaluation should test both directions with names, numbers,
technical vocabulary, dialect changes, emotional tone, interruptions, long
pauses, and overlapping speakers. It should record whether the system performs
continuous simultaneous translation or waits for turn boundaries, and whether
meaning, tone, and proper nouns survive. This is a recommended test protocol,
not a claim that the checked guide independently ran those trials.

GPT-Live-1 and Live Translate should not be ranked as identical products.
GPT-Live is a general conversational system with tools and delegated reasoning;
Live Translate is a narrower audio-to-audio translation model with predictable
language routing and no tool or thinking controls. The right comparison is
task-specific latency, speech accuracy, interruption behavior, tone retention,
privacy, and stability under the same audio conditions.

[![Watch OpenAI's GPT-Live demonstration](https://i.ytimg.com/vi/EAN5Cj347PY/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#gpt-live-official)

*Official OpenAI demonstration. The Google Live Translate guide links its own
AI Studio demo and product videos in the sources below.*

## Image and Video Models

![Current live-audio, image, and video model map](../assets/model-guides/multimodal-model-map-2026.svg)

### GPT Image 2

OpenAI documents GPT Image 2 as its state-of-the-art image generation and
editing model with text and image input, image output, flexible sizes, and
high-fidelity image inputs. It is available through the Images API and image
generation tool paths. The product documentation emphasizes typography,
prompt adherence, precise editing, and reference consistency, but those are
capabilities to evaluate with full-resolution outputs rather than guarantees
for every prompt.

The claim that GPT Image 2 is a “reasoning-integrated fully autoregressive
image model that reasons like a Transformer” is **unconfirmed**. The checked
OpenAI model and image guides do not publish that internal architecture. An
autoregressive image-token model would predict image tokens sequentially;
diffusion and latent diffusion iteratively denoise pixels or latent features.
A separate planning stage could reason before generation, while hidden prompt
rewriting could improve prompts without changing the generator architecture.
An interface “thinking” indicator could represent any of those product steps.
Observed behavior cannot identify which mechanism is used. Until OpenAI
publishes a technical source, the guide records the disclosed inputs, outputs,
controls, and quality goals, and marks architecture as undisclosed.

### Nano Banana 2, Nano Banana Pro, and Nano Banana 2 Lite

The official mapping is:

| Product name | Model ID | Role |
| --- | --- | --- |
| Nano Banana 2 Lite | `gemini-3.1-flash-lite-image` | Fastest and cheapest, high-volume generation |
| Nano Banana 2 | `gemini-3.1-flash-image` | General-purpose balance of quality, speed, 4K, and editing |
| Nano Banana Pro | `gemini-3-pro-image` | Highest control, world knowledge, localization, and professional use |
| Original Nano Banana | `gemini-2.5-flash-image` | Legacy model Google recommends replacing |

Nano Banana 2 is not Gemini 3 Pro Image. Nano Banana Pro is Gemini 3 Pro Image.

#### Nano Banana 2

Nano Banana 2, officially Gemini 3.1 Flash Image, is the general-purpose path.
Google documents fast generation, search-grounded current knowledge, text
rendering, subject consistency, image editing, reference-image input, and
resolutions up to 4K. Thinking controls are available where the model and API
surface document them. Search and thinking should still be recorded in any
test because enabling them can change latency, cost, and output.

#### Nano Banana Pro

Nano Banana Pro, officially Gemini 3 Pro Image, targets higher-control
professional work. Google emphasizes world knowledge, localization,
typography, complex layouts, and production control. It should be compared
with Nano Banana 2 on the same brief and editable output requirements rather
than treated as a renamed version of the Flash model.

#### Nano Banana 2 Lite

Nano Banana 2 Lite, officially Gemini 3.1 Flash Lite Image, trades capability
for lower latency and price. Google positions it for iteration, brainstorming,
and high-volume use, with an approximately four-second generation target in
the official launch material. The same source warns that it is not optimized
for many reference images or long sequential editing. Those constraints make
it a draft engine, not an automatic replacement for Pro on complex layouts.

### Seedream 5.0 Pro

ByteDance's Dreamina surface presents Seedream 5.0 Pro as a professional image
generation and editing model. Public English technical documentation is less
detailed than the Google and OpenAI API pages, so claims about internal
reasoning, layer architecture, or web search should be attributed to the
product page and treated as vendor claims until a technical report is public.

This model is suitable for side-by-side evaluation on typography, layout,
reference consistency, targeted editing, and production control. The test set
should use the same prompts, aspect ratios, reference images, and human scoring
rubric across providers. Dreamina advertises text-to-image, image editing,
reference control, typography, production layouts, and prompt adherence. Those
claims should be checked on original full-resolution outputs. Compressed X or
YouTube frames can hide small text errors, edge artifacts, and reference drift.
The limited English first-party technical disclosure does not establish a
particular diffusion, autoregressive, or reasoning architecture.

### Image-model videos

[![Watch a GPT Image 2, Nano Banana 2, and Seedream comparison](https://i.ytimg.com/vi/FDhx79PU5KQ/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#image-model-comparison)

*Third-party comparison by Code And Create. Use identical prompts and inspect
the original outputs before accepting any winner claim. This video is an image-
model comparison only; it is not a Gemini Omni Flash demonstration.*

[![Watch OpenAI's 21-minute ChatGPT Images 2.0 introduction](https://i.ytimg.com/vi/sWkGomJ3TLI/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#gpt-image-2-official)

*Official OpenAI product demonstration.*

### Gemini Omni Flash

Gemini Omni Flash is a multimodal generative-video system, not an image-model
comparison. Google's preview API model ID is `gemini-omni-flash-preview`. It
can combine text, images, existing video, and prompt-described audio to produce
video with generated audio. Google documents conversational editing through
the Interactions API, including iterative changes intended to preserve
unmentioned parts of a clip. The product material also emphasizes character
and voice consistency, but those remain quality claims to test across multiple
edits and scenes.

Distribution spans the Gemini app, Flow, YouTube creation surfaces, and a paid
Gemini API preview. Google says image and text outputs are planned later; this
guide does not treat those planned outputs as current API capability. The
model page lists 3-to-10-second output at 720p and 24 frames per second, a
1,048,576-token context window, and video input up to 10 seconds for editing.
The detailed API guide also lists current limits: uploaded audio references
are unsupported, multi-video reasoning is unsupported, video extension and
interpolation are unsupported, and voice editing is unsupported. The schema
accepts video references up to three seconds but Google warns that the current model does not
process them correctly. Those are preview limitations, not an invitation to
infer undocumented workarounds.

The video research pack uses precise discovery searches for Gemini Omni Flash
official demos, full tests, Omni-versus-Veo comparisons, and Google I/O 2026.
No unrelated YouTube ID is relabeled as an Omni demonstration.

## How to Choose Without Chasing a Single Winner

The following is an **interpretation** of the cited product controls and dated
evaluations, not a universal ranking:

| Decision area | Evidence to inspect | Practical reading of the current snapshot |
| --- | --- | --- |
| Mathematics and science | GPQA Diamond, CritPt, SciCode, full solution checks | Sol and Fable are strong broad candidates, but subtest and proof verification matter more than the one-point composite gap |
| Engineering and repositories | Coding Agent Index, terminal recovery, tests, diff quality | Sol Max in Codex leads the cited composite; Terra, Grok, Luna, Fable, and Opus trade score, cost, time, and harness behavior differently |
| Open-ended problem solving | Intelligence components, AA-Briefcase, correction burden | Fable leads the cited broad and analytical artifact views; Sol leads the coding composite and Presentation Elo cited here |
| Reliability | Repeated task success, retries, hallucination measures, regression tests | No single published number proves reliability for a private workload |
| Safeguards | Vendor system cards, refusal quality, fallback notices, audit logs | Fable's documented Opus fallback changes model identity; OpenAI and other vendors apply their own controls |
| User happiness | Preference studies, latency, edit burden, trust, predictable access | The checked sources do not provide a universal satisfaction ranking; local user studies are required |

Strengths and weaknesses are therefore conditional. Sol offers the strongest
cited coding-agent result and a broad product surface, but higher efforts and
Ultra can cost more and add coordination. Terra and Luna lower cost and latency
but have less headroom on the cited composites. Fable leads the dated broad
index and analytical artifact view, but is expensive and its fallback weakens
pure model comparisons. Opus is a more stable Claude baseline but trails Fable
and the GPT-5.6 coding configurations in the cited composite. Grok is
cost-efficient and search-aware in Grok Build, while its harness and safety
behavior must be tested for the intended repository. Muse and Gemini offer
different multimodal, throughput, and tool integrations that the coding table
does not capture.

For repository completion, start with the coding-agent index and then run your
own representative tasks. Sol Max currently has the strongest cited composite.
Terra and Luna offer lower task cost. Fable remains strong on long-horizon work
and AA-Briefcase but is more expensive and includes a fallback path. Grok 4.5
offers a strong cost-performance point in Grok Build. Opus 4.8 remains a useful
Claude baseline without the Fable safeguard layer.

For math and science, inspect GPQA, CritPt, SciCode, and task-specific error
analysis. A composite can hide a model that is excellent at one scientific
domain and weaker at another.

For professional documents, inspect AA-Briefcase rubric score, Analytical
Quality Elo, Presentation Elo, citation accuracy, and editability. A polished
slide deck can still contain a weak conclusion.

For live voice, choose a conversational full-duplex model when interaction and
tool delegation matter. Choose a translation model when the job is continuous
speech translation with predictable language routing.

For images, compare prompt adherence, typography, reference consistency,
editing precision, latency, price, resolution, safety policy, provenance
marking, and commercial terms. A blind preference leaderboard alone does not
measure whether a diagram is factually correct.

## Uncertainties and Known Limits

- Work and Codex UI menus can differ by plan, workspace policy, app version,
  region, and staged rollout. The local Codex catalog is evidence for this
  machine on the checked date, not every account.
- OpenAI's public pages confirm Work models and Max/Ultra eligibility but do
  not enumerate every lower Work label on every surface.
- Artificial Analysis pages are live and can update. The local charts preserve
  the checked date, benchmark version, model effort, harness, and fallback.
- Fable scores include the production Opus 4.8 fallback where Artificial
  Analysis labels it that way.
- No independent source cited here tests Sol Ultra against Fable Max. Ultra is
  orchestration, while the benchmark uses Sol Max.
- GPT Image 2's claimed fully autoregressive architecture is not established in
  the checked OpenAI documentation.
- Seedream 5.0 Pro has limited English first-party technical disclosure.
- Third-party videos are qualitative context. They are not the factual source
  for pricing, access, architecture, or benchmark scores.

## Sources

Primary sources, accessed 2026-07-11:

- [OpenAI: GPT-5.6 launch](https://openai.com/index/gpt-5-6/), published 2026-07-09.
- [OpenAI Help: GPT-5.6 in ChatGPT](https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt).
- [OpenAI Help: ChatGPT Work and Codex](https://help.openai.com/en/articles/20001275/).
- [OpenAI Help: ChatGPT Pro tiers](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers).
- [OpenAI API model catalog](https://developers.openai.com/api/docs/models).
- [OpenAI API: GPT-5.6 Terra](https://developers.openai.com/api/docs/models/gpt-5.6-terra).
- [OpenAI: Introducing GPT-Live](https://openai.com/index/introducing-gpt-live/), published 2026-07-08.
- [OpenAI Help: GPT-Live in ChatGPT](https://help.openai.com/en/articles/20001274/).
- [OpenAI: GPT-Live system card](https://deploymentsafety.openai.com/gpt-live).
- [OpenAI API: GPT Image 2](https://developers.openai.com/api/docs/models/gpt-image-2).
- [Anthropic: Claude Fable 5 and Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5).
- [Anthropic Help: Fable 5 promotional access](https://support.claude.com/en/articles/15424964-claude-fable-5-promotional-access).
- [Anthropic API: effort controls](https://platform.claude.com/docs/en/build-with-claude/effort).
- [Anthropic API: pricing](https://platform.claude.com/docs/en/about-claude/pricing).
- [SpaceXAI: Introducing Grok 4.5](https://x.ai/news/grok-4-5).
- [SpaceXAI Docs: Grok 4.5](https://docs.x.ai/developers/grok-4-5).
- [SpaceXAI: Grok Build CLI](https://x.ai/cli).
- [SpaceXAI: Grok Build changelog](https://x.ai/build/changelog).
- [Meta: Introducing Muse Spark 1.1](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/).
- [Google: Gemini 3.5 Flash changes](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5).
- [Google Gemini Apps Help: thinking levels](https://support.google.com/gemini/answer/16275805?hl=en).
- [Google: Live translation with Gemini Live API](https://ai.google.dev/gemini-api/docs/live-api/live-translate).
- [Google: Gemini 3.5 Live Translate](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/).
- [Google: Nano Banana image generation](https://ai.google.dev/gemini-api/docs/image-generation).
- [Google: Nano Banana 2](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-nano-banana-2/).
- [Google: Nano Banana 2 Lite and Gemini Omni Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/).
- [Google: Nano Banana Pro](https://blog.google/innovation-and-ai/products/nano-banana-pro/).
- [Google: Gemini Omni Flash API guide](https://ai.google.dev/gemini-api/docs/omni).
- [Google: Gemini Omni Flash model page](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash).
- [Google: Gemini Omni Flash and Flow](https://blog.google/innovation-and-ai/models-and-research/google-labs/flow-updates/).
- [ByteDance Dreamina: Seedream 5.0 Pro](https://dreamina.capcut.com/seedream/seedream-5-0-pro).

Independent sources, accessed 2026-07-11:

- [Artificial Analysis: GPT-5.6 benchmarks](https://artificialanalysis.ai/articles/gpt-5-6-has-landed).
- [Artificial Analysis: Claude Code versus Codex](https://artificialanalysis.ai/agents/coding-agents/comparisons/claude-code-vs-codex).
- [Artificial Analysis: Grok 4.5](https://artificialanalysis.ai/articles/grok-4-5-brings-spacexai-to-the-the-intelligence-frontier).
- [Artificial Analysis: Muse Spark 1.1](https://artificialanalysis.ai/models/muse-spark-1-1).
- [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index).
- [Artificial Analysis coding-agent comparisons](https://artificialanalysis.ai/agents/coding-agents/comparisons).
- [Artificial Analysis: AA-Briefcase](https://artificialanalysis.ai/evaluations/aa-briefcase).

## Method

Official sources establish names, product controls, rollout, pricing, and
vendor-described architecture. Artificial Analysis supplies independent model
and harness results. The local Codex catalog was queried through `codex debug
models` and filtered to the three GPT-5.6 model IDs. Videos were checked with
`yt-dlp`; every embedded selection was public and reported
`playable_in_embed=True` on the checked date. Original SVGs reproduce values
and relationships, not third-party chart artwork.

The [video research pack](../research/video-research-pack-2026-07-11.md)
records verified titles, channels, upload dates, roles, and limitations. It
also keeps discovery searches separate so an unverified result cannot silently
become evidence.
