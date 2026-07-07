# Non-Normative Source Notes

These notes explain public-reference inputs behind this protocol. They are not
required for normal coding tasks and are not normative requirements.

The source window for the 2026-07-07 approval pass was 2026-04-07 through
2026-07-07 unless a source is official living documentation retrieved during the
pass.

## Evidence Labels

| Label | Meaning | Allowed use |
| --- | --- | --- |
| A0 | Official, dated within the review window | Product behavior, compatibility, release claims |
| A1 | Official living docs retrieved during the review | Current product mechanics; cite access date |
| B1 | Active, highly starred or widely used project updated in the window | Implementation or evaluation precedent, not product guarantees |
| B2 | Recognized expert dated in the window | Anecdotal risk or design signal only |
| C | Vendor, press, or low-star community source | Topic discovery only |
| D | Undated, low-trust, transcriptless video, leaked or alleged prompt source | Not evidence |

Broad claims such as "improves lower models" require local evaluation results or
must be phrased as a hypothesis.

## Accepted References

- A0, Anthropic, "Prompting Claude Fable 5":
  https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
  - Supports Fable-specific operating patterns: long-running action, progress
    claim grounding, boundary setting, early-stopping prevention, memory, and
    subagent guidance.
  - Limit: Fable-specific guidance does not prove that other models gain the
    same capability.

- A0, Anthropic, "Introducing Claude Fable 5 and Claude Mythos 5":
  https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5
  - Supports Fable capability and integration claims such as long-horizon
    agentic work and refusal/fallback handling.
  - Limit: product capability source, not a portable-protocol evaluation.

- A1, OpenAI Codex, "Custom instructions with AGENTS.md":
  https://developers.openai.com/codex/guides/agents-md
  - Supports Codex instruction discovery, layering, precedence, and size-limit
    mechanics.
  - Limit: Codex-specific behavior belongs in adapters.

- A1, OpenAI Codex, "Agent Skills":
  https://developers.openai.com/codex/skills
  - Supports skill packaging with `SKILL.md`, references, scripts, assets, and
    agents.
  - Limit: packaging precedent, not proof of model uplift.

- A1, OpenAI Codex, "Subagents":
  https://developers.openai.com/codex/concepts/subagents
  - Supports explicit subagent triggering and the cost/coordination tradeoff.
  - Limit: subagents are optional and should not be required by the core.

- A0, GitHub Changelog, "Copilot code review: AGENTS.md support and UI
  improvements", 2026-06-18:
  https://github.blog/changelog/2026-06-18-copilot-code-review-agents-md-support-and-ui-improvements/
  - Supports repository-level `AGENTS.md` as a cross-agent portability signal.
  - Limit: Copilot review-specific, not a universal instruction standard.

- B1, AGENTS.md open format:
  https://agents.md/
  - Supports a predictable repository-level instruction format used across many
    open-source projects.
  - Limit: ecosystem signal, not tool-behavior proof.

- B1, Inspect AI changelog and docs:
  https://inspect.aisi.org.uk/CHANGELOG.html
  - Supports current evaluation-harness precedent for agent, model, logging, and
    tool-integration mechanics.
  - Limit: this repo does not require Inspect AI.

- B1, SWE-bench:
  https://www.swebench.com/SWE-bench/
  - Useful precedent for patch-based software-engineering evaluation on
    reproducible issues.
  - Limit: too heavy to claim from this repo's pilot alone.

- B1, OpenAI Evals:
  https://github.com/openai/evals
  - Useful precedent for evaluating language-model systems with explicit
    samples, scorers, and run artifacts.
  - Limit: framework precedent only; this repo's claims still require local
    results.

- B1, mini-swe-agent:
  https://github.com/SWE-agent/mini-swe-agent
  - Useful active local agent-harness reference.
  - Limit: implementation precedent only.

- B2, Addy Osmani, "Loop Engineering":
  https://addyosmani.com/blog/loop-engineering/
  - Recognized-practitioner signal that agent workflows are moving from one-shot
    prompts toward loops, checks, and automation.
  - Limit: expert framing, not evaluation evidence.

## Quarantined Or Rejected As Evidence

- Low-star Fable prompt packs and skill repos: useful for demand discovery and
  anti-pattern mining, not for efficacy claims.
- Vendor reviews and press trend pieces: useful for topic discovery only.
- Transcriptless YouTube results: not evidence unless the dated transcript is
  accessible and the author qualifies as a recognized expert.
- Leaked or alleged system prompts, Reddit prompt templates, and copied prompt
  packs: do not copy and do not treat as proof.

## Incorporation Decisions

- Reframe the repo as lower-model operating-behavior scaffolding, not model
  equivalence.
- Keep official and observed behavior patterns, not provider-specific prompt
  text.
- Put product or harness details in adapters.
- Keep the core protocol model-neutral and capability-oriented.
- Use lazy-loaded references rather than one monolithic instruction file.
- Add lower-model scaffolds for state, decomposition, evidence, uncertainty,
  recovery, self-review, stop rules, and completion gates.
- Require local evaluation before claiming uplift.
