# Task Mode Selector

Choose one mode before meaningful work. If the task grows beyond the selected
mode, switch modes and say why.

## Tiny

Use when the change is one file, low risk, and has obvious verification.

Required:

- Inspect target.
- Edit or answer narrowly.
- Run or describe one relevant check.
- Report result and missing evidence.

Compressed form:

```text
Goal:
Context checked:
Check run or missing:
Result:
```

## Standard

Use for normal coding tasks.

Required:

- Task ledger.
- Pre-edit checklist.
- Targeted verification.
- Completion gate.

## High Risk

Use for generated files, vendor boundaries, secrets, production, hardware,
destructive operations, data loss, broad refactors, or unclear ownership.

Required:

- Explicit approval boundaries.
- Evidence log.
- Critic or verifier pass.
- No completion claim without verification or limitation disclosure.

## Eval

Use for benchmark or protocol-evaluation runs.

Required:

- Immutable seed or reset script.
- Captured prompt and condition.
- Diff/status artifact.
- Command log and test output.
- Final response.
- Scorer JSON.
