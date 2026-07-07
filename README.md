# Fable5 Portable Agent Protocol

This repository distills Fable5-inspired coding-agent operating patterns into a
portable, harness-neutral instruction pack. It is meant to help lower-capability
tool-using agents behave more like disciplined long-horizon engineering agents.

It cannot give weaker models the same planning depth, judgment, or latent
knowledge as a frontier model. It can externalize some control structure that
stronger models often carry internally: task state, phase gates, uncertainty
calibration, evidence discipline, verifier passes, scoped autonomy, and stop
rules.

## Structure

- `AGENTS.md` is the short always-loaded entry point for compatible agents.
- `skills/portable-coding-agent-protocol/SKILL.md` is the installable skill entry.
- `skills/portable-coding-agent-protocol/references/` holds lazy-loaded modules.
- `skills/portable-coding-agent-protocol/adapters/` holds concrete runtime
  mapping templates and lower-model forms.
- `evals/protocol-uplift/` holds local evaluation plans, rubrics, and pilot
  results.
- `ADOPTION.md` helps teams decide whether and how to migrate an existing agent
  architecture.

Read only the modules needed for the current task. This avoids spending context
on bugfix, feature, refactor, embedded, evaluation, or adoption details when
they are not relevant.

## Adopt The Protocol

This repository defines an agent operating protocol, not an agent runtime. It
does not require Codex, Claude, Fable, MCP, a specific shell, a specific
sandbox, or a specific tool API. Product-specific bindings belong in adapters.

Normative requirements are behavior-level:

- Classify task size and scale the process.
- Maintain task state for multi-step work.
- Inspect before editing.
- Preserve local work.
- Keep diffs scoped.
- Verify with evidence.
- Disclose missing checks.
- Complete a visible or internal completion gate before final claims.
- Run a pre-final self-review.
- Ask before destructive, external, production, or device-affecting actions.

Example invocation for environments that support skills:

```text
Use $portable-coding-agent-protocol to handle this coding task with scoped edits
and explicit verification.
```

## What This Does Not Promise

- It does not make a weaker model equivalent to a stronger model.
- It does not replace sandboxing, approvals, secret handling, code review, CI,
  hardware safety, or production-change controls.
- It does not prove broad benchmark improvement without local measurement.
- It does not require copying leaked prompts or provider-specific system text.

The honest claim is narrower: on suitable tasks, the protocol should reduce
predictable agent failure modes and may close part of the process-quality gap to
stronger models. Measure that locally before broad rollout.

In other words, this repo is aligned with a "make lower models behave more like
disciplined long-horizon coding agents" goal only when adapters and evaluation
are used. The Markdown alone is not a safety mechanism or proof of equivalence.

## Evaluation

Use `skills/portable-coding-agent-protocol/references/instruction-pack-evaluation.md`
to run an A/B/C comparison:

- `L0`: lower-capability agent with normal instructions.
- `L1`: same lower-capability agent with this protocol.
- `S0`: stronger model with normal instructions.

Report protocol uplift, success uplift, and gap closure. Keep the claim local
unless you run broader benchmarks.

## Design Notes

This pack deliberately avoids hard dependencies on specific harness concepts
such as tool names, channels, sandbox names, or model identities. Put those
constraints in an environment adapter, not in the core protocol.
