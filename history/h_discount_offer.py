# Task 5: Discount Offer at a Store.
# A store offers a discount for customers who buy more than 10 items or spend more than
# $100. Write a program that asks for the number of items and the total bill amount. If the
# conditions are met, print "Discount Applied", otherwise print "No Discount".
amount_of_items = input("How many items are you willing to purchase?? ")
cost_of_items = input("How much do all those items (or that item) cost?? ")
amount_of_items = int(amount_of_items)
cost_of_items = int(cost_of_items)
if amount_of_items >= 10 or cost_of_items >= 100:
    print("Discount Applied")
else:
    print("No Discount Applied")
