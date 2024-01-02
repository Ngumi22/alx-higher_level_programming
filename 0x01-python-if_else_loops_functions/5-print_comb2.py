#!/usr/bin/python3

for number in range(99):
    if number < 10:
        print(f"0{number}", end=', ' if number < 98 else '')
    else:
        print(f"{number}", end=', ' if number < 98 else '')

print()
