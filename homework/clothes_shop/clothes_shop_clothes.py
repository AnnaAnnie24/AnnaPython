from clothes_source import (print_clothes_list,
                            get_clothes_price)

print("Welcome To Annie's Clothes Shop!!")

print_clothes_list()
clothes = input("What Piece Of Clothing Would You Like?? ")
clothes_price = get_clothes_price(clothes)

total = clothes_price

print("Your total will be:", total)
