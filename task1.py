# Task #01
# Write a Python-script that performs simple arithmetic operations: '+', '-', '*', '/'. The type of operator and data
# are set on the command line when the script is run.
# The script should be launched like this:
# $ python my_task.py 1 * 2
# Notes:
# Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any parameters
# (like -f or --function).

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("first", help="first number to calculate", type=int)
parser.add_argument("action", help="how to treat this two numbers")
parser.add_argument("second", help="second number to calculate", type=int)
args = parser.parse_args()

if args.action == "*":
    print(args.first*args.second)
elif args.action == "+":
    print(args.first+args.second)
elif args.action == "-":
    print(args.first-args.second)
elif args.action == "/":
    try:
        print(args.first / args.second)
    except:
        print("You have better not")
