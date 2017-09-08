#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/minimum-number-to-form-the-sum-even/0
"""

def process_array(size, value):
    numbers = value.split(' ')
    if len(numbers) != size:
        raise ValueError
    s = 0
    for number in numbers:
        v = int(number[-1])
        s = (s + v) % 10
    if s % 2 == 0:
        print('2')
    else:
        print('1')
        
t = int(input())
for i in range(0, t):
    arr_size = int(input())
    arr_value = input().strip()
    process_array(arr_size, arr_value)


