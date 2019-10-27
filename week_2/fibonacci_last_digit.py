# Uses python2
import sys

def get_fibonacci_last_digit(n):
    if (n <= 1):
        return n
    else:
        n_previous = 0
        n_current = 1
        for i in xrange(2,n):
            n_temp = (n_previous + n_current) % 10
            n_previous = n_current
            n_current = n_temp
    return (n_previous + n_current) % 10

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(get_fibonacci_last_digit(n))
