#!/usr/bin/python3
def uppercase(s):
    output = ""
    for char in s:
        uppercase_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        output += uppercase_char
    print("{}".format(output))
