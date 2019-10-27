# Uses python2
from __future__ import print_function
import sys


# def get_majority_element(a, n):
#     cnt = {}
#     m = n/2
#     for i in a:
#         cnt.setdefault(i,0)
#         cnt[i] += 1
#     for k in cnt:
#         if cnt[k] > m:
#             return 1
#     return -1

def get_majority_element(a, n):
    maj_index = 0
    cnt = 1
    for i in xrange(1, n):
        if a[i] == a[maj_index]:
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            maj_index = i
            cnt = 1

    cnt = 0
    for i in xrange(n):
        if a[i] == a[maj_index]:
            cnt +=1
    if cnt > n/2:
        return 1
    else:
        return -1



if __name__ == '__main__':
    input = sys.stdin.readlines()
    data = []
    for line in input:
        data.extend(map(int, line.strip().split()))
    n = data[0]
    a = data[1:n + 1]
    if get_majority_element(a, n) != -1:
        print(1)
    else:
        print(0)
