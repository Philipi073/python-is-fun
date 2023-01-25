#!/usr/bin/python3
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguement")

for arg in sys.argv[1:]:

    print("Hello, my name is", arg)
