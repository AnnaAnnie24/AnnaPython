# weekdays
# weekends

day = input("Day Of Week: ")

if day == "Sunday" or day == "Saturday" or day == "1" or day == "7":
    print("Weekend 🥳")
elif day == "Monday" or day == "2" or day == "Tuesday" or day == "3" or day == "Wednesday" or day == "4" or day == "Thursday" or day == "5" or day == "Friday" or day == "6":
    print("Weekday 😔")
else :
    print("That is not a weekday or a weekend!! 😔")

