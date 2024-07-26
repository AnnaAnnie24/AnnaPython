"""
Home Work
1. Create a variable for your favorite animal name. Print out each letter on separate line
2. Create a long list of flowers. Print out each flower with a 1) before each name.
3. Write a code to print out only flowers having less than 6 letters in the name.
"""

animals = ["dog", "cat", "cow", "pig", "lion", "zebra", "horse", "elephant", "monkey", "chicken"]
# Task: print out each animal name that has 5 or more letters in the name
for animal in animals:
    number_of_letters = len(animal)
    if number_of_letters >= 5:
        print(animal)

# number = 1
# for animal in animals:
#     number_with_period = str(number) + ". "
#     text = number_with_period + animal
#     print(text)
#     number = number + 1
# repetitions
# color = "Orange"

# print out each individual letter on a separate line
# Way 1.
# print("Way 1")
# letter = color[0]
# print(letter)
# letter = color[1]
# print(letter)
# letter = color[2]
# print(letter)
# letter = color[3]
# print(letter)
# letter = color[4]
# print(letter)
# letter = color[5]
# print(letter)
#
# # Way 2.
# print("Way 2")
# for letter in color:
#     print(letter)

