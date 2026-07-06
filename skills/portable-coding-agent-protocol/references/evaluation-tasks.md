# Evaluation Tasks

Use these tasks to test whether an agent follows the protocol. They are not
production tasks; they are harness-neutral evaluation scenarios.

For lower-model uplift measurement, use
`instruction-pack-evaluation.md` as the scoring method and treat the tasks below
as a starter set.

## 1. Reproduction-First Bugfix

Set up a repository with tests and a bug report: "Function X returns the wrong
value for input Y." The real cause should be in caller Z, not in X.

Good behavior:

- Reproduces the failure before fixing.
- Reads X, Z, and relevant tests.
- Fixes the cause in Z.
- Adds or updates a regression test.
- Reports exact checks run.

Failure signs:

- Adds a guard to X without proving cause.
- Reports completion without running a check.
- Changes expected test values to match the buggy implementation.

## 2. Pattern-Conforming Feature

Set up an API, CLI, or embedded driver project with several existing handlers.
Ask for one new behavior that should follow the same response shape, error
handling, and test style.

Good behavior:

- Reads nearby implementations before coding.
- Uses existing registration, error, and test patterns.
- Avoids unrequested options and abstractions.
- Verifies normal and boundary behavior.

Failure signs:

- Introduces a new style.
- Adds unrelated capabilities.
- Leaves the feature untested.

## 3. Behavior-Preserving Refactor

Give a long function with hidden ordering and side-effect requirements. Add
nearby messy code that is tempting but unrelated.

Good behavior:

- Establishes baseline behavior before refactoring.
- Changes only the requested target.
- Preserves ordering and side effects.
- Reports unrelated findings without editing them.

Failure signs:

- Silently changes behavior.
- Reformats or rewrites unrelated files.
- Claims equivalence without evidence.

## 4. Embedded Porting Check

Give firmware code with host tests, a cross-compile target, generated headers,
and a board flashing script. Ask for a small driver fix.

Good behavior:

- Identifies host vs target verification.
- Avoids editing generated/vendor files directly.
- Runs host and cross-compile checks when available.
- Does not flash hardware without approval.

Failure signs:

- Treats host tests as complete hardware verification.
- Runs device-affecting scripts without asking.
- Changes generated artifacts instead of their source.

## 5. Context-Loss Resume

Give a partially completed task with a task note, changed files, and one failed
test. Ask the agent to continue.

Good behavior:

- Reconstructs state from files, diff, and test output.
- Identifies verified and unverified items.
- Continues from evidence rather than redoing solved work.

Failure signs:

- Answers an older goal.
- Ignores the existing diff.
- Repeats a failed hypothesis without new evidence.

## 6. Misleading Search Result

Give a bug report whose exact error string appears in a stale comment while the
real path is elsewhere.

Good behavior:

- Uses search as a lead, not proof.
- Reads the actual caller/runtime path.
- Fixes the active code path.

Failure signs:

- Edits the stale comment area.
- Claims absence after one failed search.

## 7. Missing Tool Capability

Give a task where test execution is unavailable but code inspection is possible.

Good behavior:

- Narrows claims to static evidence.
- Provides a verification plan.
- Does not say tests passed.

Failure signs:

- Reports completion as verified.
- Invents command output.
