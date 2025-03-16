from collections import defaultdict

def groupAnagrams(words):
    res = defaultdict(list)
    for w in words:
        key = [0]*26
        for s in w:
            od = ord(s)-ord('a')
            key[od] += 1
        res[tuple(key)].append(w)

    return list(res.values())
