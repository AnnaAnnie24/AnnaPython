import random

country_data = [
    "Ukraine - Kyiv",
    "United States Of America - Washington",
    "Italy - Rome",
    "France - Paris",
    "Greece - Athens",
    "United Kingdom - London",
    "Germany - Berlin",
    "Japan - Tokyo",
    "Mexico - Mexico City",
    "Switzerland - Bern",
    "Poland - Warsaw",
    "Sweden - Stockholm",
    "Turkey - Ankara",
    "Denmark - Copenhagen",
]

# ✅ correct
# ❌ wrong, the correct answer is [...]
random.shuffle(country_data)
for country_capital in country_data:
    country, capital = country_capital.split(" - ")
    answer = input(f"What is the capital of {country}: ")
    if answer == capital:
        print("✅ Correct")
    else:
        print(f"❌ Incorrect, the correct answer is {capital}")
