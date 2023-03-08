#!/usr/bin/python3


class Student:
    pass


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house= input("house: ")
    return student


if __name__ == "__main__":
    main()
