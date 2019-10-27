#Uses python2
import numpy as np

import sys

def lcs3(a, b, c):
    #write your code here
    # e = get_best_aligment(a,b)
    # q = get_best_aligment(e[1],c)
    # print'q', q[0]
    return len(q[1])

def get_distance_matrix(s, t):
    #write your code here
    n = len(s) + 1
    m = len(t) + 1
    distance_matrix = np.zeros((n, m), dtype=int)
    distance_matrix[0, :] = range(m)
    distance_matrix[:, 0] = range(n)
    for j in xrange(1, m):
        for i in xrange(1, n):
            insertion = distance_matrix[i,j-1] + 1
            deletion = distance_matrix[i-1,j] + 1
            match = distance_matrix[i-1,j-1]
            mismatch = distance_matrix[i-1,j-1] + 1
            if s[i-1] == t[j-1]:
                distance_matrix[i,j] = min(insertion, deletion, match)
            else:
                distance_matrix[i,j] = min(insertion,deletion,mismatch)
    # print distance_matrix
    # print distance_matrix
    # print
    return distance_matrix

# def optimal_aligment(distance_matrix,i,j,s):
#     if i == 0 and j == 0:
#         # print 's,p',s,p
#         return s
#     elif i > 0 and distance_matrix[i,j] == distance_matrix[i-1,j] + 1:
#         return optimal_aligment(distance_matrix,i-1,j,s)
#     elif j > 0 and distance_matrix[i,j] == distance_matrix[i,j-1] + 1:
#         return optimal_aligment(distance_matrix,i,j-1,s)
#     elif j > 0 and distance_matrix[i,j] == distance_matrix[i-1,j-1] + 1:
#         return optimal_aligment(distance_matrix,i-1,j-1,s)
#     else:
#         s += 1
#         return optimal_aligment(distance_matrix,i-1,j-1,s)


def optimal_aligment(s,t,u):
    n = len(s) + 1
    m = len(t) + 1
    p = len(u) + 1
    aligment_matrix = np.zeros((n, m, p), dtype=int)
    # aligment_matrix[0, :, 0] = range(m)
    # aligment_matrix[:, 0, 0] = range(n)
    # aligment_matrix[0, 0, :] = range(p)
    for j in xrange(1, m):
        for i in xrange(1, n):
            for k in xrange(1,p):
                if s[i-1] == t[j-1] == u[k-1]:
                    aligment_matrix[i,j,k] = aligment_matrix[i-1,j-1,k-1] + 1
                else:
                    aligment_matrix[i,j,k] = max(aligment_matrix[i-1,j,k], aligment_matrix[i,j-1,k],
                                                 aligment_matrix[i,j,k-1])
    return aligment_matrix[n-1,m-1,p-1]



# def optimal_aligment(s,t):
#     n = len(s) + 1
#     m = len(t) + 1
#     aligment_matrix = np.zeros((n, m), dtype=int)
#     aligment_matrix[0, :] = 0
#     aligment_matrix[:, 0] = 0
#     for j in xrange(1, m):
#         for i in xrange(1, n):
#                 if s[i-1] == t[j-1]:
#                     # print 'match',
#                     aligment_matrix[i,j] = aligment_matrix[i-1,j-1] + 1
#                 else:
#                     aligment_matrix[i,j] = max(aligment_matrix[i-1,j], aligment_matrix[i,j-1])
#     print aligment_matrix




# def count_aligment(distance_matrix,i,j,s,p,r):
#     # print i,j,s,p
#     if i == 0 and j == 0:
#         # print 's,p',s,p
#         return s
#     elif i > 0 and distance_matrix[i,j] == distance_matrix[i-1,j] + 1:
#         s += 1
#         return count_aligment(distance_matrix,i-1,j,s,p,r)
#     elif j > 0 and distance_matrix[i,j] == distance_matrix[i,j-1] + 1:
#         s += 1
#         return count_aligment(distance_matrix,i,j-1,s,p,r)
#     elif j > 0 and distance_matrix[i,j] == distance_matrix[i-1,j-1] + 1:
#         s += 1
#         return count_aligment(distance_matrix,i-1,j-1,s,p,r)
#     else:
#         s += 1
#         p.append(r[i-1])
#         return count_aligment(distance_matrix,i-1,j-1,s,p,r)






# def get_best_aligment(s,t):
#     distance_matrix = get_distance_matrix(s,t)
#     i = distance_matrix.shape[0] - 1
#     j = distance_matrix.shape[1] - 1
#     # print distance_matrix
#     # print distance_matrix.shape
#     p = []
#     ops = count_aligment(distance_matrix,i,j,0,p,s)
#     # print 'ops,p', ops,p
#     best_aligment = ops - distance_matrix[i-1,j-1]
#     # print i,j
#     p.reverse()
#     print 'reverse', p
#     return best_aligment,p



if __name__ == '__main__':
    input = sys.stdin.readlines()

    data = []
    for line in input:
        data.extend(map(int, line.strip().split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    # print an,a,bn,b,cn,c
    # print(lcs3(a, b, c))
    # print get_best_aligment('editing','distance')
    print optimal_aligment(a,b,c)

    # c = get_distance_matrix('editing','distance')
    # s = optimal_aligment(c,c.shape[0]-1, c.shape[1]-1,0)
    # print s

    # print optimal_aligment('123','213','135')
    # print optimal_aligment('83217','82138107','683147')

    # print optimal_aligment('editing','distance')
