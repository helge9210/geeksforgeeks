#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/a-simple-fraction/0
"""

def get_fraction(number, divisor):
    after_dot = []
    reminders = []
    ratios = []
    ratio, reminder = divmod(number, divisor)
    #print(number, divisor, ratio, reminder)
    before_dot = ratio
    number = reminder*10
    periodic = False
    ind = None
    while True:
        ratio, reminder = divmod(number, divisor)
        #print(number, divisor, ratio, reminder)

        if (ratio, reminder) in reminders:
            ind = reminders.index((ratio, reminder)) - 1
            break
        elif reminder == 0:
            ratios.append(ratio)
            break
        else:
            reminders.append((ratio, reminder))
            ratios.append(ratio)
        number = reminder*10
    #print(reminders)


    if ind is not None:
        #print(before_dot, '.', ratios, ind + 1)
        return '{}.{}({})'.format(before_dot,
                                 ''.join([str(v) for v in ratios[0:ind+1]]),
                                 ''.join([str(v) for v in ratios[ind+1:]]))
    elif len(ratios) == 0:
        return before_dot
    elif len(ratios) == 1 and ratios[0] == 0:
        return before_dot
    else:
        return '{}.{}'.format(before_dot,
                              ''.join([str(v) for v in ratios]))


t = int(input())
for i in range(0, t):
    n = int(input())
    d = int(input())
    print(get_fraction(n, d))


