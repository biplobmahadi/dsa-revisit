class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        dp = {}
        def solve(i):
            if i == len(s):
                return True
            if i in dp:
                return dp[i]
            for word in wordDict:
                if i+len(word) <= len(s) and s[i: i+len(word)] == word:
                    if solve(i+len(word)):
                        return True
            dp[i] = False
            return False
        return solve(0)
