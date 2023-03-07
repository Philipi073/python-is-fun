#!/usr/bin/python3
import csv


name = input("what is your name? ")
home = input("what is your home? ")

with open("writer.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
