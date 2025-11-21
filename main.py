from engine.recommender import recommend

def ask(prompt, options):
    answer = input(prompt).strip().lower()
    if answer not in options:
        print("Pick one of:", ", ".join(options))
        return ask(prompt, options)
    return answer

if __name__ == "__main__":
    print("Skin Care System – quick quiz")

    skin_type = ask(
        "Skin type? (dry/oily/combination/normal/sensitive): ",
        {"dry", "oily", "combination", "normal", "sensitive"}
    )

    concern = ask(
        "Top concern? (acne/dryness/redness/dark-spots/dullness): ",
        {"acne", "dryness", "redness", "dark-spots", "dullness"}
    )

    avoid_alcohol = ask(
        "Avoid alcohol in products? (yes/no): ",
        {"yes", "no"}
    ) == "yes"

    routine = recommend(skin_type, concern, avoid_alcohol)

    print("\nYour suggested routine:")
    for step in routine:
        print("•", step)
