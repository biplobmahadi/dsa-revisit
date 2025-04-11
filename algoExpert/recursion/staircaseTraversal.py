def staircaseTraversal(height, maxSteps):
    dp = {}
    def solve(height, maxSteps):
        if height == 0: return 1
        if height < 0: return 0
        if height in dp:
            return dp[height]
        dp[height] = 0
        for i in range(1, maxSteps+1):
            dp[height] += solve(height-i, maxSteps)
        return dp[height]

    return solve(height, maxSteps)
