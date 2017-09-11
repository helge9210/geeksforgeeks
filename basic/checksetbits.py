#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/check-set-bits/0
"""


def check_set_bits(number):
    if number == 0:
        return 'NO'
    ratio = number
    while ratio != 0:
        ratio, reminder = divmod(ratio, 2)
        print(ratio, reminder)
        if reminder == 0:
            return 'NO'
    return 'YES'


t = int(input())
for i in range(0, t):
    n = int(input())
    print(check_set_bits(n))
