# Secure Enterprise AX Gemini Worker Playbook

This playbook is for a locked-down enterprise workstation where AI agents are
contracted through approved enterprise channels, local context is sensitive, and
Gemini is available as a lower-cost cloud worker. It assumes a stronger control
plane owns task framing, routing, verification, and final claims.

It is intentionally model-neutral where possible. Product names appear only as
adapter examples.

## Operating Claim

Use Gemini as a high-throughput worker, dispatcher, compressor, and verifier
assistant. Do not use it as the final authority for code correctness, security,
production readiness, or private-context release.

The practical pattern is:

```text
strong control plane -> local scout -> Gemini contract workers -> verifier
                   \-> stronger model for judgment, security, or repeated failure
```

The system is only as strong as its harness. Prompt text can guide behavior, but
runtime logs, schema validation, tests, diffs, approvals, and human review create
the real control boundary.

## Architecture

```mermaid
flowchart TD
    U["User request"] --> C["Control plane"]
    C --> R{"Router<br/>risk, privacy, cost, complexity"}
    C <--> SK["Skill registry<br/>runbooks, adapters, policies"]

    R -- "private/local recon" --> LS["Local LLM scout"]
    LS --> CP["Context packet<br/>paths, lines, claims, uncertainty"]

    R -- "cheap parallel work" --> GD["Gemini dispatcher"]
    CP --> GD
    GD --> GW1["Gemini worker<br/>test planner"]
    GD --> GW2["Gemini worker<br/>context compressor"]
    GD --> GW3["Gemini worker<br/>mechanical patch candidate"]

    R -- "security/design/final judgment" --> HM["Stronger model or human reviewer"]

    GW1 --> V["Harness verifier<br/>schema, tests, lint, build, diff"]
    GW2 --> V
    GW3 --> V
    HM --> V

    V --> G{"Completion gate"}
    G -- "pass" --> C
    G -- "retry budget remains" --> GD
    G -- "repeat failure/high risk" --> HM
    C --> OUT["Final answer or PR summary<br/>evidence-bound claims"]

    V --> T[("Trace store<br/>jsonl, spans, costs, failures")]
    C --> K[("Local knowledge<br/>runbooks, failure memory")]
```

## Gemini Role Map

| Role | Use Gemini For | Do Not Let Gemini Do |
| --- | --- | --- |
| Dispatcher | Split a task into narrow work orders with allowed tools and expected evidence. | Own final routing or security policy decisions. |
| Context compressor | Convert local scout output into file/path/line/evidence packets. | Upload raw private repository context without a release rule. |
| Test planner | Propose regression tests, smoke checks, and failure repro commands. | Claim tests passed without observed command output. |
| Patch candidate generator | Produce small, reversible patch intent for low-risk changes. | Edit broad architecture, secrets, auth, prod config, or generated/vendor files unsupervised. |
| Diff claim extractor | Extract claims implied by a diff and the evidence needed to support them. | Approve the diff. |
| Batch worker | Run bulk summarization, option generation, or low-risk artifact drafting. | Block an interactive workflow on 24-hour batch turnaround. |

## Routing Matrix

| Task Type | First Tier | Escalate When |
| --- | --- | --- |
| Local file discovery, logs, symbol search | Local scout | Scout cannot cite files/lines or repeats the same miss twice. |
| Context packet cleanup | Gemini compressor | Packet contains unsupported claims or raw private data. |
| Test ideas, docs, boilerplate, migration inventory | Gemini worker | Output fails schema validation or exceeds scope. |
| Small mechanical code candidate | Gemini worker plus harness | Test/build/diff evidence fails twice. |
| Architecture, security, data integrity, production, approvals | Stronger model or human | Always high-risk by default. |
| Final user report or public release claim | Control plane | Never delegated. |

## Enterprise Control Baseline

For a security-sensitive workstation, put a local enterprise broker between the
PC and any cloud model endpoint:

```text
agent UI -> local broker -> policy/redaction -> approved model endpoint
        -> local tool broker -> allowlisted tools -> sandbox/worktree
```

The broker should enforce:

- Data classification before any model call.
- `store: false` or equivalent zero-retention controls where the approved API
  supports them.
- No grounding, file upload, explicit cache, or batch use for confidential data
  unless the enterprise policy explicitly approves the retention profile.
- Prompt/content logging disabled for sensitive prompts; telemetry may record
  metadata, costs, spans, tool names, and hashes.
- Per-agent identity, least privilege, and separate credentials for automation.
- Egress control through an approved gateway or proxy.
- MCP/tool allowlists and per-tool input validation.
- A temporary branch/worktree for any write path.
- Human approval for destructive, external, production, credential, or hardware
  actions.

If deploying managed agents, prefer enterprise controls such as Agent Runtime,
Agent Gateway, Agent Identity, IAM, private connectivity, tracing, and Model
Armor-style prompt/response policy. If running locally, emulate those controls
with allowlists, sandboxing, central settings, trace logs, and review gates.

## Data Release Rules

| Data Class | Cloud Worker Rule | Allowed Form |
| --- | --- | --- |
| Public | Allowed through approved endpoint. | Raw or summarized. |
| Internal | Allowed only through approved enterprise endpoint and trace policy. | Minimal excerpts, no secrets. |
| Confidential | Local-first; cloud only after redaction and policy approval. | File names, symbol names, short snippets, hashes, error classes. |
| Secret | Never send to Gemini or any model worker. | Block and escalate. |

The local scout should prefer evidence packets over raw files. A useful packet
contains paths, line numbers, symbol names, command summaries, and uncertainty,
not entire source trees.

## Work Order Contract

Gemini receives one work order at a time:

```json
{
  "task_id": "T-014",
  "role": "test_planner",
  "goal": "Create regression coverage for the observed pricing bug.",
  "inputs": [
    {"kind": "context_packet", "ref": "runs/T-014/scout.json"}
  ],
  "allowed_actions": ["read_referenced_files", "propose_tests"],
  "forbidden_actions": [
    "edit_unreferenced_files",
    "claim_test_passed",
    "request_external_network",
    "touch_secrets_or_credentials"
  ],
  "done_when": [
    "Each proposed test maps to a cited behavior path.",
    "Each claim has file and line evidence or is listed as unresolved."
  ],
  "retry_budget": 1,
  "escalate_if": [
    "Required evidence is missing.",
    "The same schema or verification failure repeats.",
    "The task crosses security, production, or destructive boundaries."
  ]
}
```

Gemini responds only with a schema-bound result:

```json
{
  "task_id": "T-014",
  "status": "proposed",
  "actions_taken": [],
  "files_referenced": [
    {"path": "tests/test_cart.py", "lines": "12-48", "why": "pricing tests"}
  ],
  "proposed_changes": [
    {
      "path": "tests/test_cart.py",
      "intent": "Add combined coupon/member discount regression test."
    }
  ],
  "expected_verification": ["pytest tests/test_cart.py"],
  "claims": [
    {
      "claim": "Existing tests cover single discount paths only.",
      "evidence": {"path": "tests/test_cart.py", "line": 18}
    }
  ],
  "unresolved": []
}
```

## Self-Healing Automation

Use Gemini to assist scheduled automation, not to own unattended changes.

Recommended loop:

```mermaid
sequenceDiagram
    participant S as Scheduler
    participant H as Harness
    participant L as Local scout
    participant G as Gemini worker
    participant V as Verifier
    participant R as Reviewer

    S->>H: run approved routine
    H->>H: load policy, repo allowlist, budgets
    H->>L: gather logs, failing command, recent diff
    L-->>H: local context packet
    H->>G: classify failure and propose recovery
    G-->>H: schema-bound recovery plan
    H->>V: validate plan safety

    alt safe mechanical recovery
        H->>H: apply patch in branch/worktree
        H->>V: run exact verification
        V-->>H: pass/fail evidence
    else unsafe or unclear
        H->>R: ask for human review
    end

    H->>H: append failure memory
    H->>R: report branch, evidence, unresolved items
```

Mandatory guardrails:

- Use an allowlist of repositories, commands, directories, and output paths.
- Run in a temporary branch or worktree.
- Cap loop depth with a numeric `max_attempts`; default is 2 for code changes
  and 3 for command/environment diagnosis.
- Never auto-merge, auto-release, auto-post, or mutate production.
- Write a local failure memory entry only after observed evidence, not after a
  model guess.
- If a command fails the same way twice, stop and escalate.
- Treat issue bodies, PR text, fork code, web pages, tickets, and model output as
  untrusted input until a maintainer or policy promotes them.
- Keep full logs separate from concise model summaries so verbose tool output
  does not bury the useful state.

Good self-healing targets:

- Re-run flaky local checks with captured logs.
- Repair missing generated artifacts by re-running the documented generator.
- Update a local runbook when an environment setup step is discovered.
- Open a review branch with a small patch and exact test evidence.

Bad self-healing targets:

- Secret rotation, credential repair, firewall changes, production deploys,
  database migrations, hardware flashing, or broad dependency upgrades.

GitHub automation baseline:

- Require pull requests, approvals, stale-approval dismissal, and required
  status checks on protected branches.
- Use Workload Identity Federation or equivalent keyless auth instead of
  long-lived service account keys.
- Pin actions and dependencies.
- Keep token permissions minimal.
- Prefer maintainer-triggered workflows for untrusted pull requests or issues.
- Limit untrusted-input workflows to read-only tools such as list, read, and
  search.

## Lessons From Public Signals

| Signal | Source Type | Playbook Decision |
| --- | --- | --- |
| ADK supports specialized agents, workflow agents, hierarchy, sequential, parallel, and loop orchestration. | Official Google Cloud | Model the AX environment as a small specialist team, not one super-agent. |
| ADK codelabs use `LoopAgent` with `max_iterations` and `ParallelAgent` fan-out. | Official codelab | Every Gemini retry loop must have an explicit max iteration and exit condition. |
| Gemini API supports JSON-schema structured output for agentic workflows. | Official Gemini docs | Make schema validation a hard gate for every Gemini worker. |
| Gemini thinking controls allow lower thinking for simple tasks and budget control for cost. | Official Gemini docs | Set thinking budget by role instead of using one default. |
| Gemini context caching and batch jobs reduce repeated-context cost but batch is not interactive. | Official Gemini docs | Cache stable runbooks and use batch only for offline jobs. |
| Gemini CLI subagents isolate complex or high-volume tasks in separate context windows. | Official GitHub discussion | Prefer isolated worker contexts over one overloaded session. |
| Public Gemini CLI issue reports custom skills/subagents may not be chosen automatically. | GitHub issue, anecdotal but product-adjacent | The control plane should invoke skills explicitly; do not rely on model discovery. |
| Official GitHub Action guidance recommends WIF, branch protection, pinned actions, least privilege, and trusted/untrusted input separation. | Official Google GitHub docs | Treat repository automation as CI security work, not just prompt design. |
| Gemini enterprise guidance supports central settings, tool/MCP allowlists, sandboxing, proxy control, telemetry, and disabling YOLO mode. | Official Gemini CLI docs | Use central policy controls; prompts are not enough. |
| HN users report Gemini can be useful for large-codebase investigation and summary for a stronger reviewer. | Community anecdote | Use Gemini as scout/compressor or bulk investigator, then re-check with stronger control. |
| HN users report loops, repeated tool failures, over-editing, and rate-limit confusion. | Community anecdote | Add retry budgets, stuck detection, provider fallback, and final diff review. |
| Reddit examples route Gemini/Antigravity as executor while a stronger model handles design/verification. | Community anecdote | Adopt "frontier conductor, cheap executor, verifier gate" as the default shape. |
| Security-oriented Gemini CLI guidance emphasizes project instruction files, tests, lint, and security scans. | Vendor practitioner article | Put policy and verification commands in repo instructions and make scans observable. |
| Public issue reports describe destructive behavior under broad/no-sandbox permissions and data overwrite risk. | GitHub issue/community anecdote | Disable YOLO, block root/workspace-wide deletes, snapshot writable state, and prefer append-safe memory tools. |

Community anecdotes are not proof of general performance. They are used here as
risk discovery signals and must be validated locally.

## Case Matrix

| Channel | Useful Pattern To Keep | Failure To Design Against |
| --- | --- | --- |
| Official Gemini GitHub Actions | Async issue triage, PR review, and on-demand delegated repo work. | Treating CI text from issues, PRs, and forks as trusted instructions. |
| Official Gemini enterprise docs | Central settings, sandboxed tools, MCP allowlists, telemetry, and disabled YOLO mode. | Assuming local user prompt rules can replace admin/runtime controls. |
| Official ADK/A2A docs | Specialized agents, workflow agents, explicit invocation, state, sequential/parallel/loop patterns. | Building one overloaded "super-agent" with too many tools and instructions. |
| GitHub issues/discussions | Subagents isolate work; skills may need explicit invocation. | Skill non-use, looping, long delays, quota surprises, broad destructive actions, and overwritten unversioned state. |
| Hacker News | Gemini can investigate large codebases and summarize for a stronger reviewer. | Weak autonomous editing, repeated tool failure, rate-limit opacity, and over-editing. |
| Reddit | Stronger conductor plus Gemini/Antigravity executor can reduce grunt-work cost. | Quota burn, immature harness behavior, weak interruption, and deletion stories under broad filesystem access. |
| YouTube/tutorials | Useful enablement material for setup, demos, and mental models. | Treat transcriptless demos as proof of safety or quality. |
| Security blogs | Useful attack-surface discovery for CI, shell, trust, and workspace controls. | Copying exploit-prone workflow patterns without admission checks. |

## Vendor Dependency Exit Plan

Keep the architecture portable:

- Put model-specific names in adapters, not in core protocol.
- Make every worker communicate through JSON contracts that another model can
  implement.
- Store traces in open formats such as JSONL and OpenTelemetry.
- Keep deterministic tools outside the model provider.
- Maintain a model capability matrix with empirical local evals, not vendor
  marketing claims.
- Run a quarterly failover drill: replace Gemini worker with another approved
  cloud model or a local model for dispatcher/compressor/test-planner roles.
- Keep secrets, schedules, approvals, and policy in your own broker so changing
  model providers does not rewrite governance.

Gemini is a worker plug-in. The AX system should survive if Gemini is slower,
rate-limited, retired, or replaced.

## Tomorrow Rollout

1. Create a repo allowlist and command allowlist.
2. Add a `runtime-capabilities.yaml` adapter for the enterprise workstation.
3. Add explicit worker contracts for `dispatcher`, `compressor`,
   `test_planner`, `patch_candidate`, and `diff_claim_extractor`.
4. Configure Gemini API or approved Antigravity/enterprise endpoint. Avoid
   relying on retired consumer Gemini CLI paths.
5. Configure the local broker: redaction, `store: false` where applicable,
   telemetry without prompt logging, model allowlist, proxy/gateway, and per-task
   budgets.
6. Put stable public runbooks and schemas in cached context where the API and
   retention policy support it.
7. Add a local trace file per run:

   ```text
   runs/<date>/<task-id>/trace.jsonl
   runs/<date>/<task-id>/scout.json
   runs/<date>/<task-id>/worker-result.json
   runs/<date>/<task-id>/verification.txt
   ```

8. Pilot on three low-risk tasks:
   - analysis-only repository inventory,
   - test generation without code edits,
   - one small mechanical patch in a temporary branch.
9. Score each run for schema validity, evidence quality, verification success,
   scope control, privacy compliance, cost, and latency.
10. Only then enable scheduled self-healing routines, starting with read-only
   diagnosis and branch-only patch proposals.

## Metrics

Track per task, not only per token:

- `schema_valid`: Gemini output parsed and passed validation.
- `evidence_bound_claims`: final claims with file/line/command evidence.
- `verification_passed`: exact commands and exit codes.
- `retry_count`: retries before pass or escalation.
- `escalation_reason`: privacy, risk, repeated failure, missing evidence, or
  provider failure.
- `private_context_released`: none, summary only, approved excerpt, or blocked.
- `diff_scope`: expected files only or out-of-scope.
- `latency_seconds` and `estimated_cost`.

## Public Repo Hygiene

Before publishing:

- Remove personal names, internal hostnames, repo paths, tokens, contract terms,
  security architecture details, ticket IDs, and proprietary model evaluations.
- Replace enterprise specifics with placeholders.
- Do not publish raw traces from private code.
- Label community reports as anecdotal.
- Do not claim Gemini, local LLMs, or this protocol provide safety enforcement.
- Do not claim lower models become frontier-equivalent.

## Minimum Viable Policy

```yaml
gemini_worker_policy:
  default_role: "contract_worker"
  final_judgment_allowed: false
  raw_private_context_allowed: false
  output_schema_required: true
  max_code_retry_attempts: 2
  max_diagnostic_retry_attempts: 3
  allowed_default_roles:
    - dispatcher
    - context_compressor
    - test_planner
    - patch_candidate_generator
    - diff_claim_extractor
  forbidden_without_human_approval:
    - production_change
    - credential_or_secret_action
    - external_post_or_email
    - destructive_command
    - hardware_or_device_state_change
    - broad_dependency_upgrade
  retention_controls:
    store_false_required: true
    grounding_for_confidential_data: false
    explicit_cache_for_confidential_data: false
    file_upload_for_confidential_data: false
    prompt_logging_allowed: false
  tool_controls:
    yolo_mode_allowed: false
    workspace_root_delete_allowed: false
    mcp_servers_require_allowlist: true
    shell_commands_require_allowlist: true
  verifier_source_of_truth:
    - git_diff
    - command_exit_code
    - test_output
    - lint_or_build_output
    - schema_validation
```
