from test_data_20 import animal_questions


def is_correct_answer(question, answer):
    correct = question["correct"]
    if answer == correct:
        return True
    else:
        return False
def print_title():
    print("Hello!!")
    print("Today We Have Some Questions For You About Animals!!")
    print("Good Luck!!")


    # abstracting
    from test_data_20 import animal_questions

if __name__ == '__main__':
    counter = 0
    # question1
    print_title()

    question1 = animal_questions[0]

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
        counter += 1
    else:
        print("Incorrect")

    # question2

    question2 = animal_questions[1]

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
        counter += 1
    else:
        print("Incorrect")

    # question3
    question3 = animal_questions[2]

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
        counter += 1
    else:
        print("Incorrect")
    # question4
    question4 = animal_questions[3]

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
        counter += 1
    else:
        print("Incorrect")
    # question5
    question5 = animal_questions[4]

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
        counter += 1
    else:
        print("Incorrect")

    # question6
    question6 = animal_questions[5]

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
        counter += 1
    else:
        print("Incorrect")

    # question7

    question7 = animal_questions[6]

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
        counter += 1
    else:
        print("Incorrect")

    # question 8
    question8 = animal_questions[7]

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
        counter += 1
    else:
        print("Incorrect")

    # question9
    question9 = animal_questions[8]

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
        counter += 1
    else:
        print("Incorrect")

    # question 10
    question10 = animal_questions[9]

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
        counter += 1
    else:
        print("Incorrect")
    counter = str(counter)
    print("You Scored " + counter + " Of 10")
