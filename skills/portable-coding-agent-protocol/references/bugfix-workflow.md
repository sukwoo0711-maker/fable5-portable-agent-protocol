# Bugfix Workflow

Use this module for defects, regressions, errors, failing tests, bad logs, or
incorrect runtime behavior.

## 1. Reproduce First

Before fixing, observe the failure when practical:

- Existing failing test.
- New minimal failing test.
- Reproduction script.
- Local command.
- Simulator, emulator, board run, UI interaction, or log capture.

If reproduction is not practical, say why and base the fix on code-path evidence.

## 2. Read Failure Evidence

Read the first meaningful error, not only the last line:

- Stack trace frame where project code first appears.
- Expected vs actual output.
- Input data shape and boundary values.
- Recent changes in the affected area.
- Environment differences such as OS, toolchain, target, flags, or config.

## 3. Narrow Cause Candidates

Use observations that distinguish one cause from another:

- Add temporary logs or probes only when they are removed before completion.
- Compare known-good and failing inputs.
- Separate data issues from code issues.
- Bisect or inspect recent history when timing is unclear.

If the same hypothesis fails twice, change the diagnostic approach.

## 4. Fix The Cause, Not Only The Symptom

Before adding defensive code, identify where the invalid state is created. Fix
the creation point when possible.

Symptom blocking is acceptable only when:

- The cause is outside the current scope.
- The defensive behavior is part of the expected contract.
- Time or risk requires a local guard.

When using a symptom-level guard, state that explicitly in the report.

## 5. Lock The Regression

Add or update a test for the reproduced failure when the project has a test
practice. If tests do not exist, record the manual reproduction and verification
steps in the final report.

Do not rewrite expected test values to match the implementation unless the
specification or user request confirms the behavior changed.
