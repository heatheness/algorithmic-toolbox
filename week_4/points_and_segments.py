# Uses python2
from __future__ import print_function
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    # sort all coordinates in asc order and label each coordinate
    coordinates = []
    for i in starts:
        coordinates.append((i,1))
    for i in xrange(len(points)):
        coordinates.append((points[i],2,i))
    for i in ends:
        coordinates.append((i,3))

    coordinates = sorted(coordinates, key=lambda x: (x[0],x[1]))
    # print(coordinates)

    c = 0
    for i in coordinates:
        if i[1] == 1:
            c +=1
        elif i[1] == 3:
            c -= 1
        else:
            cnt[i[2]] = c

    return cnt




# def naive_count_segments(starts, ends, points):
#     cnt = [0] * len(points)
#     for i in range(len(points)):
#         for j in range(len(starts)):
#             if starts[j] <= points[i] <= ends[j]:
#                 cnt[i] += 1
#     return cnt

if __name__ == '__main__':
    input = sys.stdin.readlines()
    data = []
    for line in input:
        data.extend(map(int, line.strip().split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
