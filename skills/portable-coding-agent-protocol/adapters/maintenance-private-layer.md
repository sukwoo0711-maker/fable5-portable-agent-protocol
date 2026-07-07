# Maintenance And Private Layer

Use this adapter to keep a public protocol useful while preserving enterprise
details in a private operational layer.

## Why A Private Layer Exists Even With Enterprise Contracts

Enterprise contracts reduce provider-side risk. They do not make every internal
detail appropriate for a public repository.

A private layer protects:

- Internal repository names and paths.
- Proxy, gateway, region, project, and tenant identifiers.
- Tool names, command allowlists, and scheduler names that reveal attack paths.
- Security exceptions, approval chains, and incident response procedures.
- Model quotas, contract terms, and cost centers.
- Eval results on proprietary code.
- Failure traces, logs, stack traces, and customer data.
- Names of people, teams, systems, and internal tickets.

The public repo should contain reusable shapes: contracts, schemas, gates,
runbook templates, and evidence rules. The private layer contains the values
that make those shapes executable in one organization.

## Layer Split

| Public Repo | Private Layer |
| --- | --- |
| Generic worker contract. | Actual model endpoint, region, account, project, and quota. |
| Example policy skeleton. | Real command allowlist, write roots, denied commands, and exception list. |
| Data class definitions. | Internal data catalog and repo-specific classification. |
| Optional recovery automation possibility note. | Real scheduler, service names, branch naming, enablement switch, and alert channel. |
| Synthetic trace examples. | Real traces, logs, costs, and failure memory. |
| Source notes and claims. | Enterprise contract terms and legal/security approvals. |

## Private Adapter Layout

Keep private files outside the public repo or in a private sibling repository:

```text
enterprise-ax-private/
  runtime-capabilities.yaml
  model-endpoints.yaml
  command-allowlist.yaml
  repo-allowlist.yaml
  data-classification.yaml
  optional-automation-routines.yaml
  approval-boundaries.yaml
  failure-memory/
  traces/
```

The public protocol can reference these by interface name, not by path.

## Maintenance Cadence

| Cadence | Action |
| --- | --- |
| Weekly | Review failed runs, repeated escalations, and worker schema rejects. |
| Monthly | Check provider release notes, deprecated model names, CLI migration notes, and security advisories. |
| Quarterly | Re-run local evals, update capability matrix, and perform provider failover drill. |
| Before public release | Run secret scan, internal-name scan, link check, and claim audit. |

## Source Freshness Rules

- Official living docs should record the retrieval date in `source-notes.md`.
- Dated official docs may support product history and migration decisions.
- Community reports may motivate controls, but must stay non-normative.
- Product names and parameter names belong in adapters.
- Core protocol claims must remain model-neutral unless backed by local evals.

## Maintenance Checklist

```text
Docs maintenance:
- Current provider docs checked:
- Deprecated APIs or CLIs found:
- Source notes updated:
- Broken links checked:
- Public/private boundary checked:
- New security advisories reviewed:
- Local evals rerun or explicitly deferred:
- Adapter defaults changed:
- Migration action owner:
```

## Drift Triggers

Update the private layer immediately when:

- A model endpoint changes or is retired.
- A CLI migration changes tool permissions or workspace trust.
- A new security advisory affects agent execution, CI, MCP, or shell tools.
- A worker repeatedly fails schema validation.
- A worker causes broad diffs, loops, or repeated tool errors.
- A private repo, scheduler, proxy, or approval process changes.
