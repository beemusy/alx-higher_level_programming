#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    numOfArg = len(argv) - 1
    if numOfArg == 0:
        print("{} arguments.".format(numOfArg))
    else:
        print("{} arguments:".format(numOfArg))
        for i in range(0, numOfArg):
            print("{}: argv[i]".format(i))
