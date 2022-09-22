# Task #03
# Write a Python-script that determines whether the input string is the correct entry for the 'formula' according EBNF
# syntax (without using regular expressions).
# Formula = Number* | (Formula Sign Formula)
# Sign = '+' | '-'
# Number = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
# Input: string
# Result: (True / False, The result value / None)
# Example,
# user_input = '1+2+4-2+5-1' result = (True, 9)
# user_input = '123' result = (True, 123)
# user_input = 'hello+12' result = (False, None)
# user_input = '2++12--3' result = (False, None)
# user_input = '' result = (False, None)
# Example how to call the script from CLI:
# $ python task_1_ex_3.py 1+5-2
# Hint: use argparse module for parsing arguments from CLI

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input", help="how to treat this two numbers")
args = parser.parse_args()

res = None
buff = None
action = None
digitEntered = False

for i in args.input:
    if i.isdigit():
        if not res:
            res = int(i)
        elif not buff and not digitEntered:
            buff = int(i)
        elif res and not buff and digitEntered:
            res*=10 + int(i)
        elif buff and digitEntered:
            res*=10 + int(i)
        digitEntered = True
    elif i == "+" or i == "-":
        if action == "+":
            res+=buff
            buff = None
        elif action == "-":
            res-=buff
            buff = None
        action = i
        digitEntered = False

if digitEntered:
    if action == "+":
        res += buff
    elif action == "-":
        res -= buff

if res:
    print(f"(True, {res})")
else:
    print(f"(False, None)")
