# Task 12: Guess my birthday
# Create a program where user is trying to guess your birthday date.
# Extra 1
# Give user an infinite number of attempts.
# Extra 2
# ASer each incorrect guess give user a hint like: “My birthday is earlier” and “My
print("Hello welcome to the infinite birthday guesser!!! 🥳")
while True:
    answer = input("Guess my birthday:")
    if answer == "9/24" or answer == "24th September" or answer == "September 24th" or answer == "24th september" or answer == "september 24th":
        print("You're correct!!! 🥳")
        break
    else:
        print("You're incorrect!!! 😔")
