#!/usr/bin/python3
import random


class Hat:
    def __init__(self):
        self.houses = ["Okotu", "Azudo", "Mgbudu", "Ezebazu"]


    def sort(self, name):
        print(name, "is in", random.choice(self.houses))


hat = Hat()
hat.sort("Harry")
