# First Reviewed Agent Task

This 5 to 15 minute tutorial produces one review report and one deterministic
verification result. It is deliberately small. New users need a first success,
not a pilgrimage through thirty-seven modules.

## Run it

1. Open `task-input.md` and `work-order.md`.
2. Give the work order to your coding agent from this directory, or write
   `report.md` yourself.
3. Compare the result with `expected-report.md`.
4. Run:

```powershell
python examples/first-reviewed-agent-task/check_report.py
```

Expected result:

```text
PASS: first reviewed agent report satisfies the contract
```

The checker validates the output contract. It does not pretend to evaluate the
quality of every possible sentence.
