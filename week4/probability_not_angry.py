def not_angry(n):
    tbl = [1] * (n + 1)
    if n > 0:
        tbl[1] = 2
    for i in range(2, n + 1):
        tbl[i] = tbl[i - 1] + tbl[i - 2]
    return tbl[n]
