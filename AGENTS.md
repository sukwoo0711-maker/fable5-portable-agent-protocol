# Portable Coding Agent Protocol

Use `skills/portable-coding-agent-protocol/SKILL.md` for coding tasks,
debugging, refactoring, repository analysis, embedded porting work, and review
of coding-agent operating instructions.

Keep this entry point short. Load only the reference module needed for the
current task:

- `core-workflow.md` for every coding task.
- `lower-model-amplification.md` when the goal is to improve a weaker agent's
  long-horizon behavior or emulate selected Fable-style operating discipline.
- `long-horizon-control.md` for multi-step, ambiguous, resumed, or long-running work.
- `control-budgets.md` when lower-capability models need numeric tripwires.
- `long-work-scaffolding.md` when durable task, todo, or checkpoint files are needed.
- `capability-calibration.md` when uncertainty, missing tools, or model limits matter.
- `evidence-and-claims.md` whenever the agent must decide what it may safely claim.
- `self-review.md` before finalizing meaningful edits.
- `context-management.md` when the task spans many files, tool calls, or sessions.
- `tool-use-discipline.md` when tools are available but the runtime mapping is unclear.
- `bugfix-workflow.md` when fixing a defect or failing test.
- `feature-workflow.md` when adding behavior.
- `refactor-workflow.md` when preserving behavior while changing structure.
- `repository-analysis.md` for analysis-only repository assessment or instruction review.
- `embedded-porting.md` for firmware, toolchains, hardware, lab, or target-board work.
- `agent-portability.md` when adapting these instructions to another agent or harness.
- `adoption-and-migration.md` when evaluating rollout into an existing agent architecture.
- `instruction-pack-evaluation.md` when measuring protocol uplift.
- `evaluation-tasks.md` for starter eval scenarios.
- `anti-patterns.md` when reviewing failures or tightening a process.
- `source-notes.md` when checking why the protocol is shaped this way.

Do not assume a specific AI product, model, tool API, shell, sandbox, browser,
MCP server, memory system, or approval mechanism. Use the safest available local
mechanisms to read, search, edit, execute, verify, and report.
