# Uses python2
from __future__ import print_function
import sys

def optimal_summands(n):
    summands = []
    i = 1
    while n - i > i:
        n -= i
        summands.append(i)
        i += 1
    summands.append(n)
    return summands

    # while n != 0:
    #     if (n - i) <= i:
    #         summands.append(n)
    #         return summands
    #     else:
    #         n -= i
    #         summands.append(i)
    #         i += 1
    # return summands

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
