# Task 4: Bank Loan Eligibility Checker
# Ask the user for their age and monthly income. If their age is greater than 21 and monthly
# income is greater than or equal to $3000, print "Eligible for loan", otherwise print "Not
# eligible for loan".
print("Welcome to Bank of America")
entrance = input("Please enter your age : ")
second_entrance = input("Please enter your monthly income : ")
entrance = int(entrance)
second_entrance = int(second_entrance)
if entrance >= 21 and second_entrance >= 3000:
    print("Eligible to loan")
else:
    print("Not eligible to loan")
