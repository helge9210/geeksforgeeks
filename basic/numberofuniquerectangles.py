#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/number-of-unique-rectangles/0
"""

def calculate_rectangles(n_cubes):
    result = 0
    for i in range(1, n_cubes + 1):
        for j in range(i, n_cubes + 1):
            if i*j <= n_cubes:
                result += 1
    return result


t = int(input())
for i in range(0, t):
    n = int(input())
    print(calculate_rectangles(n))


