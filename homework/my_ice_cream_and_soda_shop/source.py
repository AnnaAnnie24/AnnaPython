from menu import ice_cream_dict, soda_dict


def print_ice_cream_menu():
    number = 1
    for name, price in ice_cream_dict.items():
        print(f"Option {number}: {name} – ${price}")
        number += 1


def print_soda_menu():
    number = 1
    for name, price in soda_dict.items():
        print(f"Option {number}: {name} – ${price}")
        number += 1


def get_ice_cream_price(ice_cream):
    number = int(ice_cream)
    count = 1
    for name, price in ice_cream_dict.items():
        if number == count:
            return price
        else:
            count += 1


def get_soda_price(soda):
    number = int(soda)
    count = 1
    for name, price in soda_dict.items():
        if number == count:
            return price
        else:
            count += 1
