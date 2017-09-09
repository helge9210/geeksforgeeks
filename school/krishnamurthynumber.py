#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/krishnamurthy-number/0
"""

import math

def check_number(number):
    value = int(number)
    s = 0
    for digit in number:
        factorial = math.factorial(int(digit))
        s += factorial
    if s == value:
        return 'YES'
    else:
        return 'NO'

t = int(input())
for i in range(0, t):
    n = input().strip()
    print(check_number(n))

