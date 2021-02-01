def binarySearch(A, l, r, t):
    if l >= r:
        return -1
    mid = (l + r) // 2
    if A[mid] == t:
        return mid
    if A[mid] > t:
        return binarySearch(A, l, mid, t)
    return binarySearch(A, mid + 1, r, t)