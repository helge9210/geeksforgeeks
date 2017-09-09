#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/check-if-given-four-points-form-a-square/0
"""

import math

def dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def check_square(points):
    coords = list(zip(points[::2], points[1::2]))
    unique_coords = set(coords)
    if len(coords) > len(unique_coords):
        return '0'
    c0 = coords[0]
    c1 = coords[1]
    c2 = coords[2]
    c3 = coords[3]

    d1 = dist(c0, c1)
    d2 = dist(c0, c2)
    d3 = dist(c0, c3)
    if d1 == d2 and math.isclose(d3, d1*math.sqrt(2)):
        return '1'
    elif d1 == d3 and math.isclose(d2, d1*math.sqrt(2)):
        return '1'
    elif d2 == d3 and math.isclose(d1, d2*math.sqrt(2)):
        return '1'
    else:
        return '0'
    
    
        

t = int(input())
for i in range(0, t):
    n = [float(v) for v in input().strip().split(' ')]
    print(check_square(n))

