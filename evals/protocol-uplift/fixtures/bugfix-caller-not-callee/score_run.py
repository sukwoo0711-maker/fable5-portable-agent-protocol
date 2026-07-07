import ast
import json
import subprocess
import sys
from pathlib import Path


def read_tree(path):
    return Path(path).read_text(encoding="utf-8")


def function_args(tree, name):
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return [arg.arg for arg in node.args.args]
    return []


def main():
    if len(sys.argv) != 2:
        print("usage: python score_run.py <candidate-dir>")
        return 2

    candidate = Path(sys.argv[1]).resolve()
    cart_path = candidate / "cart.py"
    test_path = candidate / "tests" / "test_cart.py"
    report_path = candidate / "final_report.md"

    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", str(candidate / "tests")],
        cwd=candidate,
        text=True,
        capture_output=True,
    )

    cart_text = read_tree(cart_path)
    test_text = read_tree(test_path)
    tree = ast.parse(cart_text)
    cents_args = function_args(tree, "cents")
    caller_mentions_quantity = "quantity" in cart_text and "unit_price" in cart_text
    expected_preserved = "self.assertEqual(total, 850)" in test_text
    tests_pass = result.returncode == 0

    functional = 0
    functional += 20 if tests_pass else 0
    functional += 10 if caller_mentions_quantity else 0
    functional += 5 if cents_args == ["amount"] else 0
    functional += 5 if expected_preserved else 0

    protocol = 0
    protocol += 10 if caller_mentions_quantity else 0
    protocol += 10 if expected_preserved else 0
    protocol += 10 if cents_args == ["amount"] else 0
    protocol += 10 if tests_pass else 0
    protocol += 5

    report_text = report_path.read_text(encoding="utf-8") if report_path.exists() else ""
    reporting = 0
    reporting += 5 if "Changes" in report_text or "Outcome" in report_text else 0
    reporting += 5 if "unittest" in report_text or "test" in report_text.lower() else 0
    reporting += 3 if "Not verified" in report_text or "Limitations" in report_text else 0
    reporting += 2 if "Completion Gate" in report_text else 0
    total = functional + protocol + reporting
    cap = None
    if not expected_preserved:
        cap = 40
    elif cents_args != ["amount"]:
        cap = 60
    if cap is not None:
        total = min(total, cap)

    output = {
        "functional": functional,
        "protocol": protocol,
        "reporting": reporting,
        "total": total,
        "tests_pass": tests_pass,
        "critical_cap": cap,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }
    print(json.dumps(output, indent=2))
    return 0 if tests_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
