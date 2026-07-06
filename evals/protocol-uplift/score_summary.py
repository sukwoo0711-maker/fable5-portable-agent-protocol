import json
from pathlib import Path


def mean(values):
    return sum(values) / len(values)


data = json.loads(Path("scores.json").read_text(encoding="utf-8"))
means = {}
for key, condition in data["conditions"].items():
    values = list(condition["scores"].values())
    means[key] = mean(values)

protocol_uplift = means["L1"] - means["L0"]
stronger_gap = means["S0"] - means["L0"]
gap_closure = protocol_uplift / max(1, stronger_gap)

print(f"L0 mean: {means['L0']:.1f}")
print(f"L1 mean: {means['L1']:.1f}")
print(f"S0 mean: {means['S0']:.1f}")
print(f"Protocol uplift: +{protocol_uplift:.1f} points")
print(f"Gap closure vs stronger model: {gap_closure:.0%}")
print(f"L1 as percent of S0: {means['L1'] / means['S0']:.1%}")
