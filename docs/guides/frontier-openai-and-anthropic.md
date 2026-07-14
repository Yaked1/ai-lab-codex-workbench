# OpenAI and Anthropic frontier systems

[← Frontier models index](frontier-models-and-multimodal-systems-2026.md)

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

### The July 19 Subscription Access Update

Anthropic's [Fable 5 promotional-access terms](https://support.claude.com/en/articles/15424964-claude-fable-5-promotional-access)
state that the promotion is extended through **July 19, 2026 at 11:59:59 PM
PT**. Its linked [Claude Code weekly-limits promotion](https://support.claude.com/en/articles/15910845-claude-code-may-july-2026-weekly-limits-promotion)
states that the 50% increase to Claude Code weekly usage limits runs through the
same date. The promotion is available to Pro, Max, Team, and premium seats on
seat-based Enterprise plans where the organization enables it. Recheck the live
terms before a billing or availability decision because this is a dated
promotional condition, not a permanent product entitlement.

The promotion covers included promotional access through subscription limits
rather than API usage. Do not
rewrite the extension as an API-price, regional-availability, Enterprise-policy,
or product-surface claim beyond the terms Anthropic publishes.

The promotion covers Claude web, mobile, Desktop, Cowork, Claude Code, Design,
Microsoft 365, Teams, and Tag where the account and organization are eligible.
Claude Code requires version 2.1.170 or later, and Cowork requires the latest
Claude Desktop version. Cowork on the web or desktop still requires the
eligible account and product access documented by Anthropic; the promotional
allowance does not convert API use into subscription use.

After July 19, Fable leaves ordinary included weekly subscription usage but
remains available through separately billed usage credits. API availability
and pricing are separate surfaces that require current API documentation before
either is asserted. A subscription-access update must not be rewritten as an
API-price or API-availability update without that documentation.

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

## Claude Sonnet 5

**Official, checked 2026-07-12.** Anthropic released Claude Sonnet 5 on
2026-06-30. Its launch post says it is available on every Claude plan, in Claude
Code, and through the Claude Platform as `claude-sonnet-5`. The introductory API
price is $2 input / $10 output per million tokens through 2026-08-31, changing
to $3 / $15 afterward. These are vendor-published product facts, not an
independent cost or capability comparison.

Anthropic positions Sonnet 5 as its most agentic Sonnet model. It narrows the
gap to Opus 4.8 on some agentic tasks, but that positioning does not establish
that it replaces Fable 5 or Opus 4.8. The launch post confirms browser and
terminal tool use in the product description; it does not make a browser,
terminal, or agent harness available automatically to every API caller.

| Decision | Evidence-conscious guidance |
| --- | --- |
| Normal knowledge work and cost-sensitive coding | Start with Sonnet 5 where its lower dated API price is appropriate; supply an explicit deliverable and a verification step. |
| Long-running or tool-using work | Define the tool boundary, stop conditions, and recovery behavior. Record the product surface and actual tool configuration. |
| High-effort work | The checked launch source compares effort levels but does not publish a complete cross-surface effort menu. Confirm the live API or product control before claiming a particular value. |
| Fable or Opus comparison | Treat Sonnet, Fable, and Opus as distinct released models. Select with a matched task evaluation, not a family-name assumption. |

Use the [Sonnet 5 prompting guide](model-prompting/claude-sonnet-5-prompting.md)
for source-aware work orders and unsupported-use boundaries.

<!-- frontier-migration-boundary -->
