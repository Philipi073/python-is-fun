#!/usr/bin/python3
name = input("What is your name? ")

f = open("file1.txt", "w")
f.write(name)
f.close()
