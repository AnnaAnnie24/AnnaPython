#  Task 3
# Using if-elif-else tell user what he can buy depending on the sum of money he has.

money = int(input("How much money do you have?? "))
if money <= 5:
    print("Sorry that is not a lot, but maybe you can find something "
          "at the dollar store 💲 or five below 5️⃣.")
elif money <= 10:
    print("You can buy some snack 😋 or candy 🍬, or even sodas 🥤.")
elif money <= 20:
    print("You have some money 🤑, can I please have some?? "
          "You can buy something that you desire maybe a phone 📱 or laptop 💻.")
else:
    print("That is too much 💰, but you can buy a car 🚗 or a house 🏠.")


