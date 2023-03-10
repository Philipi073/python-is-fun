#!/usr/bin/python3
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["okotu", "azudo", "mgbudu", "ezebazu"]:
            raise ValueError("Invalid House")
        self._house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")



def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
