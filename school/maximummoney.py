#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/maximum-money/0
"""
import math

def calculate_money(row):
    houses, money = [int(v) for v in row.split(' ')]
    return int(math.ceil(houses/2)*money)

t = int(input())
for i in range(0, t):
    n = input().strip()
    print(calculate_money(n))

