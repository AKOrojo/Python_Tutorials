student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for n in student_scores:
    score = student_scores[n]
    if score > 90:
        student_grades[n] = "A"
    elif score > 80:
        student_grades[n] = "B"
    elif score > 70:
        student_grades[n] = "C"
    elif score > 60:
        score = "D"
    else:
        score = "F"


# 🚨 Don't change the code below 👇
print(student_grades)
