# Task 3 “The best job”
# Ask the user’s opinion:
# 1) How much does a waitress earn $ per month?
# 2) How much does an airplane pilot earn $ per month?
# 3) How much does a common youtuber earn $ per month?
# 4) How much does a pizza-delivery person earn $ per month?
# 5) How much does a doctor earn $ per month?
# Show the user his highest salary choice. For example:
# “You think that a pizza-delivery man earn the highest salary of $7000 per month”
# Then just ask the user why does he/she think so?
# Reply to this quesWon could be always the same.

waitress = input("How much does a waitress earn $ per month? ")
pilot = input("How much does an airplane pilot earn $ per month? ")
youtuber = input("How much does a common youtuber earn $ per month? ")
pizza = input("How much does a pizza-delivery person earn $ per month? ")
doctor = input("How much does a doctor earn $ per month? ")

pizza = int(pizza)
pilot = int(pilot)
waitress = int(waitress)
youtuber = int(youtuber)
doctor = int(doctor)

if waitress > pilot and waitress > youtuber and waitress > pizza and waitress > doctor:
    print("You think that a waitress earns the most money??")
    input("Why do you think that this job gets the most money???")
    print("Ok, bye!!!")

elif pilot > waitress and pilot > youtuber and pilot > pizza and pilot > doctor:
    print("You think that a pilot earns the most money??")
    input("Why do you think that this job gets the most money???")
    print("Ok, bye!!!")

elif youtuber > waitress and youtuber > pilot and youtuber > pizza and youtuber > doctor:
    print("You think that a youtuber earns the most money??")
    input("Why do you think that this job gets the most money???")
    print("Ok, bye!!!")

elif pizza > waitress and pizza > pilot and pizza > youtuber and pizza > doctor:
    print("You think that a pizza-delivery person earns the most money??")
    input("Why do you think that this job gets the most money???")
    print("Ok, bye!!!")

elif doctor > waitress and doctor > pilot and doctor > youtuber and doctor > pizza:
    print("You think that a waitress earns the most money??")
    input("Why do you think that this job gets the most money???")
    print("Ok, bye!!!")
