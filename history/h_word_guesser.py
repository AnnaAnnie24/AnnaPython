#  Task 1 “First & second symbol”
# Ask the user for any text, then tell what is the first and what it the second symbol of input
# text.

word = input("Please enter any word with 2 letters and more - ")
length = len(word)
length = int(length)
text = " letters in your word."
two = 2
two = int(two)
if length <= two:
    print("Your word is too short :(")
else:
    first_symbol = word[0]           # square brackets
    second_symbol = word[1]
    print("Your first letter is " + first_symbol + ", and your second letter is " + second_symbol + ".")
    length = str(length)
    print(length + text)
