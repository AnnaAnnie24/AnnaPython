# modulo operator
import random

cookies = 37
friends = 5

print("Each friend will get", cookies // friends, "cookies")
print(cookies % friends, "cookies left over")

number = 6
two = 2
leftover = number % two

# is number odd or even?
if leftover == 0:
    print("Even!!! :)")
else:                       # leftover == 1
    print("Odd!!! :)")

# 43 // 8 = 5
# divided // divisor = result
# 43 % 8 = 3

number = random.randint(3, 35) * 5

print("number", '=', number)
leftover = number % 10
print("leftover =", leftover)
if leftover == 0:
    print(number, "is divisible by 10")
else:
    print(number, "isn't divisible by ten")
