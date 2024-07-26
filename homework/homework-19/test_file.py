from test_data import questions
def is_correct_answer(question, answer):
    correct = question["correct"]
    if answer == correct:
        return True
    else:
        return False


def print_title():
    print("Hello!!")
    print("Today We Have Some Questions For You About Harry Potter!!")
    print("Good Luck!!")

    from test_data import questions

if __name__ == '__main__':

    # question1
    print_title()

    question1 = questions[0]

    title = question1["title"]
    options = question1["options"]
    correct = question1["correct"]

    print(title)

    print(options[0])
    print(options[1])
    print(options[2])
    print(options[3])
    answer = input("Answer:")

    if answer == "a" or answer == "A":
        print("✅ Correct")
    else:
        print("Incorrect")

    # question2

    question2 = questions[1]

    title = question2["title"]
    options = question2["options"]
    correct = question2["correct"]

    print(title)

    print(options[0])
    print(options[1])
    print(options[2])
    print(options[3])
    answer = input("Answer:")

    if answer == "c" or answer == "C":
        print("✅ Correct")
    else:
        print("Incorrect")

    # question3
    question3 = questions[2]

    title = question3["title"]
    options = question3["options"]
    correct = question3["correct"]

    print(title)

    print(options[0])
    print(options[1])
    print(options[2])
    print(options[3])
    answer = input("Answer:")

    if answer == "b" or answer == "B":
        print("✅ Correct")
    else:
        print("Incorrect")
# question4
    question4 = questions[3]

    title = question4["title"]
    options = question4["options"]
    correct = question4["correct"]

    print(title)
    print(options[0])
    print(options[1])
    print(options[2])
    print(options[3])
    answer = input("Answer:")

    if answer == "d" or answer == "D":
        print("✅ Correct")
    else:
        print("Incorrect")
# question5
    question5 = questions[4]

    title = question5["title"]
    options = question5["options"]
    correct = question5["correct"]

    print(title)

    print(options[0])
    print(options[1])
    print(options[2])
    print(options[3])
    answer = input("Answer:")
if answer == "c" or answer == "C":
    print("✅ Correct")
else:
    print("Incorrect")

# question6
    question6 = questions[5]

    title = question6["title"]
    options = question6["options"]
    correct = question6["correct"]

    print(title)

    print(options[0])
    print(options[1])
    print(options[2])
    print(options[3])
    answer = input("Answer:")
if answer == "b" or answer == "B":
    print("✅ Correct")
else:
    print("Incorrect")

    # question7

    question7 = questions[6]

    title = question7["title"]
    options = question7["options"]
    correct = question7["correct"]

    print(title)

    print(options[0])
    print(options[1])
    print(options[2])
    print(options[3])
    answer = input("Answer:")
if answer == "a" or answer == "A":
    print("✅ Correct")
else:
    print("Incorrect")

# question 8
    question8 = questions[7]

    title = question8["title"]
    options = question8["options"]
    correct = question8["correct"]

    print(title)

    print(options[0])
    print(options[1])
    print(options[2])
    print(options[3])
    answer = input("Answer:")
if answer == "d" or answer == "D":
    print("✅ Correct")
else:
    print("Incorrect")

# question9
    question9 = questions[8]

    title = question9["title"]
    options = question9["options"]
    correct = question9["correct"]

    print(title)

    print(options[0])
    print(options[1])
    print(options[2])
    print(options[3])
    answer = input("Answer:")
if answer == "a" or answer == "A":
    print("✅ Correct")
else:
    print("Incorrect")

# question 10
    question10 = questions[9]

    title = question10["title"]
    options = question10["options"]
    correct = question10["correct"]

    print(title)

    print(options[0])
    print(options[1])
    print(options[2])
    print(options[3])
    answer = input("Answer:")
if answer == "c" or answer == "C":
    print("✅ Correct")
else:
    print("Incorrect")




