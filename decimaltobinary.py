#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/decimal-to-binary/0
"""

def decimal_to_binary(number):
    result = []
    rest = number
    while rest > 0:
        ratio, reminder = divmod(rest, 2)
        result.append(reminder)
        rest = ratio
    return ''.join([str(r) for r in reversed(result)])



t = int(input())
for i in range(0, t):
    n = int(input().strip())
    print(decimal_to_binary(n))


