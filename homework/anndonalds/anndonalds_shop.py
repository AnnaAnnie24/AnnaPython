from anndonalds_source import (print_anndonalds_list,
                               display_menu,
                               get_food_price,
                               )

print("Welcome To AnnDonalds!!")

print_anndonalds_list()
total = 0
while True:
    food = input("What Would You Like To Eat?? ")
    if not food.isnumeric():
        print("Oops... I expect you to enter a number")
        continue
    food = int(food)
    if food > 12 or food < 1:
        print("Try Again Please...")
        food = input("What Food Can I Get You?? ")
    else:
        food_price = get_food_price(food)
        total = total + food_price
        display_menu(food)
        answer = input("Do you want to continue buying food?? ")
        if answer == "Yes":
            continue
        else:
            break


print(f"Your total will be: {round(total, 2)}$")
