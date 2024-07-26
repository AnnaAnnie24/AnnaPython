
# print("The sum of" + (number_one) + "and" + number_two + "is" + number_one + number_two + "!!!")
# Task 7: Area of Circle Calculator
# Write a program that calculates the area of a circle given its radius.
radius = 20
diameter = 40
print(3.14 * (radius * 2))
# Task 8: Check leap year
# Develop a program that checks whether a year entered by the user is a leap year or not.
current_year = input("What is the year?? ")

if current_year % 4 == 0 and current_year % 100 >= 0:
    print(current_year, "is a leap year")
elif not current_year % 4 == 0:
    print(current_year, "is not a leap year")
# Task 9: Metric convertor
# Create a program to convert meters to inches.

# Task 10: Season descriptor
# Write a program that describes a season entered by a user.
users_season = input("What season is it?? ")
if users_season == "Winter":
    print("In winter it is cold, it usually snows. Children participate in winter activities, "
          "which are snow boarding, skiing, building snowman, drinking hot co-co, and more!!")
elif users_season ("Spring"):
    print("In spring, flowers begin to grow, more rain. The weather in spring is warm. "
          "Children play in the grassy meadows")

elif users_season ("Summer"):
    print("In the summer it is hot, the bright sun shines on your face. "
           "Children eat ice-cream, have fun at water-parks, and they even get a summer break!!")

elif users_season ("Autumn"):
    print("Autumn is a very calm and cool season. "
          "Leaves are changing colors from green to red or brown or orange or even yellow."
          "Children usually love collecting those leaves and making awesome pictures from them.")

# Task 11: Math quiz
# Ask a user to answer several math ques3ons. Grade a user according to results.
# Extra
# Give a user 2 aQempts: user can try to answer again if he (or she) failed the first 3me.
print("Hello, welcome to the math quiz!!!")
user_pick = input("Please pick a level:"
      "Hard: very difficult"
      "Medium: not hard but not easy"
      "Easy: very simple")
if user_pick == "medium":
    input("What is 6 * 4")
    input("What is 90 / 3")
    input("What is 5+4-6")
elif user_pick == "hard":
    input("What is (24/3)*6")
    input("What is 24 * 4")
    input("If a diameter is 64 what is the radius")
elif user_pick == "easy":
    input("What is 23 + 6")
    input("What is 6 * 2")
    input("What is 24 - 3")

# Task 12: Guess my birthday
# Create a program where user is trying to guess your birthday date.
# Extra 1
# Give user an infinite number of atempts.
# Extra 2
# ASer each incorrect guess give user a hint like: “My birthday is earlier” and “My
print("Hello welcome to the infinite birthday guesser!!! 🥳")
answer = input("Guess my birthday:")
if answer == "9/24" or answer == "24th September" or answer == "September 24th" or answer == "24th september" or answer == "september 24th":
    print("You're correct!!! 🥳")
else:
    print("You're incorrect!!! 😔")
