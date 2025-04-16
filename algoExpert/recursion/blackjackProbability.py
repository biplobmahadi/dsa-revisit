def blackjackProbability(target, startingHand):
    dp= {}
    def solve(curr):
        if curr > target:
            return 1
        if target-4<= curr <= target:
            return 0
        if curr in dp:
            return dp[curr] 
        dp[curr] = 0
        for i in range(1, 11):
            dp[curr] += solve(curr+i)*.1
        return dp[curr]
    n = solve(startingHand)
    return round(n, 3)