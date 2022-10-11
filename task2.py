# Task #02
# Write a Python-script that performs the standard math functions on the data.
# The name of function and data are set on the command line when the script is run.
# The script should be launched like this:
# $ python my_task.py add 1 2
# Notes:
# Function names must match the standard math functions from the built-in libraries.
# Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any parameters
# (like -f or --function).

import operator
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("action", help="how to treat this two numbers")
parser.add_argument("first", help="first number to calculate", type=int)
parser.add_argument("second", help="second number to calculate", type=int)
args = parser.parse_args()

args.action = (operator, args.action, None)

if 'add' in args.action:
    print(args.first + args.second)
elif 'sub' in args.action:
    print(args.first + args.second)
elif 'truediv' in args.action:
    if args.second == 0:
        raise ZeroDivisionError("Divider cannot be 0")
    print(args.first / args.second)
elif 'mul' in args.action:
    print(args.first * args.second)
