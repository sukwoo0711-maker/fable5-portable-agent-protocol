import unittest

from cart import invoice_total_cents


class InvoiceTotalTests(unittest.TestCase):
    def test_invoice_total_uses_quantity(self):
        lines = [
            {"sku": "A", "unit_price": 2.50, "quantity": 2},
            {"sku": "B", "unit_price": 3.50, "quantity": 1},
        ]

        total = invoice_total_cents(lines)

        self.assertEqual(total, 850)


if __name__ == "__main__":
    unittest.main()
