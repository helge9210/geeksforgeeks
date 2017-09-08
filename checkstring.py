#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/check-string/0
"""

def check_string(string):
    if len(set(list(string))) == 1:
        print('YES')
    else:
        print('NO')

t = int(input())
for i in range(0, t):
    s = input().strip()
    check_string(s)

