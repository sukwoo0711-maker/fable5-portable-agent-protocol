# Portable Coding Agent Protocol

Use `skills/portable-coding-agent-protocol/SKILL.md` for coding tasks,
debugging, refactoring, repository analysis, embedded porting work, and review
of coding-agent operating instructions.

Keep this entry point short. Load only the reference module needed for the
current task:

- `core-workflow.md` for every coding task.
- `bugfix-workflow.md` when fixing a defect or failing test.
- `feature-workflow.md` when adding behavior.
- `refactor-workflow.md` when preserving behavior while changing structure.
- `embedded-porting.md` for firmware, toolchains, hardware, lab, or target-board work.
- `agent-portability.md` when adapting these instructions to another agent or harness.
- `anti-patterns.md` when reviewing failures or tightening a process.
- `source-notes.md` when checking why the protocol is shaped this way.

Do not assume a specific AI product, model, tool API, shell, sandbox, browser,
MCP server, memory system, or approval mechanism. Use the safest available local
mechanisms to read, search, edit, execute, verify, and report.
