
Anna_countries = ["United States Of America", "Ukraine", "France", "Germany",
                  "Switzerland", "Spain", "Brazil", "Poland", "Nigeria", "Greenland",
                  "Australia", "China", "India", "Israel", "Vietnam", "Mexico", "Ireland",
                  "Japan", "Palestine", "Pakistan"]

Maks_countries = ["Belgium", "Poland", "Mongolia", "France", "United States Of America",
                  "Democratic Republic Of Congo", "Ukraine", "Egypt", "Chile", "Brazil",
                  "Spain", "Great Britain", "Iceland", "Australia", "Japan",
                  "India", "Iraq", "Iran", "Mexico", "Italy"]

counter = 0
# for-loop
for Anna_country in Anna_countries:
    if Anna_country in Maks_countries:
        # print(f"Maks also have {Anna_country} in his list.")
        counter += 1

print(f"There are {counter} countries that are both in Anna's and Maks' lists.")

fruit_list = ["Apples", "Bananas", "Passion Fruit", "Dragon Fruit", "Oranges", "Blueberries",
              "Cherries", "Strawberries", "Lemon", "Raspberries"]

for fruit in fruit_list:
    print(fruit)

# How to iterate over numbers between 1 and 1,000
