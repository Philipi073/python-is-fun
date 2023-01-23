#!/usr/bin/python3
def main():
    x = getint()
    print(f"x is {x}")


def getint():
    while True:
        try:
            x = int(input("What is x: "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x

main()
