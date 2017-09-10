#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/total-number-of-strings/0
"""

from math import factorial as f

def check_combinations(str_len):
    if str_len == 1:
        return 3
    elif str_len == 2:
        return 8
    elif str_len > 2:
        return int(1 + 2*n + f(n)/f(n-2) + f(n)/(f(n-3)*2) + f(n)/(2*f(n-2)))


t = int(input())
for i in range(0, t):
    n = int(input())
    print(check_combinations(n))
