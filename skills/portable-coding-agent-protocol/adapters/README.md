# Environment Adapters

Adapters map the protocol's neutral capability names to a concrete runtime.
Keep product names, tool schemas, channels, shell details, approval behavior, and
logging requirements here instead of in the core protocol.

## Required Capability Names

- `search_project`
- `list_files`
- `read_file`
- `edit_file`
- `run_command`
- `inspect_diff`
- `request_approval`
- `report_progress`
- `report_final`
- optional: `browser_or_ui`
- optional: `simulator_or_hardware`
- optional: `memory_or_checkpoint`
- optional: `subagent_or_verifier`

Conformance is judged by artifacts: files read, commands run, diffs inspected,
approvals requested, checks observed, and final claims tied to evidence.

## Files

- `runtime-capabilities.yaml`: fill this out for a host runtime.
- `task-mode-selector.md`: choose tiny, standard, high-risk, or eval controls.
- `lower-model-run-prompt.md`: compact prompt wrapper for lower-capability
  models.
- `gemini-worker-contracts.md`: schema-bound contracts for Gemini-style
  dispatcher, compressor, planner, candidate, and diff-claim workers.
- `self-healing-routine.md`: bounded scheduled/event automation loop with
  allowlists, retry limits, evidence logging, and escalation.
- `task-ledger.txt`: external working-memory form.
- `pre-edit-checklist.md`: concrete before-edit guard.
- `evidence-record.md`: claim-to-evidence form.
- `pre-final-review.md`: final audit form.
- `codex.md`: example mapping for Codex-like environments.
- `generic-embedded-agent.md`: example mapping for firmware or lab workflows.

These are templates, not mandatory product bindings.
