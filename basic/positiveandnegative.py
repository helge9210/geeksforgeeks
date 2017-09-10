#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/positive-and-negative-elements/0
"""

def arrange_array(array):
    l = len(array)
    p_ind = 0
    n_ind = 0
    output = []
    while True:
        cont = False
        while p_ind < l:
            if array[p_ind] >= 0:
                output.append(array[p_ind])
                p_ind += 1
                break
            else:
                p_ind += 1
        while n_ind < l:
            if array[n_ind] < 0:
                output.append(array[n_ind])
                n_ind += 1
                break
            else:
                n_ind += 1
        if p_ind == l and n_ind == l:
            break
    return ' '.join([str(v) for v in output])

t = int(input())
for i in range(0, t):
    n = int(input())
    arr = [int(v) for v in input().strip().split(' ')]
    print(arrange_array(arr))


