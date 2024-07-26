# 5 options to buy an ice cream with smily faces
#
import sys

vanilla_bean = "Sweet vanilla ice cream, on a cone or a cup. 🍨☀️🏖️"
mint_chocolate_chip = "Peppermint mint ice cream, served with chocolate chips on top and a mint leaf. 🍫🍃🍦"
chocolate_brownie = "Chocolate brownie ice cream, served with a delicious brownie on top. 🍫🤎🍦"
cookie_dough = "Cookie dough ice cream, served with mini cookie dough pieces inside. 🍦🍪🏖️"
sweet_strawberry = "Strawberry ice cream, with strawberries and strawberry syrup on top. 🍓🍨🏖️"

"""
Plan:
User has a budget = $5
1) Ice cream for him
    1. Pick a flavor: 5 options
    2. Pick a size: 3 sizes: small, medium, large
2) Ice cream for his friend
"""

ice_cream_prices = [1.50, 2.50, 3.00, 3.00, 2.50]


def choose_an_ice_cream():
    print("\nOption 1: ", vanilla_bean,
          "\nOption 2: ", mint_chocolate_chip,
          "\nOption 3: ", chocolate_brownie,
          "\nOption 4: ", sweet_strawberry,
          "\nOption 5: ", cookie_dough, )
    chosen_option = input("What flavor would you like?? ")
    chosen_option = int(chosen_option)
    base_price = ice_cream_prices[chosen_option - 1]
    size = input("What size would you like?? ")
    if size == "small":
        user_icecream_price = base_price * 0.70
    elif size == "medium":
        user_icecream_price = base_price * 1.10
    elif size == "large":
        user_icecream_price = base_price * 1.50
    else:
        print("Sorry I don't understand, come back another time!!")
        sys.exit(0)  # finish program execution
    return user_icecream_price


# The program is going to be down here
print("\nChoose an icecream for yourself")
user_icecream_price = choose_an_ice_cream()
print("\nChoose an icecream for friend")
friends_icecream_price = choose_an_ice_cream()
total_price = user_icecream_price + friends_icecream_price
if total_price > 5:
    print("You have to pay", total_price, "dollars")
    print("But you only have $5!!!")
    print("You lose!! 😭")
else:
    print("You have to pay", total_price, "dollars")
    print("Enjoy your icecream!! ☺️")

### Homework: Same thing but about pizza.
