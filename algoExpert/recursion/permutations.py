def getPermutations(array):
    if not array:
        return []
    res = [[]]
    for num in array:
        newRes = []
        for n in res:
            for i in range(len(n)+1):
                arr = n.copy()
                arr.insert(i, num)
                newRes.append(arr)
        res = newRes
    return res

