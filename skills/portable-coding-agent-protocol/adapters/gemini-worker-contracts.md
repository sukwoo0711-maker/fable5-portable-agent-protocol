# Gemini Worker Contracts

Use this adapter when Gemini or another lower-cost cloud model is used as a
worker under a stronger control plane.

## Role Rules

- The control plane chooses the worker role.
- Gemini receives one narrow work order.
- Gemini output must be structured and machine-validated.
- Gemini may propose, summarize, classify, or generate candidates.
- Gemini must not declare final completion, production safety, security
  approval, or test success.
- The harness owns schema validation, command execution, diff inspection,
  logging, and escalation.
- Privacy and retention controls are enforced before the work order is sent.
  Confidential data must be redacted, summarized locally, or blocked.

## Worker Roles

| Role | Allowed Actions | Required Output |
| --- | --- | --- |
| `dispatcher` | Decompose into work orders and route suggestions. | `work_orders[]`, risk, expected evidence. |
| `context_compressor` | Compress provided scout results. | Evidence packet with paths, lines, claims, uncertainty. |
| `test_planner` | Propose tests and commands. | Test intent, target files, verification commands. |
| `patch_candidate_generator` | Propose small patch intent or patch candidate where the runtime allows it. | Changed paths, rationale, expected verification. |
| `diff_claim_extractor` | Read a diff and extract claims to verify. | Claims, evidence requirements, unresolved risks. |

## Shared Input Schema

```json
{
  "task_id": "string",
  "role": "dispatcher|context_compressor|test_planner|patch_candidate_generator|diff_claim_extractor",
  "goal": "string",
  "task_mode": "tiny|standard|high_risk|eval",
  "privacy_level": "public|internal|confidential|secret",
  "allowed_actions": ["string"],
  "forbidden_actions": ["string"],
  "inputs": [
    {
      "kind": "user_request|context_packet|diff|log|file_excerpt|policy",
      "ref": "string",
      "content": "string"
    }
  ],
  "done_when": ["string"],
  "retry_budget": 0,
  "escalate_if": ["string"]
}
```

## Shared Output Schema

```json
{
  "task_id": "string",
  "role": "string",
  "status": "proposed|blocked|needs_escalation",
  "actions_taken": ["string"],
  "files_referenced": [
    {
      "path": "string",
      "lines": "string",
      "why": "string"
    }
  ],
  "proposed_changes": [
    {
      "path": "string",
      "intent": "string"
    }
  ],
  "expected_verification": ["string"],
  "claims": [
    {
      "claim": "string",
      "evidence": {
        "path": "string",
        "line": 0,
        "command": "string",
        "observed": "string"
      }
    }
  ],
  "unresolved": ["string"],
  "escalation_reason": "string"
}
```

## Prompt Wrapper

```text
You are a contract worker, not the final decision maker.

Return only JSON matching the provided schema.
Do not include prose outside JSON. No markdown. No preamble. No apology.
Do not claim tests, builds, deployments, or scans passed unless an observed
result was included in the input.
Do not request or expose secrets.
Do not expand scope beyond the work order.
If evidence is missing, set status to "needs_escalation" or add an item to
"unresolved".
Use tools only when required by allowed_actions.
Stop after the first repeated tool error and set status to "needs_escalation".
```

## Thinking Budget Defaults

| Role | Default Budget |
| --- | --- |
| `dispatcher` | medium |
| `context_compressor` | low |
| `test_planner` | medium |
| `patch_candidate_generator` | medium |
| `diff_claim_extractor` | low |
| high-risk exception review | escalate instead of raising Gemini budget |

Use provider-specific thinking controls in the runtime adapter. Do not encode
provider-specific parameter names in the core protocol.

For Gemini 3.5 Flash, map these defaults to `thinking_level` when using the
Interactions API. For older Gemini APIs, map to the closest supported thinking
budget control.

If a worker overuses tools or loops, lower the role's thinking setting before
adding more prompt text. If a worker under-reasons, escalate the task rather than
giving a broad worker more autonomy.

## Failure Suppression Controls

These controls are mandatory for Gemini-style workers:

```yaml
gemini_failure_suppression:
  output:
    response_schema_required: true
    prose_allowed: false
    max_output_tokens: 1200
  loop_control:
    max_tool_calls: 8
    max_same_error_retries: 1
    wall_clock_timeout_seconds: 300
  edit_control:
    patch_intent_required_before_edit: true
    max_changed_files: 3
    write_roots_required: true
  tool_control:
    allowed_actions_required: true
    deny_unlisted_tools: true
    deny_untrusted_input_writes: true
  reporting:
    final_completion_claim_allowed: false
    unresolved_required_for_missing_evidence: true
```

## Rejection Reasons

The harness should reject and retry or escalate with one of these reasons:

- `json_parse_failed`
- `prose_detected`
- `schema_missing_required_field`
- `claim_without_evidence`
- `forbidden_action_requested`
- `unlisted_tool_requested`
- `tool_loop_detected`
- `same_error_repeated`
- `diff_scope_exceeded`
- `private_data_release_blocked`
- `verification_missing`

## Privacy And Retention Controls

The runtime adapter should support:

```yaml
retention:
  store_false_required: true
  disallow_grounding_for_confidential_data: true
  disallow_file_api_for_confidential_data: true
  disallow_explicit_cache_for_confidential_data: true
  allow_implicit_cache_if_policy_allows: true
  prompt_logging: false
```

If a work order contains private code, secrets, credentials, customer data, or
proprietary incident details, the broker must either redact it locally or reject
the request before it reaches Gemini.

## Validation Gates

Reject Gemini output when:

- JSON parsing fails.
- Required fields are missing.
- Prose, markdown framing, or apology text appears outside the JSON object.
- A claim lacks evidence or is not listed as unresolved.
- The worker proposes forbidden actions.
- The worker changes or references files outside the work order without a reason.
- The same failure repeats after one retry for code changes.
- Tool calls exceed the role budget.
- Proposed changed files exceed the work order or adapter limit.

## Escalation Output

When rejected, the harness should produce a short structured rejection:

```json
{
  "task_id": "T-014",
  "rejected": true,
  "reason": "claim_without_evidence",
  "retry_allowed": true,
  "next_instruction": "Return claims only with file/line evidence or list as unresolved."
}
```
