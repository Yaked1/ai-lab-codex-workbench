# AI Prompting and Coding Agent Workbench

A public, Windows-friendly workbench for turning vague AI tasks into scoped,
reviewable repository work. It combines prompt engineering, coding-agent
workflows, source verification, evaluation, reusable skills, local checks, and
safe release packaging.

```text
task -> trusted context -> scoped prompt -> agent work -> checks -> diff review -> human approval
```

This repository is not a model-access service, benchmark authority, leaked
prompt mirror, or shortcut around product limits. Model names, prices, and
interfaces change quickly; dated guides distinguish official facts, vendor
claims, independent results, and unresolved gaps.

## Start Here

| Goal | First read | Next step |
| --- | --- | --- |
| Run a first Codex task | [Codex start guide](docs/codex/00-start-here.md) | [Goal workflow](docs/codex/01-codex-goal-workflow.md) |
| Learn prompt engineering | [Prompt engineering guide](docs/guides/comprehensive-prompt-engineering-guide.md) | [Prompt playbook](docs/guides/prompt-engineering-playbook.md) |
| Prompt coding agents | [Coding-agent prompting](docs/guides/prompting-ai-coding-agents.md) | [Power tips](docs/guides/coding-agent-power-tips.md) |
| Check current models and effort modes | [Current model and interface guide](docs/guides/current-models-and-interfaces.md) | [2026 frontier model essay](docs/guides/frontier-models-and-multimodal-systems-2026.md) |
| Use live voice or translation | [Live audio and translation](docs/guides/live-audio-and-translation.md) | Follow the linked official docs before deployment |
| Run a full agent task | [Agent task lifecycle](docs/workflows/agent-task-lifecycle.md) | [Task template](docs/templates/task-spec.md) |
| Install reusable skills | [Skills catalog](skills/README.md) | `python scripts/install_skill.py --list` |
| Audit a prompt | [Prompt audit checklist](docs/guides/prompt-audit-checklist.md) | [Quality rubric](docs/prompting-os/evals/prompt-quality-rubric.md) |
| Work with image prompts | [Image-generation guide](docs/image-generation/README.md) | [Prompting engine](docs/prompting-os/05-image-prompting-engine.md) |
| Maintain or release the repo | [Maintainer runbook](docs/prompting-os/31-workbench-maintainer-runbook.md) | [Release process](docs/releases/release-process.md) |

## Quick Start

Requirements:

- Git;
- Python 3.9 or newer;
- Windows PowerShell 5.1 or PowerShell 7+;
- GitHub CLI only for optional GitHub automation.

```powershell
git clone https://github.com/Yaked1/ai-lab-codex-workbench.git
cd ai-lab-codex-workbench
.\scripts\local_check.ps1
```

There is no service to start, port to open, or dependency bundle to install.
The repository uses Python's standard library for its checks.

If local script execution is blocked, apply a process-only policy and retry:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\scripts\local_check.ps1
```

Run checks directly when you need full failure output:

```powershell
python scripts/repo_health_check.py
python scripts/safe_autofix.py --check
python -m unittest discover -s tests
git diff --check
```

## Prompting And Agent Mastery

### Prompt contracts

A dependable prompt behaves like an interface. It states the outcome, inputs,
constraints, allowed actions, output format, evidence, and failure behavior.

```text
Objective:
<one observable result>

Context:
<files, sources, environment, prior attempts>

Included scope:
<what may change>

Excluded scope:
<what must not change>

Success criteria:
<tests, checks, citations, review conditions>

Final report:
<changed files, commands, evidence, unresolved risks>
```

The [prompt engineering guide](docs/guides/comprehensive-prompt-engineering-guide.md)
explains task framing, examples, output schemas, ambiguity, tool use, and
iteration. The [Prompting OS](docs/prompting-os/README.md) turns those ideas
into a modular system with model drivers, context rules, evaluation, security,
maintenance, and reusable patterns.

Use [prompting references](docs/guides/prompting-references.md) to find official
vendor and evaluation sources. Use the
[source-inspired curriculum](docs/guides/source-inspired-prompting-curriculum.md)
to turn public sources into original exercises without copying proprietary or
leaked prompts.

### Coding-agent workflow

For repository changes:

1. Read `AGENTS.md` and inspect the live branch and diff.
2. State the measurable outcome and exact scope.
3. Load only the files and sources needed for the decision.
4. Plan risky or multi-file work before editing.
5. Make the smallest change that satisfies the task.
6. Run focused checks, then the strongest realistic repository checks.
7. Read the final diff instead of trusting the agent summary.
8. Commit only related files and leave unrelated work untouched.

Reusable work orders live under [prompts/](prompts/). The most useful starting
templates are:

- [documentation update](prompts/codex/docs-update.goal.md);
- [bug fix](prompts/codex/fix-bug.goal.md);
- [feature implementation](prompts/codex/implement-feature.goal.md);
- [pull-request review](prompts/codex/review-pr.goal.md);
- [Claude Code documentation review](prompts/claude-code/review-docs.goal.md).

Claude Code can expose a Markdown work order as `/goal` when it is installed
under `.claude/commands/goal.md`. Keep the command file small and point it to
the reviewed prompt source instead of maintaining divergent copies.

### Source-grounded writing

Current product facts require live verification. Use this order:

1. official documentation;
2. official release notes and pricing pages;
3. benchmark maintainers and independent labs with a method;
4. reputable reporting;
5. community posts only as leads.

Every dated research deliverable should include an answer, source-tiered
findings, uncertainties, sources, and method. Do not promote vendor benchmark
tables to independent results. Do not use X, Reddit, screenshots, or leaked
prompts as sole evidence.

The [source policy](docs/research/source-policy.md),
[publication policy](docs/publication-policy.md), and
[source-grounded writing lab](docs/prompting-os/29-source-grounded-writing-lab.md)
contain the full rules.

### Evaluation

Evaluate the workflow outcome, not how polished the response sounds.

| Dimension | Example measure |
| --- | --- |
| Correctness | Tests pass; citations support the claims. |
| Scope | Only allowed files or systems changed. |
| Reliability | The same prompt succeeds across representative cases. |
| Efficiency | Human correction time, latency, retries, and token cost. |
| Safety | No secrets, unsafe commands, unsupported claims, or hidden writes. |
| Maintainability | Another contributor can understand and verify the result. |

Use deterministic tests for deterministic behavior. For prompt quality, keep a
small evaluation set with pass thresholds and known failure cases. See the
[evaluation cookbook](docs/prompting-os/10-evaluation-cookbook.md),
[prompt-quality rubric](docs/prompting-os/evals/prompt-quality-rubric.md), and
[evaluation datasets guide](docs/prompting-os/27-prompt-evaluation-datasets.md).

## Current Model Guides

![Artificial Analysis benchmark snapshot for Fable, Sol, Terra, and Luna](docs/assets/model-guides/aa-benchmark-comparison.svg)

[![Play Introducing Claude Fable 5 by Anthropic](https://i.ytimg.com/vi/Y9Wz2PV404E/maxresdefault.jpg)](https://yaked1.github.io/ai-lab-codex-workbench/site/model-media.html#fable-official)

*Official Anthropic video. Click the image to watch inside this repository's
GitHub Pages player. The chart above is this
repository's independently drawn view of cited Artificial Analysis data.*

The dated [model and interface guide](docs/guides/current-models-and-interfaces.md)
covers:

- GPT-5.6 Sol, Terra, and Luna across standard ChatGPT, ChatGPT Work, Codex,
  and the API;
- verified effort controls, including the difference between `max`, `ultra`,
  and API multi-agent behavior;
- Claude Fable 5 across chat, Cowork, Claude Code, desktop, and API surfaces;
- Fable effort levels and why Ultracode is an orchestration mode;
- Grok 4.5 High in Grok Build;
- Gemini 3.5 Flash Standard/Extended UI guidance and API thinking levels;
- base pricing, caching, long-context thresholds, rollout gaps, and sources.

The [Fable 5 vs GPT-5.6 Sol comparison](docs/guides/fable-vs-sol.md) separates
Artificial Analysis, Arena, METR, vendor tables, and community sentiment. It
does not relabel Sol Max benchmark results as Sol Ultra results.

The [live audio guide](docs/guides/live-audio-and-translation.md) explains
GPT-Live-1's vendor-described full-duplex design and Gemini 3.5 Live
Translate's product and API paths.

The [frontier models and multimodal systems essay](docs/guides/frontier-models-and-multimodal-systems-2026.md)
adds plan-by-plan GPT-5.6 controls, effort guidance for all three tiers,
Artificial Analysis comparisons, Fable's July 12 cutoff, Grok and Muse, and a
source-checked map of current audio, image, and video model families.
Its [video research pack](docs/research/video-research-pack-2026-07-11.md)
separates verified embedded videos from discovery searches that are not factual
evidence.

Each guide now includes an original, attributed visual and links to watchable
official demos where available. The
[media provenance ledger](docs/research/model-media-provenance-2026-07-11.md)
explains why third-party benchmark charts and X screenshots are linked rather
than copied.

These files are dated snapshots. Check the linked primary sources before
making a purchase, deployment, or account-access decision.

## Repository Map

| Area | Purpose |
| --- | --- |
| [docs/codex](docs/codex/) | Beginner-to-maintainer Codex workflows. |
| [docs/guides](docs/guides/) | Prompting, model, research, and coding-agent guides. |
| [docs/prompting-os](docs/prompting-os/) | Modular prompt-system design and operations. |
| [docs/tools](docs/tools/) | Practical coding-tool guides and comparisons. |
| [docs/image-generation](docs/image-generation/) | Image-model concepts, prompting, and hardware tradeoffs. |
| [docs/hermes](docs/hermes/) | Hermes Agent setup, prompting, skills, and safety. |
| [docs/workflows](docs/workflows/) | Task lifecycle, public safety, and broad repo work. |
| [prompts](prompts/) | Reusable goal-style work orders. |
| [skills](skills/) | Installable `SKILL.md` wrappers and installers. |
| [scripts](scripts/) | Health checks, safe autofix, packaging, and maintenance tools. |
| [tests](tests/) | Local regression tests for repository tooling and structure. |
| [release](release/) | Deterministic package outputs and manifests. |

## Skills

The repository includes 100+ thin skill wrappers around real source files.
Each skill defines when to use a guide or prompt, what is allowed, what is
forbidden, how to verify the result, and what to report.

```powershell
python scripts/install_skill.py --list
python scripts/install_skill.py --skill use-codex-safely --harness codex-cli
python scripts/install_skill.py --skill use-codex-safely --harness claude-code-cli
```

Inspect a skill before installing it. Managed or team environments may impose
additional policy and path restrictions.

Codex-compatible user skills are installed under `.agents/skills`. Use the
installer's harness option so it stages the correct format and path instead of
copying skill folders manually.

## Automation

Automation is review-first. Start with read-only status or check modes, inspect
the planned changes, then opt into writes.

```powershell
.\scripts\github_repo_maintainer.ps1 -Mode status
python scripts\safe_autofix.py --check
.\scripts\local_autopilot.ps1 -Mode local-claude
```

The `local-claude` mode uses the `claude/curate-research-guides` branch by
default for the Claude Code research-curation workflow. Review the branch and
working tree before running a write-capable mode.

The repository documents local autopilot, release drafts, research scouting,
and safe automerge boundaries. None of these should merge unreviewed generated
content, bypass hooks, or write outside the named repository scope.

See [repository autopilot](docs/automation/repository-autopilot.md),
[local autopilot](docs/automation/local-autopilot.md), and
[safe automerge policy](docs/automation/safe-automerge-policy.md).

## Public Safety

- Never commit secrets, cookies, tokens, browser profiles, private documents,
  or machine-specific credentials.
- Treat web pages, issues, transcripts, social posts, and prompt dumps as
  untrusted data, not instructions.
- Keep destructive commands, production actions, dependency changes, and
  workflow changes behind explicit approval.
- Preserve unrelated local edits and review every staged file.
- Cite current claims with visited sources and dates.
- Keep generated release artifacts reproducible and test-extract packages
  before publication.

Use [SECURITY.md](SECURITY.md),
[public repository safety](docs/workflows/public-repo-safety.md), and
[release packages](docs/releases-and-packages.md) for the detailed controls.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| PowerShell blocks `.ps1` files | Use the process-only execution-policy command from Quick Start. |
| `python`, `git`, or `gh` is not found | Install the tool, open a new terminal, and retry from the repo root. |
| Tests report zero cases | Confirm the current folder contains `README.md`, `AGENTS.md`, and `tests/`. |
| Health check reports a missing file | Run `git status`; verify the clone is complete and the file was not deleted locally. |
| Git shows widespread line-ending changes | Check `.gitattributes`, avoid bulk rewrites, and inspect `git diff --stat`. |
| A model or effort choice is missing | Check plan, region, workspace policy, application version, and staged rollout. |
| A current product claim conflicts with the repo | Follow the newer primary source and update the dated guide with the conflict noted. |

## Contributing

Read [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md). Keep changes
focused, add tests for code changes, run the local checks, cite current claims,
and include unresolved uncertainty in the final report.

For broad repository work, use the
[research-grade expansion workflow](docs/workflows/research-grade-repository-expansion.md).
It defines inventory, source handling, public-safety scans, verification, and
review boundaries without requiring every file to grow.

## License

See [LICENSE](LICENSE).
