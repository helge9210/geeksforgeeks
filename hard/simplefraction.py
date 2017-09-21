#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/a-simple-fraction/0
"""

def get_fraction(number, divisor):
    after_dot = []
    reminders = set()
    ratio, reminder = divmod(number, divisor)
    before_dot = ratio
    number = reminder*10
    periodic = False
    while True:
        ratio, reminder = divmod(number, divisor)
        print(ratio, reminder, number, divisor)
        number = reminder*10
        if reminder == 0:
            after_dot.append(ratio)
            break
        if reminder in reminders:
            periodic = True
            break
        else:
            after_dot.append(ratio)
            reminders.add(reminder)

    #after_dot.append(ratio)

    if periodic:
        output = '{}.({})'.format(before_dot,
                                  ''.join([str(v) for v in after_dot]))
    else:
        output = '{}.{}'.format(before_dot,
                                ''.join([str(v) for v in after_dot]))


    return output


t = int(input())
for i in range(0, t):
    n = int(input())
    d = int(input())
    print(get_fraction(n, d))


