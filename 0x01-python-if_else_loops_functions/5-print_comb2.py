#!/usr/bin/python3

for number in range(100):
    print("{:02d}{}".format(number, ", " if number < 99 else "\n"), end='')
