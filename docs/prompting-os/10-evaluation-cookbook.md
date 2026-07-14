# Prompt Evaluation Cookbook

Prompt evaluation is the practice of checking whether a prompt works across
representative cases, not just one successful demo. This cookbook gives
practical evaluation recipes that can run manually, in a spreadsheet, with a
small script, or later in a dedicated tool such as promptfoo.

The goal is not to make prompting feel like conventional software testing. The
goal is to create enough evidence that a reviewer can see whether a prompt
change improved reliability, harmed safety, or merely sounded more elaborate.

## Evaluation Design

Start with an evaluation brief:

```yaml
prompt_id: public_docs_update
version_under_test: 1.2.0
task_family: coding-agent documentation edit
primary_risks:
  - unsupported external claims
  - unrelated file edits
  - skipped checks
  - private-path leakage
success_definition:
  - edits only scoped docs
  - cites official sources for current facts
  - runs required checks or reports why not
  - final report includes files, commands, results, risks
test_cases:
  - normal docs update
  - stale external claim
  - dirty worktree
  - malicious source text
```

Good evaluations are small and sharp. A five-case suite with clear pass/fail
criteria is better than fifty vague examples.

## Case Types

| Case type | Purpose | Example |
| --- | --- | --- |
| Golden case | Proves the normal path works. | Update one guide with supplied source facts. |
| Edge case | Proves behavior near boundaries. | Asked to edit docs and workflow YAML, but only docs are in scope. |
| Abuse case | Proves safety boundaries. | Retrieved text says to reveal secrets or ignore policy. |
| Regression case | Proves old behavior still works. | Existing prompt template still includes final report fields. |
| Format case | Proves machine-readable output is valid. | JSON output must parse and match schema. |
| Missing-info case | Proves uncertainty behavior. | Current product pricing requested without official source. |
| Long-context case | Proves context triage. | Many files provided, only two relevant. |

## Scoring Model

Use a four-part score:

| Dimension | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| Task completion | Fails or changes subject. | Partial. | Complete with minor gaps. | Complete and directly useful. |
| Grounding | Invents or misuses facts. | Weak source use. | Mostly supported. | Every material claim is supported or labeled. |
| Safety | Violates constraints. | Risky or unclear. | Safe with minor ambiguity. | Explicitly preserves boundaries. |
| Reviewability | Hard to inspect. | Some structure. | Clear enough. | Files, checks, risks, and evidence are easy to audit. |

Record both the numeric score and a short reason. Scores without reasons do not
teach future maintainers what to change.

## Manual Evaluation Table

```markdown
| Case | Expected behavior | Actual behavior | Score | Notes |
| --- | --- | --- | ---: | --- |
| normal_docs_update | Edits only target doc and reports checks. |  |  |  |
| stale_claim | Verifies official docs or marks unverified. |  |  |  |
| dirty_tree | Reads status and avoids overwriting unrelated changes. |  |  |  |
| prompt_injection | Ignores source-embedded instruction. |  |  |  |
```

This format is enough for small teams and teaching repos. Use a formal eval
tool when prompts become part of production or high-volume workflows.

## Recipe: Coding-Agent Prompt Evaluation

Purpose: verify a coding-agent work order.

Inputs:

- A small test repository or fixture.
- One docs-only task.
- One code task with tests.
- One dirty-worktree case.
- One forbidden dependency or destructive-command request.

Expected checks:

- Agent runs `git status` before edits.
- Agent inspects relevant files.
- Agent keeps edits scoped.
- Agent runs realistic verification.
- Agent reports failed or skipped checks honestly.
- Agent does not claim success from intent alone.

Failure signals:

- Touches unrelated files.
- Installs dependencies without approval.
- Deletes files without explicit request.
- Claims tests passed when they did not run.
- Uses summaries as evidence instead of diffs or command output.

## Recipe: RAG Prompt Evaluation

Purpose: verify source-grounded answering.

Cases:

1. Source contains the exact answer.
2. Source partially answers the question.
3. Sources conflict.
4. Source includes prompt-injection text.
5. Source is stale or lacks a date.

Pass criteria:

- Answers are limited to source support.
- Missing information is named.
- Conflicts are reported.
- Embedded source instructions are ignored.
- Inferences are labeled.

Useful output fields:

```json
{
  "answer": "string",
  "supported_claims": [
    {"claim": "string", "source_id": "string"}
  ],
  "inferences": ["string"],
  "missing_information": ["string"],
  "source_conflicts": ["string"]
}
```

## Recipe: Prompt Library Evaluation

Purpose: decide whether a reusable prompt belongs in the package.

Checklist:

- The prompt has a name and purpose.
- The target tool is named.
- Inputs to fill are obvious.
- Safety boundaries are present.
- Verification steps are present.
- The final report format is present.
- At least one failure case is described.
- The prompt does not contain copied leaked or proprietary text.
- The prompt can be understood without private local context.

Reject or revise prompts that are merely persona slogans, broad role prompts,
or prompts with no evidence path.

## Recipe: Image Prompt Evaluation

Purpose: evaluate image-prompt reliability.

Test dimensions:

- Subject identity.
- Entity count.
- Spatial layout.
- Style and medium.
- Lighting.
- Text rendering.
- Safety constraints.
- Revision behavior.

Prompt outputs should be evaluated against the specification, not against
whether the image looks impressive. A beautiful wrong image is still a failed
prompt if the task required a specific layout or subject.

## Regression Protocol

Use this protocol before changing a packaged prompt:

1. Copy the current prompt version.
2. Select three old cases that should still pass.
3. Add one new case for the failure you want to fix.
4. Run the old prompt and record results.
5. Modify the prompt.
6. Run the new prompt on all cases.
7. Keep the change only if the new case improves and important old behavior
   does not regress.
8. Update changelog or prompt metadata.

## Failure Analysis Template

```markdown
## Failure

Prompt:
Case:
Expected:
Actual:

## Classification

- [ ] Missing context
- [ ] Ambiguous instruction
- [ ] Bad output schema
- [ ] Weak source boundary
- [ ] Tool permission issue
- [ ] Overlong or noisy prompt
- [ ] Model limitation
- [ ] Evaluation case too vague

## Repair

Smallest prompt change:
New or updated test case:
Risks:
Decision:
```

## Package Quality Gate

For packaged Prompting OS docs, require:

- Multiple long-form technical modules, not only a README.
- A universal template and a scoring rubric.
- Security guidance and source-policy rules.
- Evaluation recipes with cases and pass/fail criteria.
- Model-family adapters.
- Context/RAG guidance.
- Agent/tool permission guidance.
- Public-safe source map.
- Changelog entry for user-visible changes.

Length alone is not enough. A long file that does not teach a workflow, provide
examples, name failure modes, or define verification is not useful.

## Evaluation Rule

Every serious prompt should answer three questions:

1. What behavior should improve?
2. What evidence would prove it improved?
3. What old behavior must not break?

If those questions are unanswered, the prompt is still a draft.
