from anndonalds_menu import anndonalds_menu_dict


def print_anndonalds_list():
    """
    Shows all items from anndonalds_menu_dict with its prices
    """
    number = 1
    for name, price in anndonalds_menu_dict.items():
        print(f"Option {number}: {name} – ${price}")
        number += 1


def display_menu(option_number):
    count = 1
    for name, price in anndonalds_menu_dict.items():
        if option_number == count:
            print("You have purchased a", name)
            break
        else:
            count += 1


def get_food_price(clothes):
    number = int(clothes)
    count = 1
    for name, price in anndonalds_menu_dict.items():
        if number == count:
            return price
        else:
            count += 1
