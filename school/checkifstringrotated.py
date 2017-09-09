#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/check-if-string-is-rotated-by-two-places/0
"""

def check_rotated(original, rotated):
    original_left = original[2:] + original[:2]
    original_right = original[-2:] + original[:-2]
    if rotated == original_left or rotated == original_right:
        return '1'
    else:
        return '0'

t = int(input())
for i in range(0, t):
    s1 = input().strip()
    s2 = input().strip()
    print(check_rotated(s1, s2))

