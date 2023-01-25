#!/usr/bin/python3
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("Hello, my name is " + sys.argv[1])
