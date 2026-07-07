# Source Audit, 2026-07-07

Review window: 2026-04-07 through 2026-07-07, except official living docs
retrieved during the review.

## Accepted Sources

- A0: Anthropic, "Prompting Claude Fable 5".
  Supports Fable-specific long-horizon action, progress-claim grounding,
  boundary setting, early stopping prevention, memory, and subagent guidance.

- A0: Anthropic, "Introducing Claude Fable 5 and Claude Mythos 5".
  Supports Fable capability and integration claims such as long-horizon agentic
  work and refusal/fallback handling.

- A1: OpenAI Codex `AGENTS.md`, skills, and subagents docs.
  Supports instruction layering, skill packaging, progressive disclosure, and
  explicit subagent workflow mechanics in Codex-like environments.

- A0: GitHub Changelog, "Copilot code review: AGENTS.md support and UI
  improvements", 2026-06-18.
  Supports current repository-level `AGENTS.md` portability in Copilot code
  review.

- B1: AGENTS.md open format.
  Supports ecosystem use of a predictable repository-level instruction format.

- B1: Inspect AI docs/changelog, SWE-bench, mini-swe-agent, and OpenAI Evals.
  Support evaluation-harness and patch-eval precedent, not claims about this
  protocol's efficacy.

- B2: Addy Osmani, "Loop Engineering", 2026-06-07.
  Recognized-practitioner signal for loop/check/eval-oriented agent workflows.

## Rejected Or Quarantined

- Low-star Fable prompt packs: demand discovery only.
- Vendor reviews and press trend pieces: topic discovery only.
- Transcriptless YouTube results: not evidence.
- Leaked prompts, alleged system prompts, copied prompt packs, and Reddit
  templates: not evidence and not copied.

## Wording Limits

Allowed:

- "Inspired by current coding-agent practices."
- "Consistent with official Fable5 prompting guidance."
- "Adapter-backed and locally measurable."
- "Directional local evidence."

Avoid:

- "Proves uplift."
- "Fable5-equivalent."
- "Safety enforcement" for prose-only adoption.
- "Benchmark improvement" without staged executable results.
