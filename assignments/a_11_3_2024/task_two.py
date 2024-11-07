animals_classification = {
    "Lion": "Mammal",
    "Eagle": "Bird",
    "Shark": "Fish",
    "Frog": "Amphibian",
    "Cobra": "Reptile",
    "Elephant": "Mammal",
    "Salmon": "Fish",
    "Iguana": "Reptile",
    "Dolphin": "Mammal",
    "Penguin": "Bird"
}
# TODO: write a code with for cycle to print out only Mammals
for animal, classification in animals_classification.items():
    if classification == "Mammal":
        print(animal)
values = list(animals_classification.values())
mammals = values.count("Mammal")
print("=-==-=-=-==-=-=-=-=-=-")
print(mammals, "mammals")
print("=-==-=-=-==-=-=-=-=-=-")
