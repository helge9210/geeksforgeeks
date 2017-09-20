#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/n-queen-problem/0
"""

import copy


def fill_danger(board, row, position):
    for offset in range(1, len(board) - row):
        board[row+offset][position] = 'd'
        if position+offset < len(board):
            board[row+offset][position+offset] = 'd'
        if position-offset >= 0:
            board[row+offset][position-offset] = 'd'

    return board


def check_positions(board, row):
    combinations = []
    if row == len(board):
        output = []
        for r in board:
            output.append(r.index('q')+1)
        return '[' + ' '.join([str(v) for v in output]) + ' ]'
    found = False
    for position in range(len(board)):
        if board[row][position] != 'd':
            found = True
            p_board = copy.deepcopy(board)
            p_board[row][position] = 'q'
            p_board = fill_danger(p_board, row, position)
            c = check_positions(p_board, row+1)
            if c:
                if isinstance(c, list):
                    combinations.extend(c)
                else:
                    combinations.append(c)
    if not found:
        return False

    if len(combinations) == 1:
        return combinations[0]
    else:
        return combinations


def find_n_queens(size):
    board = []
    if size == 1:
        return '[1 ]'
    for _ in range(size):
        board.append(['0']*size)
    combinations = check_positions(board, 0)
    if combinations:
        return ' '.join(combinations)
    else:
        return '-1'


t = int(input())
for i in range(0, t):
    n = int(input())
    print(find_n_queens(n))
