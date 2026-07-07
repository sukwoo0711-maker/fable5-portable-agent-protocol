# Runtime Enforcement Bridge

Use this adapter when Markdown instructions need to become observable runtime
controls. The goal is not to build a full platform on day one. The goal is to
turn the highest-risk prose rules into machine gates first.

## Enforcement Ladder

| Level | What Exists | What It Fixes | Still Missing |
| --- | --- | --- | --- |
| P0, Prompt Only | Instructions and checklists. | Shared language and expectations. | No hard stop. |
| P1, Audited | Trace logs, schema validation, diff/test capture. | False claims and hidden failures become visible. | A bad action may still run. |
| P2, Guarded | Allowlists, sandbox/worktree, output budgets, retry caps. | Most loops, broad edits, and risky tools are blocked. | Complex policy still needs review. |
| P3, Enforced | Broker, identity, approvals, gateway/proxy, CI policy. | Sensitive egress and privileged actions are controlled. | Human governance and maintenance remain required. |

Start at P1 for every worker and P2 for any writer. Use P3 for CI, production,
hardware, credentials, or private repositories.

## Minimal Gate Sequence

```text
classify input -> check policy -> redact/block -> build work order
-> call worker -> validate JSON -> validate claims -> validate proposed actions
-> run deterministic checks -> inspect diff -> completion gate -> final report
```

The model never decides whether a gate passed. The harness decides from observed
data.

## Policy Skeleton

```yaml
runtime_policy:
  default_mode: audited
  data_classes:
    public:
      cloud_worker: allowed
    internal:
      cloud_worker: approved_endpoint_only
    confidential:
      cloud_worker: redacted_packet_only
    secret:
      cloud_worker: blocked
  worker_limits:
    max_tool_calls: 8
    max_same_error_retries: 1
    max_code_attempts: 2
    max_changed_files: 3
    max_output_tokens: 1200
    prose_allowed: false
  tool_policy:
    shell_allowlist:
      - "git status --short"
      - "git diff --"
      - "<project test command>"
    denied_patterns:
      - "rm -rf"
      - "del /s"
      - "format"
      - "curl *|*sh"
      - "Invoke-Expression"
    write_roots:
      - "docs/"
      - "tests/"
    require_human_approval:
      - production
      - credentials
      - external_posting
      - destructive_command
      - hardware_state
  evidence_policy:
    final_claims_require_observed_evidence: true
    tests_passed_requires_exit_code_zero: true
    no_unrelated_changes_requires_diff_inspection: true
```

## Gate Artifacts

Each run should write:

```text
runs/<date>/<task-id>/input-classification.json
runs/<date>/<task-id>/work-order.json
runs/<date>/<task-id>/worker-output.json
runs/<date>/<task-id>/gate-result.json
runs/<date>/<task-id>/verification.txt
```

These files are local/private by default. Publish only synthetic examples.

## Gate Result Schema

```json
{
  "task_id": "string",
  "schema_valid": true,
  "policy_allowed": true,
  "prose_detected": false,
  "tool_call_count": 0,
  "changed_files": [],
  "denied_patterns": [],
  "evidence_failures": [],
  "verification": [
    {"command": "string", "exit_code": 0, "summary": "string"}
  ],
  "decision": "pass|retry|escalate|block",
  "reason": "string"
}
```

## Speed Controls

Not every task needs the full pipeline.

| Mode | Path | Use When |
| --- | --- | --- |
| `fast_read` | classify -> local read/search -> final | Read-only, low-risk explanation. |
| `fast_worker` | classify -> Gemini schema output -> final | Public or internal non-editing work. |
| `standard_edit` | full gate sequence | Small code/doc/test edits. |
| `high_risk` | full gate sequence plus human approval | Security, prod, credentials, hardware, destructive actions. |

The router should default to `fast_read` for tiny analysis tasks and only add
Gemini/scout/verifier stages when the task risk or evidence need justifies it.
