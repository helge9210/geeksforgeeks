#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/longest-valid-parentheses/0
"""

def count_parentheses(par_string):
    stack = []
    intervals = []
    end_points = []
    merged_intervals = []
    for ind, el in enumerate(par_string):
        if el == '(':
            stack.append((el, ind))
        else:
            if len(stack) > 0 and stack[-1][0] == '(':
                s_ind = stack.pop()[1]
                intervals.append((s_ind, ind))

    intervals.sort(key=lambda x: x[0])
    #print(intervals)
    start = intervals[0][0]
    end = intervals[0][1]
    for ind, interval in enumerate(intervals[1:]):
        #print(start, end, interval)
        if start < interval[0] and end < interval[0]:
            merged_intervals.append((start, end))
            start = interval[0]
            end = interval[1]
        elif start < interval[0] and end > interval[1]:
            pass
    merged_intervals.append((start, end))

    conc_intervals = []
    start = merged_intervals[0][0]
    end = merged_intervals[0][1]
    for ind, interval in enumerate(merged_intervals[1:]):
        if end + 1 == interval[0]:
            end = interval[1]
        else:
            conc_intervals.append((start, end))
            start = interval[0]
            end = interval[1]

    conc_intervals.append((start, end))
    return max([v[1] - v[0] + 1 for v in conc_intervals])


t = int(input())
for i in range(0, t):
    n = input().strip()
    print(count_parentheses(n))

