# Prompting OS Kernel

The kernel is the part of prompting that stays true across almost every model.

## Kernel Contract

```text
Goal: What must be produced.
Context: What information matters.
Constraints: What must be included or excluded.
Method: How the model should approach the work.
Format: What shape the answer must take.
Verification: How success will be checked.
Failure behavior: What to do when uncertain, blocked, or missing context.
```

A weak prompt says: “Make this better.”

A kernel prompt says: “Produce this specific result, using this context, under these boundaries, in this format, and verify it this way.”

## Universal Prompt Template

```text
Role:
You are acting as [expert role].

Goal:
Produce [specific deliverable] for [audience/use case].

Context:
[Relevant facts, examples, files, source snippets, prior decisions.]

Scope:
Include:
- [Allowed item]
- [Allowed item]

Exclude:
- [Forbidden item]
- [Forbidden item]

Method:
1. Inspect the context.
2. Identify missing or uncertain information.
3. Produce the result.
4. Verify it against the quality bar.

Output format:
[Markdown, JSON, table, code block, checklist, etc.]

Quality bar:
- Accurate.
- Specific.
- Complete enough for the use case.
- Honest about uncertainty.
- No unsupported claims.
- No private or proprietary content.

Failure behavior:
If information is missing, state what is missing and make the safest useful assumption.
```

## Kernel Syscalls

| Syscall | Use | Prompt pattern |
| --- | --- | --- |
| `EXTRACT` | Pull facts from text. | “Extract only facts explicitly present in the source.” |
| `TRANSFORM` | Rewrite or reformat. | “Preserve meaning, change only structure/style.” |
| `PLAN` | Break work into steps. | “List the smallest safe steps before execution.” |
| `GENERATE` | Create new content. | “Use the goal, context, constraints, and format.” |
| `VERIFY` | Check output. | “Compare against rubric, schema, and source evidence.” |
| `REPAIR` | Fix detected issues. | “Revise only the failed parts.” |
| `COMPRESS` | Shorten without losing rules. | “Preserve constraints, format, and safety.” |
| `ROUTE` | Pick a workflow/model/tool. | “Classify the task and choose the best driver.” |

## Kernel Sections in Detail

### Goal

The goal should name a deliverable, not a theme.

Weak:

```text
Tell me about prompt engineering.
```

Strong:

```text
Write a beginner-friendly guide explaining five prompt engineering patterns,
with one example, one failure mode, and one verification step for each pattern.
```

Use verbs that imply observable output: write, extract, classify, transform,
compare, diagnose, generate, verify, package, summarize, or revise.

### Context

Context should be relevant and labeled. Do not mix instructions, examples,
sources, and random background into one block. A model may treat everything as
equally important unless the prompt tells it what each piece is for.

Good context labels:

- `Trusted repo rules`
- `Task objective`
- `Source evidence`
- `Examples to imitate structurally`
- `Examples to avoid`
- `Assumptions`
- `Out of scope`

### Constraints

Constraints should include both positive and negative boundaries.

Positive constraints:

- Use Markdown.
- Keep claims source-grounded.
- Edit only named files.
- Include a final checklist.

Negative constraints:

- Do not add dependencies.
- Do not include private paths.
- Do not copy leaked prompt text.
- Do not claim checks passed unless they ran.

Negative constraints are not hostile. They make the task smaller and more
reviewable.

### Method

The method section controls the work loop. It should be short enough to follow
and concrete enough to prevent the model from skipping inspection.

Common method loops:

| Loop | Use |
| --- | --- |
| Inspect -> Plan -> Edit -> Verify -> Report | Coding-agent and docs changes. |
| Read -> Extract -> Compare -> Answer -> Cite | Source-grounded answers. |
| Draft -> Critique -> Revise -> Finalize | Writing and review tasks. |
| Classify -> Route -> Execute driver -> Validate | Multi-mode assistants. |
| Generate -> Evaluate -> Repair -> Re-run | Prompt optimization. |

### Format

Format is part of correctness. If the output will be parsed, reviewed, copied
into a PR, or used as a prompt asset, define the shape.

Good format rules:

- "Return a Markdown table with columns `Risk`, `Why it matters`, `Mitigation`."
- "Return valid JSON only. Do not include Markdown."
- "Use sections: Summary, Files Changed, Checks, Risks."
- "Use PowerShell commands, not Bash, because this repo is Windows-friendly."

### Verification

Verification turns prompt output into evidence. It can be a command, a rubric,
a source check, a schema validation, a screenshot review, or a package manifest.

Weak:

```text
Make sure it is good.
```

Strong:

```text
Run `python scripts/repo_health_check.py`, inspect `git diff --stat`, and
report any skipped checks.
```

### Failure Behavior

Failure behavior prevents the model from hiding uncertainty.

Useful failure instructions:

- If sources do not support the answer, say what is missing.
- If a command fails, report the command and failure.
- If the requested action is unsafe, explain the boundary and offer a safe
  alternative.
- If the task is too broad, finish a concrete bounded slice and report the
  remaining work.

## Kernel Decision Table

| User asks for | Add to prompt | Reason |
| --- | --- | --- |
| Current product behavior | Official-doc verification date and source links. | Product behavior changes. |
| Code edits | File scope, checks, dirty-tree handling. | Prevent unrelated edits and false success claims. |
| Research synthesis | Source policy, citations, stale-source handling. | Prevent unsupported claims. |
| Prompt library work | Metadata, inputs, failure cases, versioning. | Make prompts maintainable. |
| Image generation | Subject inventory, composition, style, constraints. | Reduce under-specified outputs. |
| Tool use | Permission profile and approval gates. | Prevent unwanted side effects. |

## Kernel Failure Modes

| Failure | Cause | Repair |
| --- | --- | --- |
| Hallucination | No source boundary. | Require source-grounding and uncertainty labels. |
| Format drift | Output shape vague. | Provide exact schema and examples. |
| Scope creep | Goal too broad. | Name allowed and forbidden work. |
| Over-answering | No audience/depth constraint. | Define audience, length, and priority. |
| Brittle prompt | No tests. | Add golden cases and edge cases. |
| Tool damage | Permissions unclear. | Use read-only defaults and approval gates. |

## Kernel Review Checklist

- [ ] The deliverable is named.
- [ ] The audience or use case is named.
- [ ] Trusted context is separated from untrusted source text.
- [ ] Included scope is explicit.
- [ ] Excluded scope is explicit.
- [ ] Tool permissions are clear when tools exist.
- [ ] Output format is testable.
- [ ] Verification is concrete.
- [ ] Failure behavior is explicit.
- [ ] Fast-changing claims require current official sources.
- [ ] Private data and leaked prompt text are excluded.

## Kernel Rule

Never ask for “best” without defining the scoring function. Otherwise the model optimizes for whatever ghost is living in the probability distribution that day.
