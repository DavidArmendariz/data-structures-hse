from collections import deque


def sliding_window_min(a, k):
    d = deque()
    result = []
    for i, element in enumerate(a):
        while d and a[d[-1]] > element:
            d.pop()
        d.append(i)
        if d[0] == i - k:
            d.popleft()
        if i >= k - 1:
            result.append(a[d[0]])
    return result