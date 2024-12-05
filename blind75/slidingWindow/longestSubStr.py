class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l, r = 0, 0
        visit = set()
        while r < len(s):
            if s[r] not in visit:
                res = max(res, r-l+1)
                visit.add(s[r])
                r+=1
                continue
            visit.remove(s[l])
            l+=1
        return res