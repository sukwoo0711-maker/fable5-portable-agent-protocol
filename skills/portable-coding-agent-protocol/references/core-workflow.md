# Core Workflow

Use this module for every coding task.

## 0. Classify Task Size

Choose the smallest process profile that can still prevent false completion:

| Size | Examples | Required controls |
| --- | --- | --- |
| Tiny | One-line text, config, or comment change with no behavior claim | Define done, inspect target, check diff/status if VCS exists, disclose unverified. |
| Small | Single-file bugfix, narrow feature, local testable edit | Tiny controls plus caller/test context, targeted verification, completion gate. |
| Medium | Multi-file change, uncertain bug, generated files, public API, embedded host checks | Small controls plus task ledger, baseline or reproduction, failed-hypothesis tracking, self-review. |
| Large | Broad refactor, migration, resumed work, hardware/production/security impact | Medium controls plus checkpoint files, separate critic/verifier, explicit approval boundaries, staged verification. |

For lower-capability models, default one size higher when the task is ambiguous.
For frontier models, controls may be compressed, but evidence, approval, and
final-claim rules are never optional.

## 1. Define Done

Write the completion condition in observable terms:

- What user-visible behavior, test result, build result, file state, or artifact
  must exist when the task is complete?
- What is explicitly out of scope?
- What would require user approval before proceeding?

If the request is ambiguous, make the smallest reasonable assumption that keeps
the work reversible. Ask only when different interpretations would produce
materially different implementations or external side effects.

## 2. Maintain State

For multi-step work, keep a compact task ledger:

- Goal.
- Done when.
- Non-goals.
- Assumptions.
- Evidence observed.
- Current phase.
- Open questions.
- Next action.
- Stop condition.

Use the ledger to prevent goal drift. Update it after failed hypotheses,
meaningful edits, and verification results.

## 3. Inspect Before Editing

Before editing a file, read enough context to understand it:

- The target function, type, class, module, or configuration block.
- Its callers and direct dependencies.
- Nearby tests or fixtures.
- Project instructions such as AGENTS, CONTRIBUTING, editor config, build files,
  manifests, or CI workflow files.
- Current repository state and recent work when version control is available.

Do not edit from a filename, stack frame, or diff hunk alone.

## 4. Search Narrowly, Then Deepen

Start with exact strings from the request: error messages, public API names,
UI labels, function names, test names, filenames, or config keys.

If exact search fails, vary casing, naming style, and nearby domain words. Use
directory structure only after string search fails or points to multiple areas.

When a target function is found, trace definitions and call sites before
changing its signature or behavior.

Default search tripwire: try at least three meaningfully different search keys
before concluding that something is absent. If three searches disagree, inspect
the active call path rather than trusting search alone.

## 5. Learn Existing Patterns

Read two or three nearby examples before adding new code:

- Error handling and return shape.
- Logging and diagnostics.
- Dependency injection and configuration.
- File layout and naming.
- Test style and fixture setup.
- Export/import or public API conventions.

Use local patterns unless there is a concrete reason not to.

## 6. Choose The Smallest Responsible Change

Prefer changes in this order:

1. Change a condition, parameter, data mapping, or call site.
2. Change an existing function or module.
3. Add a helper in an existing module.
4. Add a new module only when the concept is genuinely new or repeated.

Add abstractions only when they remove real duplication or match an established
project boundary. Leave discovered but unrelated issues as notes.

## 7. Preserve User Work

Treat uncommitted or untracked files as user work unless you created them in the
current task. Do not revert, reformat, or move unrelated changes.

If user changes overlap the target file, read carefully and build on them. Ask
only if the overlap makes the requested task impossible or risky.

## 8. Verify With Evidence

Run the most specific useful check first, then broaden as time and risk require:

1. Direct test for the changed file or behavior.
2. Module or package tests.
3. Build, lint, type check, static analysis, or integration checks.
4. Full suite when practical and proportionate.

If no tests exist, run the changed path manually through a small script, command,
simulator, emulator, UI interaction, device log, or other observable check.

Evidence quality matters. Static inspection can support a hypothesis, but it is
not the same as a passing runtime check. Label static-only conclusions as
unverified when reporting.

Default verification tripwire: after two failed verification cycles with the
same failure shape, stop repeating edits and change the diagnostic approach.
Record the failed hypothesis before continuing.

## 9. Review Before Final

Before final response, inspect:

- Current diff and status.
- Verification output.
- Scope boundaries.
- Temporary logs, scratch files, and generated artifacts.
- Whether every final claim has evidence.

Downgrade or remove claims that lack evidence.

## 10. Completion Gate

Before any final response on a small or larger task, produce or internally
complete this gate:

```text
Completion Gate:
- Done condition met: yes/no/partial, with evidence.
- Diff/status inspected: yes/no/not applicable.
- Verification run: command or method plus result.
- Missing evidence disclosed: yes/no/not applicable.
- Scope audit: only requested changes, or named exception.
- Stop reason: complete, blocked by missing input, or explicitly diagnostic-only.
```

If any answer is `no`, the final report must either keep working, narrow the
claim, or name the blocker.

## 11. Early-Termination Guard

Before ending, check the last paragraph of the planned response. If it is a
plan, a question, a list of next steps, or a promise about reversible work that
follows from the request, do that work now. End only when the task is complete,
diagnostic-only by request, or blocked on input only the user can provide.

Do not end with "I can", "next I would", "let me know if", "shall I", or
equivalent non-blocking permission requests when the original request already
authorized the work.

## 12. Report Clearly

Final reports must include:

- What changed.
- What was verified, with command or method and result.
- What was not verified and why.
- Any risks, assumptions, or follow-up findings that were intentionally left out
  of the diff.

Never call work complete based only on intent. Completion requires either
verification evidence or an explicit "not verified" disclosure.
