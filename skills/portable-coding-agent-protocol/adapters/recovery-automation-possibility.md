# Recovery Automation Possibility Note

Use this note when discussing whether an enterprise workstation should add
scheduled or event-triggered recovery automation around Gemini-style workers.

This file is not an implementation adapter and does not recommend enabling
automation by default. It records what is technically plausible, what public
sources support, and what must be decided in the private enterprise layer.

## Evidence-Bounded Claim

Public sources support these narrow claims:

- Workflow frameworks can run deterministic loops with explicit iteration limits
  and termination conditions.
- Gemini-style repository automation is used for issue triage, pull request
  review, and delegated repository tasks.
- Headless or CI automation has real trust and allowlist risk, especially when
  processing untrusted input.

They do not prove that unattended self-repair is safe for a private enterprise
PC, proprietary repository, production system, device, or credentialed workflow.

## Possible Safe Uses

Treat these as candidates for private-layer evaluation, not default features:

- Read-only failure diagnosis from already-captured logs.
- Flaky check re-run with exact command and output capture.
- Generation of a reviewable issue, runbook note, or branch proposal.
- Suggested patch intent for a narrow, non-production path.
- Local failure memory entry after observed evidence.

## Out Of Scope For Public Repo Defaults

Do not enable from this public protocol:

- Scheduled writes.
- Auto-merge, auto-release, auto-deploy, or auto-posting.
- Secret rotation, credential repair, firewall changes, database migration, or
  hardware flashing.
- Workflows over untrusted issues, pull requests, tickets, or web content unless
  the private broker has read-only isolation and maintainer promotion.
- Any routine whose allowlist, scheduler, alert path, repo path, endpoint, or
  approval chain would reveal internal operations.

## Private Decision Gate

An enterprise PC or private operations repository decides whether to implement
automation. Before enabling it, require:

```text
Decision:
Owner:
Repository allowlist:
Command allowlist:
Write roots:
Input trust model:
Model endpoint and retention policy:
Telemetry and prompt logging policy:
Retry and timeout budgets:
Branch/worktree policy:
Human approval boundaries:
Rollback plan:
Evidence artifact location:
Pilot task results:
```

If any field is missing, keep the workflow manual or read-only.

## Minimal Pilot Shape

If the private layer approves a pilot, start with read-only diagnosis:

```text
scheduled/manual trigger -> run approved check -> capture logs locally
-> local scout summarizes evidence -> optional Gemini schema-bound diagnosis
-> broker validates output -> human reviews result
```

Move to branch-only patch proposals only after the read-only pilot demonstrates
schema validity, no private-data leakage, bounded latency, and useful human
review outcomes.

## Required Controls If Implemented Privately

- Explicit repo, command, tool, MCP, and write-root allowlists.
- Sandbox or temporary branch/worktree for any write path.
- Schema-only worker output with no prose, no completion claim, and a small
  tool/output budget.
- Stop after one repeated tool error or one repeated verification failure.
- Treat issue bodies, PR text, fork code, tickets, web pages, and model output
  as untrusted until promoted by policy.
- Keep raw logs local; send only redacted evidence packets to cloud workers.
- Record exact command output, exit codes, diff inspection, and unresolved items.

## Position In This Repo

This public repo may describe the possibility and guardrails. It must not carry
the real scheduler, repo paths, commands, endpoint names, alert channels, traces,
or enablement switch. Those belong in the private enterprise layer.
