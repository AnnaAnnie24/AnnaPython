aquarium = []

# while-loop
while True:
    fish = input("next fish: ")
    if fish == "exit":
        break
    else:
        aquarium.append(fish)

number = len(aquarium)

if number < 10:
    print("You are not very smart")
elif 10 <= number and number < 30:
    ...
