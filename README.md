# AI Prompting, Agent Skills, and Image Generation Playbook

A practical guide to advanced prompting for language models, coding agents, Claude Code skills, Codex operating instructions, tool-using agents, and modern image generation systems. The focus is simple: turn vague intent into reliable outputs that can be checked, repeated, refined, and safely reused.

This guide combines durable ideas from major public prompt-engineering projects, official agent documentation, prompt evaluation tools, and modern image-generation research. It does not copy prompt dumps. It extracts reusable structures, patterns, checklists, and failure modes.

## Core Principle

A prompt is not a magic phrase. It is an operating specification.

A strong prompt tells the model:

| Component | Purpose |
| --- | --- |
| Task | What must be produced or changed. |
| Context | What background information matters. |
| Constraints | What must be avoided. |
| Method | How the work should be approached. |
| Output format | How the answer should be structured. |
| Verification | How success should be checked. |
| Failure behavior | What to do when information is missing or uncertain. |

Weak prompts ask the model to guess. Strong prompts reduce guessing.

## Prompt Anatomy

Use this structure for most serious prompts:

```text
Role:
You are acting as [specialist role].

Goal:
Produce [specific output] for [specific audience/use case].

Context:
Here is the relevant background, files, examples, constraints, and definitions.

Scope:
Include [allowed areas]. Exclude [forbidden areas].

Method:
First inspect the provided context, then plan, then produce the answer, then verify it.

Output format:
Use [Markdown/table/JSON/checklist/code block/etc.].

Quality bar:
The answer must be accurate, complete, concise where possible, and honest about uncertainty.

Verification:
Check for [facts, tests, formatting, safety, edge cases, source alignment].

Failure mode:
If information is missing, state exactly what is missing and make the safest useful assumption.
```

The structure matters more than fancy wording. Models do not need theatrical language. They need constraints, context, and a clear finish line. Humanity keeps rediscovering this and naming it a productivity breakthrough.

## Prompting Techniques

| Technique | Best use | Risk |
| --- | --- | --- |
| Zero-shot prompting | Direct tasks where the model already knows the pattern. | Too little context for specialized work. |
| Few-shot prompting | Matching a style, schema, grading pattern, or transformation. | Bad examples teach bad behavior. |
| Role prompting | Framing the level of expertise and viewpoint. | Empty role labels do little without task constraints. |
| Chain-of-thought style decomposition | Breaking complex work into steps, plans, or visible summaries. | Can become verbose or overconfident. Ask for concise reasoning summaries, not hidden reasoning. |
| Self-consistency | Asking for multiple candidate answers or checks before final output. | Costs more time and tokens. |
| Prompt chaining | Splitting a large workflow into inspect, extract, plan, draft, verify. | Requires clean handoffs between steps. |
| ReAct-style prompting | Combining reasoning summaries with tool use and observations. | Tool access increases risk if permissions are broad. |
| RAG prompting | Grounding answers in retrieved documents or source snippets. | Retrieval errors become answer errors. |
| Program-aided prompting | Using code or calculations for exactness. | Bad code gives precise nonsense. |
| Tree or graph exploration | Exploring multiple solution paths before selection. | Can explode in cost and complexity. |
| Prompt compression | Shortening a prompt while preserving constraints. | Important safety rules may be cut accidentally. |
| Evaluation prompting | Testing outputs against rubrics or fixtures. | A weak evaluator can approve weak work. |

## The Work-Order Pattern

For coding agents, research agents, and document agents, use a work-order prompt:

```text
Task:
[One sentence describing the final result.]

Read first:
[List the exact files, snippets, docs, or examples.]

Allowed changes:
[List what may change.]

Forbidden changes:
[List what must not change.]

Procedure:
1. Inspect the relevant material.
2. Summarize the current state.
3. Propose the smallest safe plan.
4. Apply the plan.
5. Verify the result.
6. Report changed items, checks, and risks.

Acceptance criteria:
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]

Final report:
- What changed
- Why it changed
- How it was checked
- What remains uncertain
```

This pattern prevents the classic agent disaster: “I improved everything,” which usually means “I touched eleven unrelated files and invented a test result.”

## Context Engineering

Prompting is not only the words you type. It is the management of everything the model sees.

Good context engineering answers:

- What information is required?
- What information is distracting?
- What should be loaded now?
- What should be linked or summarized instead?
- What should be turned into a durable instruction file?
- What should be checked with a tool rather than trusted from memory?

### Context Budget Rules

| Rule | Reason |
| --- | --- |
| Put stable rules in instruction files. | Repeating them wastes context and invites inconsistency. |
| Put examples near the task. | Models imitate nearby patterns strongly. |
| Remove stale conversation history. | Old instructions can conflict with the current task. |
| Prefer source snippets over source summaries when accuracy matters. | Summaries can erase important details. |
| Separate facts from instructions. | The model should know what is true and what it must do. |
| Label assumptions. | Hidden assumptions become hidden errors. |

## Prompt Libraries and Prompt Functions

Public prompt collections teach an important lesson: a prompt is often a reusable function.

A prompt function maps:

```text
input data + instructions + constraints -> expected output
```

Good reusable prompts have:

- A name.
- A purpose.
- Inputs to fill.
- A target audience.
- A schema or output format.
- Examples.
- Edge cases.
- Evaluation criteria.
- Version notes.

### Prompt Function Template

```text
Name:
[Short descriptive name]

Purpose:
[What this prompt reliably does]

Inputs:
- {input_1}: [description]
- {input_2}: [description]

Prompt:
[Reusable prompt body with placeholders]

Expected output:
[Schema or format]

Good examples:
[Examples that should pass]

Bad examples:
[Examples that should fail]

Evaluation:
[How to judge the output]
```

## Prompt Evaluation

A prompt is not good because it sounds clever. It is good when it performs reliably.

Evaluate prompts with:

| Evaluation type | What to check |
| --- | --- |
| Golden examples | Does the prompt pass known cases? |
| Edge cases | Does it handle weird but valid inputs? |
| Refusal cases | Does it avoid unsafe or out-of-scope tasks? |
| Format checks | Does the output follow the required schema? |
| Factual checks | Are claims grounded in sources? |
| Regression checks | Did a prompt update break previous behavior? |
| Human review | Is the output actually useful, not just valid-looking? |

### Prompt Test Case

```text
Test name:
[Case name]

Input:
[What the model receives]

Expected behavior:
[What a good answer must do]

Forbidden behavior:
[What would make the answer fail]

Scoring:
- 0 = fails core task
- 1 = partially correct
- 2 = correct but weak
- 3 = correct, robust, and well formatted
```

## Claude Code Skills

Claude Code skills are reusable procedures that Claude can load when relevant or when invoked directly. A skill should be narrow, operational, and testable.

A good Claude Code skill has:

- A clear `description` that says when to use it.
- A focused `SKILL.md` body.
- Optional supporting files for templates, examples, scripts, or reference material.
- Tool permissions that are no broader than necessary.
- A final report format.
- Verification steps.
- Failure behavior.

### Claude Code Skill Skeleton

```markdown
---
description: Use this skill when [specific trigger or task].
allowed-tools: Read Grep
disable-model-invocation: false
---

# Skill: [Name]

## Purpose
Perform [specific recurring task].

## Inputs
- [Input 1]
- [Input 2]

## Procedure
1. Inspect the relevant context.
2. Identify the smallest safe action.
3. Apply the action only if it is within scope.
4. Verify the result.
5. Report the outcome.

## Verification
- [Check 1]
- [Check 2]

## Failure behavior
If required context is missing, stop and report what is missing.
If a check fails, report the failure and do not claim success.

## Final report
- Action taken
- Evidence
- Remaining risks
```

### Claude Code Skill Design Rules

| Rule | Why it matters |
| --- | --- |
| One skill, one job. | Broad skills trigger unpredictably. |
| Put the trigger in the description. | Claude uses the description to decide when to load the skill. |
| Keep the body concise. | Loaded skill text stays in context. |
| Use supporting files for long references. | Keeps the main procedure readable. |
| Prefer read-only tools first. | Tool access is where mistakes become real edits. |
| Use subagents for isolated work. | Keeps context cleaner and reduces cross-task contamination. |
| Test skills on small cases. | A reusable bad instruction is just a mistake factory. |

## Codex Skills and AGENTS.md Patterns

Codex-style prompting works best when standing instructions are separated from task prompts.

Use durable instruction files for:

- Persistent conventions.
- Coding style.
- Test commands.
- Safety boundaries.
- Review expectations.
- Change discipline.
- What not to touch.

Use the immediate prompt for:

- The current task.
- Current files or snippets.
- Acceptance criteria.
- Verification commands.
- Final reporting requirements.

### Codex Operating Instruction Skeleton

````markdown
# Agent Instructions

## Purpose
This workspace is for [purpose].

## Rules
1. Inspect before editing.
2. Keep changes focused.
3. Do not touch secrets or private files.
4. Do not add dependencies unless requested.
5. Do not claim tests passed unless they were run.

## Style
- [Formatting rule]
- [Naming rule]
- [Documentation rule]

## Checks
Run:

```text
[check command 1]
[check command 2]
```

## Final Response
Report:
- Changed files
- Commands run
- Check results
- Risks or limitations
````

### Codex Task Prompt Skeleton

```text
Goal:
[Specific outcome]

Read first:
[Files, snippets, or docs]

Allowed scope:
[What may change]

Excluded scope:
[What must not change]

Implementation rules:
- Make the smallest useful change.
- Preserve existing style.
- Add or update checks only when relevant.
- Do not invent external facts.

Verification:
Run [commands] or explain why they cannot be run.

Final report:
Changed files, checks, risks, and remaining work.
```

## Agentic Coding Prompts

Agentic coding is not autocomplete. It is delegated work with review gates.

Use this sequence:

1. **Inspect.** Ask the agent to read relevant files first.
2. **Plan.** Ask for a small plan before edits.
3. **Edit.** Allow only scoped changes.
4. **Verify.** Run tests, linters, type checks, or focused commands.
5. **Review.** Inspect the diff yourself or ask a separate reviewer agent.
6. **Report.** Require exact changed files and check output.

### Coding Agent Anti-Patterns

| Anti-pattern | Better version |
| --- | --- |
| “Fix everything.” | “Fix the failing config parser test only.” |
| “Improve the code.” | “Refactor this function without changing behavior, then run the existing tests.” |
| “Make it professional.” | “Rewrite the introduction for beginners, keep links unchanged, and preserve headings.” |
| “Run whatever you need.” | “Run only these commands unless you ask first.” |
| “Use the best approach.” | “Prefer the smallest change that satisfies these acceptance criteria.” |

## Tool-Using Agents and MCP

Tool access changes the risk profile. A model that can call tools can affect files, accounts, services, and data.

Safe tool-use prompting includes:

- Start read-only.
- Name allowed tools.
- Name forbidden tools.
- Require confirmation before writes.
- Keep private data out of prompts unless required and allowed.
- Log what was read, changed, or skipped.
- Require the agent to stop on unexpected access or missing permission.

### Tool-Use Prompt Pattern

```text
You may use only these tools:
- [tool 1]
- [tool 2]

You must not use:
- [forbidden tool/action]

Before any write action:
1. Explain what will change.
2. Explain why it is necessary.
3. Wait for approval unless approval is already explicitly granted.

After tool use:
Report every tool call category, what it affected, and what remains unverified.
```

## General Image Prompting

Image prompts work best when they describe visual evidence, not abstract wishes.

A strong image prompt specifies:

| Element | Example of what to define |
| --- | --- |
| Subject | Main person, object, creature, scene, or symbol. |
| Composition | Framing, perspective, foreground, middle ground, background. |
| Spatial relations | What is left, right, above, behind, near, far, centered, overlapping, separated. |
| Medium | Photograph, oil painting, 3D render, ink drawing, cinematic still. |
| Lighting | Soft dawn, hard noon sun, rim light, volumetric fog, studio softbox. |
| Material and texture | Stone, brushed metal, wet asphalt, fabric weave, old paper. |
| Color palette | Muted earth tones, monochrome, high contrast, warm gold and deep blue. |
| Detail priority | What must be sharp, what can be atmospheric. |
| Negative constraints | What must not appear. |
| Output use | Poster, concept art, product shot, UI asset, 3D reference, storyboard frame. |

### Image Prompt Skeleton

```text
Create [image type] of [main subject].

Composition:
[Camera angle, framing, spatial layout, foreground/background.]

Visual details:
[Materials, textures, colors, lighting, atmosphere.]

Style:
[Medium, genre, rendering style, realism level.]

Constraints:
[Object count, anatomy, text rules, forbidden elements, safety limits.]

Use case:
[Poster, reference image, product mockup, game asset, storyboard, etc.]
```

## Diffusion Model Prompting

Diffusion systems usually generate by iteratively denoising from noise toward an image conditioned on text, images, masks, or other controls. Prompting therefore often benefits from clear visual descriptors, style anchors, negative constraints, and model-specific parameters.

### Diffusion Prompt Structure

```text
Subject:
[Main visual content]

Scene:
[Environment and composition]

Style:
[Medium, genre, rendering quality]

Lighting:
[Light source, intensity, mood]

Camera:
[Lens, distance, perspective, depth of field]

Details:
[Materials, textures, fine features]

Negative prompt:
[Artifacts, wrong anatomy, unwanted objects, text, watermark, distortion]

Controls:
[Aspect ratio, seed, steps, guidance, reference image, mask, ControlNet/IP-adapter/etc. when supported]
```

### Diffusion Prompting Rules

| Rule | Why it works |
| --- | --- |
| Put the main subject early. | Early tokens often steer composition strongly. |
| Describe visible traits. | Models respond better to concrete visual evidence than abstract intentions. |
| Use negative prompts carefully. | Overloaded negatives can suppress useful detail. |
| Separate content from style. | Mixing them causes muddier outputs. |
| Use references or control signals for strict layout. | Text alone is weak for exact geometry. |
| Iterate one variable at a time. | Otherwise you cannot tell what improved the result. |
| Save seeds and settings. | Reproducibility matters when refining. |

### Diffusion Failure Modes

- Extra limbs or distorted anatomy.
- Incorrect text rendering.
- Unwanted logos or watermarks.
- Style overwhelming subject accuracy.
- Negation failure, such as asking for “no X” and still getting X.
- Weak spatial reasoning when many objects interact.
- Over-sharpened or plastic textures from excessive quality tags.

## Autoregressive Image Model Prompting

Autoregressive image systems generate visual tokens or elements sequentially. Some newer systems combine language-style reasoning with image generation. Prompting these models should emphasize ordered structure, explicit spatial constraints, and concise visual planning.

### Autoregressive Prompt Structure

```text
Goal:
Generate [image type] with [main subject and purpose].

Global layout:
[Overall composition before details.]

Spatial constraints:
[Exact relationships between objects.]

Entity list:
- Object 1: [appearance, position, role]
- Object 2: [appearance, position, role]

Rendering priorities:
[What must be coherent first: anatomy, object count, perspective, typography, material, lighting.]

Style and finish:
[Medium, color, detail level, lighting.]

Do not include:
[Forbidden elements or common artifacts.]
```

### Autoregressive Prompting Rules

| Rule | Why it matters |
| --- | --- |
| State the global layout before details. | Sequential generation benefits from a stable plan. |
| Use object inventories. | Helps preserve counts and identities. |
| Specify spatial relations explicitly. | Reduces overlap and placement ambiguity. |
| Keep reasoning concise. | Overlong visual reasoning can add contradictions. |
| Prioritize constraints. | The model should know which details are non-negotiable. |
| Avoid decorative overload. | Too many adjectives compete with structure. |

### Autoregressive vs Diffusion Prompting

| Need | Diffusion emphasis | Autoregressive emphasis |
| --- | --- | --- |
| Mood and texture | Strong style, lighting, medium, negative prompt. | Style after layout and entity constraints. |
| Exact composition | Use control images, masks, or layout tools when available. | Write explicit global layout and spatial rules. |
| Object count | Keep prompt simple, use negatives sparingly. | Use an entity list and count constraints. |
| Iteration | Adjust seed, guidance, negatives, reference strength. | Adjust planning, ordering, and constraint wording. |
| Detail control | Layer descriptive tokens and references. | Prioritize detail after structure. |

## Reasoning-Integrated Image Prompting

For models that reason before or during image generation, ask for **visual planning**, not endless internal explanation.

Good instruction:

```text
Before generating, internally plan the composition, spatial relationships, lighting, materials, and negative constraints. Do not show the reasoning. Render only the final image.
```

Better when the model accepts visible planning:

```text
Use a concise visual plan with these fields only:
1. Subject
2. Layout
3. Lighting
4. Materials
5. Constraints
Then generate the image from that plan.
```

Avoid:

```text
Think forever about the metaphysics of the chair, then create a realistic chair.
```

The chair does not need a tragic backstory unless the image actually requires it.

## Prompt Compression

Prompt compression means preserving the task while removing waste.

Keep:

- Goal.
- Non-negotiable constraints.
- Required context.
- Output format.
- Verification.
- Safety boundaries.

Cut:

- Repeated adjectives.
- Motivational filler.
- Contradictory style labels.
- Vague intensifiers like “best,” “amazing,” or “professional” without criteria.
- Long explanations of why the task matters unless they affect the output.

### Compression Example

Weak:

```text
Please make a really amazing and super detailed image that looks extremely professional and beautiful and cinematic and very high quality with perfect lighting.
```

Stronger:

```text
Create a cinematic 35mm-style portrait with soft rim lighting, shallow depth of field, realistic skin texture, muted warm colors, and no visible text or watermark.
```

## Prompt Audit Checklist

Before using a serious prompt, check:

- Does it state the exact output?
- Does it name the audience or use case?
- Does it include the necessary context?
- Does it exclude unsafe or irrelevant actions?
- Does it define success?
- Does it define failure behavior?
- Does it specify format?
- Does it avoid copied proprietary prompt text?
- Does it avoid private data?
- Does it avoid unverifiable claims?
- Does it tell the model how to verify the result?

## Advanced Prompt Patterns

### Critic-Builder Loop

```text
First, critique the draft against the rubric.
Second, identify the top three defects.
Third, revise only those defects.
Fourth, provide the final answer without repeating the full critique.
```

### Multi-Pass Extraction

```text
Pass 1: Extract facts only.
Pass 2: Group facts by theme.
Pass 3: Identify contradictions or missing data.
Pass 4: Produce the final structured summary.
```

### Specification-First Coding

```text
Write a short specification first.
Then identify edge cases.
Then implement the smallest change.
Then run or describe verification.
```

### Rubric-Guided Generation

```text
Use this rubric:
- Accuracy: [criteria]
- Completeness: [criteria]
- Clarity: [criteria]
- Safety: [criteria]
- Format: [criteria]
Generate the answer, then check it against the rubric before finalizing.
```

### Source-Grounded Answering

```text
Use only the provided sources.
For each factual claim, connect it to a source.
If the sources do not answer a question, say so.
Do not fill gaps from memory.
```

## Common Failure Modes

| Failure | Cause | Fix |
| --- | --- | --- |
| Hallucinated facts | Prompt allows unsupported claims. | Require source-grounding and uncertainty labels. |
| Format drift | Output schema is vague. | Provide exact schema and examples. |
| Scope creep | Task is too broad. | Name allowed and forbidden work. |
| Overlong answers | No length or priority constraints. | Specify audience, depth, and section limits. |
| Weak code changes | Agent edits before inspecting. | Require read-plan-edit-verify sequence. |
| Bad image composition | Prompt lists aesthetics but not layout. | Add spatial constraints and object inventory. |
| Prompt brittleness | No test cases. | Add representative examples and edge cases. |
| Unsafe tool use | Permissions are too broad. | Use read-only tools first and require approval for writes. |

## Prompt Improvement Formula

For any weak prompt, improve it by adding:

```text
1. Specific goal
2. Relevant context
3. Explicit constraints
4. Output format
5. Verification method
6. Failure behavior
```

Example:

Weak:

```text
Explain AI agents.
```

Strong:

```text
Explain AI agents to a beginner who knows basic programming. Cover what agents are, how they use tools, how they differ from chatbots, common safety risks, and one simple example. Use headings, a comparison table, and a short checklist. Avoid hype and unverifiable product claims.
```

## Master Template

```text
You are [role].

Goal:
[Specific deliverable]

Audience:
[Who will use the output]

Context:
[Relevant facts, examples, source snippets, files, or assumptions]

Scope:
Include:
- [Allowed item]
- [Allowed item]

Exclude:
- [Forbidden item]
- [Forbidden item]

Method:
1. Analyze the provided context.
2. Identify missing or uncertain information.
3. Produce the answer using the required structure.
4. Verify the output against the quality bar.

Output format:
[Exact format]

Quality bar:
- Accurate
- Specific
- Complete enough for the use case
- No unsupported claims
- No private data
- No copied proprietary prompt text

Final check:
Before finalizing, confirm that the output satisfies the goal, scope, format, and constraints.
```

## Minimal Template

```text
Task: [What to do]
Context: [What matters]
Constraints: [What not to do]
Format: [How to answer]
Check: [How to verify]
```

Use the minimal template for simple work. Use the master template for serious work. Use skill files for recurring work. Use evaluation cases when quality matters. Use caution when tools can write, delete, publish, spend money, or expose private data.

That is the whole boring miracle: clear instructions, bounded context, controlled tools, and verification. Apparently civilization needed neural networks to rediscover checklists.
