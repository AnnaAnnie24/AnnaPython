amphibians = "4 legs"
reptile = "4 legs"
mammals = "4 legs"
animals = ["elephant", "giraffe", "cheetah", "tiger", "zebra", "panda", "bear",
           "red panda", "polar bear", "eagle", "parrot", "lion", "monkey", "gorilla",
           "flamingo", "alligator", "crocodile", "camel"]
answer = input("Welcome To The National State Zoo, What Animal Would You Like To See: ")
if answer in animals:
    print("Yes, we have a", answer, "in our zoo")
else:
    print("Sorry, we don't have a", answer, "in our zoo")
