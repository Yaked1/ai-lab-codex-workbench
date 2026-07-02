# Failure Mode Catalog

This catalog lists recurring failures in prompt systems, coding-agent work,
source-grounded writing, package releases, and public documentation. Use it as
a pre-flight checklist before running an agent and as a post-flight checklist
before claiming completion.

The catalog is intentionally practical. Each failure includes the symptom, the
usual cause, and the preferred repair.

## Prompt Design Failures

| Failure | Symptom | Repair |
| --- | --- | --- |
| Vague goal | Output is generic or off-target. | Add deliverable, audience, scope, and success criteria. |
| Missing inputs | Agent guesses values. | Add `Inputs to fill` section or ask a clarifying question. |
| No excluded scope | Agent edits unrelated files. | Name out-of-scope files and actions. |
| No verification | Final report says done without evidence. | Add command checks or manual review criteria. |
| No failure behavior | Agent invents missing facts. | Require uncertainty and skipped-item reporting. |
| Overloaded prompt | Important constraints are buried. | Split stable rules, task context, source text, and output format. |

## Coding-Agent Failures

| Failure | Symptom | Repair |
| --- | --- | --- |
| Dirty worktree ignored | User changes overwritten or staged accidentally. | Run `git status`; preserve and stage explicit paths. |
| Local rules skipped | Edits violate repository conventions. | Read `AGENTS.md` before changing files. |
| Dependency drift | New dependency appears for a simple task. | Ask first; prefer standard library when repo does. |
| Test mismatch | Tests pass but do not cover the requested behavior. | Add or run focused checks tied to requirement. |
| Destructive shortcut | Agent proposes reset, clean, or delete. | Refuse unless explicitly requested and approved. |
| Stale final answer | Reports old objective after interruption. | Re-read newest user request and current state. |

## Source Failures

| Failure | Symptom | Repair |
| --- | --- | --- |
| Source laundering | Community source becomes official claim. | Label source status and verify official facts. |
| Prompt injection | Retrieved text controls the agent. | Treat source as evidence only. |
| Quote overuse | Guide copies source prose. | Extract structure and write original synthesis. |
| Local path leak | Public doc contains private machine path. | Replace with sanitized source name or relative repo path. |
| Unreadable source assumed | Content inferred from archive name. | Mark skipped unless directly inspected. |
| Freshness overclaim | Exact pricing or model support stated permanently. | Verify in official docs or mark as needing verification. |

## Package Failures

| Failure | Symptom | Repair |
| --- | --- | --- |
| Thin package | ZIP exists but content is too small to teach. | Enforce Markdown file and byte floors. |
| Manifest not inspected | Build passed but contents unknown. | Open manifest and derive metrics. |
| Missing hash | Release cannot be identified. | Record ZIP SHA-256. |
| Private path in manifest | Manifest leaks local environment. | Use relative path rendering and scan output. |
| Required module absent | Package index links to missing file. | Add required file tests and health checks. |
| Generated artifact committed | Repo includes local build output. | Keep output ignored unless explicitly tracked. |

## Documentation Failures

| Failure | Symptom | Repair |
| --- | --- | --- |
| Landing page only | README does not teach workflow. | Add start path, map, commands, safety, package, and maintenance. |
| No beginner path | New reader cannot start. | Add "Start Here" table and reading order. |
| No advanced path | Maintainer cannot audit. | Add package, tests, source-policy, and release sections. |
| No examples | Reader cannot apply concepts. | Add command blocks, filled prompts, and review reports. |
| No failure modes | Reader cannot recover. | Add troubleshooting table. |
| Broken navigation | New modules are undiscoverable. | Update README, package README, guide index, and static site if needed. |

## Tool-Use Failures

| Failure | Symptom | Repair |
| --- | --- | --- |
| Permission ambiguity | Agent runs risky command. | Add allowed, ask-first, and forbidden lists. |
| Browser account risk | Agent uses logged-in state unexpectedly. | Ask before account actions or form submission. |
| RAG/tool blending | Tool output becomes hidden instruction. | Label tool output as evidence. |
| Approval bypass | Agent seeks workaround after blocked command. | Respect approval boundary and report blocker. |
| Overbroad staging | Unrelated files included. | Use explicit `git add` paths. |

## Review Failures

| Failure | Symptom | Repair |
| --- | --- | --- |
| Style-first review | Real risks missed. | Review scope, safety, behavior, evidence, then style. |
| No severity | Findings are hard to prioritize. | Use critical/high/medium/low. |
| No file references | Findings are not actionable. | Cite file and line when possible. |
| No residual risk | Review implies false certainty. | State what was not verified. |
| Tests treated as magic | Green tests overclaim. | Explain coverage and gaps. |

## Recovery Workflow

When a failure is found:

1. Stop expanding scope.
2. Identify the requirement affected.
3. Gather direct evidence.
4. Make the smallest aligned fix.
5. Rerun the focused check.
6. Update docs, tests, or changelog if the fix changes public behavior.
7. Report the failure and repair.

## Pre-Completion Checklist

- [ ] Goal and scope are explicit.
- [ ] Local rules were read.
- [ ] Dirty worktree state is known.
- [ ] Source status is labeled.
- [ ] Permission boundaries are explicit.
- [ ] Required checks ran or are reported as skipped.
- [ ] Package manifest is inspected when package changed.
- [ ] Public-safety scan ran.
- [ ] New docs are linked from the relevant index.
- [ ] Final report avoids overclaiming.
<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->
## Research-Grade Review Addendum

This file is part of the repository's **Prompting OS module** surface. During broad
maintenance, reviewers should treat `docs/prompting-os/37-failure-mode-catalog.md` as a contract-bearing artifact
rather than passive prose. The file should keep a clear audience, explicit
scope, concrete operating steps, public-safety boundaries, and verification
evidence that a maintainer can inspect without trusting an agent summary.

Research-grade review questions for this file:

- Does `37 failure mode catalog` state what decision, workflow, or reusable behavior it supports?
- Are included scope, excluded scope, and unsafe actions clear enough for an
  agent or contributor to follow?
- Are examples public-safe, repository-relative, and free of private data?
- Are fast-changing product or platform claims phrased conservatively or marked
  for official-doc verification?
- Does the file point to the next artifact a reader should inspect: a command,
  template, test, manifest, package, or deeper guide?
- Could a reviewer cite this file in a PR review and know what evidence proves
  the work is complete?

Keep future edits focused on stronger evidence, clearer failure modes, better
navigation, and safer automation boundaries. Do not add length unless the new
material makes the repository easier to operate, teach, audit, or recover.
<!-- RESEARCH-GRADE-EXPANSION:END -->
