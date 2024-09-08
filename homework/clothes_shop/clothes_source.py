from stuff import clothes_dict
def print_clothes_list():
    number = 1
    for name, price in clothes_dict.items():
        print(f"Option {number}: {name} – ${price}")
        number += 1

def get_clothes_price(clothes):
    number = int(clothes)
    count = 1
    for name, price in clothes_dict.items():
        if number == count:
            return price
        else:
            count += 1
