#   Task 7 “Weather dresser” Design a program that asks the user about the current weather (temperature, rain,
# etc.). Based on the input, use if-elif-else statements to suggest appropriate clothing
# for the day. Include funny pictures or emojis to personalize the recommendations!
print("You can say something like rain ☔, snow ❄️, sunny 🌞, hail 🧊, warm 😊, "
      "cool 😎, thunderstorm ⛈️, windy 💨, and cloudy ☁️!! :)")
weather = input("What Is The Weather Today?? ")
weather = str(weather)
if weather == "Rain":
    print("Wear a raincoat and rain boots. Also consider bringing an umbrella. ☔")
elif weather == "Snow":
    print("It might be very cold. Wear a snowsuit and snow boots. "
          "A hat, scarf, and mittens will do. ❄️")
elif weather == "Sunny":
    print("You should wear a t-shirt and leggings. Maybe bring a sweatshirt. 🌞")
elif weather == "Hail":
    print("I would stay home if the hail is extremely huge. Bring an umbrella "
          "to shield yourself, wear a hat and scarf, maybe mittens. "
          "Also wear something warm. 🧊")
elif weather == "Warm":
    print("Wear shorts and a t-shirt. Bring a sweatshirt just in case. I recommend "
          "bringing a cold water bottle. 😊")
elif weather == "Cool":
    print("Wear leggings, a t-shirt, and a sweatshirt. Some sneakers would do too. 😎")
elif weather == "Thunderstorm":
    print("Stay at home!!! It is very unsafe. ⛈️")
elif weather == "Windy":
    print("Some jeans, a shirt, a sweater, and a coat would be good. Also hold on "
          "to your items, they might fly away. 💨")
elif weather == "Cloudy":
    print("It might rain so bring an umbrella. Wear a long sleeve shirt, pants, "
          "and a sweater. ☁️")
else:
    print("I'm sorry, I don't understand. Please try again. 😔")

