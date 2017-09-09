#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/student-record/0
"""

def find_maximum_avg(number, records):
    averages = {}
    for _ in range(number):
        name, p1, p2, p3 = records[:4]
        records = records[4:]
        avg = int((int(p1) + int(p2) + int(p3))/3)
        if avg not in averages:
            averages[avg] = []
        averages[avg].append(name)
    max_avg = max(averages.keys())
    return ' '.join([' '.join(averages[max_avg]), str(max_avg)])


t = int(input())
for i in range(0, t):
    n = int(input())
    d = input().strip().split(' ')
    print(find_maximum_avg(n, d))


