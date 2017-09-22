#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/find-prime-numbers-in-a-range/0
"""


def find_prime_numbers(start, end):
    output = []
    block = end
    sieve = list([False]*block)
    sieve[0] = True
    sieve[1] = True
    prime = 2
    while prime < len(sieve):
        for i in range(2, end):
            if i*prime < len(sieve):
                sieve[i*prime] = True
            else:
                break

        found = False
        for j in range(prime+1, len(sieve)):
            if not sieve[j]:
                prime = j
                found = True
                break
        if not found:
            break

    for ind, el in enumerate(sieve):
        if not el:
            output.append(ind)

    return ' '.join([str(v) for v in output if v >= start])


t = int(input())
for i in range(0, t):
    n, m = [int(v) for v in input().strip().split(' ')]
    print(find_prime_numbers(n, m))
