def minimumCharactersForWords(words):
    hashMap = {}
    for w in words:
        curr = {}
        for s in w:
            curr[s] = curr.get(s, 0) + 1
        for k, v in curr.items():
            hashMap[k] = max(v, hashMap.get(k, 0))
    res = []
    for k, v in hashMap.items():
        for _ in range(v):
            res.append(k)
    return res
            
