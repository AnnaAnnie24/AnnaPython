# I'm here

Anna_s_friends = ["Maks", "Bob", "Maks' brother", "George"]

# if number is 1, then index is 0
# if number is 2, then index is 1
# if number is 5, then index is 4
# if index is 9, then number is 10
first_friend = Anna_s_friends[0]
Anna_s_friends[2] = "Alexander"
Anna_s_friends.append("Sergey")
name = input("Who do we forget? ")
Anna_s_friends.append(name)
print(Anna_s_friends)
number_of_friends = len(Anna_s_friends)
print(number_of_friends)
