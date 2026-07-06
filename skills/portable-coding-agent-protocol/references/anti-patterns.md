# Anti-Patterns And Corrections

Use this module to review a failed run or tighten agent behavior.

| Anti-pattern | Correction |
| --- | --- |
| Editing a file from its name or a diff hunk only | Read the target code, surrounding function, and relevant call sites first. |
| Ignoring existing project patterns | Read nearby examples before adding new code. |
| Expanding scope because a related issue is visible | Leave unrelated findings in the report unless they block the task. |
| Reporting success without running checks | Report success only with verification evidence; otherwise say "not verified." |
| Hiding partial test failures | Name the failed check, failure reason, and whether it appears related. |
| Repeating the same failed fix | After two similar failures, change the diagnostic approach. |
| Updating tests to match buggy behavior | Change test expectations only when the requested or documented behavior changed. |
| Adding defensive guards without tracing cause | Find where invalid state is created; guard locally only with a stated reason. |
| Refactoring while fixing a bug | Separate behavior changes from structure changes unless inseparable. |
| Touching generated or vendor files directly | Change the source, generator config, wrapper, or patch process. |
| Assuming host checks prove embedded target behavior | State the evidence layer and run target checks when available. |
| Asking questions that do not change the next action | Make a reasonable assumption and proceed, then report it. |
| Doing external or destructive work without approval | Stop and ask before irreversible, public, production, or device-affecting actions. |
| Losing the original goal after exploration | Maintain a task ledger and re-check the latest user request before final response. |
| Treating search results as proof | Open/read the target and tie claims to file content, command output, or test evidence. |
| Continuing after repeated failed hypotheses | After two similar failures, change the diagnostic approach or narrow scope. |
| Claiming equivalence from static inspection alone | Run before/after checks or label the refactor as not behavior-verified. |
| Reporting intended edits instead of actual diffs | Inspect current diff/status before final response. |
| Letting a weaker model handle broad work without phase gates | Split the task into evidence-producing slices with stop conditions. |

## Completion Gate

Before final response, confirm:

- The diff contains only requested or necessary changes.
- Debug output, scratch files, and accidental formatting churn are removed.
- Verification has been run or the missing verification is explicitly disclosed.
- Any user work present before the task is preserved.
- The final response leads with the outcome, then evidence.
