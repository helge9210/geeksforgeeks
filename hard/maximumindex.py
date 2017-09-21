#!/usr/bin/env python


"""
http://practice.geeksforgeeks.org/problems/maximum-index/0
"""

class BSTNode(object):
    """
    Binary search tree node implementation
    """
    def __init__(self, value, extract_value=lambda x: x[0],
                 extract_index=lambda x: x[1]):
        self.value = value
        self.left = None
        self.right = None
        self.extract_value = extract_value
        self.extract_index = extract_index

    def __str__(self):
        return '({}, {}, {})'.format(self.left,
                                   self.value,
                                   self.right)

    def insert(self, value):
        if self.extract_value(value) >= self.extract_value(self.value):
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)

    def max_index(self):
        if self.right:
            max_right = max(self.extract_index(self.value),
                            self.right.max_index())
        else:
            max_right = self.extract_index(self.value)
        if self.left:
            max_left = max(self.extract_index(self.value),
                           self.left.max_index())
        else:
            max_left = self.extract_index(self.value)

        return max(max_right, max_left)

    def min_max_index_right(self):
        if self.right:
            diff_right = (self.right.max_index() -
                          self.extract_index(self.value))

        else:
            diff_right = 0

        if self.left:
            diff_left = self.left.min_max_index_right()
        else:
            diff_left = 0
        return max(diff_left, diff_right)


def find_max_index(array):
    m = BSTNode(array[0])
    for el in array[1:]:
        m.insert(el)

    return m.min_max_index_right()


t = int(input())
for i in range(0, t):
    n = int(input())
    arr = [(int(v), ind) for ind, v in enumerate(input().strip().split(' '))]
    print(find_max_index(arr))


