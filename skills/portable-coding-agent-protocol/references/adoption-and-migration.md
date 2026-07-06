# Adoption And Migration

Use this module when deciding whether to integrate the protocol into an existing
agent architecture.

## Adapter Contract

Adapters must document how the host environment provides:

- Search, read, edit, and diff.
- Command execution and test/build conventions.
- Approval boundaries.
- Progress and final reporting.
- Optional browser/UI, simulator, debugger, hardware, memory, and parallel work.
- Instruction precedence across global, project, directory, and user messages.

Conformance is judged by observable behavior, not by whether an agent used a
particular tool name, prompt syntax, model family, or message channel.

## Benefits

- Reduces common weaker-agent failures by externalizing state and evidence loops.
- Gives teams a shared behavior contract across agents.
- Makes verification and missing evidence visible.
- Supports embedded and hardware safety gates.
- Allows local measurement of protocol uplift.

## Costs And Risks

- More steps and tokens for simple tasks.
- Slower completion when tests, hardware, or verifier passes are required.
- Risk of prompt cargo culting if teams copy modules without adapters.
- False confidence if prose instructions are not backed by runtime guardrails.
- Possible conflicts with existing internal policy unless precedence is defined.

## Migration Checklist

1. Inventory existing agent instructions, hooks, tools, and safety controls.
2. Remove duplicate or stale workarounds that conflict with this protocol.
3. Define adapter mappings and approval gates.
4. Choose conformance level.
5. Run local evaluation tasks.
6. Pilot on low-risk repositories.
7. Measure failures and revise.
8. Pin a version before organization-wide rollout.

## Conformance Levels

- Advisory: guidance only; no measurement.
- Evidence discipline: final claims must map to observed evidence.
- Workflow control: task ledger, phase gates, self-review, and retry limits are
  required for non-trivial work.
- Enforced runtime: sandbox, approvals, logging, and eval gates are enforced by
  the host, not only by prompt text.

## Non-Goals

This protocol does not replace security policy, code review, CI, runtime
sandboxing, production controls, hardware lab controls, or human ownership.
