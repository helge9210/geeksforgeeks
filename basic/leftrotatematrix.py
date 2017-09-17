#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/left-rotate-matrix-k-times/0
"""

def rotate_matrix(rows, cols, k, array):
    k = k % cols
    output = []
    if k == 0:
        return ' '.join(array)

    for r_ind in range(rows):
        col_start = r_ind*cols
        for c_ind in range(cols):
            output.append(array[col_start + ((c_ind + k) % cols)])

    return ' '.join(output)


t = int(input())
for i in range(0, t):
    r, c, k  = [int(v) for v in input().strip().split(' ')]
    arr = input().strip().split(' ')
    print(rotate_matrix(r, c, k, arr))
