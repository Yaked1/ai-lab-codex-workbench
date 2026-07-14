# First Reviewed Agent Work Order

## Objective

Read `task-input.md` and create `report.md` that identifies the documented
check, the two missing review details, and a safe next action.

## Included scope

- Read `task-input.md`.
- Create or replace only `report.md` in this directory.

## Excluded scope

- Do not edit repository scripts, workflows, or documentation.
- Do not run network tools or publish anything.

## Output contract

The report must contain these headings:

1. `## Summary`
2. `## Evidence`
3. `## Missing Details`
4. `## Verification`

It must quote the command exactly, name both missing details, and state that the
command was documented but not executed during this read-only exercise.

## Verification

Run:

```powershell
python examples/first-reviewed-agent-task/check_report.py
```
