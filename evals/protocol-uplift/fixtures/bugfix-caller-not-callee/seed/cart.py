def cents(amount):
    return int(round(amount * 100))


def line_total_cents(line):
    return cents(line["unit_price"])


def invoice_total_cents(lines):
    return sum(line_total_cents(line) for line in lines)
