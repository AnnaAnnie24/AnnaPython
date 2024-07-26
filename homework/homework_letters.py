word_one = input("Please enter a word with 4 or more letters : ")
word_two = input("Please enter your second word with 4 or more letters : ")
three_first_letters_one = word_one[0:3]         # 2 letters at indices 0, 1
three_first_letters_two = word_two[0:3]
if three_first_letters_one == three_first_letters_two:
    print("These words have the first same 3 letters!!!")
else:
    print("These words do not have the first same 3 letters!!!")
