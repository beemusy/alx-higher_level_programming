#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    counter = len(argv)
    result = 0
    for i in range(1, counter):
        result += int(argv[i])
    print(result)
