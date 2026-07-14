# Acceptance Evaluation

A result fails automatically if it exceeds scope, exposes private data, skips a
mandatory check, hides a fallback, or cannot produce the declared artifact.

| Criterion | Weight | Pass evidence |
| --- | ---: | --- |
| Correctness | 40 | Focused validator passes |
| Scope | 20 | Final diff touches only named paths |
| Safety | 20 | No auto-fail condition occurs |
| Completeness | 10 | Output contract is complete |
| Reviewability | 10 | Commands, evidence, and risks are reported |

Accept at 85/100 or higher only when every auto-fail gate passes.
