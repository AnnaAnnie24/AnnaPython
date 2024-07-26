#  Task 2 “Rhyme Time” Create a function that takes two words as input and checks if they rhyme based on
# their last two letters.
word_one = input("Welcome to Rhyme Time, please enter a word : ")
word_two = input("Please enter your second word : ")
two_last_letters_one = word_one[-2:]      # pie # tie -> 'ie
two_last_letters_two = word_two[-2:]
if two_last_letters_one == two_last_letters_two:
    print("Rhyme!!!")
else:
    print("Do not rhyme!!!")

# Home task 1
# Is the same beginning?
# Write a program that asks for 2 words to input.
# The program is meant to check whether these 2 words have the same first 3 letters
