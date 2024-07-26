# Task 5: Posi;ve or Nega;ve Number Checker
# Create a program that determines if a number entered by the user is posi3ve or nega3ve.
text = input("Please enter your number?? ")       # str
number = int(text)
two = 2
leftover = number % two
if leftover == 0:
    print("Even!!! :)")
else:
    print("Odd!!! :)")

