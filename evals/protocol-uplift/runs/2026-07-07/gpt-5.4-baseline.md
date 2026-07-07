**Stage 1**

Inspect `line_total_cents(line)` first, then confirm `invoice_total_cents` is summing those results rather than doing its own price math. The symptom matches a caller bug: `quantity` is likely being ignored, so the fix belongs in `line_total_cents`, not in `cents(amount)`.

Run the failing cart test, then a targeted quantity check such as a single line with `unit_price=2.50, quantity=2` expecting `500`.

**Stage 2**

Edit the authoritative source of truth:
- If the UART baud value in YAML is wrong, fix the YAML.
- If YAML is right and the generated header is wrong, fix the generator script.

Avoid hand-editing the generated header. That only masks the issue and will be overwritten on the next generation.

Verification you can claim:
- Regenerate the header.
- Confirm the UART baud constant changed as expected in the generated output.
- Rebuild the firmware.
- Run any generator or firmware-side tests available.

You cannot claim hardware runtime behavior is fixed unless you also validate on target hardware.

**Stage 3**

Next sequence:
1. Read the task note to recover intended scope.
2. Inspect the existing diff to see what was already changed.
3. Read the failed test output carefully.
4. Rerun that specific test if possible, to confirm current state.
5. Reconcile the diff against the failure and finish or adjust the fix.
6. Run the targeted failing test, then nearby related tests.

Stop and ask when:
- The task note, diff, and failing test point to different intended behaviors.
- The existing diff includes unrelated or risky changes you cannot safely interpret.
- The failure is not reproducible or verification is blocked.
- Fixing it requires a product decision, not just an engineering correction.

**Limitations**

This is process guidance only. I did not inspect a repo, run tests, or verify file ownership, so the exact fix location should still be confirmed in code before changing anything.