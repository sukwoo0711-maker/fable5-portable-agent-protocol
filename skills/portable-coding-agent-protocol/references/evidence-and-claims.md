# Evidence And Claims

Use this module whenever the agent must decide what it may safely claim.

## Evidence Levels

- Proof: a relevant test, build, type check, static check, device run, simulator
  run, user-visible interaction, or log directly covers the claim.
- Strong smoke evidence: a minimal executable path covers the changed behavior
  but not all regressions.
- Static evidence: code inspection supports the claim but runtime behavior was
  not executed.
- Assumption: chosen default without proof.
- Missing evidence: no relevant check was run or available.

Use the strongest true label. Do not upgrade evidence by wording.

## Claim Rules

- "Passed" requires a command or check result.
- "Fixed" requires reproduction evidence plus post-change success, or a clear
  statement that reproduction was unavailable.
- "Preserved behavior" requires before/after evidence or a stated limitation.
- "Works on hardware" requires hardware evidence, not host tests.
- "No unrelated changes" requires diff inspection.
- "Safe" requires policy and permission evidence, not just intent.

## Final Report Template

```text
Completion Gate:
- Done condition met:
- Diff/status inspected:
- Verification run:
- Missing evidence disclosed:
- Scope audit:
- Stop reason:

Outcome:
Changes:
Evidence:
Not verified:
Assumptions:
Risks or follow-ups:
```

Keep it short, but do not omit missing evidence.

The completion gate may be internal for tiny tasks. For small or larger tasks,
include it when the runtime, reviewer, or evaluation harness needs visible
evidence of disciplined completion.

## Forbidden Claim Patterns

- "Should work" without labeling it as unverified.
- "Tests pass" without test output.
- "Only touched X" without diff inspection.
- "Root cause was Y" when only a symptom was observed.
- "Equivalent refactor" without before/after behavior evidence.
