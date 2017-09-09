#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/equal-to-product/0
"""

def check_product(array, product):
    for ind, el in enumerate(array):
        ratio = product / el
        try:
            ind_1 = array.index(ratio)
            if ind_1 != ind:
                return 'Yes'
        except ValueError:
            pass
    return 'No'
    
t = int(input())
for i in range(0, t):
    n, p = [int(v) for v in input().strip().split(' ')]
    a = [int(v) for v in input().strip().split(' ')]
    print(check_product(a, p))

