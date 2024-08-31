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

def permutation(arr):
    curr = [[]]
    
    for n in arr:
        newCurr = []
        for p in curr:
            for j in range(len(p)+1):
                new = p.copy()
                new.insert(j, n)
                newCurr.append(new)
        curr = newCurr
    return curr

print(permutation([1, 2, 3, 4]))
