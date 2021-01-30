count = 0


def foo(n):
    global count
    count += 1
    if n == 0 or n == 1 or n == 2:
        return 1
    return foo(n - 1) + 2 * foo(n - 3)


if __name__ == "__main__":
    foo(6)
    print(count)