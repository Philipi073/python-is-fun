#!/usr/bin/python3
with open("name.txt", "r") as file:
    for line in file:
        print(line.rstrip())
