class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char = [0] * 26
        l, res = 0, 0
        for r in range(len(s)):
            char[ord(s[r])-ord('A')] += 1
            maxChar = max(char)
            if (r-l+1) - maxChar <= k:
                res = max(res, r-l+1)
            else: 
                char[ord(s[l])-ord('A')] -= 1
                l+=1
        return res