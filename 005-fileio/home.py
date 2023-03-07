#!/usr/bin/python3
import csv

students = []
with open("students-home.csv") as file:
    reader = csv.reader(file)
    for name,home in reader:
        students.append({"name":name, "home":house})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{studen['name']} is from {student['home']}")

