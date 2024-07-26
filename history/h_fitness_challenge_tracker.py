# Task 6: Fitness Challenge Tracker
# Create a program where the user inputs the number of steps they walked and the number of
# liters of water they drank in a day. If they walked more than 10000 steps or drank more than
# 2 liters of water, print "Challenge completed!", else "Try again tomorrow!".
print("Hello, Welcome To The Fitness Challenge Tracker!!")
walked = input("How many steps have you walked today?? ")
drank = input("How much liters of water have you drank today?? ")
walked = int(walked)
drank = float(drank)
if walked >= 10000 or drank >= 2:
    print("Challenge Complete!!!")
else:
    print("Try again tomorrow!!!")
