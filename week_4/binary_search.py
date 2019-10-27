# Uses python2
from __future__ import print_function
import sys


def binary_search(a,x,l,r):
    if l > r:
        return -1
    else:
        mid = (l + (r-l)/2)
        # print ("mid ", mid)
        if a[mid] == x:
            return mid
        elif x < a[mid]:
            # print ("<--- left")
            return binary_search(a,x,l,mid-1)
        else:
            # print ("---> right")
            return binary_search(a,x,mid+1,r)


if __name__ == '__main__':
    input = sys.stdin.readlines()
    data = []
    for line in input:
        data.extend(map(int, line.strip().split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x, 0, n-1), end = ' ')
