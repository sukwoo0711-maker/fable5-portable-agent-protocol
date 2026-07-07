# Staged Smoke Report, 2026-07-07

This run checks whether the revised protocol is aligned with the user's goal:
helping lower-capability models show more Fable5-like operating discipline.

Claim level: **directional only**. This is not a supported local-improvement
benchmark because the model tasks were prompt-level staged responses, not full
patch runs across executable fixtures.

## What Ran

Environment:

- Codex CLI `exec`
- read-only sandbox
- approval policy `never`
- workdir outside the repo to avoid accidental project-instruction loading

Models/conditions:

| Condition | Model | Protocol rules included | Output |
| --- | --- | --- | --- |
| lower baseline | `gpt-5.4-mini` | no | `gpt-5.4-mini-baseline.md` |
| lower protocol | `gpt-5.4-mini` | yes | `gpt-5.4-mini-protocol.md` |
| mid baseline | `gpt-5.4` | no | `gpt-5.4-baseline.md` |
| mid protocol | `gpt-5.4` | yes | `gpt-5.4-protocol.md` |
| stronger attempt | `gpt-5.5` / `gpt-5` | attempted | `gpt-5.5-attempt.md` |

Stages:

1. Easy: caller-not-helper cart bug.
2. Medium: generated embedded header and host-vs-target evidence.
3. Hard: context-loss resume from task note, diff, and failed test.

## Manual Scores

| Condition | Functional | Protocol | Reporting | Total |
| --- | ---: | ---: | ---: | ---: |
| `gpt-5.4-mini` baseline | 35 | 38 | 10 | 83 |
| `gpt-5.4-mini` protocol | 38 | 44 | 13 | 95 |
| `gpt-5.4` baseline | 39 | 42 | 11 | 92 |
| `gpt-5.4` protocol | 40 | 45 | 14 | 99 |

Observed directional effect:

- Lower model: +12 total, mostly from sharper source-of-truth placement,
  preserved-diff language, evidence limits, and completion gate.
- Mid model: +7 total, mostly from observable done, stricter claim limits, and
  completion gate.
- Stronger model: fresh staged run unavailable; historical pilot still contains
  a `gpt-5.5` text baseline but is not used as fresh staged evidence.

## Fixture Smoke

The new executable fixture `fixtures/bugfix-caller-not-callee` was reset and run.
The seed fails as expected:

```text
AssertionError: 600 != 850
```

`score_run.py` also returns a failing seed score, confirming the fixture can
detect the target failure. No model patch run was performed against the fixture
in this pass.

## Interpretation

The revised protocol is better aligned with the user's purpose than the previous
repo state because it no longer relies only on philosophy. It now adds:

- concrete adapter forms,
- task-size routing,
- visible completion gates,
- early-termination guard,
- diagnostic/fix mode boundary,
- numeric tripwires,
- source-evidence grading,
- executable eval fixture structure.

However, the result does not prove Fable5-grade performance. The honest claim is:

> In prompt-level staged smoke tests, protocol-loaded lower and mid models showed
> more explicit source-of-truth selection, evidence discipline, and completion
> gating than their baseline answers.

Supported local improvement still requires the staged executable evaluation in
`../../staged-eval-plan.md`.
