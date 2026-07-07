# Non-Normative Source Notes

These notes explain public-reference inputs behind this protocol. They are not
required for normal coding tasks and are not normative requirements.

The source window for the 2026-07-07 approval pass was 2026-04-07 through
2026-07-07 unless a source was official living documentation retrieved during
the pass. The secure enterprise AX addendum added official Gemini, ADK, A2A,
MCP, and GitHub Action sources retrieved on 2026-07-08; dated official sources
outside the original window are used only for product-history or architecture
context.

## Evidence Labels

| Label | Meaning | Allowed use |
| --- | --- | --- |
| A0 | Official, dated source | Product behavior, compatibility, release claims |
| A1 | Official living docs retrieved during the review | Current product mechanics; cite access date |
| B1 | Active, highly starred or widely used project updated in the window | Implementation or evaluation precedent, not product guarantees |
| B2 | Recognized expert dated in the window | Anecdotal risk or design signal only |
| C | Vendor, press, or low-star community source | Topic discovery only |
| D | Undated, low-trust, transcriptless video, leaked or alleged prompt source | Not evidence |

Broad claims such as "improves lower models" require local evaluation results or
must be phrased as a hypothesis.

## Accepted References

- A0, Google Developers Blog, "An important update: Transitioning Gemini CLI to
  Antigravity CLI", 2026-05-19:
  https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/
  - Supports the migration warning that consumer Gemini CLI and Code Assist IDE
    extension request serving stops on 2026-06-18.
  - Limit: applies to product packaging and access, not model quality.

- A1, Google Agent Development Kit:
  https://adk.dev/
  - Supports ADK as a current framework for building, running, debugging,
    evaluating, and deploying agent systems, including model routing,
    observability, context management, tools, skills, MCP, and A2A.
  - Limit: framework capability does not prove a specific deployment is safe.

- A1, Google ADK with Agent2Agent protocol:
  https://adk.dev/a2a/
  - Supports A2A as an official pattern for multi-agent collaboration.
  - Limit: integration pattern only; local security controls still belong in
    the runtime.

- A0, Google Cloud Blog, "Building Collaborative AI: A Developer's Guide to
  Multi-Agent Systems with ADK", 2025-11-06:
  https://cloud.google.com/blog/topics/developers-practitioners/building-collaborative-ai-a-developers-guide-to-multi-agent-systems-with-adk
  - Supports specialized LLM, workflow, and custom agents; hierarchy;
    sequential, parallel, and loop workflow patterns; and explicit invocation.
  - Limit: conceptual and tutorial guidance, not production validation.

- A0, Google Cloud Blog, "How to build a simple multi-agentic system using
  Google's ADK", 2025-07-03:
  https://cloud.google.com/blog/products/ai-machine-learning/build-multi-agentic-systems-using-google-adk
  - Supports the "avoid one overloaded super-agent; use focused specialists"
    design rationale.
  - Limit: example pattern only.

- A1, Gemini API, "Structured outputs":
  https://ai.google.dev/gemini-api/docs/structured-output
  - Supports JSON Schema/Pydantic/Zod structured output for agentic workflows.
  - Limit: schema compliance should still be validated by the harness.

- A1, Gemini API, "Thinking":
  https://ai.google.dev/gemini-api/docs/thinking
  - Supports controlling thinking budget and using lower thinking for simple
    retrieval/classification tasks.
  - Limit: provider-specific parameter mapping belongs in adapters.

- A1, Gemini API, "What's new in Gemini 3.5 Flash":
  https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5
  - Supports `thinking_level` as the current Gemini 3.5 Flash control surface.
  - Limit: only applies to supported Gemini 3.5 API surfaces.

- A1, Gemini API, "Zero data retention in the Gemini Developer API":
  https://ai.google.dev/gemini-api/docs/zdr
  - Supports ZDR cautions: paid-service training restrictions, `store:false`
    for Interactions API state, grounding retention, File API storage, explicit
    cache storage, and implicit in-memory cache behavior.
  - Limit: enterprise policy must still decide which features are allowed.

- A1, Gemini API, "Context caching" and "Batch API":
  https://ai.google.dev/gemini-api/docs/caching
  https://ai.google.dev/gemini-api/docs/batch-api
  - Supports caching repeated context and using batch requests for offline work.
  - Limit: batch SLOs are not suitable for interactive completion gates.

- A1, Langfuse OpenTelemetry integration:
  https://langfuse.com/integrations/native/opentelemetry
  - Supports OpenTelemetry-based tracing with token, cost, prompt, and scoring
    metadata for LLM systems.
  - Limit: observability does not enforce policy by itself.

- A1, Gemini Enterprise Agent Platform, "Scale your agents":
  https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale
  - Supports Agent Runtime, sessions, memory, security, and observability as
    enterprise deployment concepts.
  - Limit: managed-platform controls may not exist in a local workstation setup.

- A1, Gemini Enterprise Agent Platform, "Route Agent Runtime traffic through
  Agent Gateway":
  https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-gateway-runtime-deploy
  - Supports Agent Gateway as an ingress/egress governance component for users,
    agents, tools, models, APIs, and other agents.
  - Limit: product-specific; local deployments need equivalent gateway/proxy
    controls.

- A1, Gemini Enterprise Agent Platform, "Use Agent Identity with Agent Runtime":
  https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity
  - Supports per-agent identity, access control, and logging both user and agent
    identity for delegated flows.
  - Limit: product-specific; local runners need separate credentials and logs.

- A1, A2A Protocol specification:
  https://a2a-protocol.org/latest/specification/
  - Supports tasks, artifacts, agent cards, security schemes, and traceable
    agent-to-agent communication.
  - Limit: protocol structure is not an access-control policy by itself.

- A1, Model Context Protocol tools specification:
  https://modelcontextprotocol.io/specification/2025-06-18/server/tools
  - Supports tool input validation, access controls, rate limits, output
    sanitization, user confirmation for sensitive operations, timeouts, and
    audit logging.
  - Limit: each MCP server still needs local sandbox and permission review.

- A0, Google, "Gemini CLI GitHub Actions: AI coding made for collaboration",
  2025-08-06:
  https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-cli-github-actions/
  - Supports asynchronous repo workflows such as issue triage, PR review,
    delegated tasks, WIF, command allowlisting, and OpenTelemetry.
  - Limit: beta/repo automation guidance, not proof of autonomous safety.

- A1, Google GitHub Actions `run-gemini-cli`, best practices and trust guidance:
  https://github.com/google-github-actions/run-gemini-cli/blob/main/docs/best-practices.md
  https://github.com/google-github-actions/run-gemini-cli/blob/main/docs/trust-guidance.md
  - Supports branch protection, approver restrictions, WIF, secrets handling,
    pinned actions, least privilege, trusted/untrusted input separation, and
    read-only tools for untrusted workflows.
  - Limit: GitHub Actions-specific.

- A1, Gemini CLI enterprise guide:
  https://geminicli.com/docs/cli/enterprise/
  - Supports central settings, tool allowlists, MCP allowlists, sandboxing,
    proxy control, telemetry without prompt logging, and disabling YOLO mode.
  - Limit: local admin users may bypass configuration; this is policy support,
    not a foolproof security boundary.

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
- GitHub issues, Hacker News threads, Reddit posts, and transcriptless YouTube
  videos about Gemini CLI, Antigravity, skills, subagents, or self-healing
  loops: useful as risk-discovery signals and field anecdotes only. They may
  motivate controls such as explicit skill invocation, retry budgets,
  structured outputs, and verifier gates, but they do not prove performance.
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
