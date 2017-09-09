#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/difference-between-sums-of-odd-and-even-digits/0
"""

def sum_digits(digits):
    return sum([int(digit) for digit in digits])

def diff_digits(value):
    odd_digits = value[1::2]
    even_digits = value[0::2]
    if (sum_digits(odd_digits) - sum_digits(even_digits)) == 0:
        print('Yes')
    else:
        print('No')

t = int(input())
for i in range(0, t):
    n = input().strip()
    diff_digits(n)

