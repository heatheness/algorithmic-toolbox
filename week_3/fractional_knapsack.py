# Uses python2
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.0
    item_weight = sorted(zip(weights, [v/w for v,w in zip(values,weights)]), key=lambda x: x[1], reverse=True)
    for i in xrange(len(item_weight)):
        if capacity == 0:
            return value
        else:
            a = min(item_weight[i][0], capacity)
            value += a*item_weight[i][1]
            capacity -= a
    return value


if __name__ == "__main__":
    raw_data = sys.stdin.readlines()
    data = []
    for line in raw_data:
        data.extend(map(float, line.strip().split()))
    n = int(data[0])
    capacity = data[1]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
