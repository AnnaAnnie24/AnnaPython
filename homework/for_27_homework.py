animal = "turtle"
for letter in animal:
    print(letter)
flowers = ["Violet", "Daisy", "Rose", "Marigold", "Sunflower", "Lotus", "Poppy", "Waterlily", "Hibiscus",
           "Peony", "Zinnia", "Pansy", "Dahlia", "Jasmine", "Petunia", "Tulip", "Hyacinth", "Aster",
           "Daffodil", "Lavender", "Magnolia", "Lilac", "Cherry Blossom", "Primrose", "Dandelion", "Lily",
           "Honey Suckle", "Orchid", "Snow Drop", "Iris", "Bluebell", "Narcissus", "Carnation"]
number = 1
for flower in flowers:
    number_with_period = str(number) + ") "
    text = number_with_period + flower
    print(text)
    number = number + 1
for flower in flowers:
    number_of_letters = len(flower)
    if number_of_letters < 6:
        print(flower)
