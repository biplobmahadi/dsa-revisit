def kadanesAlgorithm(array):
    res = float('-inf')
    curr = 0
    for n in array:
        curr = max(curr+n, n)
        res = max(res, curr)
    return res