#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/chocolate-station/0
"""


def calculate_chocolates(array, cost):
    stations = [0]
    current = 0
    to_buy = 0
    for station in array:
        price = stations[-1] - station
        current += price
        if current < 0:
            to_buy += abs(current)
            current = 0
        stations.append(station)

    return to_buy*cost


t = int(input())
for i in range(0, t):
    n = int(input())
    arr = [int(v) for v in input().strip().split(' ')]
    c = int(input())
    print(calculate_chocolates(arr, c))


