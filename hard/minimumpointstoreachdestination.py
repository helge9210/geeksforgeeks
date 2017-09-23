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
    costs = create_maze(rows, cols)
    costs[-1][-1] = 1 - maze[-1][-1]
    queue = deque()
    queue.append((rows-1, cols-1))
    while queue:
        current_cell = queue.popleft()
        print_maze(costs)
        nearby_cells = get_next_steps(costs,
                                      current_cell[0],
                                      current_cell[1])
        print(nearby_cells)
        surround_costs = []
        for nearby_cell in nearby_cells:
            if costs[nearby_cell[0]][nearby_cell[1]] is not None:
                surround_costs.append(
                    costs[nearby_cell[0]][nearby_cell[1]]
                )
            else:
                queue.append(nearby_cell)
        print(surround_costs)


t = int(input())
for i in range(0, t):
    r, c = [int(v) for v in input().strip().split()]
    arr = [int(v) for v in input().strip().split()]
    print(find_min_path(arr, r, c))


