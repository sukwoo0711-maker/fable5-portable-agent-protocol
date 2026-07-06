# Refactor Workflow

Use this module for behavior-preserving cleanup, structure changes, extraction,
renaming, or file movement.

## 1. Establish A Baseline

Before refactoring, run the narrowest meaningful test or check for the target
area. If tests do not exist, create a characterization test when practical or
record the current observable behavior.

## 2. Keep Behavior Fixed

Do not change outputs, ordering, side effects, error behavior, persistence,
timing contracts, or public APIs unless the user explicitly asks for that
behavior change.

If a behavior appears wrong, report it as a finding instead of silently fixing
it during the refactor.

## 3. Change One Kind Of Structure At A Time

Prefer separate steps for:

- Rename.
- Move.
- Extract helper.
- Split file.
- Simplify control flow.

Avoid combining movement, renaming, formatting, and logic edits in the same
diff unless the project tooling makes separation impossible.

## 4. Prove Equivalence

Run the same check after the refactor that you ran before it. Report both the
baseline and final result when useful.

If verification is unavailable, say so and keep the refactor smaller.
