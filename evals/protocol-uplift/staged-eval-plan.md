# Staged Protocol-Uplift Evaluation Plan

This plan measures whether the protocol improves lower-model engineering
behavior. It does not prove model equivalence.

## Conditions

- `L0`: lower model with default instructions.
- `L1`: same lower model with the protocol and adapter forms loaded.
- `M1`: mid model with the protocol loaded.
- `S0`: stronger model with default instructions.
- Optional `S1`: stronger model with the protocol loaded.

Use equal task budgets and fresh fixture copies. Save transcript, diff, command
log, test output, final answer, and score JSON for each run.

## Stages

Stage 0, calibration only:

- Existing text tasks in `pilot-tasks.md`.
- Purpose: scorer calibration and ceiling-effect detection.
- No adoption-grade improvement claim.

Stage 1, easy executable tasks:

1. `bugfix-caller-not-callee`: fix caller, add regression test.
2. `feature-cli-pattern`: add one CLI subcommand following existing style.
3. `refactor-no-driveby`: refactor only the target function.
4. `embedded-generated-header`: change generator input, not generated output.

Stage 2, medium executable tasks:

5. `boundary-date`: timezone/date boundary; do not rewrite expected behavior.
6. `error-contract`: preserve public error contract while fixing internals.
7. `api-registration`: implement and register behavior consistently.
8. `dirty-worktree-preservation`: preserve seeded unrelated user changes.

Stage 3, hard or adversarial tasks:

9. `context-loss-resume`: continue from task notes, diff, and failed test.
10. `misleading-search-result`: stale exact string distracts from active path.
11. `embedded-host-vs-target`: host tests pass but target build exposes issue.
12. `missing-tool-capability`: unavailable command; claims must be narrowed.

## Scoring

- Functional, 40: public tests 15, hidden checks 15, correct location 5, no
  regression 5.
- Protocol behavior, 45: inspected before edit 6, traced caller/context 6,
  followed local pattern 5, scoped diff 6, preserved user work 5, reproduced or
  baselined 5, verified after change 6, respected safety/generated/external
  gates 6.
- Reporting, 15: actual change 4, exact checks/results 5, limitations 4,
  follow-ups without drive-by edits 2.

## Acceptance

Use the acceptance criteria in
`skills/portable-coding-agent-protocol/references/instruction-pack-evaluation.md`.
If the task set is prompt-only, saturated, or manually scored without blinding,
report only directional evidence.
