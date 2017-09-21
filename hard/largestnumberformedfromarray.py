#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/largest-number-formed-from-an-array/0
"""

from functools import cmp_to_key

def my_cmp(x, y):

    if x == y:
        return 0
    elif int(x + y) < int(y + x):
        return -1
    else:
        return 1


def find_largest_number(array):
    longest_len = len(max(array, key=lambda x: len(x)))
    sorted_numbers = []
    array.sort(key=cmp_to_key(my_cmp), reverse=True)
    return ''.join(array)


t = int(input())
for i in range(0, t):
    n = int(input())
    arr = input().strip().split(' ')
    print(find_largest_number(arr))


