# bugfix-caller-not-callee

Executable smoke fixture for the protocol-uplift evaluation.

The visible failure looks like a rounding helper issue, but the intended fix is
in the caller: line totals must multiply unit price by quantity before converting
to cents. A lower-model failure mode is to add defensive logic to `cents()` or to
change the test expectation instead of tracing the caller.

## Run

```powershell
python reset_fixture.py work
python -m unittest discover -s work\tests -t work
```

The seed should fail. A correct candidate patch should make the visible test
pass without changing the expected value.

## Score

```powershell
python score_run.py work
```

This fixture proves only that the repo can host executable protocol-targeted
evals. It does not prove model uplift by itself.
