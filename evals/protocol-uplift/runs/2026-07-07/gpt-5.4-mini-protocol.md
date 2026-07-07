Observable done: the exact failing invoice/cart test reports `850` cents for the two lines, the firmware build consumes a regenerated header with the corrected UART baud constant, and the resumed bugfix's targeted test passes with the existing diff preserved.

- Stage 1: Inspect the cart test, `invoice_total_cents`, `line_total_cents`, and `cents(amount)`; fix `line_total_cents` in the caller so it applies quantity to the unit price before summing, and leave `cents()` alone; run the single failing invoice/cart test first.
- Stage 2: Edit the source YAML if it is the source of truth, or the generator script only if the bug is in generation logic; avoid hand-editing the generated register header or any vendor/generated artifact; the only safe verification claim is what you directly observe after rerunning generation and the exact firmware build, not host tests or hardware.
- Stage 3: Read the task note, existing diff, and failed test output; reproduce the same failure; inspect the narrow touched path; make the minimal fix on top of the preserved diff; rerun the exact failing test, then the smallest adjacent test slice; stop or ask if the note conflicts with the diff, the failure cannot be reproduced, the root cause is ambiguous, or continuing would overwrite work you did not author.

**Completion Gate**
I stop only when the targeted evidence passes and each claim is backed by the correct layer of observed evidence: host for host behavior, build for generated firmware artifacts, and hardware for on-device behavior.

**Limitations**
I did not edit files, browse, or execute tests in this response, so there is no new pass/fail evidence here.
