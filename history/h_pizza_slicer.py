#  Task 5 “Pizza Slicing”
# Write a program that takes the number of people and pizzas as input. Using floor
# division (//), calculate how many slices each person gets equally, and modulo (%) to
# determine the leftover slices. Display the fair sharing and any extra slices!

print("I am The God Of Fairness For Slices Of Pizza!!!")
pizza_pies = input("How many pizza pies do you have?? ")
people = input("How many people do you have?? ")
people = int(people)
pizza_pies = int(pizza_pies)
print("Each person gets " + str(pizza_pies // people) + " slices or pies.")
