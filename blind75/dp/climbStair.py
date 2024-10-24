def climb(n, dp):
    if n <= 2: return n
    if n not in dp:
        dp[n] = climb(n-1, dp) + climb(n-2, dp)
    return dp[n]

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        return climb(n, dp)