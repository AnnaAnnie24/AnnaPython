#  Task 3 “You own if-else”
# Try to create your own if-elif-else task and solve it.
opinion = input("Do you like cats or dogs or hamsters better?? ")

if opinion == "cats" or opinion == "Cats" or opinion == "CATS":
    print("Thank You for voting. Go Cats!! 🐈")
elif opinion == "dogs" or opinion == "Dogs" or opinion == "DOGS":
    print("Thank You for voting. Go Dogs!! 🐕")
elif opinion == "hamsters" or opinion == "Hamsters" or opinion == "HAMSTERS":
    print("Thank You for voting. Go Hamsters!! 🐹")
else:
    print("Sorry try again.")
