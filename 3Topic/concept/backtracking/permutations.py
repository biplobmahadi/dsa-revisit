def getPermutaions(i, arr):
    if len(arr) == i:
        return [[]]
    curr = getPermutaions(i+1, arr)
    res = []
    for n in curr:
        for j in range(len(n)+1):
            new = n.copy()
            new.insert(j, arr[i])
            res.append(new)
    return res

print(getPermutaions(0, [1, 2, 3, 4]))