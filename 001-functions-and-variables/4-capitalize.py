#!/usr/bin/python3
#prompt user for name
name = input("What is your name: ")

#strip white space
name = name.strip()

#capitalise input
name = name.capitalize()

#say hello to user
print(f"Hello, {name}")
