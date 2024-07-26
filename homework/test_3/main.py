import test_data


def is_correct_answer(question, answer):
    correct = question["correct"]
    if answer == correct:
        return True
    else:
        return False


def print_title():
    print("Hello!!")
    print("Today We Will Be Testing you On How Well You Know Harry Potter!!")
    print("Good Luck!!")


# abstracting

if __name__ == '__main__':

    print_title()

    questions = test_data.questions

    question1 = questions[0]

    title = question1["title"]
    options = question1["options"]
    correct = question1["correct"]

    print(title)

    # Plan
    #  • beautifully print options (line by line)
    #     -
    #  • Ask the user for an answer
    #  • Check if answer is correct
    #  • Print correct answer
    #
    print(options[0])
    print(options[1])
    print(options[2])
    print(options[3])
    answer = input("Answer:")

    if answer == "a" or answer == "A":
        print("✅ Correct")
    else:
        print("Incorrect")



    print_title()

    questions = test_data.questions

    question1 = questions[1]

    title = question1["title"]
    options = question1["options"]
    correct = question1["correct"]

    print(title)

    # Plan
    #  • beautifully print options (line by line)
    #     -
    #  • Ask the user for an answer
    #  • Check if answer is correct
    #  • Print correct answer
    #
    print(options[0])
    print(options[1])
    print(options[2])
    print(options[3])
    answer = input("Answer:")

    if answer == "c" or answer == "C":
        print("✅ Correct")
    else:
        print("Incorrect")



    print_title()

    questions = test_data.questions

    question1 = questions[2]

    title = question1["title"]
    options = question1["options"]
    correct = question1["correct"]

    print(title)

    # Plan
    #  • beautifully print options (line by line)
    #     -
    #  • Ask the user for an answer
    #  • Check if answer is correct
    #  • Print correct answer
    #
    print(options[0])
    print(options[1])
    print(options[2])
    print(options[3])
    answer = input("Answer:")

    if answer == "b" or answer == "B":
        print("✅ Correct")
    else:
        print("Incorrect")
    print_title()

    questions = test_data.questions

    question1 = questions[0]

    title = question1["title"]
    options = question1["options"]
    correct = question1["correct"]

    print(title)

    # Plan
    #  • beautifully print options (line by line)
    #     -
    #  • Ask the user for an answer
    #  • Check if answer is correct
    #  • Print correct answer
    #
    print(options[0])
    print(options[1])
    print(options[2])
    print(options[3])
    answer = input("Answer:")

    if answer == "d" or answer == "D":
        print("✅ Correct")
    else:
        print("Incorrect")


print_title()

questions = test_data.questions

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


if answer == "C" or answer == "c":
    print("✅ Correct")
else:
    print("Incorrect")

    print(options[0])
    print(options[1])
    print(options[2])
    print(options[3])
    answer = input("Answer:")

    if answer == "C" or answer == "c":
        print("✅ Correct")
    else:
        print("Incorrect")

    print(options[0])
    print(options[1])
    print(options[2])
    print(options[3])
    answer = input("Answer:")

    if answer == "C" or answer == "c":
        print("✅ Correct")
    else:
        print("Incorrect")
