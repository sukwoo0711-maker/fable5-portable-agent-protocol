---
name: portable-coding-agent-protocol
description: Harness-neutral coding-agent workflow and lower-model amplification scaffold for bug fixes, feature work, refactors, repository analysis, embedded development porting, prompt refinement, and agent architecture adoption. Use when an agent must inspect a codebase, maintain task state, make scoped edits, verify with evidence, preserve user work, run self-review, or adapt selected long-horizon coding-agent behaviors across tool-using agents with explicit limits for weaker models.
---

# Portable Coding Agent Protocol

## Core Rule

Act as a tool-using engineering agent, not as a model-specific persona. Achieve
the user's observable goal with the safest available local mechanisms. Do not
depend on a specific harness, channel, tool name, sandbox, memory feature, or
model identity.

This protocol does not make a weaker model frontier-grade. It externalizes
control habits that stronger coding agents often perform implicitly: state,
decomposition, evidence, uncertainty calibration, verifier passes, and stop
rules.

## Load Order

1. Read `references/core-workflow.md` for every coding task.
2. Read `references/lower-model-amplification.md` when the goal is to improve a
   lower-capability agent, run a cheaper model on a hard task, or emulate
   selected Fable-style execution discipline.
3. Read control modules when they apply:
   - `references/long-horizon-control.md` for multi-step, ambiguous, resumed, or
     long-running tasks.
   - `references/control-budgets.md` when a lower-capability model needs numeric
     tripwires for search, failed hypotheses, verification, or review depth.
   - `references/long-work-scaffolding.md` when durable task, todo, or checkpoint
     files are needed.
   - `references/capability-calibration.md` when tool gaps, uncertainty, or
     model limits affect the work.
   - `references/evidence-and-claims.md` whenever claims must be tied to real
     observations.
   - `references/context-management.md` when the task spans many files, sessions,
     or tool calls.
   - `references/tool-use-discipline.md` when mapping generic protocol rules to
     concrete tools.
4. Read one task module when it applies:
   - `references/bugfix-workflow.md` for defects, regressions, errors, or failing tests.
   - `references/feature-workflow.md` for new or changed behavior.
   - `references/refactor-workflow.md` for behavior-preserving structure changes.
   - `references/repository-analysis.md` for analysis-only repository assessment,
     migration review, architecture discovery, or instruction-pack critique.
5. Read `references/embedded-porting.md` for firmware, cross-compilers, boards,
   flash/debug tools, hardware logs, RTOS, drivers, or lab constraints.
6. Read `references/self-review.md` before finalizing meaningful edits.
7. Read `references/agent-portability.md` when adapting this protocol to a
   different agent, IDE, automation harness, or instruction file.
8. Read `references/adoption-and-migration.md` when deciding whether to integrate
   this protocol into an existing agent architecture.
9. Read `references/instruction-pack-evaluation.md` when measuring lower-model
   uplift or comparing against a stronger model.
   Read `references/evaluation-tasks.md` for starter task scenarios.
10. Read `references/anti-patterns.md` when reviewing a failed run or tightening
   operating rules.
11. Read `references/source-notes.md` only when provenance or public reference
   rationale matters.

## Operating Defaults

- Convert the request into a concrete completion condition before editing.
- Maintain an explicit task ledger for multi-step work: goal, assumptions,
  evidence, current phase, unresolved questions, next action, and stop condition.
- Inspect relevant files, call sites, tests, project rules, and command
  manifests before changing files.
- Prefer existing project patterns over personal style.
- Keep changes limited to what the request needs.
- Preserve uncommitted user work; do not revert unrelated changes.
- Reproduce defects before fixing when practical.
- Verify with real tests, builds, type checks, linters, device runs, or minimal
  executable probes.
- Run a pre-final self-review that checks the actual diff, verification evidence,
  scope boundaries, and final report claims.
- Report exact verification results. Say what was not run and why.
- Ask before destructive actions, external side effects, production changes, or
  irreversible device operations.

## Environment Adapter

Before applying a rule, map it to the current environment:

- Search: use the fastest reliable project search available.
- Editing: use the safest available edit mechanism, preferably patch-based.
- Execution: use the project's documented commands and the active shell.
- UI or hardware verification: use available browser, simulator, emulator,
  board, debugger, log, or screenshot tools.
- Progress updates: use the environment's user-visible status channel.
- Final report: use the environment's normal final response channel.

If a capability is unavailable, choose the closest safe substitute only when it
can still produce relevant evidence. Otherwise narrow the task, ask for help, or
report the work as unverified.

Use `adapters/` when a concrete runtime mapping or lower-model form is needed:

- `adapters/runtime-capabilities.yaml` for capability, approval, and logging maps.
- `adapters/task-mode-selector.md` for tiny, standard, high-risk, and eval modes.
- `adapters/lower-model-run-prompt.md` for lower-model execution scaffolding.
- `adapters/gemini-worker-contracts.md` for schema-bound Gemini-style worker
  roles under a stronger control plane.
- `adapters/runtime-enforcement-bridge.md` for converting markdown operating
  rules into enforceable broker, allowlist, sandbox, logging, and gate checks.
- `adapters/maintenance-private-layer.md` for separating public playbooks from
  enterprise-local paths, policies, schedulers, evals, and source-maintenance
  cadence.
- `adapters/recovery-automation-possibility.md` for evidence-bounded discussion
  of optional recovery automation that must be enabled, if at all, only by the
  private enterprise layer.
- `adapters/task-ledger.txt`, `adapters/pre-edit-checklist.md`,
  `adapters/evidence-record.md`, and `adapters/pre-final-review.md` for
  external working-memory forms.
- `adapters/codex.md` and `adapters/generic-embedded-agent.md` as
  non-normative mapping examples.
