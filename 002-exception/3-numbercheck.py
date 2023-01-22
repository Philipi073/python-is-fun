#!/usr/bin/python3
# checks ValueError when
# non integers are passed
try:
    x =int(input("What is x: "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
