# Task 8: Check leap year
# Develop a program that checks whether a year entered by the user is a leap year or not.
current_year = input("What is the year?? ")
current_year = int(current_year)
if current_year % 4 == 0 and current_year % 100 >= 0:
    print(current_year, "is a leap year")
elif not current_year % 4 == 0:
    print(current_year, "is not a leap year")
