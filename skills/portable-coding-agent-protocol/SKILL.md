---
name: portable-coding-agent-protocol
description: Harness-neutral coding-agent workflow for bug fixes, feature work, refactors, repository analysis, embedded development porting, and prompt or operating-guideline refinement. Use when an agent must inspect a codebase, make scoped edits, verify with real commands, preserve user work, or adapt Fable5-style long-running coding behavior to Codex, Claude, Opus, GPT, or other tool-using agents.
---

# Portable Coding Agent Protocol

## Core Rule

Act as a tool-using engineering agent, not as a model-specific persona. Achieve
the user's observable goal with the safest available local mechanisms. Do not
depend on a specific harness, channel, tool name, sandbox, memory feature, or
model identity.

## Load Order

1. Read `references/core-workflow.md` for every coding task.
2. Read one task module when it applies:
   - `references/bugfix-workflow.md` for defects, regressions, errors, or failing tests.
   - `references/feature-workflow.md` for new or changed behavior.
   - `references/refactor-workflow.md` for behavior-preserving structure changes.
3. Read `references/embedded-porting.md` for firmware, cross-compilers, boards,
   flash/debug tools, hardware logs, RTOS, drivers, or lab constraints.
4. Read `references/agent-portability.md` when adapting this protocol to a
   different agent, IDE, automation harness, or instruction file.
5. Read `references/anti-patterns.md` when reviewing a failed run or tightening
   operating rules.
6. Read `references/source-notes.md` only when provenance or public reference
   rationale matters.

## Operating Defaults

- Convert the request into a concrete completion condition before editing.
- Inspect relevant files, call sites, tests, project rules, and command
  manifests before changing files.
- Prefer existing project patterns over personal style.
- Keep changes limited to what the request needs.
- Preserve uncommitted user work; do not revert unrelated changes.
- Reproduce defects before fixing when practical.
- Verify with real tests, builds, type checks, linters, device runs, or minimal
  executable probes.
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

If a capability is unavailable, choose the closest safe substitute and disclose
the limitation.
