#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/sum-of-lengths-of-non-overlapping-subarrays/0
"""


def find_sum(array, max_value):
    sub_arrays = []
    sub_array = []
    for el in array:
        if el > max_value:
            if max_value in sub_array:
                sub_arrays.append(sub_array)
                sub_array = []
            else:
                sub_array = []
        else:
            sub_array.append(el)
    if max_value in sub_array:
        sub_arrays.append(sub_array)
    return sum([len(a) for a in sub_arrays])


t = int(input())
for i in range(0, t):
    n = int(input())
    arr = [int(v) for v in input().strip().split(' ')]
    max_k = int(input())
    print(find_sum(arr, max_k))
