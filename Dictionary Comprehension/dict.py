import random
from unittest import result
names = ["Alex", "Mark"]
new_dict = {names: random.randint(1, 100) for names in names}
print(new_dict)
passed_students = {student: score for (
    student, score) in new_dict.items() if score >= 50}
print(passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
new = sentence.split()
results = {word: len(word) for word in new}


print(results)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
weather_f = {day: (temp * 9/5 + 32) for (day, temp) in weather_c.items()}

# Write your code 👇 below:

print(weather_f)
