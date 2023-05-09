#!/usr/bin/python3
def uppercase(s):
new_s = ""
for x is s:
    if ord(x) >= 97 and ord(x) <= 122:
        new_s += chr(ord(c) - 32)
    else:
        new_s += x
        print("{:s}".format(new_s))
