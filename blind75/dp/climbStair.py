def climb(n, dp):
    if n <= 2: return n
    if n not in dp:
        dp[n] = climb(n-1, dp) + climb(n-2, dp)
    return dp[n]

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        return climb(n, dp)
    
class Solution2:
    def climbStairs2(self, n: int) -> int:
        if n <= 2: return n
        dpOne, dpTwo = 1, 2
        for i in range(3, n+1):
            dpOne, dpTwo = dpTwo, dpOne+dpTwo
        return dpTwo