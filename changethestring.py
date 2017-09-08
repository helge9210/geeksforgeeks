#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/change-the-string/0
"""

def process_string(string):
    first_char = string[0]
    if first_char.isupper():
        print(string.upper())
    else:
        print(string.lower())

t = int(input())
for i in range(0, t):
    s = input().strip()
    process_string(s)

