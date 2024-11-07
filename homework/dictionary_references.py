# clear() - Removes all items from the dictionary
# import key

flowers_colors = {
    "Rose": "Red",
    "Sunflower": "Yellow",
    "Tulip": "Pink",
    "Lily": "White",
    "Orchid": "Purple",
    "Daisy": "White",
    "Marigold": "Orange",
    "Hydrangea": "Blue",
    "Peony": "Peach",
    "Cherry Blossom": "Pink"
}
# TODO: count how many time color Pink appear in a list
values = list(flowers_colors.values())
pink_flowers = values.count("Pink")
print("=-==-=-=-==-=-=-=-=-=-")
print(pink_flowers, "pink flowers!!")
print("=-==-=-=-==-=-=-=-=-=-")

# copy() - Returns a shallow copy of the dictionary
kids_books_genres = {
    "Where the Wild Things Are": "Picture Book",
    "Charlotte's Web": "Classic",
    "The Very Hungry Caterpillar": "Picture Book",
    "Harry Potter and the Sorcerer's Stone": "Fantasy",
    "The Cat in the Hat": "Rhyming",
    "Goodnight Moon": "Picture Book",
    "Matilda": "Fantasy",
    "Pete the Cat: I Love My White Shoes": "Picture Book",
    "The Gruffalo": "Picture Book",
    "Winnie-the-Pooh": "Classic"
}
# TODO: find the longest key!
longest = None
for key in kids_books_genres.keys():
    if longest is None:
        longest = key
    else:
        if len(key) > len(longest):
            longest = key

print(kids_books_genres)

# fromkeys() - Creates a dictionary from the given sequence
disney_princesses = {
    "Snow White": "Kind, innocent, and optimistic.",
    "Cinderella": "Gentle, resilient, and hopeful.",
    "Aurora": "Dreamy, romantic, and caring.",
    "Ariel": "Adventurous, curious, and passionate.",
    "Belle": "Intelligent, brave, and compassionate.",
    "Jasmine": "Independent, strong-willed, and adventurous.",
    "Pocahontas": "Wise, free-spirited, and connected to nature.",
    "Mulan": "Brave, determined, and selfless.",
    "Tiana": "Hardworking, ambitious, and practical.",
    "Rapunzel": "Creative, optimistic, and curious."
}
# ✅ delete a key-value pair with the shortest key
shortest = None
for key in disney_princesses.keys():
    if shortest is None:
        shortest = key
    else:
        if len(key) < len(shortest):
            shortest = key
disney_princesses.pop(shortest)
print(disney_princesses.keys())

flowers_colors = {
    "Rose": "Red",
    "Sunflower": "Yellow",
    "Tulip": "Pink",
    "Lily": "White",
    "Orchid": "Purple",
    "Daisy": "White",
    "Marigold": "Orange",
    "Hydrangea": "Blue",
    "Peony": "Peach",
    "Cherry Blossom": "Pink"
}
# TODO: print only those key-value pairs having Purple or White or Pink color value
# "Tulip - Pink"
# "Lily - White"
# "Orchid - Purple"
# "Daisy - White"
# "Cherry Blossom - Pink"

seq = ("Rose", "Sunflower", "Tulip", "Lily", "Orchid", "Daisy", "Marigold", "Hydrangea", "Peony", "Cherry Blossom")
values = ("Red", "Yellow", "Pink", "White", "Purple", "White", "Orange", "Blue", "Peach", "Pink")
fc = disney_princesses.fromkeys(seq, values)
print(fc)
values = list(flowers_colors.values())
pink_flowers = values.count("Pink")
print("=-==-=-=-==-=-=-=-=-=-")
print(pink_flowers, "pink flowers!!")
print("=-==-=-=-==-=-=-=-=-=-")
values = list(flowers_colors.values())
yellow_flowers = values.count("Yellow")
print("=-==-=-=-==-=-=-=-=-=-")
print(yellow_flowers, "yellow flowers!!")
print("=-==-=-=-==-=-=-=-=-=-")
answer = input("Name a color for a flower - ")

# get() -  Returns the value for the given key
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
lion_classification = animals_classification["Lion"]
print(lion_classification)

# items() - Return the list with all dictionary keys with values
harry_potter_characters = {
    "Harry Potter": "Gryffindor",
    "Hermione Granger": "Gryffindor",
    "Ron Weasley": "Gryffindor",
    "Draco Malfoy": "Slytherin",
    "Luna Lovegood": "Ravenclaw",
    "Neville Longbottom": "Gryffindor",
    "Cedric Diggory": "Hufflepuff",
    "Ginny Weasley": "Gryffindor",
    "Severus Snape": "Slytherin",
    "Minerva McGonagall": "Gryffindor"
}
items = harry_potter_characters.items()
print(harry_potter_characters)

# keys() - Returns a view object that displays a list of all the keys in the dictionary in order of insertion
avril_lavigne_songs = {
    "Complicated": 30_000_000,
    "Sk8er Boi": 25_000_000,
    "Girlfriend": 35_000_000,
    "I'm with You": 20_000_000,
    "My Happy Ending": 18_000_000,
    "Nobody's Fool": 15_000_000,
    "When You're Gone": 12_000_000,
    "Keep Holding On": 10_000_000,
    "What the Hell": 14_000_000,
    "Head Above Water": 8_000_000
}
dict.keys(avril_lavigne_songs)
print(avril_lavigne_songs)

# pop() - Returns and removes the element with the given key
snacks_calories = {
    "Potato Chips": 150,
    "Chocolate Bar": 220,
    "Granola Bar": 100,
    "Popcorn (butter)": 300,
    "Pretzels": 110,
    "Ice Cream (vanilla)": 200,
    "Fruit Snacks": 80,
    "Cheese Crackers": 150,
    "Trail Mix": 200,
    "Cookies": 150
}
snacks = snacks_calories.pop("Cheese Crackers")
print(snacks_calories)

# popitem() - Returns and removes the key-value pair from the dictionary
landmarks_views = {
    "Eiffel Tower": "Offers panoramic views of Paris.",
    "Statue of Liberty": "Stunning views of New York Harbor and the skyline.",
    "Machu Picchu": "Spectacular vistas of ancient ruins surrounded by mountains.",
    "Great Wall of China": "Breathtaking views of mountainous terrain and countryside.",
    "Burj Khalifa": "Breathtaking views of Dubai from the observation decks."
}
landmarks_views.popitem()
print(landmarks_views)

# setdefault() - Returns the value of a key if the key is in the dictionary else inserts the key with a value to the dictionary
popular_online_games = {
    "Fortnite": 80_000_000,
    "Roblox": 202_000_000,
    "Minecraft": 140_000_000,
    "Call of Duty: Warzone": 100_000_000,
    "Among Us": 20_000_000
}
key = popular_online_games
# dict.setdefault(key, popular_online_games)

# values() - Returns a view object containing all dictionary values, which can be accessed and iterated through efficiently
popular_foods = {
    "Pizza": ["Dough", "Tomato sauce", "Cheese", "Toppings (pepperoni, vegetables, etc.)"],
    "Sushi": ["Rice", "Nori (seaweed)", "Fish", "Vegetables", "Soy sauce"],
    "Tacos": ["Tortillas", "Meat (beef, chicken, or beans)", "Cheese", "Lettuce", "Salsa"],
    "Pasta": ["Noodles", "Tomato sauce", "Cheese", "Vegetables", "Meat"],
    "Burgers": ["Bun", "Beef patty", "Lettuce", "Tomato", "Cheese", "Condiments"]
}
popular_foods.values()

# update() - Updates the dictionary with the elements from another dictionary or an iterable of key-value pairs. With this method, you can include new data or merge it with existing dictionary entries
mystical_animals = {
    "Unicorn": "Can purify water and heal ailments with its horn.",
    "Dragon": "Possesses the ability to fly, breathe fire, and hoard treasure.",
    "Phoenix": "Can be reborn from its ashes, symbolizing immortality and renewal.",
    "Griffin": "Combines the strengths of a lion and an eagle, known for guarding treasures.",
    "Mermaid": "Has the ability to communicate with sea creatures and control water."
}
 # dict.update([mystical_animals])
# ??????
singers_net_worth = {
    "Taylor Swift": "$400 million",
    "Adele": "$220 million",
    "Drake": "$250 million",
    "Beyoncé": "$500 million",
    "Rihanna": "$1.7 billion",
    "Justin Bieber": "$300 million",
    "Katy Perry": "$330 million",
    "Eminem": "$230 million",
    "Lady Gaga": "$320 million",
    "Bruno Mars": "$175 million"
}