#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/count-the-elements/0
"""


def count_elements(array1, array2):
    max1 = max(array1)
    max2 = max(array2)

    counters = {}
    output = []
    for el in array2:
        if el not in counters:
            counters[el] = 0
        counters[el] += 1

    max_size = max(max1, max2)
    running_sum = 0
    for i in range(0, max_size + 1):
        if i in counters:
            running_sum += counters[i]
        counters[i] = running_sum

    for j in array1:
        output.append(str(counters[j]))

    return ','.join(output)


t = int(input())
for i in range(0, t):
    n = int(input())
    arr1 = [int(v) for v in input().strip().split(' ')]
    arr2 = [int(v) for v in input().strip().split(' ')]
    print(count_elements(arr1, arr2))


