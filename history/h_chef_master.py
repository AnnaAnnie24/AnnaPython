# Task 1 “How many ingredients for a soup” Write a program that takes an input from the user as a
# number of "servings" for a
# recipe and adjusts the ingredient quantities proportionately. One serving of soup
# requires:
# • 0.54 ounces of potato
# • 0.5 ounces of rice
# • 0.2 ounces of carrot
# • 0.35 ounces of chicken meat
# • quarter teaspoon of salt
# • half of a teaspoon of pepper
servings = input("Hello, Welcome To Chef Master. Please enter your amount of servings for soup : ")
servings = int(servings)

# calculations
potato = 0.54 * servings
rice = 0.5 * servings
carrots = 0.2 * servings
chicken = 0.35 * servings
salt = 0.25 * servings
pepper = 0.5 * servings
# make numbers prettier
potato = round(potato, 2)
carrots = round(carrots, 2)
rice = round(rice, 2)
chicken = round(chicken, 2)
salt = round(salt, 2)
pepper = round(pepper, 2)
# convert into text
potato = str(potato)
rice = str(rice)
carrots = str(carrots)
chicken = str(chicken)
salt = str(salt)
pepper = str(pepper)
print("For " + str(servings) + " servings you need:")
print("Potato: " + potato + " ounces")
print("Rice: " + rice + " ounces")
print("Chicken: " + chicken + " ounces")
print("Carrots: " + carrots + " ounces")
print("Salt: " + salt + " teaspoons")
print("Pepper: " + pepper + " teaspoons")
