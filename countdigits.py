#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/count-digits/0
"""

def count_dividers(number):
    value = int(number)
    count = 0
    for digit in number:
        if digit == '0':
            continue
        ratio, reminder = divmod(value, int(digit))
        if reminder == 0:
            count += 1
    return count

t = int(input())
for i in range(0, t):
    n = input().strip()
    print(count_dividers(n))


