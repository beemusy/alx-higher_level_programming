#!/usr/bin/python3
def uppercase(s):
    new_s = ""
for x in s:
    if ord(x) >= 97 and ord(x) <= 122:
        new_s += chr(ord(x) - 32)
    else:
        new_s += x
        print("{:s}".format(new_s))
