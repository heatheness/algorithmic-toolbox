# Uses python2
from __future__ import print_function
import sys

def optimal_sequence(n):
    num_ops = [0,0]
    for i in xrange(2,n+1):
        min_ops = num_ops[i-1] + 1
        if i % 3 == 0:
            a = num_ops[i/3] + 1
            if a < min_ops:
                min_ops = a
        if i % 2 == 0:
            a = num_ops[i/2] + 1
            if a < min_ops:
                min_ops = a
        num_ops.append(min_ops)
    # reengineering the sequence
    m = num_ops[-1]
    seq = [n]
    j = n
    while m >= 1:
        if (j % 3 == 0) and num_ops[j/3] == num_ops[j] - 1:
            j /= 3
        elif (j % 2 == 0) and num_ops[j/2] == num_ops[j]-1:
            j /= 2
        else:
            j -= 1
        seq.append(j)
        m -= 1
    seq.reverse()

    return (seq)


input = sys.stdin.read()
n = int(input)
# print(optimal_sequence(n))
sequence = (optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
