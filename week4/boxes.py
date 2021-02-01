import math


def num_boxes(n):
    tbl = [math.inf] * (n + 1)
    tbl[0] = 1
    for j in range(1, n + 1):
        i = 1
        while i ** 3 <= j:
            tbl[j] = min(tbl[j], tbl[i - 1])
            i += 1
    return tbl[n]