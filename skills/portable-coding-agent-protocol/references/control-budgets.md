# Control Budgets

Use this module when a lower-capability model needs concrete tripwires. Treat
these numbers as adapter defaults, not universal law. A host runtime may tighten
or loosen them by task risk.

## Default Budgets

| Control | Tiny | Small | Medium | Large |
| --- | --- | --- | --- | --- |
| Relevant file reads before edit | 1 | 3-5 | 5-15 | 15+ with ledger |
| Search variants before "not found" | 1 | 3 | 3-5 | 5+ plus call-path tracing |
| Failed hypotheses before approach change | 1 | 2 | 2 | 2 plus critic |
| Verification cycles before escalation | 1 | 2 | 2 | 2 plus checkpoint |
| Pre-final review depth | diff/status | diff/status/evidence | full gate | gate plus reviewer |

## Escalation Rules

Escalate, narrow, or ask when:

- Required evidence cannot be produced by available tools.
- Two fixes fail with the same verification result.
- The task expands beyond the user request.
- A required action crosses destructive, external, production, or device
  boundaries.
- The model cannot name a next action tied to evidence.

## Lower-Model Use

For lower models, budgets are scaffolding. They prevent early closure and
search-myopia; they do not prove correctness. If a budget is exhausted, the
agent should change strategy, ask a stronger verifier, or report the limit
instead of continuing fluent speculation.
