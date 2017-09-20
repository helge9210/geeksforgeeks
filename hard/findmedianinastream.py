#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/find-median-in-a-stream/0
"""

import math
from heapq import *

UPPER_MIN_HEAP = []
LOWER_MAX_HEAP = []


def find_median(value):
    if len(UPPER_MIN_HEAP) == 0 and len(LOWER_MAX_HEAP) == 0:
        heappush(UPPER_MIN_HEAP, value)
        return value
    elif len(UPPER_MIN_HEAP) > len(LOWER_MAX_HEAP):
        if value > UPPER_MIN_HEAP[0]:
            temp = heappop(UPPER_MIN_HEAP)
            heappush(UPPER_MIN_HEAP, value)
            heappush(LOWER_MAX_HEAP, -1*temp)
        else:
            heappush(LOWER_MAX_HEAP, -1*value)
        return math.floor((UPPER_MIN_HEAP[0] + -1*LOWER_MAX_HEAP[0])/2)
    elif len(UPPER_MIN_HEAP) < len(LOWER_MAX_HEAP):
        if value < -1*LOWER_MAX_HEAP[0]:
            temp = -1*heappop(LOWER_MAX_HEAP)
            heappush(LOWER_MAX_HEAP, -1*value)
            heappush(UPPER_MIN_HEAP, temp)
        else:
            heappush(UPPER_MIN_HEAP, value)
        return math.floor((UPPER_MIN_HEAP[0] + -1*LOWER_MAX_HEAP[0])/2)
    else:
        if value >= -1*LOWER_MAX_HEAP[0] and value <= UPPER_MIN_HEAP[0]:
            heappush(UPPER_MIN_HEAP, value)
            return value
        elif value >= UPPER_MIN_HEAP[0]:
            temp = UPPER_MIN_HEAP[0]
            heappush(UPPER_MIN_HEAP, value)
            return temp
        else:
            temp = -1*LOWER_MAX_HEAP[0]
            heappush(LOWER_MAX_HEAP, -1*value)
            return temp


t = int(input())
for i in range(0, t):
    n = int(input())
    print(find_median(n))


