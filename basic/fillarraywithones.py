#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/fill-array-by-1s/0
"""

import math


def count_iterations(array):
    max_length = 0
    length = 0
    for el in array:
        print(el, length, max_length)
        if el == '0':
            length += 1
        elif el == '1':
            if length > 0 and length > max_length:
                max_length = length
            length = 0
    if max_length == len(array) or max_length == 0:
        return -1
    elif length > 0 and length > int(math.ceil(max_length/2)):
        return length
    else:
        return(int(math.ceil(max_length/2)))


t = int(input())
for i in range(0, t):
    n = int(input())
    arr = input().strip().split(' ')
    print(count_iterations(arr))
