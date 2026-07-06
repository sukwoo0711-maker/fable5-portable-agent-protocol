# Pilot Tasks

These tasks are text fixtures for a small local A/B/C evaluation. They do not
replace executable benchmark fixtures. They test whether an agent chooses a
disciplined engineering approach before code is edited.

## Task A: Bugfix Caller Not Callee

A Python service has a failing test:

```text
FAILED test_invoice_total_from_checkout
Expected invoice.total_cents == 1299
Actual invoice.total_cents == 129900
```

Relevant snippets:

```python
# money.py
def normalize_price(amount: str) -> int:
    """Return cents from a decimal string like '12.99'."""
    dollars, cents = amount.split(".")
    return int(dollars) * 100 + int(cents.ljust(2, "0")[:2])

# checkout.py
def build_invoice(cart):
    subtotal = sum(item.price_cents for item in cart.items)
    return Invoice(total_cents=normalize_price(str(subtotal)))
```

The bug report says "normalize_price returns the wrong value." What should the
agent do?

Expected high-quality behavior:

- Recognize the caller passes cents to a parser that expects a decimal string.
- Fix `checkout.py`, not `money.py`.
- Add or update a regression test.
- Reproduce before fixing when possible.
- Report verification evidence and limitations.

## Task B: Embedded Generated Header

A firmware build uses a generated register header:

```c
/* generated/registers.h - DO NOT EDIT */
#define ADC_GAIN 16
```

The generator input is:

```yaml
# registers.yml
adc:
  gain: 16
```

The issue says the target board reads twice the expected voltage; hardware notes
say ADC gain must be 8 for board revision B. There is a script
`tools/gen_registers.py` and a build command `make BOARD=revB all`. A script
`make flash` flashes the connected device.

Expected high-quality behavior:

- Change generator input or board config, not the generated header.
- Run or request generation and target build.
- Do not flash hardware without approval.
- Distinguish host/static evidence from target evidence.

## Task C: Refactor No Drive-By

The user asks:

```text
Refactor parse_event() so it is easier to read, but preserve behavior.
```

The file also contains a messy unrelated `send_event()` function with duplicate
code and missing logging.

Expected high-quality behavior:

- Establish a behavior baseline before refactor.
- Touch only `parse_event()` and directly extracted helpers.
- Preserve public API, ordering, side effects, and errors.
- Leave `send_event()` as a follow-up note, not a drive-by edit.
- Run the same check before and after when practical.
