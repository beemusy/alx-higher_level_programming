#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __file__ == "__main__":
    numOfArg = len(argv)

    if numOfArg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    operator = int(argv[2])
    b = int(argv[3])

    if operator == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif operator == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif operator == "/":
        print("{:d} / {:d} = {:d}".format(a, b, add(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
