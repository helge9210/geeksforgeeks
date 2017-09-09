#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/sort-first-half-in-ascending-and-second-half-in-descending/0
"""

import math

def sort_array(a):
    value_array = [int(v) for v in a.split(' ')]
    value_array.sort()
    mid_ind = math.floor(len(value_array)/2)
    result_array = value_array[:mid_ind] + list(reversed(value_array[mid_ind:]))
    return ' '.join([str(v) for v in result_array])

t = int(input())
for i in range(0, t):
    n = int(input())
    array = input().strip()
    print(sort_array(array))


