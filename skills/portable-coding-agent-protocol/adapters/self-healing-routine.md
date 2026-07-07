# Self-Healing Routine Adapter

Use this adapter for scheduled or event-triggered automation that may ask a
Gemini worker to diagnose or propose recovery.

## Boundary

Self-healing means "diagnose, attempt a bounded local recovery, record evidence,
and produce a reviewable result." It does not mean unattended production
mutation.

## Routine Manifest

```yaml
routine_id: "<name>"
owner: "<team-or-person>"
repo_allowlist:
  - "<repo-path-or-slug>"
command_allowlist:
  - "git status --short"
  - "<project test command>"
write_allowlist:
  - "docs/"
  - "tests/"
max_attempts:
  diagnostic: 3
  code_change: 2
worker_limits:
  max_tool_calls: 8
  max_same_error_retries: 1
  max_changed_files: 3
  max_output_tokens: 1200
  prose_allowed: false
  completion_claim_requires_observed_evidence: true
network_policy: "disabled | approved_endpoints_only"
secret_policy: "never_read_or_emit"
branch_policy: "temporary_branch_or_worktree"
telemetry_policy: "metadata_only_no_prompt_content"
input_trust_policy: "trusted_only | maintainer_promoted | untrusted_read_only"
approval_required_for:
  - production
  - external_posting
  - destructive_command
  - credentials
  - hardware_state
```

## Loop

1. Load the routine manifest.
2. Confirm the repo and command are allowed.
3. Capture baseline status and environment summary.
4. Run the scheduled command.
5. If it passes, log the success and stop.
6. If it fails, ask the local scout to extract relevant logs, files, and recent
   changes.
7. Redact or block sensitive content before any cloud call.
8. Ask Gemini for a schema-bound diagnosis and recovery plan.
9. Reject the worker output if it contains prose outside the schema, exceeds
   worker limits, repeats the same tool error, or claims completion without
   observed evidence.
10. Validate the plan against the manifest.
11. Apply only safe mechanical recovery in a branch or worktree.
12. Run exact verification.
13. Record the result and update local failure memory.
14. Escalate after repeated failure, forbidden action, or missing evidence.

## Failure Memory Entry

```json
{
  "routine_id": "string",
  "timestamp": "ISO-8601",
  "trigger": "schedule|event|manual",
  "symptom": "string",
  "observed_evidence": [
    {"kind": "command", "value": "pytest tests/foo.py", "exit_code": 1}
  ],
  "diagnosis": "string",
  "actions_attempted": ["string"],
  "verification": [
    {"command": "string", "exit_code": 0, "summary": "string"}
  ],
  "outcome": "recovered|branch_created|escalated|no_action",
  "next_human_action": "string"
}
```

## Stop Rules

Stop immediately when:

- The repo is not allowlisted.
- The command or write path is not allowlisted.
- The worker asks for secrets or external posting.
- The input is untrusted and the routine would require write access.
- The same verification failure appears twice.
- The fix would require production, hardware, credentials, or destructive
  changes.
- The model cannot produce a plan that validates against the schema.
- The worker emits markdown, preamble, apology text, or other prose when the
  manifest requires schema-only output.
- The worker exceeds the allowed tool-call, output-token, retry, or
  changed-file budget.
- The worker repeats the same tool error once instead of returning an
  unresolved state.
- The worker claims success without observed command output, exit codes, diff
  inspection, or equivalent verification evidence.
- The proposed patch touches paths outside the write allowlist or declared
  patch intent.

## CI Automation Controls

For GitHub Actions or similar CI:

- Treat issues, pull requests from forks, comments, and generated diffs as
  untrusted by default.
- Use maintainer-triggered workflows for untrusted inputs.
- Grant the CI token the smallest permission set possible.
- Use keyless identity where available.
- Pin action versions.
- Require branch protection, CODEOWNERS or equivalent ownership, status checks,
  and human approval before merge.
- Limit untrusted runs to read-only tools unless explicitly promoted.

## Review Artifact

Every non-read-only run should produce:

```text
Routine:
Trigger:
Branch/worktree:
Baseline status:
Failure observed:
Worker diagnosis:
Changes made:
Verification:
Unresolved:
Escalation:
```
