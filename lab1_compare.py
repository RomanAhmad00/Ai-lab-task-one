# Lab 1: compare a rule-based decision with a probability threshold

def rule_based(score, complete):
    if complete and score >= 70:
        return "Review"
    return "Hold"

def probability_based(probability):
    if probability >= 0.70:
        return "Review"
    return "Hold"

cases = [
    ("complete_high", 82, True, 0.81),
    ("complete_low", 68, True, 0.74),
    ("incomplete_high", 91, False, 0.88),
    ("boundary", 70, True, 0.70),
]

print("case | rule | threshold | disagreement")
for name, score, complete, probability in cases:
    rule_result = rule_based(score, complete)
    probability_result = probability_based(probability)
    disagreement = rule_result != probability_result
    print(name, "|", rule_result, "|", probability_result, "|", disagreement)
