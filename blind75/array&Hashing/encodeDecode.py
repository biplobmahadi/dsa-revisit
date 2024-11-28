from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for w in strs:
            s += f'{len(w)}#{w}'
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            n = int(s[i: j])
            w = s[j+1: j+1+n]
            res.append(w)
            i = j+n+1
        return res