#!/usr/bin/python3
class Wizzard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name


class Student(Wizzard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house


class Teacher(Wizzard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


wizzard = Wizzard("Albus")
student = Student("Iweka", "Okotu")
teacher = Teacher("Owusu", "English")

print(student)

