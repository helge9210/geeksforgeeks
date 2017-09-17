#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/number-of-1s-in-smallest-repunits/0
"""


def find_smallest_repunit(number):
    repuint = '1'
    while int(repuint) % number != 0:
        repuint += '1'

    return len(repuint)


t = int(input())
for i in range(0, t):
    n = int(input())
    print(find_smallest_repunit(n))
