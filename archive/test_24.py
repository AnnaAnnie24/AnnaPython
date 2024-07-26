from archive import test_data_23


def is_correct_answer(question, answer):
    """
    This functions checks whether user's answer is correct or not.
    How to do that?
    We are doing that by using the value of "correct" key inside the question.
    :param answer: it could be either 'a', 'b', 'c', or 'd'
    """
    correct = question["correct"]
    if answer == correct:
        return True
    else:
        return False


def print_title(question):
    """
    TODO: explain what this function is going to do
    This function is going to print the title which you get from the question.
    """
    pass

def print_option(question):
    """
    TODO: explain what this function is going to do
    This function will print the options for the question
    """
    pass


def ask_for_an_answer(question):
    """
    TODO: explain what this function is going to do
    This function will ask for an answer for the question
    """
    pass




question = test_data_23.questions[0]

# abstracting

if __name__ == '__main__':
    print("Welcome To Python Testing...")
    print("We Will Use Your Score To Determine How Smart You Are...")
    print("Good Luck!!")
    print_title(question)

    print_option(question)

    answer = ask_for_an_answer(question)

    b: bool = is_correct_answer(question, answer)
    if b:
        print("Correct ✅")
    else:
        print("Incorrect ")

