#!/usr/bin/python3
from sys import argv

if len(argv) > 1:
    result = sum(int(arg) for arg in argv[1:])
    print(result)
else:
    print("No arguments provided.")
