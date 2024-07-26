# Task 8: Temperature Warning System
# If the temperature is greater than 100°F or below 32°F, print a warning message for extreme
# temperatures.
temperature = input("What is the temperature outside?? ")
temperature = int(temperature)
if temperature >= 100 or temperature <= 32:
    print("Extreme weather conditions!!!")
else:
    print("Beautiful day outside!!")
