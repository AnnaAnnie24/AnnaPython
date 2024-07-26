#  Homework
# Create a simple calculator that can perform basic arithmetic operations like addition,
# subtraction, multiplication, and division.
# Hint
# You should use input 3 times, and definitely if-else statement.

# Python data types: int, str, float, bool
name = input("Please Enter Your Name:")
print("Hello " + name + ", welcome to the simple calculator!")
number_1 = input("Please enter your first number:")
user_option = input("What type of arithmetic operation would you like to use??")
number_2 = input("Please enter your second number: ")
number_1 = int(number_1)
number_2 = int(number_2)
if user_option == "*":
    print("Multiplication," + str(number_1 * number_2) + "")
elif user_option == "-":
    print("Subtraction," + str(number_1 - number_2) + "")
elif user_option == "+":
    print("Addition," + str(number_1 + number_2) + "")
elif user_option == "/":
    print("Division," + str(number_1 / number_2) + "")
else:
    print("I'm sorry, I do not understand!!!")
