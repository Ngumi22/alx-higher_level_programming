#!/usr/bin/python3

def uppercase(s):
    for char in s:
        print(chr(ord(char) - 32) if 'a' <= char <= 'z' else char, end='')
    print()
