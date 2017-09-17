#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/save-knights/0
"""

import math


def count_positions(board_size):
    if board_size == 2:
        return 4
    else:
        return math.ceil((board_size*board_size)/2.0)


t = int(input())
for i in range(0, t):
    n = int(input())
    print(count_positions(n))


