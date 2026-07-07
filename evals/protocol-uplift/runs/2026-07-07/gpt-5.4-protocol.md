**Observable done**

Each stage is done when the narrow failing behavior is explained by inspected evidence, the fix is placed in the true source of behavior, and the most specific relevant verification passes. No broader claims.

**Stage 1**

Inspect the failing cart test first, then `invoice_total_cents`, then `line_total_cents(line)`, then `cents(amount)`. The symptom `600` vs `850` matches "sum unit prices in cents, ignore quantity," so I would fix the caller logic in `line_total_cents(line)` to apply `quantity` before converting/summing, not the shared `cents(amount)` helper.

Run the most specific check: the single failing cart test or the smallest test target covering `invoice_total_cents`/`line_total_cents`. I would only claim that targeted test passed if I observed it.

**Stage 2**

Edit the source YAML or the generator script, depending on which one is wrong after inspection. Do not edit the generated UART register header directly, and do not touch vendor/generated artifacts as the primary fix.

Verification I can claim:
- If I only inspected: "host tests already pass" remains host-only evidence.
- If I regenerate and rebuild: I can claim the firmware build result I actually observed.
- I cannot claim hardware UART behavior without hardware evidence.

**Stage 3**

Next sequence:
1. Read the task note to recover intent and scope.
2. Inspect the existing diff to preserve in-flight work and avoid overwriting user changes.
3. Read the failed test output to identify the current concrete break.
4. Inspect the touched target code, its caller/callee context, and the exact test involved.
5. Make the smallest source-of-truth fix consistent with the existing diff.
6. Run the most specific failing test first, then only expand verification if needed.

Stop and ask when:
- the existing diff conflicts with the task note or failed test,
- the failure points to multiple plausible source-of-truth fixes,
- the next step would require generated/vendor direct edits,
- or verification requires unavailable build/hardware context.

**Completion Gate**

Completed: I identified what to inspect first, where each fix belongs, what to avoid editing, what verification is valid to claim, and the stop/ask conditions.  
Limitations: I did not inspect a real repo, run tests, regenerate code, build firmware, or verify hardware, so no pass/build/hardware success is claimed.
