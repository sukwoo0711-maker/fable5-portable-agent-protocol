# gpt-5.5 CLI Attempt

Condition: stronger-model staged smoke test via Codex CLI.

Result: not executed.

Reason: Codex CLI exited with status 1 immediately after session startup for
`gpt-5.5`. No final model response was produced. A separate `gpt-5` fallback
attempt also failed with:

```text
The 'gpt-5' model is not supported when using Codex with a ChatGPT account.
```

The historical pilot in `evals/protocol-uplift/scores.json` still contains an
`S0` stronger-model text result for `gpt-5.5`, but this staged smoke run should
not claim fresh stronger-model evidence.
