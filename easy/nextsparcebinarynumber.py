#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/next-sparse-binary-number/0
"""


def decimal_to_binary(number):
    result = []
    rest = number
    while rest > 0:
        ratio, reminder = divmod(rest, 2)
        result.append(reminder)
        rest = ratio
    return result


def is_sparse(binary_digits):
    previous = 0
    for digit in binary_digits:
        if digit == 1 and digit == previous:
            return False
        previous = digit
    return True


def next_sparse_number(number):
    while True:
        if is_sparse(decimal_to_binary(number)):
            return number
        number += 1


t = int(input())
for i in range(0, t):
    n = int(input())
    print(next_sparse_number(n))
