def commonCharacters(strings):
    map = {}
    for i, word in enumerate(strings):
        n = set(word)
        for s in n:
            map[s] = map.get(s, 0)+1
    l = len(strings)
    res = []
    for k, v in map.items():
        if v == l:
            res.append(k)
    return res
