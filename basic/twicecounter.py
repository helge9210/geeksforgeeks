#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/twice-counter/0
"""


def count_double_words(array):
    words = {}
    counter = 0
    for word in array:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1

    for word, c in words.items():
        if c == 2:
            counter += 1

    return counter


t = int(input())
for i in range(0, t):
    n = int(input())
    arr = input().strip().split(' ')
    print(count_double_words(arr))
