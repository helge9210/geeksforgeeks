#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/find-the-highest-number/0
"""

def find_highest(array):
    for ind, el in enumerate(array[:-1]):
        if el > array[ind + 1]:
            return el
    return array[-1]

t = int(input())
for i in range(0, t):
    n = int(input())
    arr = [int(v) for v in input().strip().split(' ')]
    print(find_highest(arr))


