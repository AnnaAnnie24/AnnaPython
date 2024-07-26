name_of_person = "Anna"
age_of_person = 11
today_is_15th_Nov_in_Kyiv = True

# concatenation
approve_text = "Yes! " + name_of_person + (", you can vote on the upcoming elections, "
                                           "because you have reached the age of 18")
disapprove_text = ("NOOOOOO!!!!!! " + name_of_person + ", you can not vote!!!!!" +
                   " Because you're only " + str(age_of_person) + " years old")

#  0      - baby
baby_text = "YOU ARE A BABY!!!!! 👶 " + name_of_person + " is too young and is not knowledgeable!!!! 👶 "
# 1-3     - toddler
toddler_text = "YOU ARE A TODDLER!!!! 👶 " + name_of_person + " is too young and is not smart!!!! 👶 "

kid_text = "YOU ARE A SMALL KID!!!! 👩‍ " + name_of_person + " is too tiny and is not cool!!!! 👩"

child_text = "YOU ARE A CHILD!!!! 👧 " + name_of_person + " is too small and is not good at making decisions!!!! 👧 "

teen_text = "YOU ARE A TEEN!!!! 🥴 " + name_of_person + " is too sarcastic and has a small brain!!!! 🥴 "

adult_text = "YOU ARE AN ADULT!!! 😏 " + name_of_person + " is very knowledgeable!!!! 😏"

elderly_text = "YOU ARE OLD!!!! 👵 " + name_of_person + " is old and might not remember much!!! 👵"

very_old_text = "YOU ARE VERY OLD!!! 👵 " + name_of_person + " is pretty old and needs a wheelchair!!! 👵"

extremely_old_text = "YOU ARE EXTREMELY OLD!!! 👵 " + name_of_person + " is super old and will die soon!!! 👵"

# ✅ YOUR ASSIGNMENT
# 4 to 7  - kid
# 8 to 12 - child
# 13-19   - teenager
# 20-59   - adult
# 60-90   - elderly
# 90+     - very old
# 110+    - surprisingly old

if 6 > 7:
    print("a")
elif 56 < 100:
    print("b")

if age_of_person <= 2:
    print(baby_text)

elif age_of_person <= 4:
    print(toddler_text)

if age_of_person <= 7:
    print(kid_text)

elif age_of_person <= 12:
    print(child_text)

elif age_of_person <= 19:
    print(teen_text)

elif age_of_person <= 59:
    print(adult_text)

elif age_of_person <= 90:
    print(elderly_text)

elif age_of_person <= 100:
    print(very_old_text)


elif age_of_person <= 110:
    print(extremely_old_text)
