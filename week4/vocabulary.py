def voc_to_list(vocabulary):
    """
    produces a list lengths such that lengths[i] is the number of
    words of length i in vocabulary
    """
    max_len = max([len(w) for w in vocabulary])
    lengths = [0] * (max_len + 1)
    for w in vocabulary:
        wordLength = len(w)
        lengths[wordLength] += 1
    return lengths


def passwords(L, vocabulary):
    lengths = voc_to_list(vocabulary)
    k = len(lengths)
    tbl = [0] * (L + 1)
    for i in range(L + 1):
        if i < k:
            tbl[i] = lengths[i]
        for j in range(min(i, k)):
            tbl[i] += tbl[j]
    print(tbl)
    return tbl[L]