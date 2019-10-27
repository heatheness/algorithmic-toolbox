# Uses python2
from __future__ import print_function
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    #write your code here
    new_segments = sorted(segments, key=lambda x: x.end)
    points = [new_segments[0].end]
    for s in new_segments:
        if not (s.start <= points[-1] <= s.end):
            points.append(s.end)
    return points

if __name__ == '__main__':
    input = sys.stdin.readlines()
    data = []
    for line in input:
        data.extend(map(int, line.strip().split()))
    n = data[0]
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[1::2], data[2::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print (p, end=' ')
