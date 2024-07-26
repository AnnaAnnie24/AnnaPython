import sys

plain_pizza = "Just cheese, bread, and sauce."
pepperoni_pizza = "Plain pizza topped with pepperoni."
veggie_pizza = "Plain bread and cheese topped with carrots, broccoli, onions, and olives."
margherita_pizza = "Plain pizza topped with extra tomatoes and fresh basil."
bbq_pizza = "Plain pizza, but with alot of cheese topped with sweet BBQ chicken."

pizza_prices = [2.00, 2.50, 3.00, 2.75, 3.00]


def choose_a_pizza():
    print("\nOption 1: ", plain_pizza,
          "\nOption 2: ", pepperoni_pizza,
          "\nOption 3: ", veggie_pizza,
          "\nOption 4: ", margherita_pizza,
          "\nOption 5: ", bbq_pizza, )
    chosen_option = input("What pizza would you like?? ")
    chosen_option = int(chosen_option)
    base_price = pizza_prices[chosen_option - 1]
    size = input("What size would you like?? ")
    if size == "small":
        user_pizza_price = base_price * 0.80
    elif size == "medium":
        user_pizza_price = base_price * 1.20
    elif size == "large":
        user_pizza_price = base_price * 1.60
    else:
        print("Sorry I don't understand, come back another time!!")
        sys.exit(0)  # finish program execution
    return user_pizza_price


# The program is going to be down here
print("\nChoose a pizza for yourself")
user_pizza_price = choose_a_pizza()
print("\nChoose a pizza for friend")
friends_pizza_price = choose_a_pizza()
total_price = user_pizza_price + friends_pizza_price
if total_price > 6:
    print("You have to pay", total_price, "dollars")
    print("But you only have $6!!!")
    print("You lose!! 😭")
else:
    print("You have to pay", total_price, "dollars")
    print("Enjoy your pizza!! ☺️")
