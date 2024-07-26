# Task 9: Library Book Category Selector
# The user inputs their age. If they are below 12, suggest 'Children's Books', if they are
# between 13 and 18, suggest 'Young Adult', otherwise suggest 'Adult FicAon'.
print("Hello, Welcome To The Malcolm E. Middle School Library!!")
age = input("Please enter your age and we will try to assist "
            "you in finding a perfect book section, sorted by age?? ")
age = int(age)
if age <= 12:
    print("The Children's Section would be the best place for you. "
          "It is down the hall in a small playful quiet corner.")
elif age <= 18:
    print("The Teens Section would be the best place for you. "
          "It is to the right then to the left in a big room.")
elif age < 117:
    print("The Adult Section is the best place for you."
          " Down to the left by the return book box.")
else:
    print("Sorry, I don't understand because you are too old.")
    # I'M here
