class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mapT, mapS = {}, {}
        for w in t:
            mapT[w] = mapT.get(w, 0) + 1
        have, need = len(mapT), 0

        l, res, curr = 0, [-1, -1], float('inf')
        for r, w in enumerate(s):
            if w in mapT:
                mapS[w] = mapS.get(w, 0) + 1
                if mapS[w] == mapT[w]:
                    need += 1

            while need == have:
                dis = r-l+1
                if dis < curr:
                    res = [l, r]
                    curr = dis
                if s[l] in mapS:
                    mapS[s[l]] -= 1
                    if mapS[s[l]] < mapT[s[l]]:
                        need -= 1
                l+=1
        return s[res[0]: res[1]+1]