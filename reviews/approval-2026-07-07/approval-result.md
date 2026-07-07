# Approval Review, 2026-07-07

Objective: check whether the repository serves the user's real goal: helping
lower-capability models approximate selected Fable5-style operating behavior,
not merely polishing a philosophy document.

## Decision

Conditional approval for a public repo update framed as:

> Portable lower-model operating-discipline scaffold with adapter templates,
> completion gates, and early evaluation infrastructure.

Not approved for these claims:

- Weaker models become Fable5-equivalent.
- The protocol is governance or safety enforcement by itself.
- Current pilot results prove broad model uplift.
- Community prompt packs prove efficacy.

## Panel Interaction Evidence

Bernoulli challenged the governance claim:

> The repo is a strong instruction pack, not an enforced runtime. "Forced
> completion gate" must be implemented by the harness or reviewer workflow.

Carson accepted the objection and narrowed the claim:

> Prose gates are not governance. They are model behavior scaffolds. Governance
> starts when the runtime logs, enforces, blocks, audits, or scores those gates.

Kepler challenged the adapter approach:

> Thin adapters are not enough. Lower models will still fail from ambiguity.
> Adapters must name exact tools, exact required pre-final checks, exact failure
> handling, and exact final format.

Carson's complement was accepted with constraints:

> Neutral core, concrete adapter. Tool names are excluded from protocol, but
> required capability outputs and evidence artifacts are explicit.

Nash rejected the existing pilot as proof:

> The current pilot is only a ceiling-effect sanity check. Claims need staged
> executable evals with L0/L1/S0, saved diffs, logs, final answers, and scorer
> JSON.

Erdos constrained the evidence base:

> Official docs, local repo evidence, and actual run artifacts may support
> claims. Community posts or leaked/alleged prompts stay non-normative.

## Required Changes Accepted

- Add task-size routing and lower-model scaling.
- Add visible completion gate and early-termination guard.
- Add diagnostic mode vs fix mode.
- Add numeric control budgets as adapter/profile defaults.
- Add concrete adapter templates and lower-model forms.
- Add repository-analysis module or remove the advertised capability.
- Add long-work checkpoint templates.
- Add source labels and quarantine weak community sources.
- Add executable eval fixture infrastructure and failure taxonomy.

## Remaining Limits

The update is sufficient for a Level 1 pilot and public documentation cleanup.
It is not sufficient for broad adoption, safety enforcement, or Fable5-equivalent
performance claims. Supported local improvement requires staged executable evals
meeting the acceptance criteria in `instruction-pack-evaluation.md`.
