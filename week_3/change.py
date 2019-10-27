# Uses python2
import sys

def get_change(n):
    denoms = [10,5,1]
    res = 0
    count = 0
    i = 0
    while res < n:
        if denoms[i] <= n:
            c = (n - res) / denoms[i]
            count += c
            res += c * denoms[i]
        i += 1
    return count

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(get_change(n))
