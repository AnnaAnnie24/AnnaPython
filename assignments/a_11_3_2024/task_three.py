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
# TODO: user enter the name of house - program print out all characters from that house
answer = input("Name a Harry Potter house: ")


for character, house in harry_potter_characters.items():
    if house == answer:
        print(character)


def manual_approach():
    if house == "Gryffindor":
        print("Harry Potter", "Hermonie Granger", "Ron Weasley", "Neville Longbottom", "Ginny Weasley",
              "Minerva McGonagall")
    elif house == "Hufflepuff":
        print("Cedric Diggory")
    elif house == "Ravenclaw":
        print("Luna Lovegood")
    elif house == "Slytherin":
        print("Draco Malfoy", "Severus Snape")
    else:
        print("Sorry I don't understand")
