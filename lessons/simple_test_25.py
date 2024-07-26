from lessons.archive.test_data_23 import questions

# questions is a list
counter = 0
question_1 = questions[0]
title = question_1["title"]
options = question_1["options"]
print(title)
print(*options, sep='\n')
answer = input("Your Answer: ")
if answer == "a" or answer == "A":
    print("✅ Correct")
    counter += 1
else:
    print("Incorrect")

question_2 = questions[1]
title = question_2["title"]
options = question_2["options"]
print(title)
print(*options, sep='\n')
answer = input("Your Answer: ")
if answer == "c" or answer == "C":
    print("✅ Correct")
    counter += 1
else:
    print("Incorrect")

question_3 = questions[2]
title = question_3["title"]
options = question_3["options"]
print(title)
print(*options, sep='\n')
answer = input("Your Answer: ")
if answer == "d" or answer == "D":
    print("✅ Correct")
    counter += 1
else:
    print("Incorrect")

question_4 = questions[3]
title = question_4["title"]
options = question_4["options"]
print(title)
print(*options, sep='\n')
answer = input("Your Answer: ")
if answer == "a" or answer == "A":
    print("✅ Correct")
    counter += 1
else:
    print("Incorrect")

question_5 = questions[4]
title = question_5["title"]
options = question_5["options"]
print(title)
print(*options, sep='\n')
answer = input("Your Answer: ")
if answer == "c" or answer == "C":
    print("✅ Correct")
    counter += 1
else:
    print("Incorrect")

question_6 = questions[5]
title = question_6["title"]
options = question_6["options"]
print(title)
print(*options, sep='\n')
answer = input("Your Answer: ")
if answer == "c" or answer == "C":
    print("✅ Correct")
    counter += 1
else:
    print("Incorrect")

question_7 = questions[6]
title = question_7["title"]
options = question_7["options"]
print(title)
print(*options, sep='\n')
answer = input("Your Answer: ")
if answer == "b" or answer == "B":
    print("✅ Correct")
    counter += 1
else:
    print("Incorrect")

question_8 = questions[7]
title = question_8["title"]
options = question_8["options"]
print(title)
print(*options, sep='\n')
answer = input("Your Answer: ")
if answer == "a" or answer == "A":
    print("✅ Correct")
    counter += 1
else:
    print("Incorrect")

question_9 = questions[8]
title = question_9["title"]
options = question_9["options"]
print(title)
print(*options, sep='\n')
answer = input("Your Answer: ")
if answer == "c" or answer == "C":
    print("✅ Correct")
    counter += 1
else:
    print("Incorrect")

question_10 = questions[9]
title = question_10["title"]
options = question_10["options"]
print(title)
print(*options, sep='\n')
answer = input("Your Answer: ")
if answer == "d" or answer == "D":
    print("✅ Correct")
    counter += 1
else:
    print("Incorrect")

question_11 = questions[10]
title = question_11["title"]
options = question_11["options"]
print(title)
print(*options, sep='\n')
answer = input("Your Answer: ")
if answer == "c" or answer == "C":
    print("✅ Correct")
    counter += 1
else:
    print("Incorrect")


question_12 = questions[11]
title = question_12["title"]
options = question_12["options"]
question_1 = questions[0]
print(title)
print(*options, sep='\n')
answer = input("Your Answer: ")
if answer == "b" or answer == "B":
    print("✅ Correct")
    counter += 1
else:
    print("Incorrect")

question_13 = questions[12]
title = question_13["title"]
options = question_13["options"]
print(title)
print(*options, sep='\n')
answer = input("Your Answer: ")
if answer == "a" or answer == "A":
    print("✅ Correct")
    counter += 1
else:
    print("Incorrect")

question_14 = questions[13]
title = question_14["title"]
options = question_14["options"]
print(title)
print(*options, sep='\n')
answer = input("Your Answer: ")
if answer == "d" or answer == "D":
    print("✅ Correct")
    counter += 1
else:
    print("Incorrect")

question_15 = questions[14]
title = question_15["title"]
options = question_15["options"]
print(title)
print(*options, sep='\n')
answer = input("Your Answer: ")
if answer == "a" or answer == "A":
    print("✅ Correct")
    counter += 1
else:
    print("Incorrect")

print(str(counter) + " questions out of 15 questions were correct.")
