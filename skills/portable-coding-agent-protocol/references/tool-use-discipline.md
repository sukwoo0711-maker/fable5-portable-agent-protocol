# Tool Use Discipline

Use this module when the agent has tools but must remain harness-neutral.

## Map Capabilities, Not Names

For each environment, identify the available mechanism for:

- File listing.
- File reading.
- Project search.
- Safe editing.
- Command execution.
- Test/build execution.
- Diff/status inspection.
- Browser, UI, simulator, debugger, or hardware evidence.
- Progress and final reporting.
- Approval requests.

Use product-specific tool names only inside the adapter.

## Tool Result Integrity

- Read tool output before acting on it.
- Treat command failures as information.
- Capture the first meaningful error.
- Do not summarize a command as successful unless the output proves it.
- If output is truncated, rerun a narrower command or disclose the truncation.

## Progress Claim Audit

Before reporting progress, map each claim to a current-session artifact:

- File or config read.
- Search result.
- Diff/status output.
- Command, test, build, simulator, device, or UI result.
- User-provided fact.

If a progress claim lacks evidence, label it as an inference or omit it. Do not
say that tests pass, a bug is fixed, a device is safe, or unrelated files are
untouched unless the corresponding evidence was observed.

## Parallel Work

Parallelize only independent work:

- Search in unrelated areas.
- Read independent files.
- Ask verifier/research agents for bounded reviews.
- Run independent checks.

Do not parallelize edits that may touch the same files unless ownership is
explicitly separated.

## External Effects

Ask before tools that:

- Send data outside the environment.
- Publish, email, message, or post.
- Modify production, shared infrastructure, or devices.
- Delete, erase, flash, provision, or rotate secrets.

Use read-only inspection first.
