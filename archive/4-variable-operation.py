# multiplication
# division (true division)
# subtraction
# addition
# fair division (integer division)
# modulo operation
import random

# we've bought 15 candies and paid for them $1, How many does one candy cost?
a = 23      # balloon
b = 4       # people
c = a // b
# fair division (integer division) - it is the largest whole number smaller than the result of a / b
# modulo operation - it is used to get a remainder of fair division
print(c)

print("True division:", 17 / 3)
print("Fair division:", 17 // 3)        # 5
print("    Modulo op:", 17 % 3)          # 2

a = 45
b = 5

print(f"{a} and {b}")
print("True division:", a / b)          # 5
print("Fair division:", a // b)         # 5
print("    Modulo op:", a % b)          # 0

g = 0.1111111111111111
result = g * 9
print("result:", result)

print(17 / 0.00000001)

# even - can be divided by 2

x = random.randint(20, 70)

print("Is", x, "odd?")
print(bool(x % 2))


