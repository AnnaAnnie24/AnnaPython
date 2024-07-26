# JACK then our program says: "Hey Jack, you are caught!",put
name = input("First person, please enter your name : ")
name_2 = input("Second person, please enter your name : ")
if name == "Jack" or name == "jack":
    print("We have caught you Jack!!")
elif name_2 == "Jack" or name_2 == "jack":
    print("We have caught you Jack!!")
else:
    age = input(name + " please enter your age : ")
    age_2 = input(name_2 + " please enter your age : ")
    age = int(age)
    age_2 = int(age_2)
    if age == age_2:
        print(name + " you are the same age as " + name_2)
    elif age < age_2:
        print(name_2 + " you are older than " + name)
    elif age > age_2:
        print(name + " you are older than " + name_2)
    elif age != age_2:
        print("You are different ages. " + name + " is " + age + " and " + name_2 + " is " + age_2 + ".")
