# Task 1: Age Checker for Movie
# Write a program that asks the user for their age. If they are 16 or older they can watch a
# movie.
age = input("We need your age to determine if you can watch Life Of Horrors!!! "
            "What is your age?? ")
age = int(age)
if age >= 16:
    print("You are allowed to watch Life Of Horrors 🥳")
else:
    print("Sorry, you are not old enough to watch Life Of Horrors 😔")