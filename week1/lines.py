def lines(a):
    newArray = []
    i = 0
    arrayLength = len(a)
    elementsRemoved = 0
    while i < arrayLength:
        currentValue = a[i]
        if i + 1 < arrayLength and currentValue == a[i + 1]:
            j = i
            count = 0
            result = []
            while j < arrayLength and a[j] == currentValue:
                count += 1
                result.append(currentValue)
                j += 1
            if count <= 2:
                newArray += result
            else:
                elementsRemoved += count
            i = j
        else:
            newArray.append(currentValue)
            i += 1
    return elementsRemoved + lines(newArray) if elementsRemoved else 0
