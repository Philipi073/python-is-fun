#!/usr/bin/python3
with open("name.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())
