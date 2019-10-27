# Uses python2
import sys


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(min(a,b), max(a,b) % min(a,b))

def lcm(a, b):
    #write your code here
    return a*b/gcd(a,b)

if __name__ == '__main__':
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(lcm(a, b))

