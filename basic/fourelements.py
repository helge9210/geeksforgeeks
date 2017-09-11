#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/four-elements/0
"""

from itertools import combinations


def find_four_elements(array, target_sum):
    size = len(array)
    pair_sums = {}
    pair_values = []
    for pair in combinations(range(size), 2):
        pair_sums[pair] = array[pair[0]] + array[pair[1]]
        pair_values.append(array[pair[0]] + array[pair[1]])

    pair_keys = sorted(pair_sums.keys())
    for ind, pair in enumerate(pair_keys):
        t = target_sum - pair_sums[pair]
        try:
            f_ind = pair_values.index(t)
            if f_ind != ind \
               and pair[0] != pair_keys[f_ind][0] \
               and pair[0] != pair_keys[f_ind][1] \
               and pair[1] != pair_keys[f_ind][0] \
               and pair[1] != pair_keys[f_ind][1]:
                return 1
        except ValueError:
            pass

    return 0


t = int(input())
for i in range(0, t):
    n = int(input())
    arr = [int(v) for v in input().strip().split(' ')]
    s = int(input())
    print(find_four_elements(arr, s))


