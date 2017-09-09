#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/check-binary-string/0
"""

def check_string(binary_number):
    """
    start | valid_no_1 | valid_1 | valid_0 | invalid
    start (0) -> valid_no_1
    start (1) -> valid_1
    valid_no_1 (0) -> valid_no_1
    valid_no_1 (1) -> valid_1
    valid_1 (1) -> valid_1
    valid_1 (0) -> valid_0
    valid_0 (0) -> valid_0
    valid_0 (1) -> invalid
    
    """
    state = 'start'
    for digit in binary_number:
        if state == 'start' and digit == '0':
            state = 'valid_no_1'
        elif state == 'start' and digit == '1':
            state = 'valid_1'
        elif state == 'valid_no_1' and digit == '0':
            state = 'valid_no_1'
        elif state == 'valid_no_1' and digit == '1':
            state = 'valid_1'
        elif state == 'valid_1' and digit == '0':
            state = 'valid_0'
        elif state == 'valid_1' and digit == '1':
            state = 'valid_1'
        elif state == 'valid_0' and digit == '0':
            state = 'valid_0'
        elif state == 'valid_0' and digit == '1':
            state = 'invalid'
            break

    if state == 'invalid':
        return 'INVALID'
    else:
        return 'VALID'


    
t = int(input())
for i in range(0, t):
    n = input().strip()
    print(check_string(n))


