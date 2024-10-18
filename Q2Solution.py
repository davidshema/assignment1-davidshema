#Solution to question 2 goes here
def identify_mushroom():
    mushrooms = {
        "Agaric jaunissant": {"gills": True, "forest": False, "ring": True, "convex_cup": True},
        "Cepe de bordeaux": {"gills": False, "forest": True, "ring": False, "convex_cup": False},
        "Amanite tue-mouche": {"gills": True, "forest": True, "ring": True, "convex_cup": True},
        "Coprin chevelu": {"gills": True, "forest": False, "ring": True, "convex_cup": False},
        "Girolle": {"gills": True, "forest": True, "ring": False, "convex_cup": False},
        "Pied Bleu": {"gills": True, "forest": True, "ring": False, "convex_cup": True}
    }

    def ask_question(question, key):
        answer = input(f"{question} (yes/no): ").strip().lower()
        if answer == "yes":
            return {name: details for name, details in mushrooms.items() if details[key] == True}
        elif answer == "no":
            return {name: details for name, details in mushrooms.items() if details[key] == False}
        else:
            print("Please answer 'yes' or 'no'.")
            return ask_question(question, key)

    mushrooms = ask_question("Does your mushroom have gills?", "gills")
    if len(mushrooms) == 1:
        print(f"The mushroom is: {list(mushrooms.keys())[0]}")
        return

    mushrooms = ask_question("Does your mushroom grow in a forest?", "forest")
    if len(mushrooms) == 1:
        print(f"The mushroom is: {list(mushrooms.keys())[0]}")
        return

    mushrooms = ask_question("Does your mushroom have a ring?", "ring")
    if len(mushrooms) == 1:
        print(f"The mushroom is: {list(mushrooms.keys())[0]}")
        return

    mushrooms = ask_question("Does your mushroom have a convex cup?", "convex_cup")
    if len(mushrooms) == 1:
        print(f"The mushroom is: {list(mushrooms.keys())[0]}")
    else:
        print("Unable to determine the mushroom.")

identify_mushroom()
