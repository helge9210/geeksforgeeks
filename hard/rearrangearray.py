#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/rearrange-an-array-with-o1-extra-space/0
"""


import math


def rearrange_array(array):
    a_n = len(array)
    for ind in range(a_n):
        array[ind] = (array[ind] +
                      (array[array[ind]] % a_n) * a_n)
    for ind in range(a_n):
        array[ind] = int(math.floor(array[ind] / a_n))
    return ' '.join([str(v) for v in array])


t = int(input())
for i in range(0, t):
    n = int(input())
    arr = [int(v) for v in input().strip().split()]
    print(rearrange_array(arr))
