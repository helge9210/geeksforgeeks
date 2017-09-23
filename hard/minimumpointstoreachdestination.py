#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/minimum-points-to-reach-destination/0
"""


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
    directions = [(-1, 0),  # up

                  (0, -1)]  # left
    for direction in directions:
        if row + direction[0] >= 0 and \
           row + direction[0] < rows and \
           col + direction[1] >= 0 and \
           col + direction[1] < cols:
            steps.append((row+direction[0],
                          col+direction[1]))
    return steps


def get_neighbours(array, row, col):
    costs = []
    rows = len(array)
    cols = len(array[0])
    directions = [(1, 0),  # down

                  (0, 1)]  # right
    for direction in directions:
        if row + direction[0] >= 0 and \
           row + direction[0] < rows and \
           col + direction[1] >= 0 and \
           col + direction[1] < cols:
            costs.append(array[row+direction[0]][col+direction[1]])
    return costs


def find_min_path(array, rows, cols):
    maze = convert_array(array, rows, cols)
    costs = create_maze(rows, cols)
    # print_maze(maze)
    # print_maze(costs)
    stack = deque()
    stack.append((rows - 1, cols - 1))
    while stack:
        current = stack.popleft()
        next_steps = get_next_steps(maze, current[0], current[1])
        for step in next_steps:
            stack.append(step)
        nearby_costs = get_neighbours(costs, current[0], current[1])
        if len(nearby_costs) == 0:
            costs[current[0]][current[1]] = max(
                1 - maze[current[0]][current[1]], 1)
        else:
            c = min([max(v - maze[current[0]][current[1]], 1)
                     for v in nearby_costs if v is not None])
            costs[current[0]][current[1]] = c
        if current == (0, 0):
            break
    # print_maze(costs)

    return costs[0][0]


t = int(input())
for i in range(0, t):
    r, c = [int(v) for v in input().strip().split()]
    arr = [int(v) for v in input().strip().split()]
    print(find_min_path(arr, r, c))
