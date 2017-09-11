#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/count-triplets-with-sum-smaller-than-x/0
"""

def count_triplets(array, x):
    array.sort()
    count = 0
    for i in range(len(array) - 2):
        j = i + 1
        k = len(array) - 1
        while (j < k):
            if array[i] + array[j] + array[k] >= x:
                k -= 1
            else:
                count += (k - j)
                j += 1

    return count

        

t = int(input())
for i in range(0, t):
    n, s = [int(v) for v in input().strip().split(' ')]
    arr = [int(v) for v in input().strip().split(' ')]
    print(count_triplets(arr, s))


