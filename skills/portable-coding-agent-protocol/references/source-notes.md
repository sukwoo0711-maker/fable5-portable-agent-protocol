# Non-Normative Source Notes

These notes explain public-reference inputs behind this protocol. They are not
required for normal coding tasks and are not normative requirements.

## High-Confidence References

- Anthropic, "Prompting Claude Fable 5":
  https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
  - Contributed patterns for long-running tasks, acting when enough context
    exists, explicit self-verification, progress handling, final-summary
    readability, and avoiding stale over-prescriptive prompts.

- Anthropic, "Introducing Claude Fable 5 and Claude Mythos 5":
  https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5
  - Contributed migration implications: long-horizon agentic work, refusal
    handling, fallback behavior, effort control, task budgets, and why some
    details belong in a harness adapter rather than the core protocol.

- Anthropic, "System Prompts":
  https://platform.claude.com/docs/en/release-notes/system-prompts
  - Confirms that product UI, API, and coding-agent surfaces should not be
    treated as one interchangeable prompt environment.

- AGENTS.md open format:
  https://agents.md/
  - Supports a predictable repository-level instruction format across multiple
    coding agents.

- OpenAI Codex, "Custom instructions with AGENTS.md":
  https://developers.openai.com/codex/guides/agents-md
  - Confirms instruction layering, project overrides, and size limits in one
    major coding-agent environment. Used as a portability data point, not as a
    required runtime.

## Evaluation References

- SWE-bench:
  https://www.swebench.com/SWE-bench/
  - Useful precedent for patch-based software-engineering evaluation on real
    issues with reproducible harnesses.

- Inspect AI:
  https://inspect.aisi.org.uk/
  - Useful as a future formal evaluation framework for coding, agentic,
    reasoning, behavior, and multimodal evals.

- mini-swe-agent:
  https://github.com/SWE-agent/mini-swe-agent
  - Useful as a simple local agent-harness reference. Not required by this repo.

## Community Signals

These sources show user demand and recurring design patterns. Treat them as
anecdotal unless their claims are independently verified.

- CodeRabbit, "Claude Fable 5 Model Review":
  https://www.coderabbit.ai/blog/fable-5-model-review
  - Supports the tradeoff that Fable5-like behavior can be strong for autonomous
    implementation but needs stop conditions, budgets, and review checkpoints.

- CheswickDEV, "claude-fable-5-prompt-optimizer":
  https://github.com/CheswickDEV/claude-fable-5-prompt-optimizer
  - Community implementation of doc-grounded prompt optimization, target
    detection, complexity routing, anti-pattern scans, and auditable rule
    references.

- kpab, "claude-fable-5-skills":
  https://github.com/kpab/claude-fable-5-skills
  - Shows demand for short skill modules organized around intent, boundaries,
    and verification hooks.

- tomicz, "fable-5-train-opus-skills-after-it-retires":
  https://github.com/tomicz/fable-5-train-opus-skills-after-it-retires
  - Strong demand signal for "use Fable-like skills with cheaper models." Its
    review phases influenced this repo's factual/doctrine/usability review
    split, but its prompt text is not copied.

- vasilichnick, "fable5":
  https://github.com/vasilichnick/fable5
  - Example of recon-first, batched-question, spec-playback workflow.

- AlessandroFare, "fable-frame":
  https://github.com/AlessandroFare/fable-frame
  - Example of packaging Fable-inspired behavior modules with agent
    orchestration templates.

- unclecatvn, "rigorous-execution-skill":
  https://github.com/unclecatvn/rigorous-execution-skill
  - Example of evidence-grounded reports and calibrated autonomy as a reusable
    skill.

- habinsong, "k-fable-opus-claude-md":
  https://github.com/habinsong/k-fable-opus-claude-md
  - Korean-language community adaptation focused on small edits, prior
    inspection, verification, concise reporting, and dangerous-command caution.

- Simon Willison, "Claude Fable is relentlessly proactive":
  https://simonwillison.net/2026/jun/11/fable-is-relentlessly-proactive/
  - Practitioner observation that frontier coding agents may invent powerful
    local tactics unless bounded. Supports explicit safety gates and budget
    awareness.

- Business Insider, "Forget prompt engineering: 'Loop engineering' is all the rage now":
  https://www.businessinsider.com/what-are-loops-ai-engineering-tips-2026-6
  - Useful as a public signal that agent users are moving from one-shot prompts
    toward loops involving automation, skills, connectors, and subagents.

## YouTube Search Notes

YouTube search found multiple relevant videos, including:

- "Claude Fable 5 Built This in Claude Code and I'm Blown Away":
  https://www.youtube.com/watch?v=I3PYGi_tGy0
- "How Anthropic Engineers Actually Prompt Fable 5":
  https://www.youtube.com/watch?v=vcU85OrwuV0
- "How to Build Claude Subagents Better Than 99% of People":
  https://www.youtube.com/watch?v=e18sdZLwP7o
- "How to use agents, skills, and instructions in Copilot CLI":
  https://www.youtube.com/watch?v=-yKALFS5ewY

These were used only as weak demand and topic-discovery signals because the
search surface exposed metadata and snippets, not a reliable transcript.

## Considered But Not Normative

- Leaked or alleged system prompts.
- Reddit prompt templates.
- Community prompt packs without reproducible before/after evidence.
- Videos without accessible transcripts.

These may inspire pattern mining, but they must not be copied wholesale or
treated as proof of efficacy.

## Incorporation Decisions

- Reframe the repo from "portable coding protocol" to "capability scaffolding
  plus portability."
- Keep official and observed behavior patterns, not provider-specific prompt
  text.
- Do not copy leaked system prompts or community templates verbatim.
- Keep core rules model-neutral and put product or harness details in adapters.
- Replace monolithic instructions with a small entry point and lazy-loaded
  references.
- Add lower-model scaffolds for state, decomposition, evidence, uncertainty,
  recovery, self-review, and stop rules.
- Add embedded-specific gates for target verification, generated/vendor files,
  and hardware safety.
