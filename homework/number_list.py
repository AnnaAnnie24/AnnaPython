import random

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

random.shuffle(number_list)
number_list.append(346)
number_list.append(120)
number_list.insert(0, -263)
# value = number_list[6]
# print(value)  # You with get 7.
idx = number_list.index(15)
print(f"List = {number_list}")
print(f"index of number 15 is {idx}")
number_list.remove(10)
count = len(number_list)
print(count)
a = number_list[1]
print(a)
b = number_list[2]
print(b)
c = number_list[-1]
print(c)
number_list.reverse()
number_list[0] = 100
print(f"First element is 100: {number_list}")
number_list[2] = 20
number_list[4] = 20
number_list[-2] = 20
print(f"Some elements are 20: {number_list}")

number_list.sort()
print(number_list)

"""
Assignment:
1. Work with number_list (it must be shuffled)
    a) Add 2 big numbers to the end of the list☑️
    b) Add 1 negative number to the beginning of the list☑️
    c) Find index of number 15☑️
    d) remove number 10 from the list☑️
    e) print out number of elements in the☑️
    f) save first element to variable a; save second element to variable b; save the last element to variable c☑️
    g) reverse the order of elements☑️
    h) change the first element to 100☑️
    i) finally sort it!☑️
2. Create a dictionary of countries and its' populations. There must be 12 elements
"""


