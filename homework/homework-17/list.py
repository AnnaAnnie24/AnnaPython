import os

twelve_female_names = ["Ella", "Anna", "Julia", "Maya", "Anya", "Olivia", "Sofia",
                       "Lily", "Nina", "Madison", "Gabriella", "Johanna"]
print(twelve_female_names)

annas_list_of_male_names = ["Bob", "George", "Mike", "Jack", "Brandon",
                            "Nick", "Dimitri", "Alexander"]
moms_list_of_male_names = ["John", "Jack", "Mike", "David", "Josh",
                           "Elijah", "Nick", "Marcel"]

common_names = []

counter = 0
for Anna_male_name in annas_list_of_male_names:
    if Anna_male_name in moms_list_of_male_names:
        counter += 1
        common_names.append(Anna_male_name)
print(common_names)
os.system("cls")
print(f"There are {counter} names that are both in Anna's and Mom's lists.")
