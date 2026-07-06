# Adoption Guide

This guide is for teams that already have an AI-agent architecture and need to
decide whether this protocol is worth adopting.

## What This Is

This is an agent operating protocol, not an agent runtime. It defines observable
engineering behavior: maintain task state, inspect before editing, preserve
local work, keep diffs scoped, verify with evidence, disclose uncertainty, and
ask before destructive or external side effects.

Runtime-specific details belong in adapters: tool names, shell, filesystem,
sandbox, approval model, browser or hardware access, memory, subagents, and
reporting channels.

## Decision Criteria

Adopt when:

- Your agents often finish without enough verification.
- Your weaker or cheaper models lose the goal during multi-step tasks.
- Your diffs contain drive-by refactors or unrelated cleanup.
- Your architecture needs a shared behavior contract across multiple agents.
- Your embedded, hardware, or production workflows need explicit safety gates.
- You can measure compliance through logs, diffs, tests, and final reports.

Do not adopt as-is when:

- Your runtime cannot capture tool results or command logs.
- Your agents cannot read and edit files safely.
- Your organization relies on enforced policy but only plans to add prose prompts.
- Your tasks require regulated approvals not represented in the adapter.
- You cannot tolerate the extra latency or token use from self-review and checks.

## Advantages

- Model-neutral behavior contract.
- Short entry point with lazy-loaded detail modules.
- Lower-model amplification through explicit state, evidence, verifier, and stop
  loops.
- Stronger reporting honesty: no success claims without evidence.
- Embedded-aware safety gates for target builds, hardware, generated files, and
  destructive operations.
- Evaluation guidance for measuring local uplift instead of assuming it.

## Disadvantages

- It adds process overhead to simple edits.
- It cannot compensate for missing model knowledge, missing tools, or poor
  runtime isolation.
- It may reduce speed when verification is slow or hardware is unavailable.
- It requires teams to define adapters and instruction precedence.
- It can create a false sense of safety if not paired with real sandboxing,
  approvals, CI, code review, and secret controls.

## Migration Concerns

- Instruction precedence: decide how this interacts with existing `AGENTS.md`,
  `CLAUDE.md`, Cursor rules, Copilot instructions, CI policy, and internal
  secure-coding rules.
- Adapter mapping: document how the host environment provides search, read,
  edit, command execution, approval, progress reporting, final reporting,
  optional memory, optional UI/browser control, and optional parallel work.
- Verification cost: define expectations for slow suites, flaky tests, paid
  cloud tests, hardware labs, unavailable devices, and manual checks.
- Governance: pin a protocol version, review changes before rollout, and keep
  leaked or community prompt references non-normative.
- Observability: log unverified completions, unrelated diffs, failed builds,
  overwritten user work, destructive-action attempts, and false verification
  claims.

## Conformance Levels

- Level 0, Advisory: the protocol is available as guidance, but compliance is
  not measured.
- Level 1, Evidence Discipline: agents must tie final claims to observed tests,
  commands, diffs, logs, or explicit limitations.
- Level 2, Workflow Control: agents must maintain task state, phase gates,
  retry limits, and pre-final self-review.
- Level 3, Enforced Runtime: the host environment enforces sandboxing,
  approvals, tool permissions, logging, and evaluation gates.

Do not describe Level 0 or Level 1 adoption as safety enforcement.

## Rollout Path

1. Map runtime capabilities and missing adapters.
2. Resolve instruction precedence.
3. Define approval and destructive-action boundaries.
4. Run the local evaluation pack on representative tasks.
5. Pilot in low-risk repositories.
6. Measure failures and revise adapters.
7. Expand to higher-risk repositories only after evidence improves.

## Non-Goals

This protocol does not replace organization security policy, CI policy, code
review, sandboxing, secret handling, production controls, hardware lab controls,
or human judgment. It also does not make weaker models equivalent to stronger
models; it aims to reduce avoidable process failures.
