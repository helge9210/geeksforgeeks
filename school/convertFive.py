
"""
http://practice.geeksforgeeks.org/problems/replace-all-0-with-5-in-an-input-integer/1
"""

def convertFive(n):
    rest = n
    result = []
    output = 0
    while rest > 0:
        rest, reminder = divmod(rest, 10)
        if reminder == 0:
            result.append(5)
        else:
            result.append(reminder)

    for ind, value in enumerate(result):
        output += value*(10**ind)

    return output

if __name__ == '__main__':
    inputs = [1004, 121, 100, 1000]
    for inp in inputs:
        print(convertFive(inp))

    
