# Capability Calibration

Use this module when the model may be weaker than the task, tools are missing,
or evidence is incomplete.

## Classify Knowledge

Tag important statements internally:

- Known: directly observed in files, command output, tests, logs, hardware, or
  user-provided facts.
- Inferred: likely from patterns but not directly proven.
- Assumed: chosen because work can proceed safely without confirmation.
- Unverified: plausible but not checked.
- Blocked: cannot be checked with available tools or permissions.

Final reports may include inferred or assumed items, but must label them.

## Capability Gaps

Before accepting a broad task, check whether the environment has:

- File read and search.
- Safe editing.
- Command execution or a way to request execution.
- Test/build/static check access.
- Evidence capture.
- Approval path for risky operations.
- Persistent notes for long work.

If several are missing, narrow the task to analysis or planning.

## Confidence Rules

- High confidence requires direct evidence.
- Medium confidence may use multiple consistent observations.
- Low confidence means the agent should inspect, test, ask, or narrow scope.
- No confidence should never be phrased as completion.

Do not let fluent explanation substitute for evidence.

## Degradation Matrix

| Missing capability | Degradation | Required response |
| --- | --- | --- |
| No command execution | Cannot prove runtime behavior | Prefer static analysis and label verification missing. |
| No safe edit mechanism | Cannot apply patch reliably | Provide patch plan or ask for an edit path. |
| No tests or build | Regression risk rises | Run a minimal manual probe or disclose missing coverage. |
| No memory or durable notes | Long tasks lose state | Use a compact task ledger in the current context. |
| No browser/UI/device access | Visual or hardware claims weaken | Use screenshots, logs, simulator, or mark target verification missing. |
| No subagents | Independent review weakens | Run role-separated self-review and label it less independent. |

## Choosing Smaller Work

For lower-capability agents, prefer thin vertical slices over broad horizontal
work. A slice should produce observable evidence before the next slice begins.

## Model-Tier Calibration

| Tier | Typical risk | Required stance |
| --- | --- | --- |
| Lower | Loses goal, stops early, overclaims, misses call paths | Externalize state, use visible gates, keep edits small, require explicit evidence. |
| Mid | Usually follows tasks but may skip edge verification | Compress tiny work, keep completion gate and diff/evidence audit for meaningful edits. |
| Frontier | Better implicit planning but may over-act or over-refactor | Scale down ceremony, keep boundaries, approval gates, and claim discipline. |

Do not ask a lower model to compensate for missing tools or missing information
by reasoning harder. Narrow the task, add an adapter capability, or escalate to a
stronger verifier.
