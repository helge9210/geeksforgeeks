#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/immediate-smaller-element/0
"""

def immediate_smaller(array):
    output = []
    for ind, el in enumerate(array[:-1]):
        if el > array[ind+1]:
            output.append(array[ind+1])
        else:
            output.append(-1)
    output.append(-1)
    return ' '.join([str(v) for v in output])
        
t = int(input())
for i in range(0, t):
    n = int(input())
    arr = [int(v) for v in input().strip().split(' ')]
    print(immediate_smaller(arr))

