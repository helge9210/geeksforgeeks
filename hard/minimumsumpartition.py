#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/minimum-sum-partition/0
"""

from pprint import pprint
import heapq
from collections import deque

def find_partition(array):
    rev_array = [-1*el for el in array]
    heapq.heapify(rev_array)
    queue = deque([rev_array[:]])
    min_diff = sum(array)
    while len(queue) > 0:
        r = queue.popleft()
        #print(r)
        #print(min_diff)
        if len(r) == 1:
            continue
        if min_diff == 1:
            break
        if -1*r[0] > -1*sum(r[1:]):
            min_diff = min(min_diff, -1*r[0] - -1*sum(r[1:]))
            continue
        elif r[0] == sum(r[1:]):
            min_diff = 0
            break
        else:
            n1 = -1*heapq.heappop(r)
            n2 = -1*heapq.heappop(r)
            queue.append(r[:])
            #print('right', n2 + n1)
            heapq.heappush(queue[-1], -1*(n2 + n1))
            queue.append(r[:])
            #print('left', n1 - n2)
            heapq.heappush(queue[-1], -1*(n1 - n2))

    return min_diff


t = int(input())
for i in range(0, t):
    n = int(input())
    arr = [int(v) for v in input().strip().split(' ')]
    print(find_partition(arr))


