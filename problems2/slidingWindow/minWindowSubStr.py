def minWindow(s, t):
    if len(s) < len(t): return ''
    
    mapT, mapS, res = {}, {}, [-1, -1]
    for n in t:
        mapT[n] = mapT.get(n, 0) + 1
    
    L, have, need, prev = 0, 0, len(mapT), len(s)
    
    for R, v in enumerate(s):
        if v in mapT:
            mapS[v] = mapS.get(v, 0) + 1
            if mapS[v] == mapT[v]:
                have += 1
        while have == need:
            curr = R - L + 1
            if curr < prev:
                res = [L, R]
                prev = curr
            
            if s[L] in mapS:
                mapS[s[L]] -= 1
                if mapS[s[L]] < mapT[s[L]]:
                    have -= 1
            L += 1
            
    return s[res[0]: res[1]+1]


print(minWindow('ADOBECODEBANC', 'ABC'))
