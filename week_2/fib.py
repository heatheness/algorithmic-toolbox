# Uses python2
def calc_fib(n):
    if (n <= 1):
        return n
    else:
        n_previous = 0
        n_current = 1
        for i in xrange(2,n):
            n_temp = n_previous + n_current
            n_previous = n_current
            n_current = n_temp
    return n_previous + n_current





n = int(raw_input())
print(calc_fib(n))
