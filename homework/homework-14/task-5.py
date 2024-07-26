#  Task 5 “Again into Celsius”
# Save the current temperature outside into the variable called temperature. Convert it
# from Fahrenheit into Celsius and save the result into another variable.

temperature = input("What is the temperature outside?? ")
temperature = int(temperature)
temp = (temperature - (temperature + 9) * 5/9)
temp = int(temp)
print("-", temp, "degrees in celsius")
# 23°F − 32) × 5/9 = -5°C



