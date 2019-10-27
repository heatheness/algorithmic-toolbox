# Uses python2
import sys
#

def get_fibonaccihuge(n, m):
    period_list = [0,1]
    if n <= 1:
        return period_list[n]
    else:
        a = 0
        b = 1
        while len(period_list) <= n:
            next_fib = (a+b) % m
            a,b = b,next_fib
            if next_fib == period_list[0]:
                temp_list = [next_fib]
                for i in xrange(2):
                    next_fib = (a+b) % m
                    a,b = b,next_fib
                    temp_list.append(next_fib)
                if period_list[0:3] == temp_list:
                    index = n % len(period_list)
                    return period_list[index]
                else:
                    period_list.extend(temp_list)
            else:
                period_list.append(next_fib)
        return period_list[-1]



if __name__ == '__main__':
    input = sys.stdin.readline();
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))
    # fib_generator = fib()
    # period_list = [next(fib_generator)]


    # for j in xrange(30):
    #     next_fib = next(fib_generator)
    #     print "period_list", period_list
    #     if next_fib % m == period_list[0]:
    #         temp_list = [next_fib % m]
    #         for i in xrange(len(period_list)-1):
    #             temp_list.append(next(fib_generator) % m)
    #         print "temp_list", temp_list
    #         if period_list == temp_list:
    #             print 'Finish', period_list
    #             break
    #         else:
    #             period_list.extend(temp_list)
    #     else:
    #         period_list.append(next_fib % m)





        #
        #
        # temp_next_fib = next(fib_generator)
        # print "temp_next_fib mod m", temp_next_fib % m
        # print "period first", period_list[0]
        # if temp_next_fib % m == period_list[0]:
        #     temp_list = [temp_next_fib]
        #     for i in xrange(len(period_list)-1):
        #         temp_list.append(next(fib_generator) % m)
        #     print 'temp', temp_list
        #     if period_list == temp_list:
        #         print 'Finish', period_list
        #         break
        # else:
        #     period_list.append(temp_next_fib % m)


