count = 0


def exp(a, b):
    global count
    count += 1
    if b == 0:
        return 1
    if b % 2 == 0:
        return exp(a, b // 2) ** 2
    return a * exp(a, (b - 1) // 2) ** 2


if __name__ == "__main__":
    exp(2, 135)
    print(count)