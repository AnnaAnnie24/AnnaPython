import csv

all_countries = []
with open("../../countries of the world.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        country = line[0]
        country = country.strip()
        all_countries.append(country)

#  print(*all_countries, sep='\n')

print("Name as many countries as you can. Once your done enter DONE.")

countries = []
# while-loop
while True:
    country = input("Next Country: ")
    if country == "DONE":
        break
    elif country not in all_countries:
        print("That is not a country!!!")
    else:
        countries.append(country)

counter = len(countries)
print(f"You have named {counter} countries.")
if counter >= 11:
    print("You are Smart! 🤓")
elif counter >= 5:
    print("Not too smart! ")
else:
    print("You are Dumb! 😩")
