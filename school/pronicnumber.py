#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/pronic-number/0
"""

def pronic_numbers(range):
    numbers = []
    mul1 = 0
    while True:
        product = mul1*(mul1+1)
        if product <= range:
            numbers.append(product)
            mul1 += 1
        else:
            break
    return ' '.join([str(n) for n in numbers])

t = int(input())
for i in range(0, t):
    n = int(input())
    print(pronic_numbers(n))


