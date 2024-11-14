class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*m for _ in range(n)]
        def solve(r, c):
            if (r < 0 or c<0 or r>=n or c>=m): return 0
            if r == n-1 and c == m-1: return 1
            if not dp[r][c]:
                count = 0
                count += solve(r+1, c) 
                count += solve(r, c+1) 
                dp[r][c] = count
            return dp[r][c]
        return solve(0, 0)