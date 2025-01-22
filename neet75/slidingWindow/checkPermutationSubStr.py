class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1Arr = [0] * 26
        for s in s1:
            p = ord(s) - ord('a')
            s1Arr[p] += 1
        s2Arr = [0] * 26
        for i in range(len(s1)):
            p = ord(s2[i]) - ord('a')
            s2Arr[p] += 1
        if s1Arr == s2Arr:
            return True
        l, r = 1, len(s1)
        s2Arr[ord(s2[0])-ord('a')] -= 1
        while r < len(s2):
            p = ord(s2[r]) - ord('a')
            s2Arr[p] += 1
            if s1Arr == s2Arr:
                return True
            pl = ord(s2[l]) - ord('a')
            s2Arr[pl] -= 1
            l+=1
            r+=1
        return False