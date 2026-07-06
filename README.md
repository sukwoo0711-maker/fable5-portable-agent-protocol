# Fable5 Portable Agent Protocol

This repository turns a Fable5-style coding operations manual into a portable,
harness-neutral instruction pack for tool-using coding agents.

The goal is not to imitate one model or one product surface. The protocol
captures transferable behavior: inspect before editing, preserve local work,
follow project patterns, keep diffs scoped, verify with real commands, and
report failures plainly.

## Structure

- `AGENTS.md` is the short always-loaded entry point for compatible agents.
- `skills/portable-coding-agent-protocol/SKILL.md` is the installable skill entry.
- `skills/portable-coding-agent-protocol/references/` holds lazy-loaded modules.

Read only the modules needed for the current task. This avoids spending context
on bugfix, feature, refactor, embedded, or portability details when they are not
relevant.

## Install As A Codex Skill

Copy or symlink `skills/portable-coding-agent-protocol` into your Codex skills
directory, or invoke it directly from this repository:

```text
Use $portable-coding-agent-protocol to handle this coding task with scoped edits
and explicit verification.
```

## Design Notes

This pack deliberately avoids hard dependencies on specific harness concepts
such as tool names, channels, sandbox names, or model identities. Put those
constraints in an environment adapter, not in the core protocol.
