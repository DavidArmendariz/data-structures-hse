def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < len(s) and right >= 0:
        if s[left] == " ":
            left += 1
            continue
        if s[right] == " ":
            right -= 1
            continue
        if left < len(s) and right >= 0 and s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True