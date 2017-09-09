#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/row-with-minimum-number-of-1s/0
"""
def process_matrix(rows, cols, vector):
    min_count_ind = [cols+1, -1]
    matrix = vector
    for i in range(rows):
        current_row = matrix[:cols]
        matrix = matrix[cols:]
        number_ones = current_row.count('1')
        if number_ones == 0:
            continue
        elif number_ones < min_count_ind[0]:
            min_count_ind[0] = number_ones
            min_count_ind[1] = i
    print(min_count_ind[1])


t = int(input())
for i in range(0, t):
    n, m = [int(v) for v in input().strip().split(' ')]
    vector = input().strip().split(' ')
    process_matrix(n, m, vector)

