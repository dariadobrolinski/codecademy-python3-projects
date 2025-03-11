#In this project, you’ll create a Python script to simulate the experience of time travel using various Python modules. You’ll start by building a custom module, then work with dates and times, perform precise calculations, implement random selection features, and finally, generate a personalized time travel message.

import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

# Get today's date
now = dt.datetime.now()
nowDate = now.strftime("%Y-%m-%d")
nowTime = now.strftime("%H:%M:%S")
print(f"Current Date: {nowDate}")
print(f"Current Time: {nowTime}")

# Calculate time travel cost
baseCost = Decimal("1200.75")
targetYear = randint(1000, 5000)
yearDiff = abs(dt.datetime.now().year - targetYear)
costMultiply = Decimal("10")
finalCost = baseCost + (costMultiply * yearDiff)

# Pick random destination
destinations = ["Greece", "Poland", "Ecuador", "Canada", "Antarctica"]
finalDestination = choice(destinations)

message = custom_module.timeTravelMessage(targetYear, finalDestination, finalCost)
print(message)

