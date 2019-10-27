# Uses python2
import numpy as np

def edit_distance(s, t):
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
    return distance_matrix[n-1,m-1]

if __name__ == "__main__":
    print(edit_distance(raw_input(),raw_input()))
