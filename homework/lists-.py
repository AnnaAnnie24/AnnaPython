# What is a list??
# A list is a data-type, that allows you to store multiple values.
# What does a list look like 👀??
# 1. Start with the name or title of your set. Example: dancing_members
# 2. Add This. ➡️ Example: dancing_members = []
# 3. In the bars ➡️ [], write your list. Example: ["Maks", "Bob", "Anna", "Jack"]
# 4. Be happy of your list ➡️. Example: dancing_members = ["Maks", "Bob", "Anna", "Jack"]
# You can also make a list of questions!!
# Here is an example ⬇️:
# friendly_questions: list[dict] = [
#     {
#         "title":
#             "How Are You Feeling Today??",
#         "options": [
#             "a. Awesome 😎",
#             "b. Ok 😐",
#             "c. Sad 😢",
#             "d. Bad 😠",
#         ],
#         "correct":
#             "a"
#     },
# And then you can expand your list later on!!

# This can also be known as a list.
# >>> a = [[1,2],[3,4]] ➡️ Is a list because: A is the name of the list, [[1,2],[3,4]] is the list.
# >>> b = [[1,2],[3,4]] ➡️ This is also a list.
# >>> a == b ➡️ This is correct because a and b are the same list, but they just have a different name.
# True 👍

# Why should you make a list??
# farm - "cow"🐄
# farm - "dog"🐕
# farm - "horse"🐴
# farm - "cat"🐈
# It will be easier to just have this:
# farm = ["cow", "dog", "horse", "cat"]
# Two reasons why ⬇️
# 1. It takes up less space. 🌌
# 2. You only need one variable rather than 4 or 5 or 10. 1️⃣

# What can we do with lists?
farm = ["cow", "dog", "horse", "cat"]
strange_list = ["cat", "dog"] * 3
# append method of a list
farm.append("chicken")
# How to remove a specific value?
# a remove method
farm.remove("cat")
print(farm)
a = "Hello"
b = "Hello, Bob"
a_length = len(a)
b_length = len(b)
print("B - A =", b_length - a_length)

"""
Create a list of your 4 favorite colors.
Add any one new color to the list.
Remove the second one.
Remove the last one.
Write a code to find out how many colors left?
"""