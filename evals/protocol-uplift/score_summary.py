import json
from pathlib import Path


def mean(values):
    return sum(values) / len(values)


def task_total(score):
    if isinstance(score, dict):
        if "total" in score:
            return score["total"]
        return (
            score.get("functional", 0)
            + score.get("protocol", 0)
            + score.get("reporting", 0)
        )
    return score


data = json.loads(Path("scores.json").read_text(encoding="utf-8"))
means = {}
success_rates = {}
for key, condition in data["conditions"].items():
    values = [task_total(score) for score in condition["scores"].values()]
    means[key] = mean(values)
    success_rates[key] = mean([1 if value >= 80 else 0 for value in values])

protocol_uplift = means["L1"] - means["L0"]
stronger_gap = means["S0"] - means["L0"]
gap_closure = protocol_uplift / max(1, stronger_gap)
success_uplift = success_rates["L1"] - success_rates["L0"]

print(f"L0 mean: {means['L0']:.1f}")
print(f"L1 mean: {means['L1']:.1f}")
print(f"S0 mean: {means['S0']:.1f}")
print(f"Protocol uplift: +{protocol_uplift:.1f} points")
print(f"Success uplift: {success_uplift:+.0%}")
print(f"Gap closure vs stronger model: {gap_closure:.0%}")
print(f"L1 as percent of S0: {means['L1'] / means['S0']:.1%}")

if max(means.values()) - min(means.values()) < 10:
    print("Claim level: directional only; score range suggests saturation/ceiling risk.")
elif protocol_uplift >= 5 and success_uplift >= 0.10:
    print("Claim level: candidate supported local improvement, pending executable artifacts.")
else:
    print("Claim level: preliminary directional evidence.")
