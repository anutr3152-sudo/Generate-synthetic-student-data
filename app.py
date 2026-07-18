import json
import random

majors = [
    "Computer Science",
    "Artificial Intelligence",
    "Mechanical Engineering",
    "Civil Engineering",
    "Electrical Engineering"
]

clubs = [
    "Coding Club",
    "Cricket Club",
    "Music Club",
    "NSS",
    "Robotics Club"
]

names = [
    "Anu",
    "Hemavarshini",
    "Ishwarya",
    "Estherjansie",
    "Kaviyashree"
]

students = []

for i in range(1,11):

    student = {

        "id": f"STU-{1000+i}",

        "full_name": random.choice(names),

        "major": random.choice(majors),

        "gpa": round(random.uniform(6.5,9.8),2),

        "extracurriculars":[random.choice(clubs)],

        "advising_history_notes":"Student needs career guidance and semester planning."

    }

    students.append(student)

with open("students.json","w") as file:

    json.dump(students,file,indent=4)

print("Student dataset generated successfully.")