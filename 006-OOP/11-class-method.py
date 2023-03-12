#!/usr/bin/python3
import random


class Hat:
    houses = ["mgbudu", "azudo", "okotu", "ezebazu"]


    @classmethod
    def sort(cls, name):
        print(name,"is in",random.choice(cls.houses))


Hat.sort("Harry")
