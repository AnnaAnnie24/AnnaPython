# Task 7: Bus Fare Calculator
# Calculate the bus fare where the regular fare is $2.50. Senior citizens (age 65 or older) or
# children (age 12 or below) get a fare of $1.00. Ask the user their age and print the
# corresponding fare.
print("Hello this is The Bus Fare Calculator!!!")
age_7 = input("What is your age?? ")
age_7 = int(age_7)
if age_7 <= 12 or age_7 >= 65:
    print("One Dollar Please... ")
else:
    print("Two Dollars And Fifty Cents Please... ")
