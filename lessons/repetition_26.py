"""
We need to repeat:
1. Modulo operator
2. str concatenation
3. str times int
4. int power operand
5. all the comparison operator
"""

x = 3 * 5  # 15

x = 12 / 5  # 2.4

x = 12 // 5  # 2

x = 12 % 5  # 2

a = 5
b = 8
c = b - a  # 3

c = 2 * c + 1  # 7

a = "A"
b = "B"
c = a + b  # ("A" + "B")

print("A" + "B")

# about str
c = 5 * a  # ("5" + "a")
print(c)   # AAAAA

# x = 6³
x = 6 ** 3 # 216

if 5 != 4 and 6 == 30 % 12:
    print("A")
elif 5 - 6 == 0:
    print("B")
else:
    print("C")
