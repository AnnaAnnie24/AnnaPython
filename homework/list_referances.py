# append() - Adds an element at the end of the list ⬇️
candy_brands = ["Skittles", "MnM", "Twizlers", "Swedish Fish"]
candy_brands.append("Nerds")
print(candy_brands)

# clear() - Removes all the elements from the list ⬇️
emotions = ["Mad", "Happy", "Sad", "Fear", "Disgust", "Anxiety"]
emotions.clear()
# We can check if there are no elements by obtaining number of them
n = len(emotions)
if n == 0:
    print("There are no elements in list emotions")

print("<<potter_characters>>")
# copy() - Returns a copy of the list ⬇️
potter_characters = ["Harry Potter", "Hermonie Granger", "Ron Weasly", "Neville Longbottom", "Dean Thomas"]
monk = potter_characters.copy()
monk[0] = 'a'
monk[1] = 'b'
print(potter_characters)


# count() - Returns the number of elements with the specified value ⬇️
boba_flavors = ["Passion Fruit", "Mango", "Strawberry", "Taro", "Peach", "Plain"]
boba_flavors.count("Passion Fruit")
print(boba_flavors)

# create a list of numbers (only from 1 to 5)
numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 1, 1, 1, 4, 1]
u = numbers.count(1)
explanation = "Returns the number of elements with the specified value"
e = explanation.count("e")
print(f"There are {e} letter e's in this text")
print(f"There are {u} numbers one in this list.")

# extend() - Add the elements of a list (or any iterable), to the end of the current list ⬇️
holidays = ["christmas", "halloween", "easter", "fourth of july"]
cars = ["Volvo", "Subaru", "BMW", "Ford"]
holidays.extend(cars)
print(holidays)

print("----------------------------------------")
# index() - Returns the index of the first element with the specified value ⬇️
cats = ["British Shorthair", "Sphynx", "Siamese", "Persian", "Japanese Bobtail"]
cats.index("Persian")
print(cats)

print("----------------------------------------")
# insert() - Adds an element at the specified position ⬇️
dogs = ["Pomeranian", "Labrador", "Border Collie", "Poodle", "German Shepard"]
dogs.insert(4, "Maltipoo")
print(dogs)

print("----------------------------------------")
# pop() - Removes the element at the specified position ⬇️
personalities = ["Respectful", "Confident", "Rude", "Kind", "Friendly"]
personalities.pop(2)
print(personalities)

print("----------------------------------------")
# remove() - Removes the element at the specified position ⬇️
presidents = ["George Washington", "John Adams", "Thomas Jefferson", "James Madison"]
number_of_presidents = len(presidents)
print(number_of_presidents)
presidents.remove("James Madison")
print(presidents)

print("----------------------------------------")
# reverse() - Reverses the order of the list ⬇️
vice_presidents = ["Aaron Burr", "George Clinton", "John Tyler", "Elbridge Gerry"]
vice_presidents.reverse()
print(vice_presidents)

print("----------------------------------------")
# sort() - Sorts the list ⬇️
pets = ["cat", "dog", "turtle", "fish", "lizard"]
pets.sort()
print(pets)
