zoo = ["Elephant", "Giraffe", "Rhino", "Lion", "Penguins", "Tiger", "Panda", "Monkey"]


def print_zoo():
    print("\n" * 1)
    print(*zoo, sep=" | ")


def stuff():
    zoo[2] = "Zebra"

    second_animal = zoo[1]
    print(second_animal)

    third_animal = zoo[2]
    print(third_animal)

    forth_animal = zoo[3]
    print(forth_animal)

    five_animal = zoo[4]
    print(five_animal)

    six_animal = zoo[5]
    print(six_animal)

    seven_animal = zoo[6]
    print(seven_animal)

    eight_animal = zoo[7]
    print(eight_animal)

    ninth_animal = zoo[8]
    print(ninth_animal)

    # how to add a Rhino to our zoo? [names_of_the_list].append(value)

    number_of_animals = len(zoo)
    print(number_of_animals, "animals in the zoo.")


# get the value from the list: the first animal
#  first_animal = zoo[0]
#  print(first_animal)

zoo.append("Rhino")
# How to get rid of the first animal
zoo.pop(0)

print_zoo()

'''
What can we do with lists?
 • Can store more than one variable
 • add a value to the end of the list via .append(value) method and replace one
 • check where the value is already in the list or in two of the lists
 • we can remove the value by index using .pop()
 • Everything is the same and list can just do cool stuff
 • lists is a list
 • Done
'''
