# Source-Inspired Prompting Curriculum

This curriculum turns the strongest patterns from public prompting guides and local archived GitHub downloads into a practical learning path for this repository. It is source-inspired, not copied: use the listed projects to understand structure, then write original public-safe guidance, templates, tests, and release notes.

## Source families used for synthesis

| Source family | What to learn from it | How this repo should use it |
| --- | --- | --- |
| DAIR.AI Prompt Engineering Guide | Broad technique taxonomy, model-agnostic prompting concepts, RAG, agents, and coding examples. | Keep a clear learning path from basics to advanced techniques; link to source for depth. |
| OpenAI Cookbook | Practical recipes, runnable examples, structured outputs, tool use, and evaluation mindset. | Prefer executable examples, validation commands, and evidence-based claims. |
| Microsoft Generative AI for Beginners and cloud sample repos | Lesson sequencing, beginner checkpoints, and workshop-style progression. | Organize docs into lessons, checkpoints, and next steps rather than giant undifferentiated pages. |
| Google Cloud generative AI samples | Product-adjacent examples, notebooks, multimodal patterns, and cloud workflow caveats. | Treat cloud examples as optional advanced paths and mark product behavior for official-doc verification. |
| Prompt Master / prompt-template libraries | Load-bearing prompts, task-specific templates, inputs, failure modes, and tool-specific adaptation. | Keep every reusable prompt operational: inputs, included scope, excluded scope, safety, verification, and report shape. |
| Awesome Prompt Engineering indexes | Source maps across papers, tools, benchmarks, courses, and communities. | Maintain curated references and avoid pretending one repo can replace official docs. |
| Structured prompt collections | Role/task/schema patterns and reusable agent shapes. | Extract structure only; do not mirror prompt dumps or leak-derived content. |
| Stop Slop / anti-slop guides | Removing filler, unsupported confidence, generic praise, and vague claims. | Add anti-slop review gates to README, release notes, and prompt-template final reports. |
| Vision-language and multimodal prompting surveys | Differences between text, image, video, audio, and multimodal prompting. | Keep image-generation and multimodal guidance distinct from text-only prompting. |
| MCP and agent bridge projects | Tool permissions, browser/file actions, bridge diagnostics, and trust boundaries. | Keep automation preview-first and permission-aware; never frame tool access as safe to run blindly. |

## Source-to-repository application map

Use this map when deciding whether the repository is genuinely useful or just
large. Each external pattern should become a local reader action, check, or
template.

| Reader need | Source pattern | Local artifact | Usefulness test |
| --- | --- | --- | --- |
| Learn the field without drowning in links. | DAIR.AI and Learn Prompting style technique maps. | [Comprehensive prompt engineering guide](comprehensive-prompt-engineering-guide.md) and [Prompting OS kernel](../prompting-os/01-kernel.md). | A beginner can name the prompt's goal, context, constraints, format, and verification step. |
| Turn prompting into repeatable work. | OpenAI Cookbook style recipes and runnable examples. | [Codex goal prompts](../../prompts/codex/docs-update.goal.md) and [Prompting OS template](../prompting-os/templates/master-prompt-template.md). | The prompt has inputs to fill, success criteria, failure behavior, and checks. |
| Practice in lessons, not a wall of prose. | Anthropic tutorial and Microsoft beginner lesson sequencing. | README reading order, [Guides README](README.md), and the curriculum layers below. | A reader knows what to read first, what to try next, and when to stop. |
| Build a prompt library safely. | Awesome ChatGPT Prompts and Awesome Copilot collection organization. | `prompts/`, [skills docs](../skills/README.md), and [coding agent power tips](coding-agent-power-tips.md). | Each prompt or instruction asset has a target tool, boundaries, and review path. |
| Avoid unsafe or misleading prompt reuse. | Brex production safety notes and leak-aware source policies. | [Public repo safety](../workflows/public-repo-safety.md), [source policy](../research/source-policy.md), and this guide's anti-slop pass. | The repo does not mirror prompt dumps, leaked prompts, private paths, or unsupported claims. |
| Prove a prompt got better. | promptfoo and evaluation-focused repos. | [Prompt quality rubric](../prompting-os/evals/prompt-quality-rubric.md), [prompt audit checklist](prompt-audit-checklist.md), and local Python checks. | Changes can be judged by test cases, rubrics, and command output, not by model confidence. |

## Curriculum layers

### 1. Kernel: universal prompt contract

Every serious prompt in this repository should state:

1. Objective.
2. Trusted context.
3. Inputs to fill.
4. Included scope.
5. Excluded scope.
6. Tool and data permissions.
7. Output format.
8. Verification steps.
9. Failure behavior.
10. Final report format.

This layer is implemented in:

- [Prompt engineering playbook](prompt-engineering-playbook.md)
- [Prompt audit checklist](prompt-audit-checklist.md)
- [Prompting OS kernel](../prompting-os/01-kernel.md)
- [Codex prompt templates](../../prompts/codex/docs-update.goal.md)

### 2. Technique map: choose the right prompting pattern

Use a small set of durable technique families instead of a giant list of magic prompts:

| Technique family | Use for | Review question |
| --- | --- | --- |
| Direct instruction | Clear one-shot tasks. | Is the output format explicit? |
| Few-shot examples | Style, schema, and pattern matching. | Are examples representative and public-safe? |
| Decomposition | Multi-step docs, code, or research tasks. | Are stop conditions and verification steps clear? |
| Retrieval/context grounding | Source-backed answers. | Are sources trusted and cited? |
| Tool-use / ReAct-style loops | Agents that inspect, edit, run commands, or browse. | Are permissions and destructive actions constrained? |
| Structured outputs | JSON, tables, manifests, issue templates, and checklists. | Is there validation or a schema-like expectation? |
| Evaluation prompts | Prompt regression, review, and anti-slop checks. | Are pass/fail criteria concrete? |
| Multimodal descriptors | Image, video, audio, and reference-image tasks. | Are modality-specific constraints separated from prose? |

### 3. Tool drivers: adapt the same task to the tool

A good prompt is not universal text pasted everywhere. It is adapted to the tool:

- Codex and coding agents need file scope, git safety, tests, and final diffs.
- Claude Code skills need a trigger, concise procedure, allowed tools, verification, and failure behavior.
- Chat models need context blocks, output shape, and uncertainty rules.
- RAG workflows need source ledgers, quote discipline, and stale-source handling.
- Image systems need subject, style, composition, lighting, constraints, reference handling, and revision criteria.
- MCP/tool bridges need permission boundaries and clear read/write separation.

Repository docs should link these drivers instead of duplicating them in every page:

- [Coding agent power tips](coding-agent-power-tips.md)
- [Skills and prompt guides](skills-and-prompt-guides.md)
- [Image generation README](../image-generation/README.md)
- [MCP tool guide](../tools/mcp.md)

### 4. Anti-slop pass

Before publishing a guide, prompt template, release note, or automation page, remove:

- Vague praise such as “powerful,” “seamless,” or “best-in-class” without evidence.
- Exact product claims not checked against official docs.
- Made-up benchmarks, model availability, plan access, or pricing.
- Unbounded verbs such as “automatically fixes everything.”
- Generic filler paragraphs that do not change reader behavior.
- Prompt-dump language copied from external sources.
- Private paths, account details, screenshots, logs, or credentials.

Replace them with:

- A specific workflow.
- A concrete checklist.
- A verification command.
- A failure mode.
- A claim marked for manual official-doc verification.

### 5. Evaluation and regression loop

Reusable prompts should be treated like small programs. Keep a regression loop:

1. Define the prompt purpose.
2. Add 2-3 representative inputs.
3. Add at least one edge case.
4. Define pass/fail behavior.
5. Run the prompt or review it manually.
6. Record changes in the changelog if public-facing behavior changes.
7. Re-run repository checks before release.

Useful evaluation artifacts:

- [Prompting OS prompt-quality rubric](../prompting-os/evals/prompt-quality-rubric.md)
- [Prompt audit checklist](prompt-audit-checklist.md)
- `python scripts/repo_health_check.py`
- `python scripts/safe_autofix.py --check`
- `python -m unittest discover -s tests`

## Repository shaping loop

Use this loop when turning archived prompting sources into repository improvements:

```text
source inventory -> pattern extraction -> public-safe synthesis -> local docs edit -> anti-slop review -> validation checks -> diff review -> changelog -> release notes
```

Rules:

- Inventory sources by name and category; do not bulk import their text.
- Extract patterns, not passages.
- Prefer official docs for tool-specific behavior.
- Keep community and awesome-list content as pointers, not authorities.
- Write new examples from scratch.
- Keep local archive paths out of public docs.
- Mark fast-changing claims for manual verification.

## Release and automation implications

Releases should include source-inspired materials only after a human review confirms:

- The content is original synthesis.
- The source map is clear.
- No leaked prompts or copied prompt dumps are mirrored.
- The README links to the right start-here path.
- Static site links are relative and offline-safe.
- Automation remains metadata/prep only unless a human runs the local agent loop.
- Prompt templates include verification and failure cases.

Automation should support the loop by preparing candidate sources, curator prompts, and checks. It should not publish finished AI-written guidance or call paid LLMs from GitHub Actions.

## Suggested reader path

1. Start with [README.md](../../README.md) for the repository map.
2. Read [Prompting AI Coding Agents](prompting-ai-coding-agents.md) for work-order prompting.
3. Read [Prompting OS](../prompting-os/README.md) for the source-inspired operating model.
4. Use [Prompting References](prompting-references.md) to find external depth.
5. Pick a Codex template from [prompts/codex](../../prompts/codex/).
6. Run the validation commands and review the diff.
