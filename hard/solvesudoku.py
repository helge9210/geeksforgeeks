#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/solve-the-sudoku/0
"""


def get_numbers_col(array, row, col):
    numbers = set()
    for r in range(9):
        number = array[r*9 + col]
        if number:
            numbers.add(number)
    return numbers


def get_numbers_row(array, row, col):
    numbers = set()
    for c in range(9):
        number = array[row*9 + c]
        if number:
            numbers.add(number)
    return numbers


def get_numbers_block(array, row, col):
    block_r = int(row / 3)*3
    block_c = int(col / 3)*3
    numbers = set()
    for r in range(3):
        for c in range(3):
            number = array[(block_r + r)*9 + block_c + c]
            if number:
                numbers.add(number)
    return numbers


def get_available_numbers(array, row, col):
    numbers = set(range(1, 10))
    row_numbers = get_numbers_row(array, row, col)
    col_numbers = get_numbers_col(array, row, col)
    block_numbers = get_numbers_block(array, row, col)
    return list(numbers - row_numbers - col_numbers - block_numbers)


def print_current(array):
    print('')
    for r in range(9):
        print(array[r*9:r*9+9])


def solve_sudoku(array):
    stack = list()
    stack.append(array)
    while stack:
        current = stack.pop()
        if 0 not in current:
            return ' '.join([str(v) for v in current])

        r, c = divmod(current.index(0), 9)
        numbers = get_available_numbers(current, r, c)
        if not numbers:
            continue

        for number in reversed(numbers):
            new_board = current[:]
            new_board[r*9 + c] = number
            stack.append(new_board)


t = int(input())
for i in range(0, t):
    arr = [int(v) for v in input().strip().split()]
    print(solve_sudoku(arr))


