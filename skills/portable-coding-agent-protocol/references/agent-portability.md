# Agent Portability

Use this module when adapting the protocol to another agent, IDE, chat product,
automation harness, or instruction file.

## 1. Separate Protocol From Runtime

Keep reusable instructions about outcomes and behavior. Move runtime-specific
details into adapters.

Reusable protocol:

- Inspect before editing.
- Preserve user work.
- Prefer project patterns.
- Keep diffs scoped.
- Verify with evidence.
- Report failures honestly.
- Ask before destructive or external side effects.

Runtime adapter:

- Tool names and schemas.
- Shell type, OS, filesystem roots, and sandbox.
- Approval policy.
- Network and browser availability.
- Parallel tool or subagent rules.
- Message channels and final response format.
- Memory file policy.

## 2. Capability-Oriented Wording

Prefer neutral wording:

- "Use the fastest reliable project search available" instead of naming one tool.
- "Use a safe patch-based edit mechanism when available" instead of naming one editor.
- "Run the documented project check" instead of inventing a generic command.
- "Use the user-visible progress channel" instead of naming a chat channel.
- "Use a separate verifier when available" instead of requiring a specific
  subagent implementation.

Keep model names only in adapter notes or examples.

## 3. Portability Assumptions

The core protocol assumes the agent can:

- Inspect a workspace.
- Search files.
- Edit files.
- Run commands or request that checks be run.
- Communicate progress and final results.

Other capabilities are optional for portability, but not equal in effect.
Long-horizon work degrades sharply without reliable command execution,
persistent task state, and evidence capture. Disclose those gaps before
accepting broad tasks.

## 4. Capability Assumptions

For capability uplift, the agent or runtime should provide:

- Task state that survives long work or compaction.
- Reliable command output capture.
- Diff and status inspection.
- A way to run targeted checks.
- A way to perform reviewer or critic passes.
- Policy gates for destructive, external, production, or device-affecting work.

If these are missing, use the protocol for scoped analysis or advisory patches
instead of claiming full implementation.

## 5. Multi-Agent Guidance

Use parallel agents only for independent work:

- Public-source research while local drafting continues.
- Portability review while implementation continues.
- Verification or critique after an artifact exists.
- Separate code slices with disjoint write sets.

Do not delegate the immediate blocker if the main agent cannot proceed without
the result. Keep delegated tasks concrete and bounded.

## 6. Token-Efficient Layout

Use a three-layer structure:

1. Tiny always-loaded entry point.
2. Short skill or protocol entry with routing instructions.
3. Lazy-loaded reference modules by task type, domain, or environment.

Do not put every rule into one large instruction file. Long monoliths waste
context and encourage agents to follow irrelevant details.
