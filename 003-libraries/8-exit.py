#!/usr/bin/python3
import sys
if len(sys.argv) < 2:
    sys.exit("Fewer arguement");
elif len(sys.argv) > 2:
    sys.exit("Too much arguement")
print("Hello,", sys.argv[1])
