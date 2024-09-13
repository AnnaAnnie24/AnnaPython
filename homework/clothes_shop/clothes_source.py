from stuff import clothes_dict


def print_clothes_list():
    number = 1
    for name, price in clothes_dict.items():
        print(f"Option {number}: {name} – ${price}")
        number += 1


def display_clothes(option_number):
    count = 1
    for name, price in clothes_dict.items():
        if option_number == count:
            print("You have purchased a", name)
            break
        else:
            count += 1


def get_clothes_price(clothes):
    number = int(clothes)
    count = 1
    for name, price in clothes_dict.items():
        if number == count:
            return price
        else:
            count += 1
