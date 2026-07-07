import shutil
import sys
from pathlib import Path


def main():
    if len(sys.argv) != 2:
        print("usage: python reset_fixture.py <target-dir>")
        return 2

    root = Path(__file__).resolve().parent
    target = Path(sys.argv[1]).resolve()
    seed = root / "seed"

    try:
        target.relative_to(root)
    except ValueError:
        print("target must be inside this fixture directory")
        return 2

    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(seed, target)
    print(f"reset {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
