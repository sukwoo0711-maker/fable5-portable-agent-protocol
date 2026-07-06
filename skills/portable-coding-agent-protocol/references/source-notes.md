# Source Notes

These notes explain the public-reference rationale behind this protocol. They
are not required for normal coding tasks.

## Public References Used

- Anthropic, "Prompting Claude Fable 5":
  https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
  - Useful for long-running task guidance, explicit self-verification,
    instruction trimming, progress handling, and final-summary readability.

- Anthropic, "Introducing Claude Fable 5 and Claude Mythos 5":
  https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5
  - Useful for migration implications: longer-horizon agentic work, refusal
    handling, fallback behavior, effort control, task budgets, and the warning
    that some details belong in a harness adapter rather than a generic protocol.

- Anthropic, "System Prompts":
  https://platform.claude.com/docs/en/release-notes/system-prompts
  - Useful for confirming that official consumer system-prompt notes exist, and
    that API, product UI, and coding-agent surfaces should not be treated as one
    interchangeable prompt environment.

- CodeRabbit, "Claude Fable 5 Model Review":
  https://www.coderabbit.ai/blog/fable-5-model-review
  - Useful for the tradeoff that Fable5-like behavior can be strong for
    autonomous implementation but needs explicit stop conditions, budgets, and
    review checkpoints.

- CheswickDEV, "claude-fable-5-prompt-optimizer":
  https://github.com/CheswickDEV/claude-fable-5-prompt-optimizer
  - Useful as a community implementation of doc-grounded prompt optimization:
    target detection, complexity routing, anti-pattern scans, and auditable rule
    references. Treat as unofficial but structured.

- kpab, "claude-fable-5-skills":
  https://github.com/kpab/claude-fable-5-skills
  - Useful for the design direction of short skill modules organized around
    intent, boundaries, and verification hooks rather than older, overly
    prescriptive instruction piles.

- mrtooher, "fable-mode":
  https://github.com/mrtooher/fable-mode
  - Useful as a compact community example of Fable-style multi-stage planning,
    optional delegation, and self-verification.

- AGENTS.md open format:
  https://agents.md/
  - Useful for the repository-level instruction layout: a predictable,
    Markdown-based location for setup, tests, style, safety, and subproject
    instructions across multiple coding agents.

- GitHub Changelog, "Copilot coding agent now supports AGENTS.md custom instructions":
  https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/
  - Useful evidence that AGENTS.md is not only a Codex convention; it is also
    supported by other coding-agent ecosystems.

- habinsong, "k-fable-opus-claude-md":
  https://github.com/habinsong/k-fable-opus-claude-md
  - Useful as a Korean-language community adaptation focused on small edits,
    prior inspection, verification, concise reporting, and dangerous-command
    caution. Treat as anecdotal and style-specific.

- Simon Willison, "Claude Fable is relentlessly proactive":
  https://simonwillison.net/2026/jun/11/fable-is-relentlessly-proactive/
  - Useful as a practitioner observation that frontier coding agents may invent
    powerful local tactics unless bounded. Supports explicit safety gates,
    budget awareness, and external-side-effect approval rules.

- Reddit discussion, "Friendly reminder to have Fable 5 write skills...":
  https://www.reddit.com/r/ClaudeAI/comments/1ukynrw/friendly_reminder_to_have_fable_5_write_skills/
  - Useful only as community evidence that users are converting Fable5-style
    behavior into reusable skills for other models. It does not prove efficacy.

- Reddit discussion, "Fable 5 and Opus 4.8 Prompt":
  https://www.reddit.com/r/claude/comments/1unhubx/fable_5_and_opus_48_prompt/
  - Useful as a community example of prompt templates plus hook-based
    enforcement. Treat as anecdotal, not authoritative.

- AY Automate, "Inside the Claude Fable 5 System Prompt":
  https://www.ayautomate.com/blog/claude-fable-5-system-prompt-leak
  - Useful mainly as a caution: leaked prompts are unverified, product-surface
    specific, and too large to copy. This protocol uses behavior-level patterns
    rather than leaked text.

- Knight Li, "Claude Fable 5 Prompting Guide":
  https://knightli.com/en/2026/06/10/claude-fable-5-prompting-guide/
  - Useful as a secondary summary of the official guidance around long tasks,
    migration, boundaries, and verification.

## Incorporation Decisions

- Keep official and observed behavior patterns, not provider-specific prompt
  text.
- Do not copy leaked system prompts or community templates verbatim.
- Keep the core protocol model-neutral and place product or harness details in
  adapters.
- Replace long monolithic instructions with a small entry point and lazy-loaded
  references.
- Add embedded-specific gates for target verification, generated/vendor files,
  and hardware safety.
