countries_population = {
    # key: value
    "China": 1_412_600_000,
    "India": 1_454_285_000,
    "United States": 331_000_000,
    "Indonesia": 273_500_000,
    "Pakistan": 225_200_000,
    "Brazil": 213_600_000,
    "Nigeria": 211_400_000,
    "Bangladesh": 166_300_000,
    "Ukraine": 41_442_615,
    "Mexico": 130_200_000,
    "Japan": 125_800_000,
    "Ethiopia": 117_800_000
}

# get all keys
key_list = countries_population.keys()
key_list = list(key_list)
print(key_list)
# get all values
values_list = countries_population.values()
values_list = list(values_list)
print(values_list)

# Poland: 38_036_000
countries_population["Poland"] = 38_036_000
countries_population.pop("Brazil")
# go over all content of a dict
for country, population in countries_population.items():
    print(f"{country} has a population of {population}")

a = [1, 2, 3, 4]
a[-1] = 10

