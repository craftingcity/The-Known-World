AlchemicalMotifs = [
    "earth",
    "water",
    "fire",
    "air",
    "healing",
    "disease",
    "illusion",
    "light",
    "arcana",
    "weight",
    "form",
    "poison",
    "desist",
    "divine",
    "regenerate",
    "necrot",
    "degenerate",
    "fabrim",
    "charm",
    "evoke",
    "immute",
    "dunam",
    "immort",
    "dragon",
    "mortal",
    "abjure",
    "bane",
    "spirit"
]

combonations = 0

for FirstMotif in AlchemicalMotifs:
    sayFirst = FirstMotif
    for SecondMotif in AlchemicalMotifs:
        saySecond = SecondMotif
        combonations += 1
        print(f"{combonations}; {sayFirst} {saySecond}")

waitForInput = input("\n...")