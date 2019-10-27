# Uses python2
import sys

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(min(a,b), max(a,b) % min(a,b))

if __name__ == "__main__":
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(gcd(a, b))
