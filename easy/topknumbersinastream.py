#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/top-k-numbers/0
"""

import heapq


def find_k_largest(k_largest, array):
    output = []
    counters = {}
    for el in array:
        if el not in counters:
            counters[el] = 0
        counters[el] += 1
        h = []
        for key, value in counters.items():
            heapq.heappush(h, (-1*value, key))

        for _ in range(min(len(h), k_largest)):
            output.append(heapq.heappop(h)[1])

    return ' '.join([str(v) for v in output])


t = int(input())
for i in range(0, t):
    n, k = [int(v) for v in input().strip().split(' ')]
    arr = [int(v) for v in input().strip().split(' ')]
    print(find_k_largest(k, arr))


