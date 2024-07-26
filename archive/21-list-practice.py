"""
An application for a zoo administrator:
1. number of animals
2. check
3. add
4. get
5. get first
6. get last
7. show zoo
8. exit
"""

zoo = ["Elephant", "Giraffe", "Rhino", "Lion", "Penguins", "Tiger", "Panda", "Monkey"]
len(zoo)
while True:
    command = input("Command: ")
    if command == "Number Of Animals":
        print(len(zoo), "animals are in the zoo.")
    elif command == "Check":
        animal = input("Animal: ")
        animal = animal.lower()
        if animal in zoo:
            print("It's Here 😀")
        else:
            print("Not Here 😔")
    elif command == "Add":
        animal = input("Animal wanted to be added: ")
        zoo.append(animal)
    elif command == "Get":
        number = input("A Number: ")
        number = int(number)
        if number > len(zoo) or number < 1:
            print("Invalid Number")
        else:
            index = number - 1
            animal = zoo[index]
            print(animal)
    elif command == "Get First":
        print(zoo[0])
    elif command == "Get Last":
        print(zoo[-1])
    elif command == "Show Zoo":
        print(zoo)

    if command == "Exit":
        break
