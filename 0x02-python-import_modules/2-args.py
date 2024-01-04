#!/usr/bin/python3
from sys import argv

if len(argv) == 2:
    print("1 argument")
    print("1:", argv[1])
elif len(argv) > 2:
    arg_len = len(argv) - 1
    print("{} arguments".format(arg_len))

    for i, arg in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, arg))
else:
    print("0 arguments")
