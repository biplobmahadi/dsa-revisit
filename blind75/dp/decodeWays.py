class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        def goo(i):
            if i == len(s): return 1
            if i not in dp:
                dp[i] = 0
                if s[i] != '0':
                    dp[i] += goo(i+1)
                if (i+1)<len(s) and ((s[i] == '1') or (s[i] == '2' and s[i+1] in '0123456')):
                    dp[i] += goo(i+2)
            return dp[i]
        return goo(0)