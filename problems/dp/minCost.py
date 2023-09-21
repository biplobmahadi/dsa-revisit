def minCostClimbingStairs(cost):
    n = len(cost)
    return min(minCost(n-1, cost), minCost(n-2, cost))

def minCost(i, cost):
    if i < 0: return 0
    if i==0 or i==1: return cost[i]
    return cost[i] + min(minCost(i-1, cost), minCost(i-2, cost))

print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))

def minCostClimbingStairsOpti(cost):
    n = len(cost)
    memo = [None] * n
    memo[0] = cost[0]
    memo[1] = cost[1]
    return min(minCostOpti(n-1, cost, memo), minCostOpti(n-2, cost, memo))

def minCostOpti(i, cost, memo):
    if i < 0: return 0
    if memo[i]: return memo[i]
    memo[i] = cost[i] + min(minCostOpti(i-1, cost, memo), minCostOpti(i-2, cost, memo))
    return memo[i]

print(minCostClimbingStairsOpti([1,100,1,1,1,100,1,1,100,1]))

def minCostBottomUp(cost):
    n = len(cost)
    if n<=1: return 0
    dp = [None] * n
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    return min(dp[n-1], dp[n-2])

print(minCostBottomUp([1,100,1,1,1,100,1,1,100,1]))

def minCostBottomUpOpti(cost):
    n = len(cost)
    if n<=1: return 0
    dpOne = cost[0]
    dpTwo = cost[1]
    for i in range(2, n):
        curr = cost[i] + min(dpOne, dpTwo)
        dpOne = dpTwo
        dpTwo = curr
    return min(dpOne, dpTwo)

print(minCostBottomUpOpti([1,100,1,1,1,100,1,1,100,1]))

