#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/minimum-points-to-reach-destination/0
"""


from pprint import pprint
from collections import deque


def print_maze(maze):
    print('')
    for row in maze:
        print(row)


def convert_array(array, rows, cols):
    output = []
    for row in range(rows):
        output.append(array[row*rows:row*rows+cols])
    return output


def create_maze(rows, cols):
    output = []
    for row in range(rows):
        output.append([None]*cols)
    return output


def get_next_steps(array, row, col):
    steps = []
    rows = len(array)
    cols = len(array[0])
    directions = [(1, 0),  # down

                  (0, 1)]  # right
    for direction in directions:
        if row + direction[0] >= 0 and \
           row + direction[0] < rows and \
           col + direction[1] >= 0 and \
           col + direction[1] < cols:
            steps.append((row+direction[0],
                          col+direction[1]))
    return steps


def find_min_path(array, rows, cols):
    maze = convert_array(array, rows, cols)
    print_maze(maze)
    stack = [((0, 0), [])]
    pathes = []
    while stack:
        current = stack.pop()
        if current[0] == (rows - 1, cols - 1):
            v = current[1][:]
            v.append(current[0])
            p = []
            for el in v:
                p.append(maze[el[0]][el[1]])
            pathes.append(p)
            continue
        if current[0] not in current[1]:
            v = current[1][:]
            v.append(current[0])
            next_steps = get_next_steps(maze, current[0][0],
                                        current[0][1])
            for n in next_steps:
                stack.append((n, v[:]))

    pprint(pathes) # calculate minimal points per path, chose min



t = int(input())
for i in range(0, t):
    r, c = [int(v) for v in input().strip().split()]
    arr = [int(v) for v in input().strip().split()]
    print(find_min_path(arr, r, c))


