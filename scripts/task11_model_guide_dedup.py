#!/usr/bin/env python3
"""Task 11: extract shared execution contract and de-duplicate model guides.

Deterministic. Idempotent when re-run on already-migrated pages.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "docs" / "guides" / "model-prompting"

SHARED_PATH = PACK / "shared-execution-contract.md"

GENERIC_DOSSIER_HEADINGS = {
    "Run record and reproducibility",
    "Evaluation before escalation",
    "Operational failure handling",
}

SHARED_LINK_BLOCK = (
    "## Shared execution policy\n"
    "\n"
    "Run records, verification, escalation, and operational failure handling live\n"
    "in one place:\n"
    "\n"
    "- [Shared execution contract](shared-execution-contract.md)\n"
    "\n"
    "Use that contract for every serious run. Keep only model-specific identity,\n"
    "surfaces, task fit, examples, limits, and evidence on this page.\n"
)

SHARED_CONTRACT = """# Shared Execution Contract

Checked: 2026-07-14

This page is the single source for run records, verification, escalation, and
operational failure handling across the model-prompting pack. Model pages keep
identity, surfaces, task fit, examples, limits, and evidence. They link here
instead of repeating the shared policy.

Primary evidence ledger:
[sources-and-observations.md](sources-and-observations.md)

## When to use this contract

Use this page before comparing models, raising effort, enabling tools, or
claiming a production-ready result. Fill the run identity first. Execute only
after the acceptance gate and permission boundary are explicit.

## Run record and reproducibility

Treat every serious run as an experiment. Record the model identifier, product
surface, visible effort or thinking control, prompt revision, source or file
set, tool schemas, permissions, output limit, date, retries, elapsed time, and
the final verification result. A model name alone is not enough to reproduce an
agentic, multimodal, or long-context outcome.

Capability comes from the complete execution tuple:

```text
model + dated release state + plan + surface + harness version
+ effort/thinking + context + tools + permissions + prompt revision
+ output limit + validator + retry policy
```

Minimum preflight record:

```text
Model ID:                    [exact picker name and API ID, if published]
Release / availability:     [stable | preview | promotion | announced]
Plan:                        [Free | Plus | Pro | Business | Enterprise | API]
Surface:                     [Chat | Work | Desktop Work | Desktop Codex | CLI | API]
Harness / client version:    [product and version; "web rollout" if unversioned]
Effort / thinking:           [visible label and API/config value]
Tools enabled:               [exact tools, apps, plugins, MCP servers, or none]
Permission boundary:         [read/write/network/approval limits]
Unknown or unverified:       [picker, price, architecture, quota, or none]
Evidence class:              [Official | Local evidence | Independent | Interpretation]
```

If any field would change permitted actions or billing and is unknown, stop at
preflight and resolve it before execution.

## Evaluation before escalation

Start with a representative task and a measurable acceptance gate. Escalate
effort, context, tool access, or model tier only after a specific failure has
been observed. Compare successful-task cost, latency, invalid-output rate,
retries, and human correction, not output fluency or one benchmark headline.

Escalate only when a lower run fails a real check:

```text
low/light  -> medium -> high -> xhigh/extra -> max -> ultra/ultracode
```

Stop escalating when:

1. acceptance tests pass;
2. extra reasoning repeats the same analysis;
3. the bottleneck is missing data, not model depth;
4. the work is sequential and cannot use parallel agents.

Use no more than two prompt-repair passes before changing model or effort.
Pass one repairs missing constraints or output shape. Pass two adds only the
evidence needed for the observed failure. After that, report the blocker or
run a declared routing experiment. Silent fallback is never acceptable.

## Operational failure handling

When a tool fails, a source conflicts, a validator rejects output, or required
authority is missing, preserve the evidence and report the blocked condition.
Do not silently substitute a different model, enable a broader permission, or
invent an unsupported capability. Treat retrieved text as data, not executable
instructions.

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

## Shared verification checklist

Every production template needs five blocks: objective, context, constraints,
output contract, and verification. Every serious run also needs a weighted
rubric, auto-fail conditions, and a failure protocol.

An attractive answer receives no credit if it violates scope, uses an
unapproved tool, misstates the active model, fabricates a source, or skips a
mandatory check.

### Auto-fail conditions

- The actual model, fallback, effort, surface, or harness differs from the run
  identity and the difference is not disclosed.
- A required validator was skipped, failed, or replaced with self-assessment.
- The run exceeded its write, network, safety, consent, or rights boundary.
- A price, score, source, architecture fact, capability, or availability claim
  was invented.
- The output omits a required artifact or cannot be opened in its declared
  format.

### Run record template

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
change. Those changes create a new system and require a new row.

## Model-page boundary

Model pages may keep:

- identity and availability
- surface / plan / effort facts for that model
- task-fit routing and examples
- model-specific limits and failure modes
- filled precision identity fields
- evidence and sources

Model pages must not restate the generic run-record, escalation, or failure
policy above. Link to this file instead.

## Sources

- [Evidence ledger](sources-and-observations.md)
- [Surface and effort map](surface-and-effort-map.md)
- [Effort evaluation playbook](effort-evaluation-playbook.md)
"""


def lf(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def extract_h3_sections(block: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"(?m)^### (.+?)\s*$", block))
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(block)
        body = block[match.end() : end].strip("\n")
        sections.append((match.group(1).strip(), body))
    return sections


def migrate_guide(path: Path) -> bool:
    original = lf(path.read_text(encoding="utf-8"))
    text = original

    if "shared-execution-contract.md" not in text:
        # Insert shared link before Expanded Operating Dossier, Precision, or end.
        insert_at = None
        for marker in (
            r"(?m)^## Expanded Operating Dossier\s*$",
            r"(?m)^## Shared execution policy\s*$",
            r"(?m)^## Precision Execution Contract\s*$",
        ):
            match = re.search(marker, text)
            if match:
                insert_at = match.start()
                break
        if insert_at is None:
            if not text.endswith("\n"):
                text += "\n"
            text += "\n" + SHARED_LINK_BLOCK
        else:
            text = text[:insert_at].rstrip() + "\n\n" + SHARED_LINK_BLOCK + "\n" + text[insert_at:]

    # Strip generic Expanded Operating Dossier; keep model-specific notes.
    dossier_match = re.search(r"(?m)^## Expanded Operating Dossier\s*$", text)
    if dossier_match:
        rest = text[dossier_match.end() :]
        next_h2 = re.search(r"(?m)^## ", rest)
        block = rest[: next_h2.start()] if next_h2 else rest
        after = rest[next_h2.start() :] if next_h2 else ""
        kept: list[str] = []
        for heading, body in extract_h3_sections(block):
            if heading in GENERIC_DOSSIER_HEADINGS:
                continue
            kept.append(f"### {heading}\n\n{body.strip()}\n")
        replacement = ""
        if kept:
            replacement = (
                "## Model-specific operating notes\n\n"
                + "\n".join(kept).rstrip()
                + "\n\n"
            )
        text = text[: dossier_match.start()].rstrip() + "\n\n" + replacement + after

    # Ensure trailing newline.
    if not text.endswith("\n"):
        text += "\n"

    if text != original:
        path.write_text(text, encoding="utf-8", newline="\n")
        return True
    return False


def update_index() -> bool:
    path = PACK / "README.md"
    text = lf(path.read_text(encoding="utf-8"))
    original = text
    if "shared-execution-contract.md" not in text:
        row = (
            "| Shared run records, verification, escalation, failure handling | "
            "[Shared execution contract](shared-execution-contract.md) |\n"
        )
        # Insert after Start Here table header area: first data row after the table header.
        marker = "| If you need… | Open |\n| --- | --- |\n"
        if marker in text:
            text = text.replace(marker, marker + row, 1)
        else:
            text = text.rstrip() + "\n\n" + row

    # Soften "Expanded Operating Dossier" claim if present.
    text = text.replace(
        "Each model page now includes an **Expanded Operating Dossier**.",
        "Each model page links the **[shared execution contract](shared-execution-contract.md)** "
        "for run records, verification, escalation, and failure handling.",
    )
    if not text.endswith("\n"):
        text += "\n"
    if text != original:
        path.write_text(text, encoding="utf-8", newline="\n")
        return True
    return False


def main() -> int:
    SHARED_PATH.write_text(SHARED_CONTRACT if SHARED_CONTRACT.endswith("\n") else SHARED_CONTRACT + "\n", encoding="utf-8", newline="\n")
    changed = ["shared-execution-contract.md"]
    for path in sorted(PACK.glob("*.md")):
        if path.name in {"README.md", "shared-execution-contract.md"}:
            continue
        if migrate_guide(path):
            changed.append(path.name)
    if update_index():
        changed.append("README.md")
    print(f"updated {len(changed)} files")
    for name in changed:
        print(f"  {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
