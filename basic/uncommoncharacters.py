#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/uncommon-characters/0
"""


def find_uncommon_chars(str1, str2):
    presence_dict = {}
    output = []
    for ch in str1:
        if ch not in presence_dict:
            presence_dict[ch] = [False, False]
        presence_dict[ch][0] = True

    for ch in str2:
        if ch not in presence_dict:
            presence_dict[ch] = [False, False]
        presence_dict[ch][1] = True

    for key in sorted(presence_dict.keys()):
        if presence_dict[key][0] != presence_dict[key][1]:
            output.append(key)

    return ''.join(output)


t = int(input())
for i in range(0, t):
    s1 = input().strip()
    s2 = input().strip()
    print(find_uncommon_chars(s1, s2))


