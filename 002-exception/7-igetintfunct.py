#!/usr/bin/python3
def main():
    x = getint("What is x: ")
    print(f"x is {x}")


def getint(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
