#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/number-of-unique-rectangles/0
"""

import math

def calculate_rectangles(n_cubes):
    result = n_cubes
    for i in range(2, int(math.sqrt(n_cubes) + 1)):
        c = max(0, math.floor(n_cubes/i) - i + 1)
        result += c
    return result


t = int(input())
for i in range(0, t):
    n = int(input())
    print(calculate_rectangles(n))


