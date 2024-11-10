"""
Megan is celebrating her birthday!
She has some number of balloons (user can enter this number).
There are some number of guests on her party (user can enter this number).
She decided to give away all her balloons for guests.
Questions:
 • how many balloons will be per guest           x
 • how many balloons you need to pop to be fair  y
"""
number_of_balloons = input("How many balloons will you buy for Megan's party?? ")
number_of_guests = input("How many guests will be arriving?? ")
b = number_of_balloons
g = number_of_guests
b = int(b)
g = int(g)

x = b // g

y = b % g
if number_of_guests == 0:
    print("Poor Megan, No guests")
elif number_of_balloons == 0:
    print("Poor Megan, No balloons")
elif g > b:
    print("More people than balloons.")
elif g < 0 or b < 0:
    print("Check your input. Number should be greater tha  zero.")
else:
    print(x, "balloons each guest receive.")
    print(y, "balloons to pop.")
