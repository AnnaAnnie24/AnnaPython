# Ice Cream
ice_cream_dict = {
    "Vanilla": 1.5,
    "Chocolate": 1.5,
    "Strawberry": 1.5,
    "Mint Chocolate-Chip": 2.0,
    "Cookies And Cream": 2.0,
    "Cookie Dough": 2.0,
    "Mint": 1.8,
    "Cherry": 1.9,
}
soda_dict = {
    "Sprite": 1.0,
    "Coca-Cola": 1.0,
    "Fanta": 1.0,
    "Pepsi": 1.0,
    "Mountain Dew": 1.0,
    "Ginger Ale": 1.0,
}
print("Welcome To Annie's Ice-Cream And Soda Shop!!")
number = 1
for name, price in ice_cream_dict.items():
    print(f"Option {number}: {name} – ${price}")
    number += 1

ice_cream = input("What Ice-Cream Would You Like?? ")
ice_cream_price = get_ice_cream_price(ice_cream)

for name, price in soda_dict.items():
    print(f"Option {number}: {name} – ${price}")
    number += 1

soda = input("What Soda Would You Like?? ")
soda_price = get_soda_price(soda)

# We need a price for the selected ice cream
# We need a price for the selected soda

print("Your total will be: ", )
