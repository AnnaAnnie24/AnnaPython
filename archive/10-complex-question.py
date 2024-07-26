# what is the capital of France
# input any number that is even

capital = input("What is the capital of France?? ")
number = input("Any even number: ")
number = int(number)
remainder = number % 2
isCorrectCapital = (capital == "Paris")
isEvenNumber = (remainder == 0)
if isCorrectCapital and isEvenNumber:
    print("Correct!!!")
else:
    print("Incorrect!!! (you have answered incorrect to 1 or both questions)")
