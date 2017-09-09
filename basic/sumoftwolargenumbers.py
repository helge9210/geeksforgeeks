#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/sum-of-numbers-or-number/0
"""

def calculate_sum(ns):
    number_x, number_y = ns.split(' ')
    result = []
    rev_num_x = [int(v) for v in list(reversed(number_x))]
    rev_num_y = [int(v) for v in list(reversed(number_y))]
    overflow = 0
    ind = 0
    while True:
        if ind < len(rev_num_x):
            x_val = rev_num_x[ind]
        else:
            x_val = 0

        if ind < len(rev_num_y):
            y_val = rev_num_y[ind]
        else:
            y_val = 0

        overflow, reminder_sum = divmod(x_val + y_val + overflow, 10)
        result.append(reminder_sum)
        ind += 1
        
        if ind >= len(rev_num_x) and ind >= len(rev_num_y):
            if overflow > 0:
                result.append(overflow)
            break

    s_result = ''.join([str(v) for v in reversed(result)])
    if len(s_result) == len(number_x):
        return s_result
    else:
        return number_x


t = int(input())
for i in range(0, t):
    ns = input().strip()
    print(calculate_sum(ns))

