# Which animal is the best at predicting future

top_animals = ["elephant", "whale", "parrot", "pig", "beaver"]
new_participant = "lion"
top_animals.append("lion")
top_animals.remove("pig")
top_three = top_animals[0:3]
print(top_three)
# ["elephant", "whale", "parrot", "pig", "beaver"]
#     ^                                     ^
#     |                                     |
# ["beaver", "whale", "parrot", "pig", "elephant"]
top_animals[0] = "beaver"
top_animals[-2] = "elephant"
top_animals[1] = "dolphin"
print(top_animals)
