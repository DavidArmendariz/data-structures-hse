def subsets(elems):
    if len(elems) == 0:
        return [[]]
    result = subsets(elems[:-1])
    elements_in_result = len(result)
    for i in range(elements_in_result):
        result.append(result[i] + [elems[-1]])
    return result