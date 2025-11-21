from .rules import RULES, CONCERN_ADDONS

def recommend(skin_type, concern, avoid_alcohol=False):
    base_steps = RULES.get(skin_type, ["gentle cleanser", "moisturizer", "spf 30+"])
    addons = CONCERN_ADDONS.get(concern, [])
    routine = base_steps + addons

    if avoid_alcohol:
        routine.append("note: avoid denatured alcohol in ingredient lists")

    return routine
