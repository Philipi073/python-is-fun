#!/usr/bin/python3
names = []
with open("name.txt") as file:
    for _ in file:
        names.append(_.strip())
for name in sorted(names):
    print("Hello,", name)

