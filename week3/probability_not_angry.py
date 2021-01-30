def probability_not_angry(n, p):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return (1 - p) * probability_not_angry(n - 1, p) + p * (
        1 - p
    ) * probability_not_angry(n - 2, p)


if __name__ == "__main__":
    # should print 0.5
    print(probability_not_angry(4, 0.5))
    # should print 0.4375
    print(probability_not_angry(2, 0.75))