
"""
http://practice.geeksforgeeks.org/problems/print-all-possible-strings/1
"""

def printSpace(arr):
    arr = arr.strip()
    size = len(arr) - 1
    if size == 0:
        print(arr + '$', end='')
        return
    permutations = 2**size
    outputs = []
    for i in range(permutations):
        spaces = format(i, '0{}b'.format(size))
        output = []
        for ind, value in enumerate(list(spaces)):
            output.append(arr[ind])
            if value == '1':
                output.append(' ')
        output.append(arr[-1])
        outputs.append(''.join(output))
        outputs.append('$')
        print(outputs)
    print(''.join(outputs))


if __name__ == '__main__':
    inputs = ['abc', 'abcd']
    for inp in inputs:
        printSpace(inp)

