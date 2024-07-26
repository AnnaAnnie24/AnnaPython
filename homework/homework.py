barely_functioning_house = 1
million_dollar_house = 1_000_000
million_dollar_house15 = 15_000_000
million_dollar_house30 = 30_000_000
million_mega_mansion45 = 45_000_000         # int - an integer number (whole number)
million_dollar_mansion69 = 69_000_000
most_luxurious_house_on_the_planet_mega_mansion = 100_000_000

print("barely_functioning_house = 1")
print(barely_functioning_house)
print(million_dollar_house)

mr_beast_bar = 5.49             # float - floating point number
height = 4.7
maks_height = 1.82 * 3.28              # float data type
print(maks_height)
date = 18
year = 2023
month_name = "october"                 # str

print(month_name)                       # str - string


# homework

# 1. Determine if a number is even
print("task 1")
# 5 odd numbers: 5, 3, 7, 11, 15
# 5 even numbers: 2, 4, 6, 8, 10

number = 6
print("number modulo 2 = ", number % 2)


# 2. Check if a number is greater than 10
print("task 2")
true_or_false: bool = 10 > 34
print(true_or_false)
# 3. Determine if a persons age is under 10, between 10
# 4. Determine whether 2 + 11 is greater than 14
print("task 4")
print(2 + 11 < 14)
# 5. If the temperature is above 25 degrees, print "hot" otherwise print "cold"
print("task 5")
temperature = 25
if temperature <= 25:
    print("Hot")
if temperature >= 26:
    print("Cold")
# 6. Check is a number is positive
# number is called positive if it's values is greater than zero: number > 0
print("task 6")
number = 34
if number > 0:
    print(number, "is a positive number.")
elif number < 0:
    print(number, "is a negative number.")


# 7. Determine whether person adult or young (adult is 20 years or more)
print("task 7")
age_of_bob = 22
adult_text = "You are an adult!!! 🥳 "
child_text = "You are a child!!! 🥳"
if age_of_bob <= 19:
    print(child_text)
if age_of_bob >= 20:
    print(adult_text)
#
#
#
#
#



# Homework
# 1.Write a program to calculate the total cost of five
# items with different prices.
pencil_pack = 2.99
notebook = 3.45
crayons = 2.99
pencil_case = 3.99
high_lighter_pack = 4.23

print("Price :", pencil_case + notebook + crayons + pencil_pack + high_lighter_pack,"dollars.")

# 2.Compute the average temperature from a list past
# three days measurements
Temp_1 = 64
Temp_2 = 23
Temp_3 = 92
print("The Average temperature of the 3 days is", (Temp_1 + Temp_2 + Temp_3)/3, "degrees in fahrenheit.")

# 3. Convert a distance given in kilometers to miles (1 km =
# 0.621371 miles).
one_km = 0.621371
number_of_km = 5
print("Number of miles per km :", one_km * number_of_km,)


# 5. Calculate the total duration in hours and minutes
# given start and end times.
time = 156
time_now = 314
hour = 60
half_an_hour = 30
minutes_in_an_hour = 60
print("Time =", time_now - time,)

# 6. Distribute a given number of candies to a specific
# number of children evenly and find out how many candies are left.
children = 13
number_of_candies = 64
print("Number of candies per child =", number_of_candies // children)
print("Number of candies left over =", number_of_candies % children)

# 7. Given a day number, determine the weekday (assuming
# day 1 is Monday).
today = 1
txt = "Today is "
if today == 1:
    print(txt+"Monday!!")
elif today == 2:
    print(txt+"Tuesday!!")
elif today == 3:
    print(txt+"Wednesday!!")
elif today == 4:
    print(txt+"Thursday!!")
elif today == 5:
    print(txt+"Friday!!")
elif today == 6:
    print(txt+"Saturday!!")
elif today == 7:
    print(txt+"Sunday!!")
else:
    print("You have done a mistake!! I don't a weekday with number", today)

# 8. Determine how many hours and minutes are left until
# the end of the day, if the current time is known
day = 24*60
current_time = 2118
minutes_in_current_time = current_time%100
hours_in_current_time = current_time//100
time = hours_in_current_time*60+minutes_in_current_time
remaining_time = day-time
hours = remaining_time//60
minutes = remaining_time % 60
print("If it's", current_time, "o'clock right now, then there's still", hours, "hours and", minutes, "minutes till midnight.")

# 9. Given a number of items and a group size, determine how
# many groups can be formed and how many items are left ungrouped.
number_of_people = 45
number_of_people_per_group = 6
print("Number of people with a group :", number_of_people//number_of_people_per_group)
print("Number of people left without a group :", number_of_people % number_of_people_per_group)

# 10. Check if a given year is a leap year (Hint: A year is a leap
# year if it is divisible by 4 but not by 100 unless it is also divisible by 400).
current_year = 2000

if current_year % 4 == 0 and current_year % 100 >= 0:
    print(current_year, "is a leap year")
elif not current_year % 4 == 0:
    print(current_year, "is not a leap year")