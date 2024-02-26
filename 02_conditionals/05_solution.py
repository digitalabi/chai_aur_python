# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman)

import random
weather_list = ["Sunny","Rainy","Snowy"]
weather = random.choice(weather_list)

if weather == "Sunny":
    activity = "Go for a walk"
elif weather == "Rainy":
    activity = "Read a book"
elif weather == "Snowy":
    activity = "Build a snowman"

print("Weather is {} so I will {} .".format(weather,activity))