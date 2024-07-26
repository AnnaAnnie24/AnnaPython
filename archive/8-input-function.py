print("Lets buy a christmas tree! 🌲")
small_tree = 34.65
medium_tree = 46.78
large_tree = 54.36
print("Option 1: $" + str(small_tree) + ". Description: Very weak and tiny, might break.")
print("Option 2: $" + str(medium_tree) + ". Description: Normal size, not to big not too small.")
print("Option 3: $" + str(large_tree) + ". Description: Large and mighty, very strong.")
user_option = input("What option did you chose? ")

if user_option == "Option 1":
    # small tree
    print("Ok, you picked the small tree!!! 🌲. "
          "That would be 34.65 $")
elif user_option == "Option 2":
    print("Ok, you picked the medium tree!!! 🌲. "
          "That would be 46.78 $")
elif user_option == "Option 3":
    print("Ok, you picked the large tree!!! 🌲. "
          "That would be 54.36 $")
else:
    print("I'm sorry, I do not understand!!! 🌲. "
          "I was programmed only to know Option 1, Option 2, and Option 3!!! \n"
          "Have a nice day!!!")



