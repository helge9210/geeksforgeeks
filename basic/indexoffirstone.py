#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/index-of-first-1-in-a-sorted-array-of-0s-and-1s/0
"""


def find_first_one(array):
    if array[-1] == 0:
        return -1
    if array[0] == 1:
        return 0
    
    size = len(array)
    if size == 1:
        return 0
    left = 0
    right = size - 1
    middle = int((right - left)/2) + left
    while True:
        print(left, right, middle, array[middle:middle+2])
        if array[middle:middle+2] == [0, 1]:
            return middle+1
        elif array[middle:middle+2] == [0, 0]:
            left = middle
            middle = int((right - left)/2) + left
        elif array[middle:middle+2] == [1, 1]:
            right = middle
            middle = int((right - left)/2) + left


t = int(input())
for i in range(0, t):
    n = int(input())
    arr = [int(v) for v in input().strip().split(' ')]
    print(find_first_one(arr))
