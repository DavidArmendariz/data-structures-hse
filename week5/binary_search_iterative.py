def binarySearchIterative(A, t):
    l = 0
    r = len(A)
    while l < r:
        mid = (l + r) // 2
        if A[mid] == t:
            return mid
        if A[mid] > t:
            r = mid
        else:
            l = mid + 1
    return -1