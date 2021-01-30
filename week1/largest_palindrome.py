def largest_palindrome(s):
    stringLength = len(s)
    if stringLength < 2:
        return s
    startIndex = 0
    greatestLength = 0

    def expandRange(s, start, end):
        while start >= 0 and end < stringLength and s[start] == s[end]:
            start -= 1
            end += 1
        nonlocal greatestLength
        nonlocal startIndex
        if greatestLength < end - start - 1:
            startIndex = start + 1
            greatestLength = end - start - 1

    for i in range(stringLength):
        expandRange(s, i, i)
        expandRange(s, i, i + 1)

    return s[startIndex : (startIndex + greatestLength)]
