#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/x-total-shapes/0
"""

from collections import deque


def print_grid(array, rows, cols):
    print('')
    for row in range(rows):
        print(array[row*cols:row*cols+cols])


def get_neighbours(array, row, col, rows, cols):
    directions = [(1, 0),  # up
                  (-1, 0),  # down
                  (0, 1),  # right
                  (0, -1)]  # left
    neigbours = []
    for direction in directions:
        if ((row+direction[0])*cols + col + direction[1]) < len(array) and \
           row+direction[0] >= 0 and \
           row+direction[0] < rows and \
           col+direction[1] >= 0 and \
           col+direction[1] < cols:
            neigbours.append((row+direction[0], col+direction[1]))
    return neigbours


def count_connected(array, rows, cols):
    # print_grid(array, rows, cols)
    count = 0
    while True:
        if 'X' in array:
            elem_ind = array.index('X')
        else:
            # print_grid(array, rows, cols)
            return count
        count += 1
        stack = deque()
        r, c = divmod(elem_ind, cols)
        stack.append((r, c))
        while stack:
            current = stack.popleft()
            if array[current[0]*cols + current[1]] == 'X':
                array[current[0]*cols + current[1]] = str(count)
                neigbours = get_neighbours(array, current[0],
                                           current[1], rows, cols)
                for neigbour in neigbours:
                    stack.append(neigbour)

        # print_grid(array, rows, cols)
    return count


t = int(input())
for i in range(0, t):
    r, c = [int(v) for v in input().strip().split()]
    arr = list(''.join([v for v in input().strip().split()]))
    print(count_connected(arr, r, c))
