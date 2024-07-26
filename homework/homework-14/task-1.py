#  Task 1 “Are you young”
# Ask a user to input his age. Then write the program that results in one of the following
# messages:
# 1) you’re probably going to school
# 2) you’re probably not going to school

age = input("What is your age?? ")
age = int(age)
if age <= 4:
    print("You are too young to go to school.")
elif age <= 18:
    print("You go to school!!!")
else:
    print("You do not go to school anymore.")
