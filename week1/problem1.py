def find_numbers(a, k):
    left, right = 0, len(a) - 1
    while left < right:
        if a[left] + a[right] == k:
            return True
        if a[right] >= k:
            right -= 1
        else:
            left += 1
    return False