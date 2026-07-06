# Context Management

Use this module when a task spans many files, many tool calls, multiple sessions,
or a large repository.

## Read For Decisions

Read enough to decide the next action, not everything. Prefer:

- Exact search strings.
- Entry points.
- Target definitions and call sites.
- Nearby tests.
- Project instructions and manifests.

Avoid flooding context with unrelated files.

## Carry Forward Facts

Keep a compact task ledger with:

- Observed facts.
- Decisions already made.
- Failed hypotheses.
- Commands run and results.
- Files changed.
- Verification still missing.

Update it when the task changes phase.

## Avoid Context Drift

Before finalizing or resuming, re-check:

- Latest user request.
- Current diff.
- Current test/build state.
- Any new user message.

Do not answer an older version of the task.

## Durable Notes

Write durable notes only when the environment permits it and the information
will matter after the session:

- Project-specific setup discoveries.
- Repeated failure modes.
- Device or toolchain constraints.
- Evaluation results.

Do not store secrets or private data unless the user explicitly asks and policy
allows it.
