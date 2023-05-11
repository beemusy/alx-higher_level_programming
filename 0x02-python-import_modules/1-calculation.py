#!/usr/bin/python3

# import functions from the file calculator_1.py

from calculator_1 import add, sub, mul, div

# define the values a and b to 10 and 5

if __name__ == "__main__":
    a = 10
    b = 5

print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))

# Print while doing some maths
