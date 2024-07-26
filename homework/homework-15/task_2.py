#  Task 2 “My longest friend”
# Ask the user for 3 names of his (her) friends. Display the friend who has the longest name.

name_1 = input("Put in one of your friends name: ")
name_2 = input("Add another name: ")
name_3 = input("One more name: ")

if len(name_1) > len(name_2) and len(name_1) > len(name_3):
    print(name_1, "is the name with the longest letters!!!")

elif len(name_2) > len(name_1) and len(name_2) > len(name_3):
    print(name_2, "is the name with the longest letters!!!")

elif len(name_3) > len(name_1) and len(name_3) > len(name_2):
    print(name_3, "is the name with the longest letters!!!")
