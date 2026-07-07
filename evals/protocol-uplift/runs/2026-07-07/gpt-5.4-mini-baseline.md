**Stage 1**
- Inspect `invoice_total_cents` first. The symptom `600` vs `850` matches summing raw unit prices (`2.50 + 3.50`) instead of line totals.
- Fix the caller in `invoice_total_cents` so it uses `line_total_cents(line)` or otherwise includes `quantity`. Do not change `cents(amount)` or `line_total_cents(line)` unless they are independently wrong.
- Run the failing cart/invoice unit test for that fixture, plus one nearby case with `quantity: 1` and one multi-line case.

**Stage 2**
- Edit the source of truth: the YAML if the baud rate is declared there, or the generator script/template if the YAML is correct and the mapping/rendering is wrong.
- Avoid hand-editing the generated header. Also avoid using passing host tests as proof that the firmware constant is correct.
- Verify by regenerating the header and rebuilding the firmware target. If possible, also check the generated header diff for the UART baud constant.

**Stage 3**
- Read the task note, inspect the existing diff, and map the failed test output to the changed code path before touching anything else.
- Apply the smallest fix that matches the failure, then rerun the specific failed test and any directly adjacent regression test.
- Stop when the original failure is gone and no new failure appears in the touched area.
- Ask when the note and diff conflict, the failure cannot be tied to the current change, or the context is insufficient to choose between competing fixes.

**Limitations**
- I did not inspect the actual workspace, so this is the generic coding-agent decision path rather than file-specific guidance or exact commands.