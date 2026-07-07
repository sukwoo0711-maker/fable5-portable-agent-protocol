# Long-Work Scaffolding

Use this module for resumed work, broad changes, embedded porting, or any task
where context loss would create risk.

## Files

Use local text files when the runtime has durable storage. Keep them compact and
delete or archive them when the task is complete if the repository should not
retain them.

### TASK.md

```text
Goal:
Done when:
Non-goals:
Approval boundaries:
Risk tier:
Primary verification:
Fallback verification:
```

### TODO.md

```text
- [ ] Recon:
- [ ] Plan:
- [ ] Edit:
- [ ] Verify:
- [ ] Critic:
- [ ] Report:
```

### CHECKPOINT.md

```text
Last updated:
Current phase:
Facts observed:
Files changed:
Commands run:
Passing checks:
Failing checks:
Failed hypotheses:
Next action:
Stop or ask condition:
```

## Resume Protocol

On resume, reconstruct from durable evidence in this order:

1. Latest user request and task file.
2. Version-control status and diff.
3. Command logs, failing tests, device logs, or screenshots.
4. Changed files and nearby context.
5. Prior checkpoint notes.

Never continue from memory alone. If notes conflict with diff or command output,
trust the observable artifact and update the checkpoint.
