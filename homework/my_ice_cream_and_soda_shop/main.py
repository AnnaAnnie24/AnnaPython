from source import (print_soda_menu,
                    print_ice_cream_menu,
                    get_ice_cream_price,
                    get_soda_price,)

print("Welcome To Annie's Ice-Cream And Soda Shop!!")

print_ice_cream_menu()
ice_cream = input("What Ice-Cream Would You Like?? ")
ice_cream_price = get_ice_cream_price(ice_cream)

print_soda_menu()
soda = input("What Soda Would You Like?? ")
soda_price = get_soda_price(soda)

total = ice_cream_price + soda_price

print("Your total will be:", total)
