# Uses python2
import sys
import numpy as np

def optimal_weight(W, w):
    n = len(w)
    value_matrix = np.zeros((n+1, W+1),dtype=int)
    for i in xrange(1,n+1):
        # print ('i', i)
        for j in xrange(1,W+1):
            # print ('j', j)
            value_matrix[i,j] = value_matrix[i-1,j]
            # w[i] - weight if i-th item. value and weight are equal in this task
            # w - capacity of current knapsack
            # i - 1 in indexing w because indexing of w starts from 0, and in matrix we filling
            # rows from the 1st row
            if w[i-1] <= j:
                # print ('yes')
                val = value_matrix[i-1,j-w[i-1]] + w[i-1]
                # print ('val', val)
                # print ('prev opt val', value_matrix[i-1,j-w[i-1]])
                if value_matrix[i,j] < val:
                    value_matrix[i,j] = val
    # print value_matrix
    return value_matrix[n,W]





    # write your code here
    # result = 0
    # for x in w:
    #     if result + x <= W:
    #         result = result + x
    # return result

if __name__ == '__main__':
    # input = sys.stdin.read()
    # W, n, *w = list(map(int, input.split()))
    # print(optimal_weight(W, w))

    input = sys.stdin.readlines()
    data = []
    for line in input:
        data.extend(map(int, line.strip().split()))
    W,n = data[0],data[1]
    w = data[2:]
    print(optimal_weight(W, w))
