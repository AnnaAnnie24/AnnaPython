from clothes_source import (print_clothes_list,
                            get_clothes_price,
                            display_clothes)

print("Welcome To Annie's Clothes Shop!!")

print_clothes_list()
total = 0
while True:
    clothes = input("What Piece Of Clothing Would You Like?? ")
    clothes = int(clothes)
    if clothes > 8 or clothes < 1:
        print("Try Again Please...")
        clothes = input("What Piece Of Clothing Do You Want?? ")
    else:
        clothes_price = get_clothes_price(clothes)
        total = total + clothes_price
        display_clothes(clothes)
        answer = input("Do you want to continue shopping?? ")
        if answer == "Yes":
            continue
        else:
            break


print("Your total will be:", round(total, 2))
