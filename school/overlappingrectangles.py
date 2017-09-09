#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/overlapping-rectangles/0
"""

def check_overlap(r1, r2):
    x_boundaries = sorted([r2[0], r2[2]])
    y_boundaries = sorted([r2[1], r2[3]])

    if (r1[0] >= x_boundaries[0] and r1[0] <= x_boundaries[1]) or \
       (r1[2] >= x_boundaries[0] and r1[2] <= x_boundaries[1]):
        horizontal_intersect = True
    else:
        horizontal_intersect = False

    if (r1[1] >= y_boundaries[0] and r1[1] <= y_boundaries[1]) or \
       (r1[3] >= y_boundaries[0] and r1[3] <= y_boundaries[1]):
        vertical_intersect = True
    else:
        vertical_intersect = False
    if vertical_intersect and horizontal_intersect:
        return '1'
    else:
        return '0'
        


t = int(input())
for i in range(0, t):
    rect1 = [int(v) for v in input().strip().split(' ')]
    rect2 = [int(v) for v in input().strip().split(' ')]
    print(check_overlap(rect1, rect2))

