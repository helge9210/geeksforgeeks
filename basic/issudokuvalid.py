#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/is-sudoku-valid/0
"""


def is_block_valid(block):
    print(block)
    elements = set()
    for element in block:
        if element == '0':
            continue
        if element in elements:
            return False
        else:
            elements.add(element)
    return True


def check_sudoku(array):
    subblocks = [(0, 0),
                 (0, 3),
                 (0, 6),
                 (3, 0),
                 (3, 3),
                 (3, 6),
                 (6, 0),
                 (6, 3),
                 (6, 6)]

    # check horizontal
    
    for row in range(9):
        block = []
        for col in range(9):
            block.append(array[row*9 + col])
        if not is_block_valid(block):
            return 0  # not valid

    # check vertical
    
    for col in range(9):
        block = []
        for row in range(9):
            block.append(array[row*9 + col])
        if not is_block_valid(block):
            return 0  # not valid

    # check subblocks

    for subblock in subblocks:
        block = []
        for row in range(3):
            for col in range(3):
                block.append(array[(subblock[1] + row)*9 + subblock[0] + col])
        if not is_block_valid(block):
            return 0  # not valid

    return 1


t = int(input())
for i in range(0, t):
    arr = input().strip().replace('  ', ' ').split(' ')
    print(check_sudoku(arr))


