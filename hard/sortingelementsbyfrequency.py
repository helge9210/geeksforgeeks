#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/sorting-elements-of-an-array-by-frequency/0
"""


def sort_by_frequency(array):
    value_counters = {}
    value_counter_pairs = []
    for el in array:
        if el not in value_counters:
            value_counters[el] = 0
        value_counters[el] += 1

    for value, c in value_counters.items():
        value_counter_pairs.append((c, value))

    value_counter_pairs.sort(key=lambda x: x[0], reverse=True)
    output = []
    for pair in value_counter_pairs:
        for _ in range(pair[0]):
            output.append(pair[1])

    return ' '.join([str(v) for v in output])


t = int(input())
for i in range(0, t):
    n = int(input())
    arr = [int(v) for v in input().strip().split(' ')]
    print(sort_by_frequency(arr))


