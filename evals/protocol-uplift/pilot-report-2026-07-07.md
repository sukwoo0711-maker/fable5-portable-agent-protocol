# Pilot Report: Protocol Uplift

Date: 2026-07-07  
Repository commit at test time: local working tree after lower-model
amplification patch, before commit  
Harness: Codex multi-agent local session  
Task file: `evals/protocol-uplift/pilot-tasks.md`  
Rubric: `evals/protocol-uplift/scoring-rubric.md`

## Purpose

Estimate whether applying the protocol improves a lower-capability agent on a
small local task set, and compare the result to a stronger-model baseline.

This is a pilot, not a benchmark-grade result.

## Conditions

| Condition | Model | Instructions |
| --- | --- | --- |
| L0 | `gpt-5.4-mini` | Read only the pilot tasks; no protocol. |
| L1 | `gpt-5.4-mini` | Use the protocol skill, then read the pilot tasks. |
| S0 | `gpt-5.5` | Read only the pilot tasks; no protocol. |

Each condition answered three text fixtures:

1. Bugfix caller not callee.
2. Embedded generated header.
3. Refactor no drive-by.

## Scores

Scores were assigned manually from the rubric. The tasks were intentionally
small, so all conditions performed well and ceiling effects were visible.

| Condition | Task A | Task B | Task C | Mean total | Success rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| L0 lower baseline | 94 | 96 | 95 | 95.0 | 100% |
| L1 lower + protocol | 96 | 97 | 96 | 96.3 | 100% |
| S0 stronger baseline | 98 | 99 | 98 | 98.3 | 100% |

## Uplift

```text
protocol_uplift = mean(L1) - mean(L0)
                = 96.3 - 95.0
                = +1.3 points

success_uplift = success_rate(L1) - success_rate(L0)
               = 100% - 100%
               = 0 percentage points

gap_closure_vs_stronger = (mean(L1) - mean(L0)) / (mean(S0) - mean(L0))
                        = 1.3 / 3.3
                        = 40%

L1_vs_S0 = 96.3 / 98.3
         = 98.0% of the stronger-model pilot score
```

## Observations

- L0 already identified the main traps in all three tasks. This limited the
  possible measured uplift.
- L1 was slightly more explicit about preserving semantics, generated-file
  boundaries, target evidence, and scope limits.
- S0 gave the most precise answers, especially around direct cents handling,
  generated output inspection, and hardware-evidence limitations.
- The protocol did not improve binary success rate on this easy pilot because
  all conditions succeeded.

## Local Conclusion

On this small local text-only pilot, the protocol improved the lower model by
about 1.3 points on a 100-point rubric and closed about 40% of the observed gap
to the stronger model. Because the task set was small and easy, this should be
read as directional evidence that the protocol improves disciplined process
behavior, not as proof that it makes a weaker model equivalent to a stronger
model.

## Limitations

- Text-only tasks do not measure actual patch application.
- No executable fixture repos were used.
- No repeated runs were performed.
- Manual scoring can introduce evaluator bias.
- The tasks were designed around protocol behaviors, so they may overestimate
  protocol-specific gains on real work.
- The lower baseline was already strong, causing a ceiling effect.

## Recommended Next Evaluation

Create executable fixtures for the 12 tasks in
`references/instruction-pack-evaluation.md`, then run:

```text
12 tasks x 3 conditions x 3 repeats = 108 runs
```

Use saved diffs, command logs, test outputs, final responses, and scorer JSON for
each run. Report only local uplift unless broader benchmarks are added.
