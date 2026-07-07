# Codex-Style Adapter Example

This example is non-normative. It shows how a Codex-like host can map protocol
capabilities without making the core protocol depend on Codex.

| Protocol capability | Example host mechanism | Required artifact |
| --- | --- | --- |
| `search_project` | Fast project search such as ripgrep or host search tool | Query and result excerpt |
| `list_files` | File listing command or workspace explorer | Listed paths |
| `read_file` | Shell read, editor read, or file tool | File path and relevant lines |
| `edit_file` | Patch-based edit tool | Patch/diff |
| `run_command` | Local shell with exit code | Command, exit code, output |
| `inspect_diff` | Version-control status and diff | Status/diff output |
| `request_approval` | User approval prompt or policy gate | Approval result |
| `report_progress` | User-visible progress message | Claim tied to observed artifact |
| `report_final` | Final response | Completion gate and evidence summary |
| `subagent_or_verifier` | Explicitly requested subagents or self-review | Reviewer summary or self-review notes |

Codex-specific AGENTS.md discovery and skill loading belong in this adapter and
project setup notes. The reusable protocol should continue to speak in
capability names.
