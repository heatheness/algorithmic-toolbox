# Uses python2
from __future__ import print_function
import sys


def merge(b,c,cnt):
    # print ('b',b)
    # print ('c',c)
    # print ('cnt', cnt)
    d = []
    cur_cnt = len(c)*len(b)
    while b and c:
        if b[0] <= c[0]:
            d.append(b.pop(0))
            cur_cnt -= len(c)
        elif b[0] > c[0]:
            d.append(c.pop(0))

    d.extend(b)
    d.extend(c)
    # print ('d, cnt', d,cnt + cur_cnt)
    return d,cnt+cur_cnt



def get_number_of_inversions(a):
    n = len(a)
    cnt = 0
    if n == 1:
        return a,cnt
    mid = n // 2
    b = get_number_of_inversions(a[:mid])
    c = get_number_of_inversions(a[mid:])
    return merge(b[0], c[0], b[1] + c[1])


if __name__ == '__main__':
    # print(merge([1,2,3,4], [2,3,4] ,0))
    input = sys.stdin.readlines()
    data = []
    for line in input:
        data.extend(map(int, line.strip().split()))
    n = data[0]
    a = data[1:n + 1]
    print(get_number_of_inversions(a)[1])
