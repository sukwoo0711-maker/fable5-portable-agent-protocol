# Self-Review

Use this module before finalizing meaningful edits, especially when no separate
reviewer or verifier agent is available.

## Role-Separated Review

Run three passes:

1. Implementer pass: what changed and why.
2. Skeptic pass: how this could be wrong, too broad, unverified, or unsafe.
3. Reporter pass: what can be honestly claimed from evidence.

Do not use the skeptic pass to invent extra work. Use it to catch risk.

## Diff Audit

Inspect the actual diff before final response:

- Does every hunk serve the request or a necessary verification artifact?
- Did formatting or generated files change unexpectedly?
- Did imports, lock files, snapshots, or build outputs change?
- Did user work get overwritten?
- Are debug logs, scratch files, or temporary probes removed?

## Verification Audit

Match each final claim to evidence:

- Claim: "Bug reproduced." Evidence: failing command or observed output.
- Claim: "Fix works." Evidence: passing command or manual run.
- Claim: "No target verification." Evidence: target unavailable or not run.
- Claim: "Only scoped files changed." Evidence: diff/status inspection.

If a claim lacks evidence, downgrade the wording.

## Failure Audit

When checks fail, report:

- Command or method.
- Failure summary.
- Whether it appears related to the change.
- What was attempted.
- What would be the next useful diagnostic.

Do not hide partial failures behind a success summary.
