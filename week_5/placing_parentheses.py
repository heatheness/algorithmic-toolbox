# Uses python2
import numpy as np
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(dataset):
    def min_and_max(i,j):
        min_val = float('inf')
        max_val = float('-inf')
        for k in xrange(i,j):
            a = evalt(max_matrix[i,k], max_matrix[k+1,j], ops[k])
            b = evalt(max_matrix[i,k], min_matrix[k+1,j], ops[k])
            c = evalt(min_matrix[i,k], max_matrix[k+1,j], ops[k])
            d = evalt(min_matrix[i,k], min_matrix[k+1,j], ops[k])
            min_val = min(min_val,a,b,c,d)
            max_val = max(max_val,a,b,c,d)
        return min_val, max_val

    ops = dataset[1::2]
    digits = dataset[::2]
    n = (len(dataset)+1)/2
    max_matrix = np.zeros((n,n), dtype=int)
    min_matrix = np.zeros((n,n), dtype=int)
    np.fill_diagonal(max_matrix,list(digits))
    np.fill_diagonal(min_matrix,list(digits))
    for s in xrange(1,n):
        for i in xrange(n-s):
            j = i + s
            min_matrix[i,j], max_matrix[i,j] = min_and_max(i,j)

    return max_matrix[0,n-1]


if __name__ == "__main__":
    print(get_maximum_value(raw_input()))
