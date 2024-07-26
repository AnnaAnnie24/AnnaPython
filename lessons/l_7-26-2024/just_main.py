flowers = ["Lavender", "Rose", "Marigold", "Daisy", "Sunflower", "Dahlia", "Peony", "Lily", "Orchid", "Poppy"]

# Print out each flower with long names (long name has 6 or more letters in it)

for flower in flowers:
    if len(flower) >= 6:
        print(flower)


# Print out each flower, which names is starting with 'D'
Dee = "D"
for flower in flowers:
    if flower[0] == Dee:
        print(flower)
