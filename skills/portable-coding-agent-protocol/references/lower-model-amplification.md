# Lower-Model Amplification

Use this module when a lower-cost, smaller, older, or less reliable agent must
handle work that would normally benefit from a stronger long-horizon model.

## Principle

Do not pretend the weaker model became stronger. The goal is narrower: make a
lower or mid-capability model reproduce selected frontier-agent operating
behaviors more often, especially persistence, scope control, evidence-grounded
claims, and verification before final output.

Move part of the missing executive function into the procedure:

- Keep task state outside short-term attention.
- Make phase gates explicit.
- Convert uncertainty into inspect/test/ask decisions.
- Require evidence before claims.
- Run a separate critic or verifier pass before final output.
- Stop or narrow scope when the evidence path is not available.

This is a correction device for lower and mid models, not a capability upgrade.
It can reduce predictable process failures, but it cannot supply missing domain
knowledge, tool access, long-context reliability, or judgment.

## Amplification Loop

Run this loop for meaningful coding work:

1. Frame: restate the observable goal, non-goals, risks, and completion evidence.
2. Recon: inspect only the files, commands, tests, and project rules needed for
   the next decision.
3. Plan: choose the smallest reversible step and name the expected evidence.
4. Act: make the scoped edit or run the diagnostic.
5. Verify: compare observed evidence with the expected evidence.
6. Critic: ask what would prove this wrong, what changed outside scope, and what
   is still unverified.
7. Continue or stop: proceed only if the next step is justified by evidence.

For small tasks, compress the loop into a few sentences. For long tasks, keep a
task ledger.

For lower models, make the loop visible in the working artifact or final report
when the task is medium or larger. Hidden discipline is less reliable than
external state.

## Task Ledger

Maintain a lightweight ledger during multi-step work:

```text
Goal:
Done when:
Non-goals:
Assumptions:
Evidence observed:
Current phase:
Open questions:
Next action:
Stop condition:
```

Do not expose the full ledger to the user unless useful. Use it to prevent goal
drift and false completion.

## When To Ask

Ask only when the answer changes the implementation, risk, or permission state.
Otherwise pick the safest reversible default, state the assumption, and proceed.

Ask before:

- Destructive or external side effects.
- Production, shared infrastructure, or device-affecting actions.
- Ambiguous requirements that would produce materially different behavior.
- Missing access that makes verification impossible for a high-risk claim.

## When To Use A Critic

Use a separate verifier, subagent, reviewer, or internal critic pass when:

- The task spans multiple files or phases.
- A bug root cause is uncertain.
- The first fix failed.
- Hardware, production, security, or data integrity is involved.
- The final report would otherwise rely on static reasoning only.

If no separate agent exists, run a role-separated self-review using
`self-review.md`.

## Output Claim

The best honest claim is:

> This protocol can improve disciplined agent behavior and reduce predictable
> failures. It does not guarantee frontier-model capability.

Do not claim "Fable5-grade performance" unless a local evaluation defines that
term operationally and shows the target model meeting it. Prefer:

> On these local tasks, the lower model showed improved Fable-inspired operating
> behavior under this protocol.

## Scale By Model Tier

- Lower model: use explicit ledgers, task-size classification, completion gates,
  numeric tripwires, and a critic pass for non-trivial work.
- Mid model: keep the same gates but compress tiny and small tasks.
- Frontier model: compress routine checklists, but still preserve approval,
  evidence, scope, and final-claim rules.
