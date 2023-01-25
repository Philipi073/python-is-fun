#!/usr/bin/python3
import sys
if len(sys.argv) < 2:
    print("Few arguement")
elif len(sys.argv) > 2:
    print("Too much arguement")
else:
    print("Hello, my name is", sys.argv[1])
