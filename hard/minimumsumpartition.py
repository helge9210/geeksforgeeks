#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/minimum-sum-partition/0
"""

from pprint import pprint

def find_partition(array):
    s = sum(array)
    p = [[True for _ in range(len(array) + 1)]]
    for _ in range(s):
        row = []
        for _ in range(len(array) + 1):
            row.append(False)
        p.append(row)
    print(s)
    for i in range(s):
        for j in range(len(array)):
            if i - array[j - 1] >= 0:
                p[i][j] = p[i][j-1] or p[i-array[j-1]][j-1]
            else:
                p[i][j] = p[i][j-1]

    pprint(p)
    print(p[int(s/2)][len(array)])



t = int(input())
for i in range(0, t):
    n = int(input())
    arr = [int(v) for v in input().strip().split(' ')]
    print(find_partition(arr))


