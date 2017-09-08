#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/fighting-the-darkness/0
"""
def find_max(arr):
    vector = [int(el) for el in arr.split(' ')]
    return max(vector)


t = int(input())
for i in range(0, t):
    n = int(input())
    array = input().strip()
    print(find_max(array))


