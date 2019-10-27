#Uses python2

import sys

def min_dot_product(a, b):
    #write your code here
    res = 0
    new_a = sorted(a)
    new_b = sorted(b, reverse=True)
    res = sum(map(lambda x: x[0]*x[1], zip(new_a, new_b)))
    return res

if __name__ == '__main__':
    input = sys.stdin.readlines()
    data = []
    for line in input:
        data.extend(map(int, line.strip().split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(min_dot_product(a, b))
    
