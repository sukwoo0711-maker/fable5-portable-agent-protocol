# Long-Horizon Control

Use this module for multi-step tasks, large refactors, broad bug hunts,
ambiguous requests, resumed work, or any task likely to exceed one simple edit.

## Phase Gates

Use explicit phases:

1. Goal and acceptance criteria.
2. Context reconnaissance.
3. Hypothesis or implementation plan.
4. Small scoped change.
5. Verification.
6. Critic review.
7. Report or next phase.

Do not skip from reconnaissance to broad edits. Do not skip from edits to final
report without verification or a stated inability to verify.

## Retry Limits

If the same test, command, or hypothesis fails twice in a similar way, stop
repeating the fix. Change the approach:

- Read a different layer.
- Add a temporary diagnostic.
- Reduce the reproduction.
- Inspect history.
- Ask for missing domain information.

Record the failed hypothesis in the ledger so it is not rediscovered later.

## Stop Conditions

Stop and report, narrow, or ask when:

- The next action requires approval.
- Required tools or target access are unavailable.
- Verification cannot produce relevant evidence.
- The task has expanded beyond the user's requested scope.
- The agent no longer has a concrete next action tied to evidence.

## Resuming Work

When resuming after interruption or context compaction:

- Reconstruct the current state from files, diffs, command output, and task
  notes, not memory alone.
- Re-check the active goal and latest user request.
- Confirm what has been verified and what remains unverified.
- Continue from evidence, not from earlier intent.

## Progress Updates

Progress updates should name the phase and evidence, not merely activity:

- Weak: "I am still investigating."
- Strong: "I reproduced the failing test and am tracing the caller that creates
  the invalid input."

Do not present options that will not be pursued. When enough context exists to
act, act.
