#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/decode-the-pattern/0
"""


def decode_pattern(step):
    pattern = ['1']
    for _ in range(1, step):
        decoded = []
        counter = 1
        last_element = None
        for el in pattern:
            if el != last_element and last_element is None:
                last_element = el
            elif el == last_element:
                counter += 1
            else:
                decoded.append(str(counter))
                decoded.append(last_element)
                counter = 1
                last_element = el
        decoded.append(str(counter))
        decoded.append(last_element)
        pattern = decoded
    return ''.join(pattern)


t = int(input())
for i in range(0, t):
    n = int(input())
    print(decode_pattern(n))

