#!/usr/bin/python3
name = input("What is your name? ")

f = open("append.txt", "a")
f.write(f"{name}\n")
f.close()
