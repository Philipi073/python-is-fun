#!/usr/bin/python3
class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("missing name")
        if house not in ["Mgbudu", "Okotu", "Azudo", "Ezebazu"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus


    def __str__(self):
        return f"{self.name} from {self.house}"


    def charm(self):
        match self.patronus:
            case "stag":
                return "*"
            case "otter":
                return "#"
            case "usher":
                return "&"
            case _:
                return "/"


def main():
    student = get_student()
    print("Expecto Petronum")
    print(student.charm())


def get_student():
    name = input("Name ")
    house = input("House ")
    patronus = input("Patronus ")


if __name__ == "__main__":
    main()
